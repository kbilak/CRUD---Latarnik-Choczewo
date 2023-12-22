import axios, { AxiosResponse } from 'axios';

interface AuthResponse {
  email: string;
  role: string;
}

export interface LoginCredentials {
  email: string;
  password: string;
}

export interface TokenCredentials {
    token: string;
}

export async function login(email: string, password: string, token: string): Promise<AuthResponse | null> {
  try {
    const headers = {
      Authorization: `Bearer ${token}`,
    };

    const data: LoginCredentials = { email, password };

    const response: AxiosResponse<AuthResponse> = await axios.post(
      'http://127.0.0.1:8000/auth/login/',
      data,
      { headers }
    );

    return response.data;
  } catch (error) {
    console.error('Error during login:', error);
    return null;
  }
}