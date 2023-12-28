// Importing axios for making HTTP requests and AxiosResponse for type checking the responses
import axios, { AxiosResponse } from 'axios';

// Defining the Coach interface to type check our coach objects
interface Coach {
    id: string;
    name: string | null;
    type: string | null;
    status: string | null;
    image: string | null;
}

// Define the base URL
const BASE_URL = 'https://api.crud.dipit.dev';

// Function to get all coaches from the API
export async function getCoaches(): Promise<Coach[] | null> {
    try {
        // Making a GET request to the coaches endpoint
        const response: AxiosResponse<Coach[]> = await axios.get(`${BASE_URL}/players/coaches/`);

        // Returning the data from the response
        return response.data;
    } catch (error) {
        // Logging any errors that occur
        console.error('Error fetching coaches:', error);
        return null;
    }
}

// Function to create a new coach
export async function createCoach(token: string, coachData: Partial<Coach>): Promise<Coach | null> {
    try {
        // Setting up the headers for the request
        const headers = {
            Authorization: `Bearer ${token}`,
        };

        // Making a POST request to the create coach endpoint
        const response: AxiosResponse<Coach> = await axios.post(`${BASE_URL}/players/coach/create/`, coachData, { headers });

        // Returning the data from the response
        return response.data;
    } catch (error) {
        // Logging any errors that occur
        console.error('Error creating coach:', error);
        return null;
    }
}

// Function to update a coach
export async function updateCoach(token: string, coachData: Partial<Coach>): Promise<Coach | null> {
    try {
        // Setting up the headers for the request
        const headers = {
            Authorization: `Bearer ${token}`, 
        };

        // Making a PUT request to the update coach endpoint
        const response: AxiosResponse<Coach> = await axios.put(`${BASE_URL}/players/coach/${coachData.id}/update/`, coachData, { headers });

        // Returning the data from the response
        return response.data;
    } catch (error) {
        // Logging any errors that occur
        console.error('Error updating coach:', error);
        return null;
    }
}

// Function to delete a coach
export async function deleteCoach(token: string, coachId: string): Promise<boolean> {
    try {
        // Setting up the headers for the request
        const headers = {
            Authorization: `Bearer ${token}`, 
        };

        // Making a DELETE request to the delete coach endpoint
        await axios.delete(`${BASE_URL}/players/coach/${coachId}/delete/`, { headers });

        // If the request is successful, return true
        return true;
    } catch (error) {
        // Logging any errors that occur
        console.error('Error deleting coach:', error);
        return false;
    }
}