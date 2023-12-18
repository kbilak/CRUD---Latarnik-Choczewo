import axios, { AxiosResponse } from 'axios';

interface Player {
  id: string;
  name: string | null;
  position: string | null;
  status: string | null;
  image: string | null;
  number: number | null;
}

interface TokenCredentials {
  token: string;
}

export async function getPlayers(): Promise<Player[] | null> {
  try {
    const response: AxiosResponse<Player[]> = await axios.get('http://127.0.0.1:8000/players/players/');

    return response.data;
  } catch (error) {
    console.error('Error fetching players:', error);
    return null;
  }
}

export async function createPlayer(token: string, playerData: Partial<Player>): Promise<Player | null> {
  try {
    const data: Partial<Player> & TokenCredentials = { ...playerData, token };
    const response: AxiosResponse<Player> = await axios.post('http://127.0.0.1:8000/players/create/', data);

    return response.data;
  } catch (error) {
    console.error('Error creating player:', error);
    return null;
  }
}

export async function updatePlayer(token: string, playerId: string, playerData: Partial<Player>): Promise<Player | null> {
  try {
    const data: Partial<Player> & TokenCredentials = { ...playerData, token };
    const response: AxiosResponse<Player> = await axios.put(`http://127.0.0.1:8000/players/${playerId}/update/`, data);

    return response.data;
  } catch (error) {
    console.error('Error updating player:', error);
    return null;
  }
}

export async function deletePlayer(token: string, playerId: string): Promise<boolean> {
  try {
    const data: TokenCredentials = { token };
    await axios.delete(`http://127.0.0.1:8000/players/${playerId}/delete/`, { data });

    return true;
  } catch (error) {
    console.error('Error deleting player:', error);
    return false;
  }
}