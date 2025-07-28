import { cookies } from "next/headers";
import { redirect } from "next/navigation";
import LogoutButton from "@/components/LogoutButton";

export default async function DashboardPage() {
  const token = (await cookies()).get("ba_token")?.value;

  console.log(token);

  const res = await fetch("http://127.0.0.1:5000/api/me", {
    headers: {
      Authorization: `Bearer ${token}`,
      "Content-Type": "application/json",
    },
    credentials: "include",
    mode: "cors",
    // 避免缓存用户信息
    cache: "no-store",
  });

  console.log(res);

  if (!res.ok) {
    redirect("/login");
  }

  const { user } = await res.json();

  return (
    <main className="p-6">
      <div className="flex justify-between items-start mb-6">
        <div>
          <h1 className="text-2xl font-bold">👋 Welcome, {user.email}</h1>
          <p className="mt-2 text-gray-600">Your role: {user.role}</p>
          <p className="mt-2 text-sm text-gray-500">
            Permissions: {user.permissions.join(", ")}
          </p>
        </div>
        <LogoutButton />
      </div>
    </main>
  );
}
