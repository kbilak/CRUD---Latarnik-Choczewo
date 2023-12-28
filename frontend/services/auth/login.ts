// Importing necessary modules and types from axios
import axios, { AxiosResponse, AxiosError } from 'axios';

// Defining the AuthResponse interface to type check the response from the API
interface AuthResponse {
  email: string;
  role: string;
}

// Exporting the LoginCredentials interface to be used elsewhere in our application
export interface LoginCredentials {
  email: string;
  password: string;
}

// Exporting the TokenCredentials interface to be used elsewhere in our application
export interface TokenCredentials {
    token: string;
}

// Define the base URL
const BASE_URL = 'https://api.crud.dipit.dev';

// Defining an async function to perform login
export async function login(email: string, password: string, token: string): Promise<AuthResponse | null> {
  try {
    // Setting up the headers for the request
    const headers = {
      Authorization: `Bearer ${token}`,
    };

    // Defining the data to be sent with the request
    const data: LoginCredentials = { email, password };

    // Making a POST request to the login endpoint
    const response: AxiosResponse<AuthResponse> = await axios.post(
      `${BASE_URL}/auth/login/`,
      data,
      { headers }
    );

    // If the request is successful, return the data from the response
    return response.data;
  } catch (error: any) {
    // If an error occurs, cast it to an AxiosError
    const axiosError = error as AxiosError;
    // If the error has a response (i.e., it's an HTTP error), log the response data
    if (axiosError.response) {
      console.error('Error during login:', axiosError.response.data);
    } else {
      // If the error doesn't have a response (i.e., it's a network error), log the error message
      console.error('Error during login:', axiosError.message);
    }
    // Return null to indicate that the login was not successful
    return null;
  }
}