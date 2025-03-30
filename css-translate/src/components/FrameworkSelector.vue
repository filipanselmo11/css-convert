<template>
    <v-radio-group v-model="model" row>
      <v-radio label="Tailwind" value="tailwind"></v-radio>
      <v-radio label="Bootstrap" value="bootstrap"></v-radio>
    </v-radio-group>
  </template>
  
  <script setup lang="ts">
  import { computed } from 'vue'
  
  const props = defineProps<{
    modelValue: 'tailwind' | 'bootstrap'
  }>()
  
  const emit = defineEmits<{
    (e: 'update:modelValue', value: 'tailwind' | 'bootstrap'): void
  }>()
  
  const model = computed({
    get: () => props.modelValue,
    set: (value: 'tailwind' | 'bootstrap') => emit('update:modelValue', value)
  })
  </script>
  