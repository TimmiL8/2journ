import { useMutation, useQueryClient } from "@tanstack/react-query";
import { useRouter } from "next/navigation";
import { authService } from "../services/auth.service";
import { setAccessToken } from "../lib/auth";
import type { LoginRequest, RegisterRequest } from "../types/auth.types";

export const useLogin = () => {
    const router = useRouter();
    const qc = useQueryClient();

    return useMutation({
        mutationFn: (data : LoginRequest) => authService.login(data),
        onSuccess: ({ accessToken }) => {
            setAccessToken(accessToken);
            qc.invalidateQueries({ queryKey: ["user", "me"] });
            router.push("/");
        },
    });
};

export const useRegister = () => {
    const router = useRouter();
    const qc = useQueryClient();

    return useMutation({
        mutationFn: (data : RegisterRequest) => authService.register(data),
        onSuccess: ({ accessToken }) => {
            setAccessToken(accessToken);
            qc.invalidateQueries({ queryKey: ["user", "me"] });
            router.push("/");
        },
    });
};

export const useLogout = () => {
    const router = useRouter();
    const qc = useQueryClient();

    return useMutation({
        mutationFn: () => authService.logout(),
        onSuccess: () => {
            setAccessToken(null);
            qc.clear();
            router.push("/login");
        },
    })
}
