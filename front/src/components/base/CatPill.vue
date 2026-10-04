<script setup>
import CATS from '@/constants/categories.js'

defineProps({
  id: {
    type: String,
    required: true,
  },
})
</script>

<template>
  <span v-if="CATS[id]" class="cat-pill">
    <i class="dot" :style="`background:${CATS[id].p.bg}`"></i>
    {{ CATS[id].n }}
  </span>
</template>
