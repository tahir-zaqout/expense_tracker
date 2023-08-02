<template>
  <div class="max-w-7xl py-12 mx-auto">
    <template>
      <Toasts />
    </template>
    <TabGroup>
      <TabList class="flex space-x-1 rounded-xl bg-blue-900/20 p-1">
        <Tab as="template" v-slot="{ selected }">
          <button :class="[
            'w-full rounded-lg py-2.5 text-sm font-medium leading-5 text-blue-700',
            'ring-white ring-opacity-60 ring-offset-2 ring-offset-blue-400 focus:outline-none focus:ring-2',
            selected
              ? 'bg-white shadow'
              : 'text-blue-100 hover:bg-white/[0.12] hover:text-white',
          ]">
            Expenses
          </button>
        </Tab>
        <Tab as="template" v-slot="{ selected }">
          <button :class="[
            'w-full rounded-lg py-2.5 text-sm font-medium leading-5 text-blue-700',
            'ring-white ring-opacity-60 ring-offset-2 ring-offset-blue-400 focus:outline-none focus:ring-2',
            selected
              ? 'bg-white shadow'
              : 'text-blue-100 hover:bg-white/[0.12] hover:text-white',
          ]">
            Dashboard
          </button>
        </Tab>
      </TabList>

      <TabPanels class="mt-2">
        <TabPanel :class="[
          'rounded-xl bg-white p-3',
          'ring-white ring-opacity-60 ring-offset-2 ring-offset-blue-400 focus:outline-none focus:ring-2']">
          <div>
            <ExpenseList />
          </div>

        </TabPanel>
        <TabPanel :class="[
          'rounded-xl bg-white p-3',
          'ring-white ring-opacity-60 ring-offset-2 ring-offset-blue-400 focus:outline-none focus:ring-2']">
          <Dashboard />
        </TabPanel>
      </TabPanels>
    </TabGroup>
  </div>
</template>

<script setup>
import {Toasts} from 'frappe-ui';
import { TabGroup, TabList, Tab, TabPanels, TabPanel } from '@headlessui/vue'
import ExpenseList from '@/components/ExpenseList.vue';
import Dashboard from '@/components/Dashboard.vue';

</script>
