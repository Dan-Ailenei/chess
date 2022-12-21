<script setup lang="ts">
import { ref } from 'vue'
import { computed } from 'vue'
import SparseMatrix from '../sparse_matrix';

defineProps<{ matrix: SparseMatrix }>()

type Position = [number, number];
type Table = Map<Position, string>;



const get_table = () => {
    const table = new Map<Position, string>();
    
    // for (const [key, value] of Object.entries({[3, 3]: 'caca', [5, 5]: 'caca'})) {
    //     console.log(`${key}: ${value}`);
    // }

    table.set([3, 3], 'caca');
    table.set([5, 5], 'caca');
    return table;
}



// const publishedBooksMessage = computed(() => {
//   return 
// })

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
                    <td class="light">{{matrix.get(7, 0)}}</td>
                    <td class="dark">{{matrix.get(7, 1)}}</td>
                    <td class="light">{{matrix.get(7, 2)}}</td>
                    <td class="dark">{{matrix.get(7, 3)}}</td>
                    <td class="light">{{matrix.get(7, 4)}}</td>
                    <td class="dark">{{matrix.get(7, 5)}}</td>
                    <td class="light">{{matrix.get(7, 6)}}</td>
                    <td class="dark">{{matrix.get(7, 7)}}</td>
                </tr>
                <tr>
                    <th>7</th>
                    <td class="dark">{{matrix.get(6, 0)}}</td>
                    <td class="light">{{matrix.get(6, 1)}}</td>
                    <td class="dark">{{matrix.get(6, 2)}}</td>
                    <td class="light">{{matrix.get(6, 3)}}</td>
                    <td class="dark">{{matrix.get(6, 4)}}</td>
                    <td class="light">{{matrix.get(6, 5)}}</td>
                    <td class="dark">{{matrix.get(6, 6)}}</td>
                    <td class="light">{{matrix.get(6, 7)}}</td>
                </tr>
                <tr>
                    <th>6</th>
                    <td class="light">{{matrix.get(5, 0)}}</td>
                    <td class="dark">{{matrix.get(5, 1)}}</td>
                    <td class="light">{{matrix.get(5, 2)}}</td>
                    <td class="dark">{{matrix.get(5, 3)}}</td>
                    <td class="light">{{matrix.get(5, 4)}}</td>
                    <td class="dark">{{matrix.get(5, 5)}}</td>
                    <td class="light">{{matrix.get(5, 6)}}</td>
                    <td class="dark">{{matrix.get(5, 7)}}</td>
                </tr>
                <tr>
                    <th>5</th>
                    <td class="dark">{{matrix.get(4, 0)}}</td>
                    <td class="light">{{matrix.get(4, 1)}}</td>
                    <td class="dark">{{matrix.get(4, 2)}}</td>
                    <td class="light">{{matrix.get(4, 3)}}</td>
                    <td class="dark">{{matrix.get(4, 4)}}</td>
                    <td class="light">{{matrix.get(4, 5)}}</td>
                    <td class="dark">{{matrix.get(4, 6)}}</td>
                    <td class="light">{{matrix.get(4, 7)}}</td>
                </tr>
                <tr>
                    <th>4</th>
                    <td class="light">{{matrix.get(3, 0)}}</td>
                    <td class="dark">{{matrix.get(3, 1)}}</td>
                    <td class="light">{{matrix.get(3, 2)}}</td>
                    <td class="dark">{{matrix.get(3, 3)}}</td>
                    <td class="light">{{matrix.get(3, 4)}}</td>
                    <td class="dark">{{matrix.get(3, 5)}}</td>
                    <td class="light">{{matrix.get(3, 6)}}</td>
                    <td class="dark">{{matrix.get(3, 7)}}</td>
                </tr>
                <tr>
                    <th>3</th>
                    <td class="dark">{{matrix.get(2, 0)}}</td>
                    <td class="light">{{matrix.get(2, 1)}}</td>
                    <td class="dark">{{matrix.get(2, 2)}}</td>
                    <td class="light">{{matrix.get(2, 3)}}</td>
                    <td class="dark">{{matrix.get(2, 4)}}</td>
                    <td class="light">{{matrix.get(2, 5)}}</td>
                    <td class="dark">{{matrix.get(2, 6)}}</td>
                    <td class="light">{{matrix.get(2, 7)}}</td>
                </tr>
                <tr>
                    <th>2</th>
                    <td class="light">{{matrix.get(1, 0)}}</td>
                    <td class="dark">{{matrix.get(1, 1)}}</td>
                    <td class="light">{{matrix.get(1, 2)}}</td>
                    <td class="dark">{{matrix.get(1, 3)}}</td>
                    <td class="light">{{matrix.get(1, 4)}}</td>
                    <td class="dark">{{matrix.get(1, 5)}}</td>
                    <td class="light">{{matrix.get(1, 6)}}</td>
                    <td class="dark">{{matrix.get(1, 7)}}</td>
                </tr>
                <tr>
                    <th>1</th>
                    <td class="dark">{{matrix.get(0, 0)}}</td>
                    <td class="light">{{matrix.get(0, 1)}}</td>
                    <td class="dark">{{matrix.get(0, 2)}}</td>
                    <td class="light">{{matrix.get(0, 3)}}</td>
                    <td class="dark">{{matrix.get(0, 4)}}</td>
                    <td class="light">{{matrix.get(0, 5)}}</td>
                    <td class="dark">{{matrix.get(0, 6)}}</td>
                    <td class="light">{{matrix.get(0, 7)}}</td>
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
.chess-board td { width: 1.5em; height: 1.5em; text-align: center; font-size: 32px; line-height: 0;}
.chess-board .light { background: #eee; }
.chess-board .dark { background: #aaa; }
</style>
