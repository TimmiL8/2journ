import { NextRequest, NextResponse } from "next/server";

const API_URL = process.env.API_URL!;

export async function POST(req: NextRequest) {
    const body = await req.json();

    const registerRes = await fetch(`${API_URL}/auth/registration/`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
            username: body.username,
            email: body.email,
            password1: body.password,
            password2: body.confirmPassword,
        }),
    })

    if (!registerRes.ok) {
        const errors = await registerRes.json();
        return NextResponse.json(errors, { status: registerRes.status });
    }

    const loginRes = await fetch(`${API_URL}/auth/login/`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ email: body.email, password: body.password }),
    })

    const data = await loginRes.json();

    if (!loginRes.ok) {
        return NextResponse.json(data, { status: loginRes.status });
    }

    const response = NextResponse.json({
        accessToken: data.access
    })

    response.cookies.set("refreshToken", data.refresh, {
        httpOnly: true,
        secure: process.env.NODE_ENV === "production",
        sameSite: "lax",
        path: "/",
        maxAge: 30 * 24 * 60 * 60,
        }
    );

    return response;
}