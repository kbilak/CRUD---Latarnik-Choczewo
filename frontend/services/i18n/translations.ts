import axios, { AxiosResponse } from 'axios';

interface TranslationItem {
  code: string;
  translation: string;
}

interface TranslationResponse {
  name: string;
  code: string;
  translations: TranslationItem[];
}

export interface Translations {
  name: string;
  code: string;
  translations: TranslationItem[];
}

export async function fetchTranslations(): Promise<Translations[]> {
  try {
    const response: AxiosResponse<TranslationResponse[]> = await axios.get(
      'http://127.0.0.1:8000/translation/translations/'
    );

    return response.data;
  } catch (error) {
    console.error('Error fetching translations:', error);
    return [];
  }
}