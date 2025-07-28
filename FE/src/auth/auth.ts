import Cookies from "js-cookie";
import type { User } from "@/types";

const TOKEN_KEY = "ba_token";

export function saveToken(token: string) {
  Cookies.set(TOKEN_KEY, token, { expires: 7 });
}

export function getToken(): string | undefined {
  return Cookies.get(TOKEN_KEY);
}

export function removeToken() {
  Cookies.remove(TOKEN_KEY);
}

export async function fetchUser(): Promise<User | null> {
  const token = getToken();
  if (!token) return null;

  try {
    const res = await fetch("http://127.0.0.1:5000/api/me", {
      headers: {
        Authorization: `Bearer ${token}`,
        "Content-Type": "application/json",
      },
      credentials: "include",
      mode: "cors",
    });

    if (!res.ok) throw new Error("Unauthorized");

    const data = await res.json();
    return data.user;
  } catch (err) {
    console.error("Failed to fetch user:", err);
    return null;
  }
}
