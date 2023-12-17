import axios, { AxiosResponse } from 'axios';

interface TokenResponse {
	token: string;
}

export async function getToken(): Promise<string | null> {
	try {
		const response: AxiosResponse<TokenResponse> = await axios.get(
			'http://127.0.0.1:8000/token/get/'
		);

		return response.data.token;
	} catch (error) {
		console.error('Error fetching token:', error);
		return null;
	}
}
