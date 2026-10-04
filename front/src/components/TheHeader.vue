<template>
  <header class="site-header">
    <div
      class="mx-auto flex max-w-7xl flex-wrap items-center gap-x-4 gap-y-3 px-4 py-3 sm:px-6 md:flex-nowrap md:gap-6"
    >
      <a href="#top" class="logo order-1 flex items-center gap-2.5" aria-label="Лента — на главную">
        <svg viewBox="0 0 28 28" width="28" height="28" aria-hidden="true">
          <rect x="3" y="5" width="22" height="5" rx="2.5" fill="rgb(189 96 70)"></rect>
          <rect x="3" y="12" width="15" height="5" rx="2.5" fill="rgb(96 128 108)"></rect>
          <rect x="3" y="19" width="19" height="5" rx="2.5" fill="rgb(106 131 160)"></rect>
        </svg>
        <span class="text-xl font-bold tracking-[-0.03em]">Лента</span>
      </a>

      <div class="order-3 basis-full md:order-2 md:basis-auto md:flex-1 md:max-w-xl">
        <label class="search" for="q">
          <svg class="ico text-mute" style="font-size: 1.1rem" viewBox="0 0 24 24">
            <circle cx="11" cy="11" r="8"></circle>
            <line x1="21" y1="21" x2="16.65" y2="16.65"></line>
          </svg>
          <input
            id="q"
            type="search"
            autocomplete="off"
            spellcheck="false"
            placeholder="Поиск по заголовкам, темам и тегам"
            aria-label="Быстрый поиск"
          />
          <button
            id="qClear"
            class="ibtn"
            style="height: 1.9rem; min-width: 1.9rem; padding: 0"
            data-clear="q"
            aria-label="Очистить поиск"
            hidden=""
          >
            <svg class="ico" viewBox="0 0 24 24">
              <line x1="18" y1="6" x2="6" y2="18"></line>
              <line x1="6" y1="6" x2="18" y2="18"></line>
            </svg>
          </button>
          <span id="qKbd" class="kbd hidden sm:inline">/</span>
        </label>
      </div>

      <div class="order-2 ml-auto md:order-3">
        <button
          class="ibtn"
          data-toggle-liked=""
          aria-pressed="false"
          aria-label="Показать понравившиеся"
        >
          <svg class="ico" viewBox="0 0 24 24">
            <path
              d="M20.84 4.61a5.5 5.5 0 0 0-7.78 0L12 5.67l-1.06-1.06a5.5 5.5 0 0 0-7.78 7.78l1.06 1.06L12 21.23l7.78-7.78 1.06-1.06a5.5 5.5 0 0 0 0-7.78z"
            ></path>
          </svg>
          <span class="hidden sm:inline">Понравилось</span>
          <span id="likedBadge" class="badge">2</span>
        </button>
      </div>
    </div>
  </header>
</template>
<style scoped>
.site-header {
  position: sticky;
  top: env(safe-area-inset-top, 0px);
  z-index: 30;
  background: rgb(var(--paper) / 0.86);
  -webkit-backdrop-filter: blur(14px);
  backdrop-filter: blur(14px);
  border-bottom: 1px solid rgb(var(--line));
}
.logo rect {
  transition: transform 0.35s cubic-bezier(0.3, 1.4, 0.5, 1);
}
.logo:hover rect:nth-child(1) {
  transform: translateX(-2px);
}
.logo:hover rect:nth-child(2) {
  transform: translateX(5px);
}
.logo:hover rect:nth-child(3) {
  transform: translateX(2px);
}

.search {
  display: flex;
  align-items: center;
  gap: 0.6rem;
  height: 2.75rem;
  padding: 0 0.9rem;
  background: rgb(var(--sunk));
  border: 1px solid transparent;
  border-radius: 0.9rem;
  transition:
    background 0.2s,
    border-color 0.2s,
    box-shadow 0.2s;
}
.search:hover {
  border-color: rgb(var(--line));
}
.search:focus-within {
  background: rgb(var(--surface));
  border-color: rgb(var(--clay) / 0.7);
  box-shadow: 0 0 0 4px rgb(var(--clay) / 0.14);
}
.search input {
  flex: 1;
  min-width: 0;
  background: transparent;
  outline: none;
  font-size: 0.9375rem;
  color: rgb(var(--ink));
}
.search input::placeholder {
  color: rgb(var(--mute) / 0.85);
}
.kbd {
  font-size: 0.75rem;
  line-height: 1;
  padding: 0.28rem 0.45rem;
  border-radius: 0.4rem;
  border: 1px solid rgb(var(--line));
  color: rgb(var(--mute));
  background: rgb(var(--surface));
}
</style>
