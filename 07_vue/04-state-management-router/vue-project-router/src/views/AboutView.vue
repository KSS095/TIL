<template>
  <div class="about">
    <h1>About View</h1>
  </div>
</template>

<script setup>
import { userRouter } from 'vue-router'
const router = userRouter
const someFunction = function () {
  //엄청 복잡하고 대단한 로직
  router.push({ name: 'userProfile' , params: { 'username': 'admin' }})
}
</script>

<style scoped>

</style>
