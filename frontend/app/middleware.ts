import { NextRequest, NextResponse } from "next/server";

const publicRoutes = ["/login", "/register"];

export function middleware(req: NextRequest) {
    const { pathname } = req.nextUrl;
    const hasRefresh = req.cookies.has("refreshToken");

    const isPublic = publicRoutes.some((route) => pathname.startsWith(route));

    if (isPublic && hasRefresh) {
        return NextResponse.redirect(new URL("/", req.url));
    }

    if (!isPublic && !hasRefresh && pathname !== "/") {
        return NextResponse.redirect(new URL("/login", req.url));
    }

    return NextResponse.next();
}

export const config = {
    matcher: ["/((?!api|_next/static|_next/image|favicon.ico|.*\\.svg$|.*\\.jpg$).*)"],
};