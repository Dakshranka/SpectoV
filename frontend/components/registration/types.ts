export interface FormData {
  // Personal Info
  firstName: string
  lastName: string
  email: string
  phone: string
  dateOfBirth: string
  gender: string
  address: string
  
  // Driving Experience
  hasLicense: string
  licenseNumber: string
  yearsOfExperience: string
  previousLessons: string
  challenges: string
  
  // Preferences
  transmissionPreference: string
  instructorGenderPreference: string
  lessonTimePreference: string
  notes: string
  termsAccepted: boolean
} 