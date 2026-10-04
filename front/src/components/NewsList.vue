<script setup>
import { onBeforeMount } from 'vue'
import { usePostsStore } from '@/stores/posts.js'
import MoreBtn from './base/MoreBtn.vue'
import NewsListBar from './NewsListBar.vue'
import NewsListItem from './NewsListItem.vue'

const postsStore = usePostsStore()

onBeforeMount(async () => {
  await postsStore.fetchPosts()
})
</script>

<template>
  <!-- Лента -->
  <section aria-label="Лента новостей" class="min-w-0">
    <NewsListBar />

    <!-- <div id="applied" class="mt-4 flex flex-wrap items-center gap-2" hidden=""></div> -->
    <div id="applied" class="mt-4 flex flex-wrap items-center gap-2">
      <button class="chip applied" data-clear="cat" aria-label="Убрать фильтр: Мир">
        Мир<svg class="ico" viewBox="0 0 24 24">
          <line x1="18" y1="6" x2="6" y2="18"></line>
          <line x1="6" y1="6" x2="18" y2="18"></line>
        </svg></button
      ><button class="chip applied" data-clear="src" aria-label="Убрать фильтр: Рынок сегодня">
        Рынок сегодня<svg class="ico" viewBox="0 0 24 24">
          <line x1="18" y1="6" x2="6" y2="18"></line>
          <line x1="6" y1="6" x2="18" y2="18"></line>
        </svg></button
      ><button class="chip sm" data-clear="all" style="border-color: transparent">
        Сбросить всё
      </button>
    </div>

    <div v-if="postsStore.posts.length" id="feed" class="mt-5">
      <div class="grid gap-4 md:grid-cols-2 xl:grid-cols-3">
        <NewsListItem v-for="post in postsStore.posts" :key="post.id" v-bind="post" />
        <!-- <article class="card" data-id="1">
          <div class="cover" data-open="1">
            <TechIcon />
            <span class="cat-pill">
              <i class="dot" style="background: #6a83a0"> </i>Технологии</span
            >
          </div>
          <div class="flex grow flex-col gap-4 p-4 md:p-6">
            <div class="flex items-center justify-between gap-3 text-[13px] text-mute">
              <span class="flex min-w-0 items-center gap-2">
                <span class="mono" style="background: #58708d" aria-hidden="true">ТП</span>
                <span class="truncate font-medium text-ink/80">Технопост</span>
              </span>
              <span class="shrink-0">12 мин назад</span>
            </div>
            <h2 class="text-2xl font-bold leading-[1.15] md:text-[1.75rem]">
              <button class="title-btn" data-open="1">
                Производители умных домов договорились об общем протоколе обновлений
              </button>
            </h2>
            <p class="text-base leading-relaxed text-mute">
              Семь компаний опубликовали черновик стандарта, по которому устройства будут получать
              обновления независимо от бренда хаба. Пользователи смогут сменить центр управления, не
              перенастраивая сценарии. Окончательную версию обещают к весне.
            </p>
            <div class="-ml-1 flex flex-wrap gap-1">
              <button class="chip sm" data-tag="умный дом" aria-label="Тег умный дом">
                #умный дом
              </button>
              <button class="chip sm" data-tag="стандарты" aria-label="Тег стандарты">
                #стандарты
              </button>
            </div>
            <div class="mt-auto border-t border-line pt-3">
              <div class="flex flex-wrap items-center gap-x-4 gap-y-1">
                <button class="act like" data-like="1" aria-pressed="false" aria-label="Нравится">
                  <svg class="ico" viewBox="0 0 24 24">
                    <path
                      d="M20.84 4.61a5.5 5.5 0 0 0-7.78 0L12 5.67l-1.06-1.06a5.5 5.5 0 0 0-7.78 7.78l1.06 1.06L12 21.23l7.78-7.78 1.06-1.06a5.5 5.5 0 0 0 0-7.78z"
                    ></path>
                  </svg>
                  <span class="cnt">96</span>
                </button>
                <span class="act" title="Просмотры">
                  <svg class="ico" viewBox="0 0 24 24">
                    <path d="M1 12s4-8 11-8 11 8 11 8-4 8-11 8-11-8-11-8z"></path>
                    <circle cx="12" cy="12" r="3"></circle>
                  </svg>
                  <span data-views="1">1,8 тыс.</span>
                </span>
                <button
                  class="act rate ml-auto"
                  data-open="1"
                  title="Рейтинг: 42 оценки"
                  aria-label="Рейтинг 4,5, открыть материал"
                >
                  <svg class="ico" viewBox="0 0 24 24">
                    <polygon
                      points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"
                    ></polygon>
                  </svg>
                  <span class="font-semibold text-ink">4,5</span>
                  <span class="opacity-70">(42)</span>
                </button>
              </div>
            </div>
          </div>
        </article>
        <article class="card" data-id="19">
          <div class="cover" data-open="19">
            <WorldIcon />
            <span class="cat-pill"> <i class="dot" style="background: #4f8583"> </i>Мир</span>
          </div>
          <div class="flex grow flex-col gap-3 px-3.5 pb-3 pt-4">
            <div class="flex items-center justify-between gap-3 text-[13px] text-mute">
              <span class="flex min-w-0 items-center gap-2">
                <span class="mono" style="background: #3f6f8f" aria-hidden="true">МО</span>
                <span class="truncate font-medium text-ink/80">Мировой обзор</span>
              </span>
              <span class="shrink-0">24 мин назад</span>
            </div>
            <h3 class="text-[1.0625rem] font-semibold leading-snug tracking-[-0.012em]">
              <button class="title-btn" data-open="19">
                Города Северной Европы тестируют единый проездной для поездов и автобусов
              </button>
            </h3>
            <p class="line-clamp-3 text-[15px] leading-relaxed text-mute">
              Пилотный проект охватил шесть городов и два железнодорожных оператора. Пассажиры
              покупают билет в одном приложении и платят по факту поездок с дневным потолком.
            </p>
            <div class="-ml-1 flex flex-wrap gap-1">
              <button class="chip sm" data-tag="транспорт" aria-label="Тег транспорт">
                #транспорт
              </button>
              <button class="chip sm" data-tag="города" aria-label="Тег города">#города</button>
            </div>
            <div class="mt-auto border-t border-line pt-3">
              <div class="flex flex-wrap items-center gap-x-4 gap-y-1">
                <button class="act like" data-like="19" aria-pressed="true" aria-label="Нравится">
                  <svg class="ico" viewBox="0 0 24 24">
                    <path
                      d="M20.84 4.61a5.5 5.5 0 0 0-7.78 0L12 5.67l-1.06-1.06a5.5 5.5 0 0 0-7.78 7.78l1.06 1.06L12 21.23l7.78-7.78 1.06-1.06a5.5 5.5 0 0 0 0-7.78z"
                    ></path>
                  </svg>
                  <span class="cnt">174</span>
                </button>
                <span class="act" title="Просмотры">
                  <svg class="ico" viewBox="0 0 24 24">
                    <path d="M1 12s4-8 11-8 11 8 11 8-4 8-11 8-11-8-11-8z"></path>
                    <circle cx="12" cy="12" r="3"></circle>
                  </svg>
                  <span data-views="19">2,6 тыс.</span>
                </span>
                <button
                  class="act rate ml-auto"
                  data-open="19"
                  title="Рейтинг: 61 оценка"
                  aria-label="Рейтинг 4,5, открыть материал"
                >
                  <svg class="ico" viewBox="0 0 24 24">
                    <polygon
                      points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"
                    ></polygon>
                  </svg>
                  <span class="font-semibold text-ink">4,5</span>
                  <span class="opacity-70">(61)</span>
                </button>
              </div>
            </div>
          </div>
        </article>
        <article class="card" data-id="2">
          <div class="cover" data-open="2">
            <svg viewBox="0 0 400 240" preserveAspectRatio="xMidYMid slice" aria-hidden="true">
              <rect width="400" height="240" fill="#DCE4EE"></rect>
              <circle cx="18" cy="16" r="2.2" fill="#33465E" opacity="0.3"></circle>
              <circle cx="49" cy="16" r="5" fill="#6A83A0" opacity="0.95"></circle>
              <circle cx="80" cy="16" r="2.2" fill="#33465E" opacity="0.3"></circle>
              <circle cx="111" cy="16" r="2.2" fill="#33465E" opacity="0.3"></circle>
              <circle cx="142" cy="16" r="2.2" fill="#33465E" opacity="0.3"></circle>
              <circle cx="173" cy="16" r="5" fill="#6A83A0" opacity="0.95"></circle>
              <circle cx="204" cy="16" r="5" fill="#6A83A0" opacity="0.95"></circle>
              <circle cx="235" cy="16" r="5" fill="#6A83A0" opacity="0.95"></circle>
              <circle cx="266" cy="16" r="5" fill="#6A83A0" opacity="0.95"></circle>
              <circle cx="297" cy="16" r="5" fill="#6A83A0" opacity="0.95"></circle>
              <circle cx="328" cy="16" r="5" fill="#6A83A0" opacity="0.95"></circle>
              <circle cx="359" cy="16" r="5" fill="#6A83A0" opacity="0.95"></circle>
              <circle cx="390" cy="16" r="5" fill="#6A83A0" opacity="0.95"></circle>
              <circle cx="18" cy="46" r="2.2" fill="#33465E" opacity="0.3"></circle>
              <circle cx="49" cy="46" r="5" fill="#6A83A0" opacity="0.95"></circle>
              <circle cx="80" cy="46" r="5" fill="#6A83A0" opacity="0.95"></circle>
              <circle cx="111" cy="46" r="5" fill="#6A83A0" opacity="0.95"></circle>
              <circle cx="142" cy="46" r="5" fill="#6A83A0" opacity="0.95"></circle>
              <circle cx="173" cy="46" r="2.2" fill="#33465E" opacity="0.3"></circle>
              <circle cx="204" cy="46" r="5" fill="#6A83A0" opacity="0.95"></circle>
              <circle cx="235" cy="46" r="2.2" fill="#33465E" opacity="0.3"></circle>
              <circle cx="266" cy="46" r="2.2" fill="#33465E" opacity="0.3"></circle>
              <circle cx="297" cy="46" r="2.2" fill="#33465E" opacity="0.3"></circle>
              <circle cx="328" cy="46" r="2.2" fill="#33465E" opacity="0.3"></circle>
              <circle cx="359" cy="46" r="2.2" fill="#33465E" opacity="0.3"></circle>
              <circle cx="390" cy="46" r="2.2" fill="#33465E" opacity="0.3"></circle>
              <circle cx="18" cy="76" r="2.2" fill="#33465E" opacity="0.3"></circle>
              <circle cx="49" cy="76" r="5" fill="#6A83A0" opacity="0.95"></circle>
              <circle cx="80" cy="76" r="2.2" fill="#33465E" opacity="0.3"></circle>
              <circle cx="111" cy="76" r="2.2" fill="#33465E" opacity="0.3"></circle>
              <circle cx="142" cy="76" r="5" fill="#6A83A0" opacity="0.95"></circle>
              <circle cx="173" cy="76" r="5" fill="#6A83A0" opacity="0.95"></circle>
              <circle cx="204" cy="76" r="2.2" fill="#33465E" opacity="0.3"></circle>
              <circle cx="235" cy="76" r="5" fill="#6A83A0" opacity="0.95"></circle>
              <circle cx="266" cy="76" r="2.2" fill="#33465E" opacity="0.3"></circle>
              <circle cx="297" cy="76" r="2.2" fill="#33465E" opacity="0.3"></circle>
              <circle cx="328" cy="76" r="2.2" fill="#33465E" opacity="0.3"></circle>
              <circle cx="359" cy="76" r="5" fill="#6A83A0" opacity="0.95"></circle>
              <circle cx="390" cy="76" r="5" fill="#6A83A0" opacity="0.95"></circle>
              <circle cx="18" cy="106" r="5" fill="#6A83A0" opacity="0.95"></circle>
              <circle cx="49" cy="106" r="2.2" fill="#33465E" opacity="0.3"></circle>
              <circle cx="80" cy="106" r="5" fill="#6A83A0" opacity="0.95"></circle>
              <circle cx="111" cy="106" r="2.2" fill="#33465E" opacity="0.3"></circle>
              <circle cx="142" cy="106" r="2.2" fill="#33465E" opacity="0.3"></circle>
              <circle cx="173" cy="106" r="5" fill="#6A83A0" opacity="0.95"></circle>
              <circle cx="204" cy="106" r="5" fill="#6A83A0" opacity="0.95"></circle>
              <circle cx="235" cy="106" r="2.2" fill="#33465E" opacity="0.3"></circle>
              <circle cx="266" cy="106" r="2.2" fill="#33465E" opacity="0.3"></circle>
              <circle cx="297" cy="106" r="2.2" fill="#33465E" opacity="0.3"></circle>
              <circle cx="328" cy="106" r="2.2" fill="#33465E" opacity="0.3"></circle>
              <circle cx="359" cy="106" r="2.2" fill="#33465E" opacity="0.3"></circle>
              <circle cx="390" cy="106" r="5" fill="#6A83A0" opacity="0.95"></circle>
              <circle cx="18" cy="136" r="5" fill="#6A83A0" opacity="0.95"></circle>
              <circle cx="49" cy="136" r="2.2" fill="#33465E" opacity="0.3"></circle>
              <circle cx="80" cy="136" r="2.2" fill="#33465E" opacity="0.3"></circle>
              <circle cx="111" cy="136" r="5" fill="#6A83A0" opacity="0.95"></circle>
              <circle cx="142" cy="136" r="2.2" fill="#33465E" opacity="0.3"></circle>
              <circle cx="173" cy="136" r="5" fill="#6A83A0" opacity="0.95"></circle>
              <circle cx="204" cy="136" r="5" fill="#6A83A0" opacity="0.95"></circle>
              <circle cx="235" cy="136" r="2.2" fill="#33465E" opacity="0.3"></circle>
              <circle cx="266" cy="136" r="5" fill="#6A83A0" opacity="0.95"></circle>
              <circle cx="297" cy="136" r="2.2" fill="#33465E" opacity="0.3"></circle>
              <circle cx="328" cy="136" r="2.2" fill="#33465E" opacity="0.3"></circle>
              <circle cx="359" cy="136" r="2.2" fill="#33465E" opacity="0.3"></circle>
              <circle cx="390" cy="136" r="5" fill="#6A83A0" opacity="0.95"></circle>
              <circle cx="18" cy="166" r="2.2" fill="#33465E" opacity="0.3"></circle>
              <circle cx="49" cy="166" r="5" fill="#6A83A0" opacity="0.95"></circle>
              <circle cx="80" cy="166" r="2.2" fill="#33465E" opacity="0.3"></circle>
              <circle cx="111" cy="166" r="5" fill="#6A83A0" opacity="0.95"></circle>
              <circle cx="142" cy="166" r="5" fill="#6A83A0" opacity="0.95"></circle>
              <circle cx="173" cy="166" r="5" fill="#6A83A0" opacity="0.95"></circle>
              <circle cx="204" cy="166" r="2.2" fill="#33465E" opacity="0.3"></circle>
              <circle cx="235" cy="166" r="2.2" fill="#33465E" opacity="0.3"></circle>
              <circle cx="266" cy="166" r="2.2" fill="#33465E" opacity="0.3"></circle>
              <circle cx="297" cy="166" r="2.2" fill="#33465E" opacity="0.3"></circle>
              <circle cx="328" cy="166" r="5" fill="#6A83A0" opacity="0.95"></circle>
              <circle cx="359" cy="166" r="2.2" fill="#33465E" opacity="0.3"></circle>
              <circle cx="390" cy="166" r="2.2" fill="#33465E" opacity="0.3"></circle>
              <circle cx="18" cy="196" r="5" fill="#6A83A0" opacity="0.95"></circle>
              <circle cx="49" cy="196" r="2.2" fill="#33465E" opacity="0.3"></circle>
              <circle cx="80" cy="196" r="2.2" fill="#33465E" opacity="0.3"></circle>
              <circle cx="111" cy="196" r="2.2" fill="#33465E" opacity="0.3"></circle>
              <circle cx="142" cy="196" r="2.2" fill="#33465E" opacity="0.3"></circle>
              <circle cx="173" cy="196" r="5" fill="#6A83A0" opacity="0.95"></circle>
              <circle cx="204" cy="196" r="2.2" fill="#33465E" opacity="0.3"></circle>
              <circle cx="235" cy="196" r="5" fill="#6A83A0" opacity="0.95"></circle>
              <circle cx="266" cy="196" r="5" fill="#6A83A0" opacity="0.95"></circle>
              <circle cx="297" cy="196" r="2.2" fill="#33465E" opacity="0.3"></circle>
              <circle cx="328" cy="196" r="5" fill="#6A83A0" opacity="0.95"></circle>
              <circle cx="359" cy="196" r="5" fill="#6A83A0" opacity="0.95"></circle>
              <circle cx="390" cy="196" r="2.2" fill="#33465E" opacity="0.3"></circle>
              <circle cx="18" cy="226" r="2.2" fill="#33465E" opacity="0.3"></circle>
              <circle cx="49" cy="226" r="2.2" fill="#33465E" opacity="0.3"></circle>
              <circle cx="80" cy="226" r="5" fill="#6A83A0" opacity="0.95"></circle>
              <circle cx="111" cy="226" r="5" fill="#6A83A0" opacity="0.95"></circle>
              <circle cx="142" cy="226" r="2.2" fill="#33465E" opacity="0.3"></circle>
              <circle cx="173" cy="226" r="2.2" fill="#33465E" opacity="0.3"></circle>
              <circle cx="204" cy="226" r="2.2" fill="#33465E" opacity="0.3"></circle>
              <circle cx="235" cy="226" r="5" fill="#6A83A0" opacity="0.95"></circle>
              <circle cx="266" cy="226" r="5" fill="#6A83A0" opacity="0.95"></circle>
              <circle cx="297" cy="226" r="2.2" fill="#33465E" opacity="0.3"></circle>
              <circle cx="328" cy="226" r="2.2" fill="#33465E" opacity="0.3"></circle>
              <circle cx="359" cy="226" r="2.2" fill="#33465E" opacity="0.3"></circle>
              <circle cx="390" cy="226" r="2.2" fill="#33465E" opacity="0.3"></circle>
              <rect x="141" y="73" width="170" height="100" rx="20" fill="#33465E"></rect>
              <rect x="194" y="131" width="120" height="70" rx="16" fill="#BD6046"></rect>
            </svg>
            <span class="cat-pill">
              <i class="dot" style="background: #6a83a0"> </i>Технологии</span
            >
          </div>
          <div class="flex grow flex-col gap-3 px-3.5 pb-3 pt-4">
            <div class="flex items-center justify-between gap-3 text-[13px] text-mute">
              <span class="flex min-w-0 items-center gap-2">
                <span class="mono" style="background: #5a5f66" aria-hidden="true">ОК</span>
                <span class="truncate font-medium text-ink/80">Открытый код</span>
              </span>
              <span class="shrink-0">35 мин назад</span>
            </div>
            <h3 class="text-[1.0625rem] font-semibold leading-snug tracking-[-0.012em]">
              <button class="title-btn" data-open="2">
                Три ошибки команд, которые переходят на локальные модели ИИ
              </button>
            </h3>
            <p class="line-clamp-3 text-[15px] leading-relaxed text-mute">
              Разработчики делятся опытом запуска моделей на собственных серверах. Чаще всего
              спотыкаются на недооценке памяти, отсутствии мониторинга качества и слишком раннем
              отказе от облачного резерва.
            </p>
            <div class="-ml-1 flex flex-wrap gap-1">
              <button class="chip sm" data-tag="ИИ" aria-label="Тег ИИ">#ИИ</button>
              <button class="chip sm" data-tag="разработка" aria-label="Тег разработка">
                #разработка
              </button>
            </div>
            <div class="mt-auto border-t border-line pt-3">
              <div class="flex flex-wrap items-center gap-x-4 gap-y-1">
                <button class="act like" data-like="2" aria-pressed="true" aria-label="Нравится">
                  <svg class="ico" viewBox="0 0 24 24">
                    <path
                      d="M20.84 4.61a5.5 5.5 0 0 0-7.78 0L12 5.67l-1.06-1.06a5.5 5.5 0 0 0-7.78 7.78l1.06 1.06L12 21.23l7.78-7.78 1.06-1.06a5.5 5.5 0 0 0 0-7.78z"
                    ></path>
                  </svg>
                  <span class="cnt">313</span>
                </button>
                <span class="act" title="Просмотры">
                  <svg class="ico" viewBox="0 0 24 24">
                    <path d="M1 12s4-8 11-8 11 8 11 8-4 8-11 8-11-8-11-8z"></path>
                    <circle cx="12" cy="12" r="3"></circle>
                  </svg>
                  <span data-views="2">5,2 тыс.</span>
                </span>
                <button
                  class="act rate ml-auto"
                  data-open="2"
                  title="Рейтинг: 188 оценок"
                  aria-label="Рейтинг 4,7, открыть материал"
                >
                  <svg class="ico" viewBox="0 0 24 24">
                    <polygon
                      points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"
                    ></polygon>
                  </svg>
                  <span class="font-semibold text-ink">4,7</span>
                  <span class="opacity-70">(188)</span>
                </button>
              </div>
            </div>
          </div>
        </article>
        <article class="card" data-id="5">
          <div class="cover" data-open="5">
            <EconomicIcon />
            <span class="cat-pill"> <i class="dot" style="background: #60806c"> </i>Экономика</span>
          </div>
          <div class="flex grow flex-col gap-3 px-3.5 pb-3 pt-4">
            <div class="flex items-center justify-between gap-3 text-[13px] text-mute">
              <span class="flex min-w-0 items-center gap-2">
                <span class="mono" style="background: #557563" aria-hidden="true">РС</span>
                <span class="truncate font-medium text-ink/80">Рынок сегодня</span>
              </span>
              <span class="shrink-0">58 мин назад</span>
            </div>
            <h3 class="text-[1.0625rem] font-semibold leading-snug tracking-[-0.012em]">
              <button class="title-btn" data-open="5">
                Цены в крупнейших экономиках растут медленнее, чем ожидали аналитики
              </button>
            </h3>
            <p class="line-clamp-3 text-[15px] leading-relaxed text-mute">
              Свежая статистика показала замедление потребительской инфляции второй месяц подряд.
              Эксперты расходятся в оценках: одни говорят об устойчивом тренде, другие — о временном
              эффекте от снижения цен на энергоносители.
            </p>
            <div class="-ml-1 flex flex-wrap gap-1">
              <button class="chip sm" data-tag="инфляция" aria-label="Тег инфляция">
                #инфляция
              </button>
              <button class="chip sm" data-tag="макроэкономика" aria-label="Тег макроэкономика">
                #макроэкономика
              </button>
            </div>
            <div class="mt-auto border-t border-line pt-3">
              <div class="flex flex-wrap items-center gap-x-4 gap-y-1">
                <button class="act like" data-like="5" aria-pressed="false" aria-label="Нравится">
                  <svg class="ico" viewBox="0 0 24 24">
                    <path
                      d="M20.84 4.61a5.5 5.5 0 0 0-7.78 0L12 5.67l-1.06-1.06a5.5 5.5 0 0 0-7.78 7.78l1.06 1.06L12 21.23l7.78-7.78 1.06-1.06a5.5 5.5 0 0 0 0-7.78z"
                    ></path>
                  </svg>
                  <span class="cnt">87</span>
                </button>
                <span class="act" title="Просмотры">
                  <svg class="ico" viewBox="0 0 24 24">
                    <path d="M1 12s4-8 11-8 11 8 11 8-4 8-11 8-11-8-11-8z"></path>
                    <circle cx="12" cy="12" r="3"></circle>
                  </svg>
                  <span data-views="5">3,1 тыс.</span>
                </span>
                <button
                  class="act rate ml-auto"
                  data-open="5"
                  title="Рейтинг: 54 оценки"
                  aria-label="Рейтинг 4,0, открыть материал"
                >
                  <svg class="ico" viewBox="0 0 24 24">
                    <polygon
                      points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"
                    ></polygon>
                  </svg>
                  <span class="font-semibold text-ink">4,0</span>
                  <span class="opacity-70">(54)</span>
                </button>
              </div>
            </div>
          </div>
        </article>
        <article class="card" data-id="16">
          <div class="cover" data-open="16">
            <SportIcon />
            <span class="cat-pill"> <i class="dot" style="background: #c58b2a"> </i>Спорт</span>
          </div>
          <div class="flex grow flex-col gap-3 px-3.5 pb-3 pt-4">
            <div class="flex items-center justify-between gap-3 text-[13px] text-mute">
              <span class="flex min-w-0 items-center gap-2">
                <span class="mono" style="background: #b8811f" aria-hidden="true">СТ</span>
                <span class="truncate font-medium text-ink/80">Стадион</span>
              </span>
              <span class="shrink-0">1 ч назад</span>
            </div>
            <h3 class="text-[1.0625rem] font-semibold leading-snug tracking-[-0.012em]">
              <button class="title-btn" data-open="16">
                Молодая команда неожиданно возглавила таблицу после десятого тура
              </button>
            </h3>
            <p class="line-clamp-3 text-[15px] leading-relaxed text-mute">
              Клуб, который весной чудом избежал вылета, выиграл шесть матчей подряд. Тренер
              объясняет успех дисциплиной в обороне и удачной работой с молодёжью.
            </p>
            <div class="-ml-1 flex flex-wrap gap-1">
              <button class="chip sm" data-tag="футбол" aria-label="Тег футбол">#футбол</button>
              <button class="chip sm" data-tag="чемпионат" aria-label="Тег чемпионат">
                #чемпионат
              </button>
            </div>
            <div class="mt-auto border-t border-line pt-3">
              <div class="flex flex-wrap items-center gap-x-4 gap-y-1">
                <button class="act like" data-like="16" aria-pressed="false" aria-label="Нравится">
                  <svg class="ico" viewBox="0 0 24 24">
                    <path
                      d="M20.84 4.61a5.5 5.5 0 0 0-7.78 0L12 5.67l-1.06-1.06a5.5 5.5 0 0 0-7.78 7.78l1.06 1.06L12 21.23l7.78-7.78 1.06-1.06a5.5 5.5 0 0 0 0-7.78z"
                    ></path>
                  </svg>
                  <span class="cnt">516</span>
                </button>
                <span class="act" title="Просмотры">
                  <svg class="ico" viewBox="0 0 24 24">
                    <path d="M1 12s4-8 11-8 11 8 11 8-4 8-11 8-11-8-11-8z"></path>
                    <circle cx="12" cy="12" r="3"></circle>
                  </svg>
                  <span data-views="16">7,4 тыс.</span>
                </span>
                <button
                  class="act rate ml-auto"
                  data-open="16"
                  title="Рейтинг: 210 оценок"
                  aria-label="Рейтинг 4,6, открыть материал"
                >
                  <svg class="ico" viewBox="0 0 24 24">
                    <polygon
                      points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"
                    ></polygon>
                  </svg>
                  <span class="font-semibold text-ink">4,6</span>
                  <span class="opacity-70">(210)</span>
                </button>
              </div>
            </div>
          </div>
        </article>
        <article class="card" data-id="3">
          <div class="cover" data-open="3">
            <TechIcon />
            <span class="cat-pill">
              <i class="dot" style="background: #6a83a0"> </i>Технологии</span
            >
          </div>
          <div class="flex grow flex-col gap-3 px-3.5 pb-3 pt-4">
            <div class="flex items-center justify-between gap-3 text-[13px] text-mute">
              <span class="flex min-w-0 items-center gap-2">
                <span class="mono" style="background: #58708d" aria-hidden="true">ТП</span>
                <span class="truncate font-medium text-ink/80">Технопост</span>
              </span>
              <span class="shrink-0">1 ч назад</span>
            </div>
            <h3 class="text-[1.0625rem] font-semibold leading-snug tracking-[-0.012em]">
              <button class="title-btn" data-open="3">
                Браузеры получат режим экономии трафика для слабых сетей
              </button>
            </h3>
            <p class="line-clamp-3 text-[15px] leading-relaxed text-mute">
              В новой версии движка страницы будут загружаться в облегчённом виде: без автозапуска
              видео и с отложенными скриптами. Для сайтов появится способ сообщить, какие элементы
              критичны.
            </p>
            <div class="-ml-1 flex flex-wrap gap-1">
              <button class="chip sm" data-tag="браузеры" aria-label="Тег браузеры">
                #браузеры
              </button>
              <button class="chip sm" data-tag="интернет" aria-label="Тег интернет">
                #интернет
              </button>
            </div>
            <div class="mt-auto border-t border-line pt-3">
              <div class="flex flex-wrap items-center gap-x-4 gap-y-1">
                <button class="act like" data-like="3" aria-pressed="false" aria-label="Нравится">
                  <svg class="ico" viewBox="0 0 24 24">
                    <path
                      d="M20.84 4.61a5.5 5.5 0 0 0-7.78 0L12 5.67l-1.06-1.06a5.5 5.5 0 0 0-7.78 7.78l1.06 1.06L12 21.23l7.78-7.78 1.06-1.06a5.5 5.5 0 0 0 0-7.78z"
                    ></path>
                  </svg>
                  <span class="cnt">141</span>
                </button>
                <span class="act" title="Просмотры">
                  <svg class="ico" viewBox="0 0 24 24">
                    <path d="M1 12s4-8 11-8 11 8 11 8-4 8-11 8-11-8-11-8z"></path>
                    <circle cx="12" cy="12" r="3"></circle>
                  </svg>
                  <span data-views="3">2,7 тыс.</span>
                </span>
                <button
                  class="act rate ml-auto"
                  data-open="3"
                  title="Рейтинг: 67 оценок"
                  aria-label="Рейтинг 4,1, открыть материал"
                >
                  <svg class="ico" viewBox="0 0 24 24">
                    <polygon
                      points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"
                    ></polygon>
                  </svg>
                  <span class="font-semibold text-ink">4,1</span>
                  <span class="opacity-70">(67)</span>
                </button>
              </div>
            </div>
          </div>
        </article>
        <article class="card" data-id="9">
          <div class="cover" data-open="9">
            <ScienceIcon />
            <span class="cat-pill"> <i class="dot" style="background: #7b6c9c"> </i>Наука</span>
          </div>
          <div class="flex grow flex-col gap-3 px-3.5 pb-3 pt-4">
            <div class="flex items-center justify-between gap-3 text-[13px] text-mute">
              <span class="flex min-w-0 items-center gap-2">
                <span class="mono" style="background: #7b6c9c" aria-hidden="true">НВ</span>
                <span class="truncate font-medium text-ink/80">Наука вслух</span>
              </span>
              <span class="shrink-0">2 ч назад</span>
            </div>
            <h3 class="text-[1.0625rem] font-semibold leading-snug tracking-[-0.012em]">
              <button class="title-btn" data-open="9">
                Астрономы нашли необычно тусклую звезду в плотной пылевой оболочке
              </button>
            </h3>
            <p class="line-clamp-3 text-[15px] leading-relaxed text-mute">
              Объект оказался ярче в инфракрасном диапазоне, чем в видимом, поэтому его так долго не
              замечали. Наблюдения помогут уточнить модели формирования звёзд.
            </p>
            <div class="-ml-1 flex flex-wrap gap-1">
              <button class="chip sm" data-tag="астрономия" aria-label="Тег астрономия">
                #астрономия
              </button>
              <button class="chip sm" data-tag="космос" aria-label="Тег космос">#космос</button>
            </div>
            <div class="mt-auto border-t border-line pt-3">
              <div class="flex flex-wrap items-center gap-x-4 gap-y-1">
                <button class="act like" data-like="9" aria-pressed="false" aria-label="Нравится">
                  <svg class="ico" viewBox="0 0 24 24">
                    <path
                      d="M20.84 4.61a5.5 5.5 0 0 0-7.78 0L12 5.67l-1.06-1.06a5.5 5.5 0 0 0-7.78 7.78l1.06 1.06L12 21.23l7.78-7.78 1.06-1.06a5.5 5.5 0 0 0 0-7.78z"
                    ></path>
                  </svg>
                  <span class="cnt">428</span>
                </button>
                <span class="act" title="Просмотры">
                  <svg class="ico" viewBox="0 0 24 24">
                    <path d="M1 12s4-8 11-8 11 8 11 8-4 8-11 8-11-8-11-8z"></path>
                    <circle cx="12" cy="12" r="3"></circle>
                  </svg>
                  <span data-views="9">6,1 тыс.</span>
                </span>
                <button
                  class="act rate ml-auto"
                  data-open="9"
                  title="Рейтинг: 173 оценки"
                  aria-label="Рейтинг 4,9, открыть материал"
                >
                  <svg class="ico" viewBox="0 0 24 24">
                    <polygon
                      points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"
                    ></polygon>
                  </svg>
                  <span class="font-semibold text-ink">4,9</span>
                  <span class="opacity-70">(173)</span>
                </button>
              </div>
            </div>
          </div>
        </article>
        <article class="card" data-id="6">
          <div class="cover" data-open="6">
            <EconomicIcon />
            <span class="cat-pill"> <i class="dot" style="background: #60806c"> </i>Экономика</span>
          </div>
          <div class="flex grow flex-col gap-3 px-3.5 pb-3 pt-4">
            <div class="flex items-center justify-between gap-3 text-[13px] text-mute">
              <span class="flex min-w-0 items-center gap-2">
                <span class="mono" style="background: #557563" aria-hidden="true">РС</span>
                <span class="truncate font-medium text-ink/80">Рынок сегодня</span>
              </span>
              <span class="shrink-0">3 ч назад</span>
            </div>
            <h3 class="text-[1.0625rem] font-semibold leading-snug tracking-[-0.012em]">
              <button class="title-btn" data-open="6">
                Малый бизнес всё чаще принимает оплату по QR-коду
              </button>
            </h3>
            <p class="line-clamp-3 text-[15px] leading-relaxed text-mute">
              Владельцы кафе и мастерских отмечают, что переход на QR снизил комиссии и ускорил
              расчёты. Сложнее всего оказалось приучить к новому способу старших покупателей.
            </p>
            <div class="-ml-1 flex flex-wrap gap-1">
              <button class="chip sm" data-tag="платежи" aria-label="Тег платежи">#платежи</button>
              <button class="chip sm" data-tag="малый бизнес" aria-label="Тег малый бизнес">
                #малый бизнес
              </button>
            </div>
            <div class="mt-auto border-t border-line pt-3">
              <div class="flex flex-wrap items-center gap-x-4 gap-y-1">
                <button class="act like" data-like="6" aria-pressed="false" aria-label="Нравится">
                  <svg class="ico" viewBox="0 0 24 24">
                    <path
                      d="M20.84 4.61a5.5 5.5 0 0 0-7.78 0L12 5.67l-1.06-1.06a5.5 5.5 0 0 0-7.78 7.78l1.06 1.06L12 21.23l7.78-7.78 1.06-1.06a5.5 5.5 0 0 0 0-7.78z"
                    ></path>
                  </svg>
                  <span class="cnt">74</span>
                </button>
                <span class="act" title="Просмотры">
                  <svg class="ico" viewBox="0 0 24 24">
                    <path d="M1 12s4-8 11-8 11 8 11 8-4 8-11 8-11-8-11-8z"></path>
                    <circle cx="12" cy="12" r="3"></circle>
                  </svg>
                  <span data-views="6">2 тыс.</span>
                </span>
                <button
                  class="act rate ml-auto"
                  data-open="6"
                  title="Рейтинг: 39 оценок"
                  aria-label="Рейтинг 4,2, открыть материал"
                >
                  <svg class="ico" viewBox="0 0 24 24">
                    <polygon
                      points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"
                    ></polygon>
                  </svg>
                  <span class="font-semibold text-ink">4,2</span>
                  <span class="opacity-70">(39)</span>
                </button>
              </div>
            </div>
          </div>
        </article> -->
      </div>
      <MoreBtn />
    </div>

    <div v-else id="feed" class="mt-5 feed-in">
      <div class="notfound rounded-xl px-6 py-14 text-center">
        <p class="text-lg font-semibold tracking-tight">Ничего не найдено</p>
        <p class="mx-auto mt-2 max-w-sm text-[15px] leading-relaxed text-mute">
          По этим условиям материалов нет. Измените запрос или сбросьте фильтры.
        </p>
        <button class="btn-quiet mt-6" data-clear="all">Сбросить фильтры</button>
      </div>
    </div>
  </section>
</template>

<style scoped>
.notfound {
  background-color: rgb(var(--surface) / 0.6);
  border: 1px solid #cccccc;
}
</style>
