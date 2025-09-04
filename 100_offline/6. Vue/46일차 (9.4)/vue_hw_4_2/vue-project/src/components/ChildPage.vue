<template>
  <div class="children">
    <h3>자식 페이지</h3>
    <p>{{ child.name }}</p>
  </div>
</template>

<script setup>
defineProps({
  child: { type: Object }
})
</script>

<style scoped>
.children {
  border: 1px solid gray;
  margin: 10px;
  padding: 10px;
}
</style>