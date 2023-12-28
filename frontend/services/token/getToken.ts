// Importing necessary modules and types from axios
import axios, { AxiosResponse, AxiosError } from 'axios';

// Defining the interface for the response data
interface TokenResponse {
	token: string;
}

// Define the base URL
const BASE_URL = 'https://api.crud.dipit.dev';

// Defining an async function to get the token
export async function getToken(): Promise<string | null> {
	try {
		// Making a POST request to the token endpoint
		const response: AxiosResponse<TokenResponse> = await axios.post(
			`${BASE_URL}/token/get/`
		);

		// If the request is successful, return the token
		return response.data.token;
	} catch (error: any) {
		// If an error occurs, cast it to an AxiosError
		const axiosError = error as AxiosError;
		// If the error has a response (i.e., it's an HTTP error), log the response data
		if (axiosError.response) {
			console.error('Error fetching token:', axiosError.response.data);
		} else {
			// If the error doesn't have a response (i.e., it's a network error), log the error message
			console.error('Error fetching token:', axiosError.message);
		}
		// Return null to indicate that no token was fetched
		return null;
	}
}