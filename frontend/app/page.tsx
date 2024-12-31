"use client"

import { RegistrationForm } from "@/components/registration/RegistrationForm"
import { Navbar } from "@/components/Navbar"
import { Chatbot } from "@/components/Chatbot"

export default function Home() {
  return (
    <>
      <Navbar />
      <main className="min-h-screen bg-gradient-to-b from-gray-50 to-gray-100 pt-24 pb-12">
        <div className="container mx-auto px-4 max-w-3xl">
          <div className="space-y-8">
            <div className="text-center space-y-2">
              <h1 className="text-4xl font-bold bg-gradient-to-r from-primary to-primary/70 text-transparent bg-clip-text">DriveWise</h1>
              <p className="text-muted-foreground text-lg">Streamlining your driving journey, from registration to road-ready!</p>
            </div>
            <div className="text-center text-muted-foreground">
              Complete these steps to get registered. Need help? Try our AI assistant! 👉
            </div>
            <RegistrationForm />
          </div>
        </div>
      </main>
      <Chatbot />
    </>
  )
}
