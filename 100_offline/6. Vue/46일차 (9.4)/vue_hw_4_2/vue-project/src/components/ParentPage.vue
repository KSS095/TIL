<template>
  <div class="parent">
    <h2>부모 컴포넌트</h2>
    <p>{{ family.father }}</p>
    <p>{{ family.mother }}</p>

    <div>
      <ChildPage 
        v-for="(child, index) in family.children" 
        :key="index" 
        :child="child" 
      />
    </div>
  </div>
</template>

<script setup>
import ChildPage from './ChildPage.vue';

defineProps({
  family: { type: Object }
})
</script>

<style scoped>
.parent {
  border: 1px solid gray;
  margin: 10px;
  padding: 10px;
}
</style>