"use client";

import Image from 'next/image'
import Link from "next/link";
import { useState, type FormEvent } from "react";
import {useLogin, useLogout} from "../../hooks/useAuth";


export default function LoginPage() {
    const logout = useLogout();

    const handleSubmit = (e: FormEvent) => {
        e.preventDefault();
        logout.mutate();
    }


    return (
        <div className="flex items-center justify-center min-h-screen w-full bg-background p-4">
            <div className="flex max-w-[1000px] w-full bg-background rounded-2xl overflow-hidden shadow-[0_0_40px_rgba(0,0,0,0.2)]">

                <div className="hidden md:flex flex-col justify-between w-1/2 bg-primary text-background p-12 lg:p-20">
                    <div className="flex flex-col items-center text-right">
                        <Image
                            src="/login.svg"
                            width={200}
                            height={200}
                            alt="Login illustration"
                            priority
                        />
                        <h2 className="font-black text-2xl my-9 leading-tight">
                            Виходиш?
                        </h2>
                        <p className="opacity-90">
                            Ну виходи...
                        </p>
                    </div>
                </div>

                <div className="w-full md:w-1/2 bg-background p-12 lg:p-20 flex flex-col justify-center shadow-[0_0_40px_rgba(0,0,0,0.2)]">
                    <h1 className="text-center font-semibold text-4xl mb-24 text-black">Вийти з акаунту</h1>

                    <form onSubmit={handleSubmit} className="flex flex-col gap-6">

                        {logout.isError && (
                            <p className="text-red-400 text-sm text-center">
                                Шось не так
                            </p>
                        )}

                        <button
                            type="submit"
                            disabled={logout.isPending}
                            className="w-full md:w-max md:self-center mt-10 py-2 px-6 font-semibold text-background bg-primary rounded-xl hover:opacity-90 transition-opacity text-lg disabled:opacity-50 disabled:cursor-not-allowed"
                        >
                            {logout.isPending ? "Вихід..." : "Вийти"}
                        </button>
                    </form>
                </div>
            </div>
        </div>
    )
}