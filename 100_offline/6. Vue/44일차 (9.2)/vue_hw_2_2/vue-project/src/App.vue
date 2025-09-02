<script setup>
import { ref } from 'vue'

// 2. 로그인 여부를 판별할 변수 isLogin, 기본값은 false
const isLogin = ref(false)

// user 정보 객체
const user = {
  userName: 'admin',
  isAdmin: true,
  passWord: '1q2w3e4r'
}

// 3. Login/Logout 버튼 클릭 시 isLogin 값을 토글하는 메서드
const toggleLogin = () => {
  isLogin.value = !isLogin.value
}
</script>

<template>
  <div id="app">
    <header>
      <div class="wrapper">
        <h1>조건문 연습하기</h1>
        
        <!-- 3. v-on directive를 사용한 이벤트 바인딩 -->
        <!-- v-if directive를 사용한 조건부 텍스트 렌더링 -->
        <button @click="toggleLogin" class="login-btn">
          {{ isLogin ? 'Logout' : 'Login' }}
        </button>
      </div>
    </header>

    <main>
      <!-- 4. v-if directive를 사용하여 isLogin이 true일 때만 user 정보 렌더링 -->
      <div v-if="isLogin" class="user-info">
        <ul class="user-list">
          <li>유저네임 : {{ user.userName }}</li>
          <li>관리자여부 : {{ user.isAdmin }}</li>
          <li>비밀번호 : {{ user.passWord }}</li>
        </ul>
      </div>
    </main>
  </div>
</template>

<style scoped>
#app {
  max-width: 800px;
  margin: 0 auto;
  padding: 20px;
  font-family: Arial, sans-serif;
}

header {
  line-height: 1.5;
  border-bottom: 2px solid #eee;
  padding-bottom: 20px;
  margin-bottom: 30px;
}

.wrapper {
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.login-btn {
  padding: 10px 20px;
  font-size: 16px;
  background-color: #007bff;
  color: white;
  border: none;
  border-radius: 5px;
  cursor: pointer;
  transition: background-color 0.3s;
}

.login-btn:hover {
  background-color: #0056b3;
}

.user-info {
  margin-top: 20px;
}

.user-list {
  list-style: disc;
  margin-left: 20px;
  padding: 0;
}

.user-list li {
  margin: 8px 0;
  font-size: 16px;
  color: #333;
}

@media (min-width: 1024px) {
  header {
    display: flex;
    place-items: center;
  }

  header .wrapper {
    display: flex;
    place-items: center;
    justify-content: space-between;
    width: 100%;
  }
}
</style>