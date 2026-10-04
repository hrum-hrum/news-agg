<template>
      <!-- Мобильные фильтры -->
    <div class="mb-5 space-y-2 lg:hidden">
      <div class="rail" data-slot="cats-m" aria-label="Категории">
        <button class="chip" data-cat="all" aria-pressed="true">Все</button
        ><button class="chip" data-cat="tech" aria-pressed="false">Технологии</button
        ><button class="chip" data-cat="eco" aria-pressed="false">Экономика</button
        ><button class="chip" data-cat="sci" aria-pressed="false">Наука</button
        ><button class="chip" data-cat="cul" aria-pressed="false">Культура</button
        ><button class="chip" data-cat="spo" aria-pressed="false">Спорт</button
        ><button class="chip" data-cat="wor" aria-pressed="false">Мир</button>
      </div>
      <div class="rail" data-slot="tags-m" aria-label="Теги">
        <button class="chip" data-tag="города" aria-pressed="false">#города</button
        ><button class="chip" data-tag="экология" aria-pressed="false">#экология</button
        ><button class="chip" data-tag="океан" aria-pressed="false">#океан</button
        ><button class="chip" data-tag="сон" aria-pressed="false">#сон</button
        ><button class="chip" data-tag="транспорт" aria-pressed="false">#транспорт</button
        ><button class="chip" data-tag="археология" aria-pressed="false">#археология</button
        ><button class="chip" data-tag="астрономия" aria-pressed="false">#астрономия</button
        ><button class="chip" data-tag="батареи" aria-pressed="false">#батареи</button
        ><button class="chip" data-tag="бег" aria-pressed="false">#бег</button
        ><button class="chip" data-tag="браузеры" aria-pressed="false">#браузеры</button
        ><button class="chip" data-tag="выставки" aria-pressed="false">#выставки</button
        ><button class="chip" data-tag="ИИ" aria-pressed="false">#ИИ</button
        ><button class="chip" data-tag="интернет" aria-pressed="false">#интернет</button
        ><button class="chip" data-tag="инфляция" aria-pressed="false">#инфляция</button
        ><button class="chip" data-tag="история" aria-pressed="false">#история</button
        ><button class="chip" data-tag="кино" aria-pressed="false">#кино</button>
      </div>
    </div>
</template>
