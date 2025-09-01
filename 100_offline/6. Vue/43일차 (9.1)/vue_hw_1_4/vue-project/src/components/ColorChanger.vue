<template>
  <div>
    <!-- 사용자 입력 -->
    <input v-model="colorClass" placeholder="red / blue / green 입력" />

    <!-- 색상 바뀌는 p 태그 -->
    <p :class="colorClass">
      입력창에 올바른 색상 명을 입력하면 글자색이 바껴요.
    </p>
  </div>
</template>

<script>
export default {
  name: "ColorChanger",
  data() {
    return {
      colorClass: "", // 사용자가 입력한 값 저장
    };
  },
};
</script>

<style scoped>
.red {
  color: red;
}
.blue {
  color: blue;
}
.green {
  color: green;
}
</style>
