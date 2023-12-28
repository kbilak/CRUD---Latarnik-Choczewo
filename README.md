# Aplikacja typu CRUD - Latarnik Choczewo (lista zawodników)

Aplikacja stworzona w ramach zadania rekrutacyjnego. Wyświetlanie, dodawanie, edycja i usuwanie zawodników/trenerów.



## Demo + dane logowania

- Frontend (właściwa aplikacja) - https://crud-latarnik-choczewo.vercel.app/auth/login 
    - Admin
        - email: admin@admin.pl
        - hasło: admin1234
    - Normalny
        - email: normal@normal.pl
        - hasło: normal1234
- Backend (panel administracyjny) - https://api.crud.dipit.dev/admin/
    - email: admin@admin.pl
    - hasło: admin1234



## Funkcjonalności - frontend

- Sortowanie danych,
- Filtrowanie danych,
- Dodawanie/edycja/usuwanie zawodników/trenerów,
- Logowanie/rejestracja,
- Zmiana liczby wyświetlanych rekordów na jednej stronie,
- Paginacja,
- Wyszukiwanie rekordów,
- Sortowanie, filtrowanie, wyszukiwanie oraz paginacja wykonane od podstaw - bez użycia żadnych gotowych komponentów np. z Vuetify (v-data-table),
- Dodawanie zdjęcia zawodnika/trenera - wybieranie z dysku, ewentualne przycięcie zdjęcie (cropper) i wysyłka zdjęcia do backendu,
- Pełna responsywność na urządzeniach mobilnych,
- Wielojęzykowość - zmiana wyświetlanego języka bez potrzeby przeładowania strony,
- Operacje na zawodnikach lub trenerach tylko dla wybranego typu konta (admin/normalny); wyświetlanie danych trenerów tylko dla adminów,
- Możliwość wylogowania się.

## Funkcjonalności - backend

- Wygodny panel administracyjny (Django),
- Możliwość zarządzania zawodnikami, trenerami oraz tłumaczeniami,
- Tłumaczenia: dodawanie kodów tłumaczeń wraz z automatycznymi tłumaczeniami w wielu językach,
- System tokenów - żądania wysyłane z frontendu są sprawdzane pod kątem poprawnego tokenu - bez poprawnego tokenu żądanie nie zostanie wykonanem.

## Planowane

- WebSocket - komunikacja 'live' miedzy użytkownikami korzystającymi z aplikacji - powiadomienia o edycji/dodaniu/usunięciu rekordu z bazy danych - z wykorzystaniem Django Channel/Redis
- Theme switcher - motyw jasny/ciemny



## Lokalna instalacja

Frontend

```bash
  cd frontend/
  npm install
  npm run dev
```
Backend (lokalna baza danych)

```bash
  cd backend/
  python -m venv venv
  source venv/bin/activate
  pip install -r requirements.txt
  python manage.py makemigrations && python manage.py migrate
  python manage.py runserver
```


    
## Tech Stack

**Frontend:** Nuxt 3.8, TypeScript, TailwindCSS, daisyUI, Vue 3.3, Vuetify 3.4, Pinia 2.1

**Backend:** Python 3.11, Django 4, Django REST framework

**Baza danych:** PostgreSQL

**Planowane:** Django Channels, Redis