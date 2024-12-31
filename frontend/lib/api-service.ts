import axios from 'axios';

const API_BASE_URL = process.env.NEXT_PUBLIC_API_URL || 'http://127.0.0.1:5000';

export type Student = {
  id?: string;
  firstName: string;
  lastName: string;
  email: string;
  phone: string;
  dateOfBirth: string;
  address: string;
  hasLicense: boolean;
  licenseNumber?: string;
  preferredTransmission: 'automatic' | 'manual';
}

export class ApiService {
  private api = axios.create({
    baseURL: API_BASE_URL,
    headers: {
      'Content-Type': 'application/json',
    },
    withCredentials: true,
  });

  async submitRegistration(data: Student): Promise<Student> {
    try {
      const response = await this.api.post('/student/register', data);
      return response.data;
    } catch (error) {
      if (axios.isAxiosError(error)) {
        throw new Error(error.response?.data?.error || 'Registration failed');
      }
      throw error;
    }
  }

  async getStudent(studentId: string): Promise<Student> {
    try {
      const response = await this.api.get(`/student/${studentId}`);
      return response.data;
    } catch (error) {
      if (axios.isAxiosError(error)) {
        throw new Error(error.response?.data?.error || 'Failed to fetch student');
      }
      throw error;
    }
  }

  async getAllStudents(): Promise<Student[]> {
    try {
      const response = await this.api.get('/student');
      return response.data;
    } catch (error) {
      if (axios.isAxiosError(error)) {
        throw new Error(error.response?.data?.error || 'Failed to fetch students');
      }
      throw error;
    }
  }
}

export const apiService = new ApiService(); 