import api from "@/services/api";
import { defineStore } from "pinia"


export const useConvertStore = defineStore('convert', {
    state: () => ({
        result: '',
        loading: false,
        error: '',
    }),
    actions: {
        async convert(css: string, framework: 'tailwind' | 'bootstrap') {
            this.loading = true;
            this.error = '';
            this.result = '';
            try {
                const response = await api.post('/convert', { css, framework });
                this.result = response.data.result;
            } catch (error) {
                this.error = 'Erro na conversão';
                console.error(error);
            } finally {
                this.loading = false;
            }
        }
    },
});