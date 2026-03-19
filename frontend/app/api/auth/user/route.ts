import { NextRequest, NextResponse } from "next/server";

const API_URL = process.env.API_URL!;

export async function GET(req: NextRequest) {
    const authHeader = req.headers.get("authorization");

    const res = await fetch(`${API_URL}/auth/user/`, {
        headers: {
            "Content-Type": "application/json",
            ...(authHeader ? { Authorization: authHeader } : {}),
        },
    });

    const data = await res.json();
    return NextResponse.json(data, { status: res.status });
}