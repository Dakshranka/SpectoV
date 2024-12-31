import { Button } from "@/components/ui/button"

export function Navbar() {
  return (
    <nav className="border-b bg-white/75 backdrop-blur-md fixed top-0 w-full z-50">
      <div className="container mx-auto px-4 h-16 flex items-center justify-between">
        <div className="flex items-center space-x-8">
          <div className="text-xl font-bold text-primary">🚗 DriveWise</div>
          <div className="hidden md:flex space-x-6">
            <a href="#" className="text-muted-foreground hover:text-primary transition">Home</a>
            <a href="#" className="text-muted-foreground hover:text-primary transition">About</a>
            <a href="#" className="text-muted-foreground hover:text-primary transition">Services</a>
            <a href="#" className="text-muted-foreground hover:text-primary transition">Contact</a>
          </div>
        </div>
        <div className="flex items-center space-x-4">
          <Button variant="outline" size="sm">Sign In</Button>
          <Button size="sm">Get Started</Button>
        </div>
      </div>
    </nav>
  )
} 