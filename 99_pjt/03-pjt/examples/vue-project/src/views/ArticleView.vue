<template>
  <div>
    <h1>Article List</h1>
    <ArticleList />
  </div>
</template>

<script setup>
import ArticleList from '@/components/ArticleList.vue';
import { useArticleStore } from '@/stores/article';
import { onMounted } from 'vue';
const articleStore = useArticleStore()
// articleStore.getArticles()
onMounted(() => {
  articleStore.getArticles()
})
</script>

<style>

</style>
