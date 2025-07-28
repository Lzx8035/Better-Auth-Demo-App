"use client";

import { useRouter } from "next/navigation";
import { removeToken } from "@/auth/auth";

export default function LogoutButton() {
  const router = useRouter();

  const handleLogout = () => {
    removeToken();
    router.push("/login");
  };

  return (
    <button
      type="button"
      onClick={handleLogout}
      className="px-4 py-2 bg-red-500 text-white rounded-md hover:bg-red-600 transition-colors duration-200"
    >
      登出
    </button>
  );
}
