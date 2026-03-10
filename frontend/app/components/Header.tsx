import Image from "next/image";
import Link from "next/link";

export default function Header() {
    return (
        <div className="h-18 w-full bg-primary flex items-center justify-between px-12 ">
                <Image
                    src="/logo.svg"
                    width={86}
                    height={35}
                    alt="logo"
                />

                <Link href="/">
                    <div className="flex gap-2.5 items-center justify-between">
                        <div>
                            <Image
                                src="/pfp-test.jpg"
                                width={43}
                                height={43}
                                alt="pfp"
                                className="rounded-full"
                            />
                        </div>
                        <div className="text-white">
                            <h3 className="text-base leading-tight">Username</h3>
                            <p className="text-xs leading-tight">Travel master</p>
                        </div>
                    </div>
                </Link>
        </div>
    )
}