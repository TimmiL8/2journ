import {JSX} from "react";
import Image from "next/image";
import Link from "next/link";

interface NavButtonProps {
    navPath: string;
    iconPath: string;
    title: string;
}

export default function SidePanel() {
    return (
        <div className="h-full w-full max-w-[280px] bg-white rounded-2xl justify-between p-9">
            <div className="flex flex-col items-start gap-3">
                <NavButton navPath={"/home"} iconPath={"/icons/home-icon.svg"} title={"Home"} />
                <NavButton navPath={"/search-place"} iconPath={"/icons/Search-place-icon.svg"} title={"Search place"} />
                <NavButton navPath={"/my-trips"} iconPath={"/icons/My-trips-icon.svg"} title={"My trips"} />
                <NavButton navPath={"/favourites"} iconPath={"/icons/Favourites-icon.svg"} title={"Favourites"} />
                <NavButton navPath={"/profile"} iconPath={"/icons/Profile-icon.svg"} title={"Profile"} />
            </div>
            <div>
                <p>Log out</p>
            </div>
        </div>
    )
}

function NavButton({navPath, iconPath, title} : NavButtonProps) : JSX.Element {
    return (
        <Link href={navPath} passHref className={"flex flex-row  items-center w-full color-background gap-4.5"}>
            <Image
                src={iconPath}
                width={32}
                height={32}
                alt={title}
            />
            <p className={"text-xl font-semibold"}>{title}</p>
        </Link>
    )
}