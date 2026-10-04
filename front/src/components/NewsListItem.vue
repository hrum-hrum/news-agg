<script setup>
import TechIcon from './icons/IconTech.vue'
import WorldIcon from './icons/IconWorld.vue'
import EconomicIcon from './icons/IconEconomic.vue'
import SportIcon from './icons/IconSport.vue'
import ScienceIcon from './icons/IconScience.vue'
import CultureIcon from './icons/IconCulture.vue'
import CatPill from './base/CatPill.vue'
import TagBtn from './base/TagBtn.vue'
import LikeBtn from './base/LikeBtn.vue'
import UserViews from './base/UserViews.vue'
import RatingData from './base/RatingData.vue'
import SentimentPill from './base/SentimentPill.vue'
import { computed } from 'vue'

// c — категория, s — источник, t — заголовок, l — лид, g — теги, m — минут назад, v — просмотры, k — лайки, r — [рейтинг, число оценок]
const props = defineProps({
  id: Number,
  c: {
    type: String,
    required: true,
  },
  s: String,
  t: String,
  l: String,
  g: Array,
  m: Number,
  v: Number,
  k: Number,
  r: Array,
  a: String,
  // title: String,
  // content: String,
  // imageUrl: String,
  // publishedAt: String,
  // comments: Array,
})

const COMPONENT_ICONS = {
  tech: TechIcon,
  eco: EconomicIcon,
  sci: ScienceIcon,
  cul: CultureIcon,
  spo: SportIcon,
  wor: WorldIcon,
}

const icon = computed(() => {
  return COMPONENT_ICONS[props.c] || null // null или дефолтная иконка, если ключ не найден
})
</script>

<template>
  <article class="card" data-id="13">
    <div class="cover" data-open="13">
      <!-- <CultureIcon /> -->
      <component :is="icon" />
      <CatPill :id="c" />
    </div>
    <div class="flex grow flex-col gap-3 px-3.5 pb-3 pt-4">
      <div class="flex items-center justify-between gap-3 text-[13px] text-mute">
        <!-- <span class="flex min-w-0 items-center gap-2">
          <span class="mono" style="background: #bd6046" aria-hidden="true">КС</span>
          <span class="truncate font-medium text-ink/80">Культурный слой</span>
        </span> -->
        <SentimentPill :id="a" />
        <span class="shrink-0">{{ m }} мин назад</span>
      </div>
      <h3 class="text-[1.0625rem] font-semibold leading-snug tracking-[-0.012em]">
        <button class="title-btn" data-open="13">
          {{ t }}
        </button>
      </h3>
      <p class="line-clamp-3 text-[15px] leading-relaxed text-mute">
        {{ l }}
      </p>
      <div v-if="g?.length" class="-ml-1 flex flex-wrap gap-1">
        <TagBtn v-for="tag in g" :key="tag" :name="tag" />
      </div>
      <div class="mt-auto border-t border-line pt-3">
        <div class="flex flex-wrap items-center gap-x-4 gap-y-1">
          <LikeBtn :likes="k" />
          <UserViews :views="v" />
          <RatingData :rate="r" />
        </div>
      </div>
    </div>
  </article>
</template>
