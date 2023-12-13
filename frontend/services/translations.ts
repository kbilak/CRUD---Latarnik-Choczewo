import axios, { AxiosResponse } from 'axios';

export interface Translations {
  [key: string]: string;
}

export async function fetchTranslations(locale: string): Promise<Translations> {
  try {
    const response: AxiosResponse<{ translations: Translations }> = await axios.get(
      `http://127.0.0.1:8000/translation/${locale}/`
    );
    return response.data.translations;
  } catch (error) {
    console.error('Error fetching translations:', error);
    return {};
  }
}
