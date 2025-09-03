<template>
  <div class="child-box">
    <h3>자식 페이지입니다.</h3>
    <p>이름 : {{ myChildren.name }}</p>
    <p>나이 : {{ myChildren.age }}</p>
  </div>
</template>

<script setup>
defineProps({
  myChildren: Object
})
</script>

<style scoped>
.child-box {
  border: 1px solid #ccc;
  padding: 10px;
  margin: 10px 0;   /* 자식 박스 사이 간격 */
}
</style>