<script setup>
import { computed } from 'vue'

const props = defineProps({
  rate: {
    type: Array,
    required: false,
    default: () => [0, 0], // Хорошая практика: задать дефолтный массив
  },
})

const average = computed(() => props.rate[0] ?? 0)
const total = computed(() => props.rate[1] ?? 0)
</script>

<template>
  <span
    class="act rate ml-auto"
    data-open="13"
    title="Рейтинг: 58 оценок"
    aria-label="Рейтинг 4,7, открыть материал"
  >
    <svg class="ico" viewBox="0 0 24 24">
      <polygon
        points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"
      ></polygon>
    </svg>
    <span class="font-semibold text-ink">{{ average }}</span>
    <span class="opacity-70">({{ total }})</span>
  </span>
</template>
