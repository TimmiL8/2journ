"use client"

import React, {JSX} from "react";
import Link from "next/link";
import { usePathname } from "next/navigation";
import HomeIcon from "@/app/icons/HomeIcon";
import SearchPlacesIcon from "@/app/icons/SearchPlacesIcon";
import MyTripsIcon from "@/app/icons/MyTripsIcon";
import SavedIcon from "@/app/icons/SavedPlacesIcon";
import ProfileIcon from "@/app/icons/ProfileIcon";
import LogOutIcon from "@/app/icons/LogOutIcon";

interface NavButtonProps {
    navPath: string;
    Icon: React.ElementType;
    title: string;
}

export default function SidePanel() {
    return (
        <div className="h-full w-full max-w-[280px] bg-white rounded-2xl flex flex-col justify-between p-6 overflow-hidden shadow-[0_0_10px_rgba(0,0,0,0.2)]">
            <div className="flex flex-col items-start gap-2">
                <NavButton navPath={"/"} Icon={HomeIcon} title={"Home"} />
                <NavButton navPath={"/search-place"} Icon={SearchPlacesIcon} title={"Search place"} />
                <NavButton navPath={"/my-trips"} Icon={MyTripsIcon} title={"My trips"} />
                <NavButton navPath={"/saved-places"} Icon={SavedIcon} title={"Saved Places"} />
                <NavButton navPath={"/profile"} Icon={ProfileIcon} title={"Profile"} />
            </div>
            <NavButton navPath={"/LogOut"} Icon={LogOutIcon} title={"Log out"} />
        </div>
    )
}

function NavButton({ navPath, Icon, title }: NavButtonProps): JSX.Element {
    const pathname : string = usePathname();
    const isActive: boolean = pathname === navPath;

    const styleIfOnPage = isActive
        ? "text-white bg-primary"
        : "text-black hover:bg-gray-50 transition-colors";

    return (
        <Link href={navPath} className={`flex flex-row h-13 items-center w-full gap-4.5 rounded-lg px-4 ${styleIfOnPage}`}>
            <Icon className={""}/>
            <p className="text-xl font-semibold">{title}</p>
        </Link>
    );
}