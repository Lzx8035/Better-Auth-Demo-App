"use client";

import { useState } from "react";
import Link from "next/link";
import { useRouter } from "next/navigation";
import { useForm } from "react-hook-form";

interface RegisterFormData {
  email: string;
  password: string;
  confirmPassword: string;
}

export default function RegisterPage() {
  const [done, setDone] = useState(false);
  const {
    register,
    handleSubmit,
    formState: { errors, isSubmitting },
    setError,
    watch,
  } = useForm<RegisterFormData>();

  const router = useRouter();
  const password = watch("password");

  const onSubmit = async (data: RegisterFormData) => {
    try {
      const res = await fetch("http://127.0.0.1:5000/api/register", {
        method: "POST",
        body: JSON.stringify({ email: data.email, password: data.password }),
        headers: { "Content-Type": "application/json" },
        credentials: "include",
        mode: "cors",
      });
      const responseData = await res.json();
      console.log(responseData);

      if (!res.ok) throw new Error(responseData.message || "Register failed");
      setDone(true);
      setTimeout(() => router.push("/login"), 1500);
    } catch (err: unknown) {
      if (err instanceof Error) {
        setError("root", { message: err.message });
      } else {
        setError("root", { message: "An unknown error occurred" });
      }
    }
  };

  return (
    <main className="p-6">
      <h1 className="text-xl font-bold mb-4">📝 Register</h1>
      <form onSubmit={handleSubmit(onSubmit)} className="space-y-3">
        <div>
          <input
            {...register("email", {
              required: "Email is required",
              pattern: {
                value: /^[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}$/i,
                message: "Invalid email address",
              },
            })}
            placeholder="Email"
            className="border px-2 py-1 w-full"
          />
          {errors.email && (
            <p className="text-red-600 text-sm mt-1">{errors.email.message}</p>
          )}
        </div>

        <div>
          <input
            type="password"
            {...register("password", {
              required: "Password is required",
              minLength: {
                value: 6,
                message: "Password must be at least 6 characters",
              },
            })}
            placeholder="Password"
            className="border px-2 py-1 w-full"
          />
          {errors.password && (
            <p className="text-red-600 text-sm mt-1">
              {errors.password.message}
            </p>
          )}
        </div>

        <div>
          <input
            type="password"
            {...register("confirmPassword", {
              required: "Please confirm your password",
              validate: (value) =>
                value === password || "Passwords do not match",
            })}
            placeholder="Confirm Password"
            className="border px-2 py-1 w-full"
          />
          {errors.confirmPassword && (
            <p className="text-red-600 text-sm mt-1">
              {errors.confirmPassword.message}
            </p>
          )}
        </div>

        {errors.root && <p className="text-red-600">{errors.root.message}</p>}

        {done && (
          <p className="text-green-700">Registered! Redirecting to login…</p>
        )}

        <button
          type="submit"
          disabled={isSubmitting}
          className="bg-green-600 text-white px-4 py-1 rounded disabled:opacity-50"
        >
          {isSubmitting ? "Registering..." : "Register"}
        </button>

        <Link href="/login" className="text-blue-600">
          Login
        </Link>
      </form>
    </main>
  );
}
