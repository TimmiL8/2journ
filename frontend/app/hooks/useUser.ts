import { useQuery } from "@tanstack/react-query";
import { userService } from "../services/user.service";

export const useUser = () => {
    return useQuery({
        queryKey: ["user", "me"],
        queryFn: () => userService.getMe(),
    })
}