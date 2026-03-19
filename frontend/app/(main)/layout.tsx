// app/(main)/layout.tsx (З навігацією + AuthGuard)

import Header from "@/app/components/Header";
import SidePanel from "@/app/components/SidePanel";
import AuthGuard from "@/app/components/guards/AuthGuard";

export default function MainLayout({ children }: { children: React.ReactNode }) {
    return (
        <AuthGuard>
            <div className="flex flex-col h-screen overflow-hidden bg-[#F3E8FF]">
                <Header />
                <div className="flex flex-1 overflow-hidden">
                    <aside className="h-full p-9 pr-0">
                        <SidePanel />
                    </aside>
                    <main className="flex-1 overflow-y-auto p-9">
                        {children}
                    </main>
                </div>
            </div>
        </AuthGuard>
    );
}