"use client"
import { useState, KeyboardEvent, useEffect } from "react"
import { Button } from "@/components/ui/button"  // Make sure this Button component supports the className prop
import { Input } from "@/components/ui/input"
import { Card } from "@/components/ui/card"
import io, { Socket } from "socket.io-client"

// Create a socket connection to the backend
const socket: Socket = io("http://127.0.0.1:5000") // Adjust to your backend URL

interface Message {
  text: string
  isBot: boolean
  timestamp: Date
  status?: "not-implemented" | "success"
}

export function Chatbot() {
  const [isOpen, setIsOpen] = useState(false)
  const [messages, setMessages] = useState<Message[]>([
    {
      text: "👋 Hi! I'm DriveBot, your virtual driving assistant. How can I assist you today?",
      isBot: true,
      timestamp: new Date(),
      status: "success"
    },
  ])
  const [input, setInput] = useState("")
  const [isListening, setIsListening] = useState(false)
  let recognition: any

  // Listen for incoming messages from the backend
  useEffect(() => {
    socket.on("message", (message: string) => {
      setMessages(prev => [
        ...prev,
        { text: message, isBot: true, timestamp: new Date() }
      ])
    })

    // Cleanup on unmount
    return () => {
      socket.off("message")
    }
  }, [])

  // Send message to backend and add user message to chat
  const handleSend = () => {
    if (!input.trim()) return

    // Add user message
    const userMessage: Message = {
      text: input,
      isBot: false,
      timestamp: new Date(),
    }

    // Emit the user message to the backend via WebSocket
    socket.emit("message", input, "user123") // Replace "user123" with actual user ID

    setMessages(prev => [...prev, userMessage])
    setInput("") // Clear input field
  }

  const handleKeyPress = (e: KeyboardEvent<HTMLInputElement>) => {
    if (e.key === "Enter") {
      handleSend()
    }
  }

  // Handle mic click and start/stop speech recognition
  const handleMicClick = () => {
    if (isListening) {
      stopListening()
    } else {
      startListening()
    }
  }

  const startListening = () => {
    recognition = new (window.SpeechRecognition || window.webkitSpeechRecognition)()
    recognition.lang = "en-US"
    recognition.continuous = true
    recognition.interimResults = true

    recognition.onstart = () => {
      setIsListening(true)
    }

    recognition.onresult = (event: any) => {
      const transcript = Array.from(event.results)
        .map((result: any) => result[0].transcript)
        .join("")
      setInput(transcript) // Update input with recognized speech
    }

    recognition.onerror = (event: any) => {
      console.error("Speech recognition error", event)
      stopListening()
    }

    recognition.onend = () => {
      stopListening() // Stop listening automatically when recognition ends
    }

    recognition.start()
  }

  const stopListening = () => {
    setIsListening(false)
    if (recognition) recognition.stop()
  }

  if (!isOpen) {
    return (
      <Button
        className="fixed bottom-4 right-4 rounded-full w-16 h-16 shadow-lg text-2xl"
        onClick={() => setIsOpen(true)}
      >
        💬
      </Button>
    )
  }

  return (
    <Card className="fixed bottom-4 right-4 w-96 h-[32rem] shadow-xl flex flex-col bg-white/95 backdrop-blur-sm">
      <div className="p-4 border-b bg-primary text-white flex justify-between items-center rounded-t-lg">
        <div className="flex items-center gap-2">
          <div className="w-3 h-3 rounded-full bg-green-400 animate-pulse" />
          <div className="font-semibold text-lg">DriveBot</div>
        </div>
        <Button
          
          className="text-white hover:text-white/90"
          onClick={() => setIsOpen(false)}
        >
          ✕
        </Button>
      </div>

      <div className="flex-1 overflow-auto p-4 space-y-4">
        {messages.map((message, index) => (
          <div
            key={index}
            className={`flex ${message.isBot ? "justify-start" : "justify-end"}`}
          >
            <div
              className={`max-w-[85%] rounded-lg p-3 ${
                message.isBot ? "bg-gray-100" : "bg-primary text-white"
              }`}
            >
              {message.text}
              {message.status === "not-implemented" && (
                <div className="text-xs mt-1 text-yellow-600 bg-yellow-100 px-2 py-1 rounded">
                  Not implemented yet
                </div>
              )}
            </div>
          </div>
        ))}
      </div>

      <div className="p-4 border-t flex gap-2 bg-gray-50">
        <Input
          value={input}
          onChange={(e) => setInput(e.target.value)}
          onKeyDown={handleKeyPress}
          placeholder="Type a message..."
          className="flex-1"
        />
        <Button
         
          className={`${isListening ? "bg-red-100 text-red-600" : ""}`}
          onClick={handleMicClick}
        >
          🎙
        </Button>
        <Button onClick={handleSend}>Send</Button>
      </div>
    </Card>
  )
}
