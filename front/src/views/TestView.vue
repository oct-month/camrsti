<template>
    <table>
        <thead>
            <th>Name</th>
            <th>Index</th>
        </thead>
        <tbody>
            <tr v-for="(row,idx) in rows" :key="idx">
                <td>{{ row.Name }}</td>
                <td>{{ row.Index }}</td>
            </tr>
        </tbody>
        <tfoot>
            <td colspan={2}>
                <button @click="exportFile">Export XLSX</button>
            </td>
        </tfoot>
    </table>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { read, utils, writeFileXLSX } from 'xlsx'

const rows = ref([])

onMounted(async () => {
  const f = await fetch("https://sheetjs.com/pres.numbers")
  const ab = await f.arrayBuffer()
  const wb = read(ab)
  rows.value = utils.sheet_to_json(wb.Sheets[wb.SheetNames[0]])
})

function exportFile() {
    const ws = utils.json_to_sheet(rows.value)
    const wb = utils.book_new()
    utils.book_append_sheet(wb, ws, 'Sheet-Data')
    writeFileXLSX(wb, 'SheetVueTest.xlsx')
}
</script>
