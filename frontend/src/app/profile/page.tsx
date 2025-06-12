"use client";
import { useEffect, useState } from "react";

export default function ProfilePage() {
  const [user, setUser] = useState<any>(null);
  const [error, setError] = useState("");

  useEffect(() => {
    const access = localStorage.getItem("access");
    if (!access) {
      window.location.href = "/login";
      return;
    }
    fetch(process.env.NEXT_PUBLIC_API_URL + "/profile/", {
      headers: { Authorization: `Bearer ${access}` },
    })
      .then(res => res.json())
      .then(data => {
        if (data.detail) throw new Error(data.detail);
        setUser(data);
      })
      .catch(err => {
        setError("Unauthorized. Please login again.");
        localStorage.removeItem("access");
        localStorage.removeItem("refresh");
        window.location.href = "/login";
      });
  }, []);

  if (!user) return <div className="flex min-h-screen items-center justify-center">Loading...</div>;

  return (
    <main className="flex min-h-screen flex-col items-center justify-center p-4">
      <div className="w-full max-w-md bg-white p-8 rounded shadow">
        <h2 className="text-2xl font-bold mb-6">Profile</h2>
        <div className="mb-2"><b>Email:</b> {user.email}</div>
        <div className="mb-2"><b>Username:</b> {user.username}</div>
        <div className="mb-2"><b>First Name:</b> {user.first_name}</div>
        <div className="mb-2"><b>Last Name:</b> {user.last_name}</div>
        <div className="mb-2"><b>Verified:</b> {user.is_verified ? "Yes" : "No"}</div>
        <button className="mt-4 bg-red-600 text-white py-2 px-4 rounded" onClick={() => {
          localStorage.removeItem("access");
          localStorage.removeItem("refresh");
          window.location.href = "/login";
        }}>Logout</button>
      </div>
    </main>
  );
} 