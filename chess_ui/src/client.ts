class Client {
    BASE_URL: string;

    constructor() { 
        this.BASE_URL = "http://127.0.0.1:8000";
    }

    get_game_details (game_id: number) {
        return fetch(`${this.BASE_URL}/games/${game_id}`)
           .then((res) => res.json())
    }

    get_piece_possible_moves(game_id: number, x: number, y: number) {
        return fetch(`${this.BASE_URL}/games/${game_id}/pieces/${x}-${y}`)
        .then((res) => res.json())
    }

    move_piece(game_id:number, x1:number, y1:number, x2:number, y2:number) {
        return fetch(`${this.BASE_URL}/games/${game_id}/moves/${x1}-${y1};${x2}-${y2}`,
            {method: 'POST'}
        )
        .then((res) => res.json())
    }
}

export const client = new Client();
