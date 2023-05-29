<script setup lang="ts">
import SparseMatrix from '../sparse_matrix';
import {client} from '../client';
import {ref} from 'vue';

const props = defineProps<{ matrix: SparseMatrix, game_id: number }>()
const possible_positions = {
    positions: [],
    piece_position: null,
};


const delete_possible_positions = () => {
    for (const position of possible_positions.positions) {
            const [px, py] = position;
            props.matrix.delete(px, py);
    }

    possible_positions.positions = []
    possible_positions.piece_position = null;
}

const get_possible_moves = (x, y) => {
    client.get_piece_possible_moves(props.game_id, x, y)
    .then((data) => {
        delete_possible_positions();

        possible_positions.piece_position = [x, y];
        for (const position of data) {
            const [px, py] = position;
            possible_positions.positions.push(position);
            props.matrix.set(px, py, '*');
        }
    })
}

const move_piece = (x1, y1, x2, y2) => {
    client.move_piece(props.game_id, x1, y1, x2, y2);
}

const piece_click = (x: number, y: number) => {
    const piece = props.matrix.get(x, y);
    if (piece === '*') {
        const [x1, y1] = possible_positions.piece_position;
        move_piece(x1, y1, x, y);
        delete_possible_positions();
    } else if (piece !== null) {
        get_possible_moves(x, y);
    }
    
}


</script>

<template>
        <table class="chess-board">
            <tbody>
                <tr>
                    <th></th>
                    <th>a</th>
                    <th>b</th>
                    <th>c</th>
                    <th>d</th>
                    <th>e</th>
                    <th>f</th>
                    <th>g</th>
                    <th>h</th>
                </tr>
                <tr>
                    <th>8</th>
                    <td @click="piece_click(7, 0)" class="light">{{matrix.get(7, 0)}}</td>
                    <td @click="piece_click(7, 1)" class="dark">{{matrix.get(7, 1)}}</td>
                    <td @click="piece_click(7, 2)" class="light">{{matrix.get(7, 2)}}</td>
                    <td @click="piece_click(7, 3)" class="dark">{{matrix.get(7, 3)}}</td>
                    <td @click="piece_click(7, 4)" class="light">{{matrix.get(7, 4)}}</td>
                    <td @click="piece_click(7, 5)" class="dark">{{matrix.get(7, 5)}}</td>
                    <td @click="piece_click(7, 6)" class="light">{{matrix.get(7, 6)}}</td>
                    <td @click="piece_click(7, 7)" class="dark">{{matrix.get(7, 7)}}</td>
                </tr>
                <tr>
                    <th>7</th>
                    <td @click="piece_click(6, 0)" class="dark">{{matrix.get(6, 0)}}</td>
                    <td @click="piece_click(6, 1)" class="light">{{matrix.get(6, 1)}}</td>
                    <td @click="piece_click(6, 2)" class="dark">{{matrix.get(6, 2)}}</td>
                    <td @click="piece_click(6, 3)" class="light">{{matrix.get(6, 3)}}</td>
                    <td @click="piece_click(6, 4)" class="dark">{{matrix.get(6, 4)}}</td>
                    <td @click="piece_click(6, 5)" class="light">{{matrix.get(6, 5)}}</td>
                    <td @click="piece_click(6, 6)" class="dark">{{matrix.get(6, 6)}}</td>
                    <td @click="piece_click(6, 7)" class="light">{{matrix.get(6, 7)}}</td>
                </tr>
                <tr>
                    <th>6</th>
                    <td @click="piece_click(5, 0)" class="light">{{matrix.get(5, 0)}}</td>
                    <td @click="piece_click(5, 1)" class="dark">{{matrix.get(5, 1)}}</td>
                    <td @click="piece_click(5, 2)" class="light">{{matrix.get(5, 2)}}</td>
                    <td @click="piece_click(5, 3)" class="dark">{{matrix.get(5, 3)}}</td>
                    <td @click="piece_click(5, 4)" class="light">{{matrix.get(5, 4)}}</td>
                    <td @click="piece_click(5, 5)" class="dark">{{matrix.get(5, 5)}}</td>
                    <td @click="piece_click(5, 6)" class="light">{{matrix.get(5, 6)}}</td>
                    <td @click="piece_click(5, 7)" class="dark">{{matrix.get(5, 7)}}</td>
                </tr>
                <tr>
                    <th>5</th>
                    <td @click="piece_click(4, 0)" class="dark">{{matrix.get(4, 0)}}</td>
                    <td @click="piece_click(4, 1)" class="light">{{matrix.get(4, 1)}}</td>
                    <td @click="piece_click(4, 2)" class="dark">{{matrix.get(4, 2)}}</td>
                    <td @click="piece_click(4, 3)" class="light">{{matrix.get(4, 3)}}</td>
                    <td @click="piece_click(4, 4)" class="dark">{{matrix.get(4, 4)}}</td>
                    <td @click="piece_click(4, 5)" class="light">{{matrix.get(4, 5)}}</td>
                    <td @click="piece_click(4, 6)" class="dark">{{matrix.get(4, 6)}}</td>
                    <td @click="piece_click(4, 7)" class="light">{{matrix.get(4, 7)}}</td>
                </tr>
                <tr>
                    <th>4</th>
                    <td @click="piece_click(3, 0)" class="light">{{matrix.get(3, 0)}}</td>
                    <td @click="piece_click(3, 1)" class="dark">{{matrix.get(3, 1)}}</td>
                    <td @click="piece_click(3, 2)" class="light">{{matrix.get(3, 2)}}</td>
                    <td @click="piece_click(3, 3)" class="dark">{{matrix.get(3, 3)}}</td>
                    <td @click="piece_click(3, 4)" class="light">{{matrix.get(3, 4)}}</td>
                    <td @click="piece_click(3, 5)" class="dark">{{matrix.get(3, 5)}}</td>
                    <td @click="piece_click(3, 6)" class="light">{{matrix.get(3, 6)}}</td>
                    <td @click="piece_click(3, 7)" class="dark">{{matrix.get(3, 7)}}</td>
                </tr>
                <tr>
                    <th>3</th>
                    <td @click="piece_click(2, 0)" class="dark">{{matrix.get(2, 0)}}</td>
                    <td @click="piece_click(2, 1)" class="light">{{matrix.get(2, 1)}}</td>
                    <td @click="piece_click(2, 2)" class="dark">{{matrix.get(2, 2)}}</td>
                    <td @click="piece_click(2, 3)" class="light">{{matrix.get(2, 3)}}</td>
                    <td @click="piece_click(2, 4)" class="dark">{{matrix.get(2, 4)}}</td>
                    <td @click="piece_click(2, 5)" class="light">{{matrix.get(2, 5)}}</td>
                    <td @click="piece_click(2, 6)" class="dark">{{matrix.get(2, 6)}}</td>
                    <td @click="piece_click(2, 7)" class="light">{{matrix.get(2, 7)}}</td>
                </tr>
                <tr>
                    <th>2</th>
                    <td @click="piece_click(1, 0)" class="light">{{matrix.get(1, 0)}}</td>
                    <td @click="piece_click(1, 1)" class="dark">{{matrix.get(1, 1)}}</td>
                    <td @click="piece_click(1, 2)" class="light">{{matrix.get(1, 2)}}</td>
                    <td @click="piece_click(1, 3)" class="dark">{{matrix.get(1, 3)}}</td>
                    <td @click="piece_click(1, 4)" class="light">{{matrix.get(1, 4)}}</td>
                    <td @click="piece_click(1, 5)" class="dark">{{matrix.get(1, 5)}}</td>
                    <td @click="piece_click(1, 6)" class="light">{{matrix.get(1, 6)}}</td>
                    <td @click="piece_click(1, 7)" class="dark">{{matrix.get(1, 7)}}</td>
                </tr>
                <tr>
                    <th>1</th>
                    <td @click="piece_click(0, 0)" class="dark">{{matrix.get(0, 0)}}</td>
                    <td @click="piece_click(0, 1)" class="light">{{matrix.get(0, 1)}}</td>
                    <td @click="piece_click(0, 2)" class="dark">{{matrix.get(0, 2)}}</td>
                    <td @click="piece_click(0, 3)" class="light">{{matrix.get(0, 3)}}</td>
                    <td @click="piece_click(0, 4)" class="dark">{{matrix.get(0, 4)}}</td>
                    <td @click="piece_click(0, 5)" class="light">{{matrix.get(0, 5)}}</td>
                    <td @click="piece_click(0, 6)" class="dark">{{matrix.get(0, 6)}}</td>
                    <td @click="piece_click(0, 7)" class="light">{{matrix.get(0, 7)}}</td>
                </tr>
            </tbody>
        </table>

</template>

<style scoped>
.chess-board { border-spacing: 0; border-collapse: collapse; }
.chess-board th { padding: .5em; }
.chess-board th + th { border-bottom: 1px solid #000; }
.chess-board th:first-child,
.chess-board td:last-child { border-right: 1px solid #000; }
.chess-board tr:last-child td { border-bottom: 1px solid; }
.chess-board th:empty { border: none; }
.chess-board td { width: 1.5em; height: 1.5em; text-align: center; font-size: 32px; line-height: 0; cursor: pointer;}
.chess-board .light { background: #eee; }
.chess-board .dark { background: #aaa; }
</style>
