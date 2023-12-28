// Importing necessary modules and types from axios
import axios, { AxiosResponse, AxiosError } from 'axios';

// Defining the AuthResponse interface to type check the response from the API
interface AuthResponse {
  email: string;
  role: string;
}

// Exporting the SignUpCredentials interface to be used elsewhere in our application
export interface SignUpCredentials {
  email: string;
  password: string;
}

// Exporting the TokenCredentials interface to be used elsewhere in our application
export interface TokenCredentials {
    token: string;
}

// Define the base URL
const BASE_URL = 'http://127.0.0.1:8000';

// Defining an async function to perform sign-up
export async function signUp(email: string, password: string, token: string): Promise<AuthResponse | null> {
  try {
    // Setting up the headers for the request
    const headers = {
      Authorization: `Bearer ${token}`,
    };

    // Defining the data to be sent with the request
    const data: SignUpCredentials = { email, password };

    // Making a POST request to the sign-up endpoint
    const response: AxiosResponse<AuthResponse> = await axios.post(
      `${BASE_URL}/auth/sign-up/`,
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
      console.error('Error during sign-up:', axiosError.response.data);
    } else {
      // If the error doesn't have a response (i.e., it's a network error), log the error message
      console.error('Error during sign-up:', axiosError.message);
    }
    // Return null to indicate that the sign-up was not successful
    return null;
  }
}