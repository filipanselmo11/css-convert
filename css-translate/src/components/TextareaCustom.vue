<template>
  <v-textarea
    :label="label"
    :model-value="model"
    @update:modelValue="val => emit('update:modelValue', val)"
    :readonly="readonly"
    :rows="rows"
    :auto-grow="autoGrow"
    outlined
  />
</template>

<script setup lang="ts">
import { computed } from 'vue'

const props = defineProps<{
  label: string
  modelValue: string
  readonly?: boolean
  rows?: number
  autoGrow?: boolean
}>()

const emit = defineEmits<{
  (e: 'update:modelValue', value: string): void
}>()

const model = computed({
  get: () => props.modelValue,
  set: (value: string) => emit('update:modelValue', value)
})
</script>
