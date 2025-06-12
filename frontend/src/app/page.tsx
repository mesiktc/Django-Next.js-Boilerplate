import Image from "next/image";

export default function Home() {
  return (
    <main className="flex min-h-screen flex-col items-center justify-center p-24">
      <h1 className="text-4xl font-bold mb-4">Django + Next.js Boilerplate</h1>
      <p className="text-lg">Welcome! This is a fullstack starter with JWT Auth, Docker, and more.</p>
    </main>
  );
}
