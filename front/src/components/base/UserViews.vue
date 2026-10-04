<script setup>
defineProps({
  views: {
    type: Number,
    required: true,
  },
})
</script>
<template>
  <span class="act" title="Просмотры">
    <svg class="ico" viewBox="0 0 24 24">
      <path d="M1 12s4-8 11-8 11 8 11 8-4 8-11 8-11-8-11-8z"></path>
      <circle cx="12" cy="12" r="3"></circle>
    </svg>
    <span data-views="13">{{ views }}</span>
  </span>
</template>
