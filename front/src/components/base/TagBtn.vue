<script setup>
defineProps({
  name: {
    type: String,
    required: true,
  },
})
</script>
<template>
  <button class="chip sm" :data-tag="`${name}`" :aria-label="`Тег ${name}`">#{{ name }}</button>
</template>
