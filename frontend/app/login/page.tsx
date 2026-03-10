import Image from 'next/image'
import Link from "next/link";

export default function LoginPage() {

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
                            Швидше тисни "Увійти" і в мандрівочку ходи
                        </h2>
                        <p className="opacity-90">
                            Якщо у вас ще немає акаунту, худко тисни реєстрацію та приєднюйся до нас
                        </p>
                    </div>
                    <button className="self-end py-2 px-8 mt-4 font-semibold text-primary bg-background rounded-xl hover:bg-opacity-90 transition-colors">
                        <Link
                        href="/register">
                            Зареєструватись
                        </Link>
                    </button>
                </div>

                <div className="w-full md:w-1/2 bg-background p-12 lg:p-20 flex flex-col justify-center shadow-[0_0_40px_rgba(0,0,0,0.2)]">
                    <h1 className="text-center font-semibold text-4xl mb-24 text-black">Вхід</h1>

                    <form className="flex flex-col gap-6">
                        <div className="flex flex-col gap-2">
                            <input
                                type="email"
                                placeholder="Електронна пошта"
                                className="w-full border-primary border rounded-md py-3 px-4 text-base outline-none focus:ring-2 ring-primary/20 transition-all"
                                required
                            />
                        </div>

                        <div className="flex flex-col gap-2">
                            <input
                                type="password"
                                placeholder="Пароль"
                                className="w-full border-primary border rounded-md py-3 px-4 text-base outline-none focus:ring-2 ring-primary/20 transition-all"
                                required
                            />
                        </div>

                        <div className="flex items-center justify-between w-full text-sm">
                            <label className="flex items-center gap-2 cursor-pointer group">
                                <input
                                    type="checkbox"
                                    id="remember-me"
                                    className="w-4 h-4 cursor-pointer accent-primary"
                                />
                                <span className="group-hover:text-primary transition-colors">Запам'ятати мене</span>
                            </label>
                            <a href="#" className="text-primary hover:underline font-medium">
                                Забули пароль?
                            </a>
                        </div>

                        <button
                            type="submit"
                            className="w-full md:w-max md:self-center mt-10 py-2 px-6 font-semibold text-background bg-primary rounded-xl hover:opacity-90 transition-opacity text-lg"
                        >
                            Увійти
                        </button>
                    </form>
                </div>
            </div>
        </div>
    )
}