"use client"

import SearchIcon from "@/app/icons/SearchIcon";
import LocationIcon from "@/app/icons/LocationIcon";
import {JSX, useState} from "react";

interface FilterButtonProps {
    title: string;

}

export default function SavedPlacesPage() {
    return (
        <>
            <div className="bg-white text-[#7F7F7F] h-11 rounded-xl overflow-hidden shadow-[0_0_10px_rgba(0,0,0,0.2)] flex flex-row items-center p-1 px-2 font-semibold text-lg">
                <div className="flex flex-[4] flex-row gap-3 items-center border-r-1 border-[#7F7F7F]">
                    <SearchIcon />
                    <input type="text" placeholder="Search" className="w-full focus:outline-none" />
                </div>
                <div className="flex flex-1 flex-row  items-center">
                    <LocationIcon className="mx-3"/>
                    <input type="text" placeholder="Location" className="w-full focus:outline-none"/>
                    <button className="bg-primary rounded-lg px-2.5 py-2 flex justify-center items-center text-white ml-0.5">
                        <SearchIcon className="w-4.5 h-4.5"/>
                    </button>
                </div>
            </div>
            <div className="flex flex-row items-center gap-2 mt-3">
                <FilterButton title={"All"}/>
                <FilterButton title={"Park"}/>
                <FilterButton title={"Hotel"}/>
                <FilterButton title={"Hotel"}/>
                <FilterButton title={"Zalupa"}/>
                <FilterButton title={"Restaurant"}/>
                <FilterButton title={"Other"}/>
            </div>
        </>
    )
}

function FilterButton( { title } : FilterButtonProps) : JSX.Element {
    const [isActive, setActive] = useState(false);
    const activeClass : string = isActive
        ? "bg-primary text-white"
        : "bg-white text-primary";

    return (
        <div>
            <button className={`h-8 px-3 text-primary text-lg overflow-hidden shadow-[0_0_10px_rgba(0,0,0,0.2)] 
            rounded-xl ${activeClass}`}
                    onClick={() => setActive(!isActive)}
            >

                {title}
            </button>

        </div>
    )
}