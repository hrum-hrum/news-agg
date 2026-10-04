<script setup>
defineProps({
  likes: {
    type: Number,
    required: true,
  },
})
</script>

<template>
  <button class="act like" data-like="13" aria-pressed="false" aria-label="Нравится">
    <svg class="ico" viewBox="0 0 24 24">
      <path
        d="M20.84 4.61a5.5 5.5 0 0 0-7.78 0L12 5.67l-1.06-1.06a5.5 5.5 0 0 0-7.78 7.78l1.06 1.06L12 21.23l7.78-7.78 1.06-1.06a5.5 5.5 0 0 0 0-7.78z"
      ></path>
    </svg>
    <span class="cnt">{{ likes }}</span>
  </button>
</template>
