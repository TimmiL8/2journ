import { NextRequest, NextResponse } from "next/server";

const API_URL = process.env.API_URL!;

export async function POST(req: NextRequest) {
    const refreshToken = req.cookies.get("refreshToken")?.value;

    if (!refreshToken) {
        return NextResponse.json({ error: "No refresh token" }, { status: 401 });
    }

    const res = await fetch(`${API_URL}/auth/token/refresh`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ refresh: refreshToken }),
    })

    const data = await res.json();

    if (!res.ok) {
        const response = NextResponse.json(data, { status: res.status });
        response.cookies.delete("refreshToken");
        return response;
    }

    return NextResponse.json({ accessToken: data.access });
}