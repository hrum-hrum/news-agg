<script setup lang="ts">
import NewsList from './NewsList.vue'
import TheMobileFilter from './TheMobileFilter.vue'
import TheSideBar from './TheSideBar.vue'
</script>

<template>
  <main class="mx-auto max-w-7xl px-4 pb-16 pt-6 sm:px-6 lg:pt-10">
    <!-- <div class="mb-6 max-w-2xl lg:mb-8">
      <h1 class="text-[2rem] font-bold leading-[1.1] tracking-[-0.035em] sm:text-4xl">
        Новости дня из&nbsp;разных источников
      </h1>
      <p class="mt-3 text-[15px] leading-relaxed text-mute">
        Заголовки восьми редакций собраны в одну ленту. Отмечайте понравившееся, оценивайте
        материалы и фильтруйте по темам.
      </p>
    </div> -->

    <TheMobileFilter />

    <div class="grid gap-10 lg:grid-cols-[15rem_minmax(0,1fr)]">
      <TheSideBar />
      <NewsList />
    </div>
  </main>
</template>
