//vscode snippet: pinia-setup
import { ref } from 'vue'
import { defineStore, acceptHMRUpdate } from 'pinia'
import NEWS from '@/constants/news'

export const usePostsStore = defineStore('posts', () => {
  const error = ref('')
  const posts = ref([])

  const fetchPosts = async (args) => {
    const { page, search } = args || {}

    // try {
    //   // const response = await fetch('http://localhost:3002/posts') Путь настроен в vite.config
    //   const response = await fetch(
    //     `/api/posts?search=${searchQuery.value}&limit=9&page=${currentPage.value}`,
    //   )
    //   if (!response.ok) {
    //     throw new Error('Posts request error')
    //   }
    //   const { data } = await response.json()
    //   posts.value = data.posts
    //   totalPage.value = data.lastPage
    //   //console.log(data)
    // } catch (e) {
    //   console.error(e)
    //   error.value = 'Ошибка получения списка статей'
    // }
    //posts.value = [...posts.value, ...NEWS]
    // Полный аналог спреда, но без оператора "..."
    posts.value = posts.value.concat(NEWS)
  }

  return { error, posts, fetchPosts }
})

if (import.meta.hot) {
  import.meta.hot.accept(acceptHMRUpdate(usePostsStore, import.meta.hot))
}
