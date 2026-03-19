import api from "../lib/axios"
import type { LoginRequest, RegisterRequest} from "@/app/types/auth.types";

export const authService = {
    login : async (data: LoginRequest) => {
        const res = await api.post<{ accessToken : string }>("/api/auth/login", data);
        return res.data;
    },

    register : async (data: RegisterRequest) => {
        const res = await api.post<{ accessToken : string }>("/api/auth/register", data);
        return res.data;
    },

    logout : async () => {
        await api.post<{ accessToken : string }>("/api/auth/logout");
    }
}