# DriveWise Frontend

A modern Next.js-based frontend for the DriveWise driving school registration system.

## Features

- Student Registration Form
- Interactive AI Chatbot
- Modern UI with Tailwind CSS
- Responsive Design

## Tech Stack

- Next.js 14
- TypeScript
- Tailwind CSS
- Shadcn UI Components
- React Hook Form
- Axios for API calls

## Project Structure

```
frontend/
├── app/                # Next.js app directory
├── components/         # React components
│   ├── ui/            # Reusable UI components
│   └── registration/  # Registration-specific components
├── lib/               # Utilities and services
└── public/            # Static assets
```

## Components

### Core Components
- `Navbar`: Main navigation bar
- `RegistrationForm`: Student registration form
- `Chatbot`: AI-powered assistance

### UI Components
- Button
- Card
- Input
- Label
- Checkbox
- Select
- Radio Group
- Form components

## Setup

1. Install dependencies:
```bash
npm install
```

2. Run the development server:
```bash
npm run dev
```

The application will be available at `http://localhost:3000`

## Development Status

### Completed
- Basic UI components
- Registration form layout
- Navigation structure
- Chatbot interface

### In Progress
- Chatbot functionality implementation
- Form validation improvements
- API integration
- User authentication

## Scripts

- `npm run dev` - Start development server
- `npm run build` - Build for production
- `npm run start` - Start production server
- `npm run lint` - Run ESLint

## Dependencies

### Production
- @hookform/resolvers
- axios
- next
- react
- react-hook-form
- tailwind-merge
- zod

### Development
- TypeScript
- ESLint
- Tailwind CSS
- PostCSS

## Contributing

1. Fork the repository
2. Create your feature branch
3. Commit your changes
4. Push to the branch
5. Create a new Pull Request
