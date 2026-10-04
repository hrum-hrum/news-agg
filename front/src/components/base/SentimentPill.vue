<script setup>
import SENTIMENTS from '@/constants/sentiments'

defineProps({
  id: {
    type: String,
    required: true,
  },
})
</script>

<template>
  <span
    v-if="SENTIMENTS[id]"
    class="mono"
    :style="`background:${SENTIMENTS[id].p.bg}`"
    aria-hidden="true"
    >{{ SENTIMENTS[id].n }}</span
  >
</template>
