<template>
  <section class="parent_box">
    <h1>부모 페이지입니다.</h1>
    <ChildPage 
      v-for="child in children"
      :key="child.name"
      :myChildren="child"
    />
  </section>
</template>

<script setup>
import ChildPage from './ChildPage.vue';
import { ref } from 'vue'

const children = ref([
  { name: '김하나', age: 30 },
  { name: '김두리', age: 20 },
  { name: '김서이', age: 10 },
])
</script>

<style scoped>
.parent_box {
  border: 1px solid #999;
  padding: 10px;
}
</style>