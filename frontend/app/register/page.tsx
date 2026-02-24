import Image from "next/image";
import Link from "next/link";

export default function registerPage() {
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

                    <form className="flex flex-col gap-6">
                        <div className="flex flex-col gap-6">
                            <input
                                type="text"
                                placeholder="Імʼя користувача"
                                className="w-full border-primary border rounded-md py-3 px-4 text-base outline-none
                                focus:ring-2 ring-primary/20 transition-all"
                                required
                            />

                            <input
                                type="email"
                                placeholder="Електронна пошта"
                                className="w-full border-primary border rounded-md py-3 px-4 text-base outline-none
                                 focus:ring-2 ring-primary/20 transition-all"
                                required
                            />

                            <input
                                type="password"
                                placeholder="Пароль"
                                className="w-full border-primary border rounded-md py-3 px-4 text-base outline-none
                                 focus:ring-2 ring-primary/20 transition-all"
                                required
                            />
                        </div>


                        <div className="w-full text-sm"> {/* Прибрав justify-between, бо тут він не потрібен */}
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

                        <button
                            type="submit"
                            className="w-full md:w-max md:self-center mt-6 py-2 px-10 font-semibold text-background
                         bg-primary rounded-xl hover:opacity-90 transition-opacity text-lg"
                        >
                            Зареєструватись
                        </button>
                    </form>
                </div>
            </div>
        </div>
    )
}