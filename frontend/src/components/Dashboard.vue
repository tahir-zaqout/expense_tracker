<template>
    <div class="my-4">
        <h1 class="text-5xl font-bold">Dashboard</h1>
    </div>
    <div class="flex items-center space-x-5">
        <div class="w-80 hover:shadow-lg" v-if="!totalCredits.loading && totalCredits.data">
            <Card title="Total Credits">
                {{ totalCredits.data }}
            </Card>
        </div>
        <div class="w-80 hover:shadow-lg" v-if="!totalDebits.loading && totalDebits.data">
            <Card title="Total Debits">
                {{ totalDebits.data }}
            </Card>
        </div>
    </div>

</template>

<script setup>
import { createResource, Card } from 'frappe-ui'
import { ref } from 'vue'

// const totalCredits = ref(null)
// const totalDebits = ref(null)


const totalCredits = createResource({
    url: 'expense_tracker.api.get_total_card',
    params: {
        type: 'Credit'
    },
    auto: true
})

const totalDebits = createResource({
    url: 'expense_tracker.api.get_total_card',
    params: {
        type: 'Debit'
    },
    auto: true
})

</script>