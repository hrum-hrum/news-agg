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
  <label v-if="SENTIMENTS[id]" class="inline-flex items-center cursor-pointer select-none">
    <input :value="id" type="checkbox" name="sentiment" class="sr-only peer" />
    <div :class="`pill ${id}`" :style="{ '--checked-bg': SENTIMENTS[id].p.bg }">
      {{ SENTIMENTS[id].n }}
    </div>
  </label>
</template>

<style scoped>
.pill {
  border: 1px solid rgb(var(--line));
  background: rgb(var(--surface));
  border-radius: 1rem;
  padding: 4px 16px;
}

.peer:checked + .pill {
  background: var(--checked-bg);
  color: #ffffff;
  border: 1px solid var(--checked-bg);
}
</style>
