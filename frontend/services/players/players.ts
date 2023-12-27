// Importing axios for making HTTP requests and AxiosResponse for type checking the responses
import axios, { AxiosResponse } from 'axios';

// Defining the Player interface to type check our player objects
interface Player {
  id: string;
  name: string | null;
  position: string | null;
  status: string | null;
  image: string | null;
  number: number | null;
}

// Function to get all players from the API
export async function getPlayers(): Promise<Player[] | null> {
  try {
    // Making a GET request to the players endpoint
    const response: AxiosResponse<Player[]> = await axios.get('http://127.0.0.1:8000/players/players/');

    // Returning the data from the response
    return response.data;
  } catch (error) {
    // Logging any errors that occur
    console.error('Error fetching players:', error);
    return null;
  }
}

// Function to create a new player
export async function createPlayer(token: string, playerData: Partial<Player>): Promise<Player | null> {
  try {
    // Setting up the headers for the request
    const headers = {
      Authorization: `Bearer ${token}`,
    };

    // Making a POST request to the create player endpoint
    const response: AxiosResponse<Player> = await axios.post('http://127.0.0.1:8000/players/create/', playerData, { headers });

    // Returning the data from the response
    return response.data;
  } catch (error) {
    // Logging any errors that occur
    console.error('Error creating player:', error);
    return null;
  }
}

// Function to update a player
export async function updatePlayer(token: string, playerData: Partial<Player>): Promise<Player | null> {
  try {
    // Setting up the headers for the request
    const headers = {
      Authorization: `Bearer ${token}`, 
    };

    // Making a PUT request to the update player endpoint
    const response: AxiosResponse<Player> = await axios.put(`http://127.0.0.1:8000/players/${playerData.id}/update/`, playerData, { headers });

    // Returning the data from the response
    return response.data;
  } catch (error) {
    // Logging any errors that occur
    console.error('Error updating player:', error);
    return null;
  }
}

// Function to delete a player
export async function deletePlayer(token: string, playerId: string): Promise<boolean> {
  try {
    // Setting up the headers for the request
    const headers = {
      Authorization: `Bearer ${token}`, 
    };

    // Making a DELETE request to the delete player endpoint
    await axios.delete(`http://127.0.0.1:8000/players/${playerId}/delete/`, { headers });

    // If the request is successful, return true
    return true;
  } catch (error) {
    // Logging any errors that occur
    console.error('Error deleting player:', error);
    return false;
  }
}