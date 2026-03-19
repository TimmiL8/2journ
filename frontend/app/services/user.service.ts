import api from "../lib/axios"
import type { User } from "../types/user.types"

export const userService = {
    getMe : async (): Promise<User> => {
        const res = await api.get<User>("/api/auth/user");
        return res.data;
    }
}
