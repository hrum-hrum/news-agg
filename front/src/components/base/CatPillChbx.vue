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
  <!-- <span v-if="CATS[id]" class="cat-pill">
    <i class="dot" :style="`background:${CATS[id].p.bg}`"></i>
    {{ CATS[id].n }}
  </span> -->

  <label v-if="CATS[id]" class="inline-flex items-center cursor-pointer select-none">
    <input type="checkbox" class="sr-only peer" name="category" :value="id" />
    <div :class="`navrow ${id}`">
      <span class="flex items-center gap-2.5">
        <i class="dot" :style="`background:${CATS[id].p.a}`"></i>
        {{ CATS[id].n }}
      </span>
    </div>
  </label>

  <!-- <label v-else-if="id === 'all'" class="inline-flex items-center cursor-pointer select-none">
    <input value="all" type="radio" name="sentiment" class="pill-input sr-only peer" />
    <div class="pill all" :style="{ '--checked-bg': '#58708D' }">Все</div>
  </label> -->
</template>

<style scoped>
/* .pill {
  border: 1px solid rgb(var(--line));
  background: rgb(var(--surface));
  border-radius: 1rem;
  padding: 4px 16px;
}

.peer:checked + .pill {
  background: var(--checked-bg);
} */

.navrow {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 0.6rem;
  width: 100%;
  text-align: left;
  padding: 0.5rem 0.7rem;
  border-radius: 0.7rem;
  font-size: 0.9rem;
  color: rgb(var(--ink) / 0.85);
  cursor: pointer;
  transition:
    background 0.18s,
    transform 0.18s;
}

.navrow:hover {
  background: rgb(var(--sunk));
  transform: translateX(2px);
}
.navrow[aria-current='true'],
.peer:checked + .navrow {
  background: rgb(var(--surface));
  box-shadow: inset 0 0 0 1px rgb(var(--line));
  font-weight: 600;
  color: rgb(var(--ink));
}
.navrow .cnt {
  font-size: 0.78rem;
  color: rgb(var(--mute));
  font-variant-numeric: tabular-nums;
}
.dot {
  width: 0.6rem;
  height: 0.6rem;
  border-radius: 3px;
  display: inline-block;
  flex: none;
}
</style>
