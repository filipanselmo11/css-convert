<template>
  <v-btn :color="color" @click="onClick">
    <slot>Converter</slot>
  </v-btn>
</template>

<script setup lang="ts">
const props = defineProps<{
  color?: string
  onClick: () => void
}>()
</script>
