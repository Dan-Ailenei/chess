class Client {
    BASE_URL: string;

    constructor() { 
        this.BASE_URL = "http://127.0.0.1:8000";
    }

    get_game_details (game_id: number) {
        return fetch(`${this.BASE_URL}/games/${game_id}`)
           .then((res) => res.json())
    }
}

export const client = new Client();
