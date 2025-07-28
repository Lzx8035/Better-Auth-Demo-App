import Link from "next/link";

export default function HomePage() {
  return (
    <main className="p-6">
      <h1 className="text-2xl font-bold">🏠 Welcome to Better Auth Demo</h1>
      <p className="mt-2">
        Try{" "}
        <Link href="/login" className="underline text-blue-600">
          Login
        </Link>{" "}
        or{" "}
        <Link href="/register" className="underline text-blue-600">
          Register
        </Link>
        .
      </p>
    </main>
  );
}
