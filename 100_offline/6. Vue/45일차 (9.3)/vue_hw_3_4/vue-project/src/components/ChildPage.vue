<template>
  <div>
    <h3>자식 페이지입니다.</h3>
    <p>이름 : {{ my_children.name }}</p>
    <p>나이 : {{ my_children.age }}</p>
    <p>용돈 : {{ my_children.balance }}</p>
    <button @click="giveMeAllowance">용돈 주세요.</button>
  </div>
</template>

<script setup>
const props = defineProps({my_children: Object})
const emit = defineEmits(['giveMeAllowance'])

const giveMeAllowance = function () {
  emit('giveMeAllowance', props.my_children.name)
}
</script>

<style scoped>

</style>