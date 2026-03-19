import { NextRequest, NextResponse } from "next/server";

const API_URL = process.env.API_URL!;

export async function POST(req: NextRequest) {
    const body = await req.json();

    const res = await fetch(`${API_URL}/auth/login/`, {
        method: "POST",
        headers: { "Content-Type" : "application/json"},
        body: JSON.stringify({ email: body.email, password: body.password }),
    })

    const data = await res.json()

    if (!res.ok) {
        return NextResponse.json(data, { status: res.status });
    }

    const response = NextResponse.json({
        accessToken: data.access,
    });

    response.cookies.set("refreshToken", data.refresh, {
        httpOnly: true,
        secure: process.env.NODE_ENV === "production",
        sameSite: "lax",
        path: "/",
        maxAge: 30 * 24 * 60 * 60,
    })

    return response;
}