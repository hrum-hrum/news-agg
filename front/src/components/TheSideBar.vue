<script setup>
import SENTIMENTS from '@/constants/sentiments'
import CATS from '@/constants/categories.js'
import CatPillChbx from './base/CatPillChbx.vue'
import SentimentPillRadio from './base/SentimentPillChbx.vue'
</script>

<template>
  <!-- Сайдбар -->
  <aside
    class="hidden lg:block lg:sticky lg:top-24 lg:max-h-[calc(100vh-7.5rem)] lg:self-start lg:overflow-y-auto lg:pr-2"
    aria-label="Фильтры"
  >
    <section>
      <h2 class="mb-2 px-2 text-sm font-semibold">Ключевые слова</h2>

      <div class="flex flex-wrap gap-1.5 px-1" data-slot="tags">
        <button class="chip" data-tag="города" aria-pressed="false">Бренд A</button>
        <button class="chip" data-tag="экология" aria-pressed="false">Продукт Б</button>
      </div>
    </section>
    <section class="mt-7 pt-4 border-t-2 border-t-gray-300">
      <div class="flex items-end justify-between gap-2 pb-4">
        <h2 class="mb-1 px-2 text-sm font-semibold">Тональность</h2>
        <button class="chip" data-sent="all" aria-current="false">Все</button>
      </div>
      <div class="grid columns-1 gap-1.5 px-1" data-slot="sentiment">
        <SentimentPillRadio v-for="(item, key) in SENTIMENTS" :key="key" :id="key" />
      </div>
    </section>

    <section class="mt-7 pt-4 border-t-2 border-t-gray-300">
      <div class="flex items-end justify-between gap-2 pb-4">
        <h2 class="mb-1 px-2 text-sm font-semibold">Категории</h2>
        <button class="chip" data-cat="all" aria-current="false">Все</button>
      </div>
      <nav class="grid columns-1 space-y-0.5" data-slot="category">
        <CatPillChbx v-for="(item, key) in CATS" :key="key" :id="key" />
      </nav>
    </section>
    <section class="mt-7 pt-4 border-t-2 border-t-gray-300">
      <h2 class="mb-3 px-2 text-sm font-semibold">Стоп слова</h2>
      <div class="flex flex-wrap gap-1.5 px-1" data-slot="tags">
        <button class="chip" data-tag="города" aria-pressed="false">ошибка</button>
        <button class="chip" data-tag="экология" aria-pressed="false">краш</button>
        <button class="chip" data-tag="океан" aria-pressed="false">суд</button>
        <button class="chip" data-tag="сон" aria-pressed="false">упал</button>
        <button class="chip" data-tag="транспорт" aria-pressed="false">слив</button>
        <button class="chip" data-tag="археология" aria-pressed="false">мошенники</button>
      </div>
    </section>
    <!-- <section class="mt-7">
      <h2 class="mb-3 px-2 text-sm font-semibold">Популярные теги</h2>
      <div class="flex flex-wrap gap-1.5 px-1" data-slot="tags">
        <button class="chip" data-tag="города" aria-pressed="false">#города</button>
        <button class="chip" data-tag="экология" aria-pressed="false">#экология</button>
        <button class="chip" data-tag="океан" aria-pressed="false">#океан</button>
        <button class="chip" data-tag="сон" aria-pressed="false">#сон</button>
        <button class="chip" data-tag="транспорт" aria-pressed="false">#транспорт</button>
        <button class="chip" data-tag="археология" aria-pressed="false">#археология</button>
        <button class="chip" data-tag="астрономия" aria-pressed="false">#астрономия</button>
        <button class="chip" data-tag="батареи" aria-pressed="false">#батареи</button>
        <button class="chip" data-tag="бег" aria-pressed="false">#бег</button>
        <button class="chip" data-tag="браузеры" aria-pressed="false">#браузеры</button>
        <button class="chip" data-tag="выставки" aria-pressed="false">#выставки</button>
        <button class="chip" data-tag="ИИ" aria-pressed="false">#ИИ</button>
        <button class="chip" data-tag="интернет" aria-pressed="false">#интернет</button>
        <button class="chip" data-tag="инфляция" aria-pressed="false">#инфляция</button>
        <button class="chip" data-tag="история" aria-pressed="false">#история</button>
        <button class="chip" data-tag="кино" aria-pressed="false">#кино</button>
      </div>
    </section> -->
  </aside>
</template>
