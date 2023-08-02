<template>
    <div class="flex items-center justify-between my-4">
        <h1 class="text-5xl font-bold">Expenses</h1>
        <Button appearance="primary" @click="showDialog = true">Add</Button>
    </div>
    <Teleport to="#modals">
        <AddExpense v-model="showDialog" />
    </Teleport>
    <div v-if="expenses.list.loading">
        <LoadingIndicator class="w-14 text-blue-500 text-center m-auto" />
    </div>
    <div v-if="!expenses.list.loading && expensesList">
        <table class="min-w-full text-left text-sm font-light">
            <thead class="border-b font-medium dark:border-neutral-500">
                <tr>
                    <th scope="col" class="px-6 py-4">ID</th>
                    <th scope="col" class="px-6 py-4">Description</th>
                    <th scope="col" class="px-6 py-4">Amount</th>
                    <th scope="col" class="px-6 py-4">Type</th>
                    <th scope="col" class="px-6 py-4">Remarks</th>
                    <th scope="col" class="px-6 py-4">Owner</th>
                </tr>
            </thead>
            <tbody>
                <tr class="border-b dark:border-neutral-500" v-for="(item, idx) in expensesList" :key="item.name">
                    <td class="whitespace-nowrap px-6 py-4 font-medium">{{ idx + 1 }}</td>
                    <td class="whitespace-nowrap px-6 py-4 font-semibold">{{ item.description }}</td>
                    <td class="whitespace-nowrap px-6 py-4 font-semibold">{{ item.amount }}</td>
                    <td class="whitespace-nowrap px-6 py-4 font-semibold">{{ item.type }}</td>
                    <td class="whitespace-nowrap px-6 py-4 font-semibold">{{ item.remarks }}</td>
                    <td class="whitespace-nowrap px-6 py-4 font-semibold">{{ item.owner }}</td>
                </tr>
            </tbody>
        </table>
    </div>
</template>

<script setup>
import AddExpense from '@/components/AddExpense.vue'
import { createListResource, LoadingIndicator, Button } from 'frappe-ui'
import { computed, ref } from 'vue'

let showDialog = ref(false)

let expenses = createListResource({
    doctype: 'Expense Record',
    fields: ['name', 'description', 'type', 'amount', 'remarks', 'owner'],
    orderBy: 'creation desc',
    auto: true,
})
const expensesList = computed(()=> expenses.data)

</script>