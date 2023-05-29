<script setup lang="ts">
import SparseMatrix from '../sparse_matrix'
import GameTable from './GameTable.vue'
import { ref, computed } from 'vue'
import {client} from '../client';


const props = defineProps<{ game_id: number }>()

const piece_translation = {
    'King,1': '♔',
    'King,2': '♚',

    'Rook,1': '♖',
    'Rook,2': '♜',

    'Bishop,1': '♗',
    'Bishop,2': '♝',

    'Knight,1': '♘',
    'Knight,2': '♞',

    'Queen,1': '♕',
    'Queen,2': '♛',
    
    'Pawn,1': '♙',
    'Pawn,2': '♟',
}

const matrix = ref(new SparseMatrix(8, 8));

function parseTuple(t) {
    var items = t.replace(/^\(|\)$/g, "").split("),(");
    items.forEach(function(val, index, array) {
       array[index] = val.split(",").map(Number);
    });
    return items;
}

const TEAMS = {
    WHITE: 1,
    BLACK: 2,
}


client.get_game_details(props.game_id)
.then(table_data=> {
    console.log(table_data.table_data.pieces);
    for (const [key, value] of Object.entries(table_data.table_data.pieces)) {
        
        const [x, y] = parseTuple(key)[0];
        console.log(`${value}`);
        matrix.value.set(x, y, piece_translation[`${value}`]);
    }
});


</script>

<template>
    <GameTable :matrix="matrix" :game_id="game_id"/>  
</template>

<style scoped>

</style>
