"use client";

import Image from "next/image";
import Link from "next/link";
import { useState, type FormEvent } from "react";
import { useRegister } from "../../hooks/useAuth";

export default function RegisterPage() {
    const [username, setUsername] = useState("");
    const [email, setEmail] = useState("");
    const [password, setPassword] = useState("");
    const [confirmPassword, setConfirmPassword] = useState("");
    const register = useRegister();

    const handleSubmit = (e: FormEvent) => {
        e.preventDefault();
        register.mutate({ username, email, password, confirmPassword });
    };

    return (
        <div className="flex items-center justify-center min-h-screen w-full bg-background p-4">
            <div className="flex max-w-[1000px] w-full bg-background rounded-2xl
             overflow-hidden shadow-[0_0_40px_rgba(0,0,0,0.2)]">

                <div className="hidden md:flex flex-col justify-between w-1/2 bg-primary text-background p-12 lg:p-20">
                    <div className="flex flex-col items-center text-right">
                        <Image
                            src="/register.svg"
                            width={200}
                            height={200}
                            alt="Register illustration"
                            priority
                        />
                        <h2 className="font-black text-3xl my-9 leading-tight">
                            Зареєструйся, поки кіт не звалив вазу
                        </h2>

                    </div>
                   <div className="flex flex-col items-center text-right">
                       <p className="opacity-90 text-base align-right">
                           Якщо у вас уже є акаунт, худко тисни вхід
                       </p>
                       <button className="self-end py-2 px-8 mt-4 font-semibold text-primary bg-background rounded-xl
                     hover:bg-opacity-90 transition-colors">
                           <Link
                               href={"/login"}>
                               Вхід
                           </Link>
                       </button>
                   </div>
                </div>

                <div className="w-full md:w-1/2 bg-background p-12 lg:p-20 flex flex-col
                 justify-center shadow-[0_0_40px_rgba(0,0,0,0.2)]">
                    <h1 className="text-center font-semibold text-4xl mb-15 text-black">Реєстрація</h1>

                    <form onSubmit={handleSubmit} className="flex flex-col gap-6">
                        <div className="flex flex-col gap-6">
                            <input
                                type="text"
                                placeholder="Імʼя користувача"
                                className="w-full border-primary border rounded-md py-3 px-4 text-base outline-none
                                focus:ring-2 ring-primary/20 transition-all"
                                value={username}
                                onChange={(e) => setUsername(e.target.value)}
                                required
                            />

                            <input
                                type="email"
                                placeholder="Електронна пошта"
                                className="w-full border-primary border rounded-md py-3 px-4 text-base outline-none
                                 focus:ring-2 ring-primary/20 transition-all"
                                value={email}
                                onChange={(e) => setEmail(e.target.value)}
                                required
                            />

                            <input
                                type="password"
                                placeholder="Пароль"
                                className="w-full border-primary border rounded-md py-3 px-4 text-base outline-none
                                 focus:ring-2 ring-primary/20 transition-all"
                                value={password}
                                onChange={(e) => setPassword(e.target.value)}
                                required
                            />

                            <input
                                type="password"
                                placeholder="Підтвердіть пароль"
                                className="w-full border-primary border rounded-md py-3 px-4 text-base outline-none
                                 focus:ring-2 ring-primary/20 transition-all"
                                value={confirmPassword}
                                onChange={(e) => setConfirmPassword(e.target.value)}
                                required
                            />
                        </div>


                        <div className="w-full text-sm">
                            <label className="flex items-start gap-3 cursor-pointer group leading-tight">
                                <input
                                    type="checkbox"
                                    id="remember-me"
                                    className="w-4 h-4 mt-0.5 cursor-pointer accent-primary rounded border-gray-300 text-primary focus:ring-primary"
                                />
                                <span className="text-gray-800">
                                     Я погоджуюся з{" "}
                                    <a href="#" className="text-primary underline hover:opacity-80 transition-opacity">
                                        Політикою конфіденційності
                                    </a>{" "}
                                        та{" "}
                                    <a href="#" className="text-primary underline hover:opacity-80 transition-opacity">
                                        Умовами використання
                                    </a>
                                 </span>
                            </label>
                        </div>

                        {register.isError && (
                            <div className="text-red-400 text-sm text-center">
                                {register.error instanceof Error && 'response' in (register.error as any)
                                    ? Object.entries((register.error as any).response?.data || {}).map(([field, msgs]) => (
                                        <p key={field}>{Array.isArray(msgs) ? msgs.join(', ') : String(msgs)}</p>
                                    ))
                                    : <p>Помилка реєстрації. Перевірте дані та спробуйте ще раз.</p>
                                }
                            </div>
                        )}

                        <button
                            type="submit"
                            disabled={register.isPending}
                            className="w-full md:w-max md:self-center mt-6 py-2 px-10 font-semibold text-background
                         bg-primary rounded-xl hover:opacity-90 transition-opacity text-lg disabled:opacity-50 disabled:cursor-not-allowed"
                        >
                            {register.isPending ? "Реєстрація..." : "Зареєструватись"}
                        </button>
                    </form>
                </div>
            </div>
        </div>
    )
}