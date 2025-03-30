<template>
  <v-container class="pa-4" max-width="800">
    <v-card elevation="2" class="pa-4">
      <v-card-title class="text-h5">Conversor de CSS</v-card-title>

      <TextareaCustom v-model="cssInput" label="Cole seu css aqui" />

      <FrameworkSelector v-model="framework" class="mt-4" />

      <ConvertButton
        @click="convertCSS"
        class="mt-4"
        :disabled="!cssInput || convertStore.loading"
      >
        <template #default>
          {{ convertStore.loading ? 'Convertendo...' : 'Converter' }}
        </template>
      </ConvertButton>

      <v-divider class="my-4" />

      <div v-if="convertStore.error" class="text-error mb-2">
        {{ convertStore.error }}
      </div>

      <TextareaCustom
        v-model="convertedOutput"
        label="Resultado"
        :readonly="true"
      />
    </v-card>
  </v-container>
</template>


<script setup lang="ts">
import { ref, watch } from 'vue';
import TextareaCustom from '@/components/TextareaCustom.vue';
import FrameworkSelector from '@/components/FrameworkSelector.vue';
import ConvertButton from '@/components/ConvertButton.vue';
import { useConvertStore } from '@/stores/convertStore';


const cssInput = ref<string>('');
const framework = ref<'tailwind' | 'bootstrap'>('tailwind');

const convertStore = useConvertStore();

watch(() => convertStore.result, (val) => {
  convertedOutput.value = val;
});

const convertedOutput = ref<string>('');

const convertCSS = () => {
  convertStore.convert(cssInput.value, framework.value);
};

</script>