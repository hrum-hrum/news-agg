<template>
  <footer class="border-t border-line bg-sunk/60">
    <div class="mx-auto max-w-7xl px-4 py-12 sm:px-6">
      <div class="grid gap-10 md:grid-cols-[1.4fr_1fr_1fr]">
        <div class="max-w-sm">
          <div class="flex items-center gap-2.5">
            <svg viewBox="0 0 28 28" width="24" height="24" aria-hidden="true">
              <rect x="3" y="5" width="22" height="5" rx="2.5" fill="rgb(189 96 70)"></rect>
              <rect x="3" y="12" width="15" height="5" rx="2.5" fill="rgb(96 128 108)"></rect>
              <rect x="3" y="19" width="19" height="5" rx="2.5" fill="rgb(106 131 160)"></rect>
            </svg>
            <span class="text-lg font-bold tracking-[-0.03em]">Лента</span>
          </div>
          <p class="mt-4 text-[15px] leading-relaxed text-mute">
            Агрегатор, который собирает новости разных редакций в одном месте и помогает быстро
            найти то, что интересно именно вам.
          </p>
          <button class="btn-quiet mt-5" data-top="">
            <svg class="ico" viewBox="0 0 24 24">
              <line x1="12" y1="19" x2="12" y2="5"></line>
              <polyline points="5 12 12 5 19 12"></polyline>
            </svg>
            Наверх
          </button>
        </div>
        <div>
          <h2 class="mb-3 text-sm font-semibold">Разделы</h2>
          <ul class="grid gap-2" id="footCats">
            <li><button class="flink" data-cat="tech">Технологии</button></li>
            <li><button class="flink" data-cat="eco">Экономика</button></li>
            <li><button class="flink" data-cat="sci">Наука</button></li>
            <li><button class="flink" data-cat="cul">Культура</button></li>
            <li><button class="flink" data-cat="spo">Спорт</button></li>
            <li><button class="flink" data-cat="wor">Мир</button></li>
          </ul>
        </div>
        <div>
          <h2 class="mb-3 text-sm font-semibold">Источники</h2>
          <ul class="grid gap-2" id="footSrcs">
            <li><button class="flink" data-src="sv">Северный вестник</button></li>
            <li><button class="flink" data-src="tp">Технопост</button></li>
            <li><button class="flink" data-src="rs">Рынок сегодня</button></li>
            <li><button class="flink" data-src="nv">Наука вслух</button></li>
            <li><button class="flink" data-src="ks">Культурный слой</button></li>
            <li><button class="flink" data-src="st">Стадион</button></li>
            <li><button class="flink" data-src="mo">Мировой обзор</button></li>
            <li><button class="flink" data-src="ok">Открытый код</button></li>
          </ul>
        </div>
      </div>
      <div
        class="mt-10 flex flex-col gap-2 border-t border-line pt-6 text-[13px] text-mute sm:flex-row sm:justify-between"
      >
        <p>Демонстрационный сайт: заголовки, тексты и названия источников вымышлены.</p>
        <p>© 2026 Лента</p>
      </div>
    </div>
  </footer>
</template>
