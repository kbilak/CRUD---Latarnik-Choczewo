// Importing necessary modules and types from axios
import axios, { AxiosResponse, AxiosError } from 'axios';

// Defining the TranslationItem interface to type check our translation items
interface TranslationItem {
  code: string;
  translation: string;
}

// Defining the TranslationResponse interface to type check the response from the API
interface TranslationResponse {
  name: string;
  code: string;
  translations: TranslationItem[];
}

// Exporting the Translations interface to be used elsewhere in our application
export interface Translations {
  name: string;
  code: string;
  translations: TranslationItem[];
}

// Define the base URL
const BASE_URL = 'http://127.0.0.1:8000';

// Defining an async function to fetch translations from the API
export async function fetchTranslations(): Promise<Translations[]> {
  try {
    // Making a GET request to the translations endpoint
    const response: AxiosResponse<TranslationResponse[]> = await axios.get(
      `${BASE_URL}/translation/translations/`
    );

    // If the request is successful, return the data from the response
    return response.data;
  } catch (error: any) {
    // If an error occurs, cast it to an AxiosError
    const axiosError = error as AxiosError;
    // If the error has a response (i.e., it's an HTTP error), log the response data
    if (axiosError.response) {
      console.error('Error fetching translations:', axiosError.response.data);
    } else {
      // If the error doesn't have a response (i.e., it's a network error), log the error message
      console.error('Error fetching translations:', axiosError.message);
    }
    // Return an empty array to indicate that no translations were fetched
    return [];
  }
}