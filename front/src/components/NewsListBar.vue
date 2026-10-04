<template>
  <div class="flex flex-col gap-3 sm:flex-row sm:items-center sm:justify-between">
    <p id="count" class="text-sm text-mute" aria-live="polite">22 материала, показано 9</p>
    <div class="flex items-center gap-2">
      <div class="min-w-0 overflow-x-auto" style="scrollbar-width: none">
        <div class="seg" role="group" aria-label="Сортировка">
          <button data-sort="new" aria-pressed="true">Свежие</button>
          <button data-sort="views" aria-pressed="false">Просмотры</button>
          <button data-sort="rating" aria-pressed="false">Рейтинг</button>
          <button data-sort="likes" aria-pressed="false">Лайки</button>
        </div>
      </div>
      <div class="seg shrink-0" role="group" aria-label="Вид ленты">
        <button data-view="grid" aria-label="Карточки" aria-pressed="true">
          <svg class="ico" viewBox="0 0 24 24">
            <rect x="3" y="3" width="7" height="7" rx="1.5"></rect>
            <rect x="14" y="3" width="7" height="7" rx="1.5"></rect>
            <rect x="14" y="14" width="7" height="7" rx="1.5"></rect>
            <rect x="3" y="14" width="7" height="7" rx="1.5"></rect>
          </svg>
        </button>
        <button data-view="list" aria-label="Список" aria-pressed="false">
          <svg class="ico" viewBox="0 0 24 24">
            <line x1="8" y1="6" x2="21" y2="6"></line>
            <line x1="8" y1="12" x2="21" y2="12"></line>
            <line x1="8" y1="18" x2="21" y2="18"></line>
            <line x1="3" y1="6" x2="3.01" y2="6"></line>
            <line x1="3" y1="12" x2="3.01" y2="12"></line>
            <line x1="3" y1="18" x2="3.01" y2="18"></line>
          </svg>
        </button>
      </div>
    </div>
  </div>
</template>
