"use client";

import { useUser } from "../../hooks/useUser";
import { useRouter } from "next/navigation";
import { useEffect, type ReactNode } from "react";

export default function AuthGuard({ children } : { children: ReactNode }) {
    const {data : user, isLoading, isError} = useUser();
    const router = useRouter();

    useEffect(() => {
        if (!isLoading && (isError || !user)) {
            router.push("/login");
        }
    }, [isLoading, isError, user, router])

    if (isLoading) {
        return (
            <div style={{ display: "grid", placeItems: "center", height: "100vh" }}>
                Loading...
            </div>
        );
    }

    if (!user) return null;

    return <>{children}</>;
}