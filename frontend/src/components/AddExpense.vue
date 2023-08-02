<template>
  <Dialog :options="{
    title: 'Add New Expenses',
    icon: {
      name: 'plus',
      appearance: 'success',
    },
    size: 'lg',
    actions: [
      {
        label: 'Add',
        appearance: 'primary',
        handler: ({ close }) => {
          addExpenses()
          close() // closes dialog
        },
      },
      { label: 'Cancel' },
    ],
  }">
    <template #body-content>
      <Input class="mt-2" type="text" placeholder="Description" v-model="expenseValues.description" />
      <Input class="mt-2" type="number" placeholder="Amount" v-model="expenseValues.amount" />
      <Input class="mt-2" type="select" :options="['Credit', 'Debit']" placeholder="Type" v-model="expenseValues.type" />
      <Input class="mt-2" type="textarea" placeholder="Remarks" v-model="expenseValues.remarks" />
      <input class="mt-2" type="file" placeholder="file" @change="handleFile" />
    </template>
  </Dialog>
</template>

<script setup>
import { toast, Dialog, createListResource, createResource, fileToBase64 } from 'frappe-ui'
import { reactive } from 'vue';

const expenseValues = reactive({
  description: '',
  amount: null,
  type: 'Credit',
  remarks: ''
})
const addExpenses = () => {
  if (validateInputs()) {
    const expenseDoc = createListResource({ doctype: "Expense Record" })
    expenseDoc.insert.submit(expenseValues)
    toast({
      title: 'Success',
      text: 'Expense Added Successfully!',
      icon: 'check',
      iconClasses: 'text-green-500',
    })

  }
}
// TODO: specific validation for every field.
const validateInputs = () => {
  if (!expenseValues.description || !expenseValues.amount) return false

  return true
}
// TODO: handle upload file
const handleFile = e => {
  let file = e.target.files[0]
  if (!file) {
    return;
  }

}
</script>
