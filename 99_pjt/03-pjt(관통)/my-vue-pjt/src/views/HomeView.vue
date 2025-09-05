<template>
  <div class="home">
    <h1>🎬 영화 추천 서비스에 오신 것을 환영합니다!</h1>
    <p>최신 인기 영화와 리뷰, 예고편까지 한 번에 만나보세요.</p>
    <div class="actions">
      <RouterLink :to="{ name: 'MovieListView' }" class="main-btn">추천 영화 보러가기</RouterLink>
      <RouterLink :to="{ name: 'ReviewSearchView' }" class="main-btn">예고편 검색하기</RouterLink>
    </div>
    <div class="bg-movie"></div>
  </div>
</template>

<script setup>
import { RouterLink } from 'vue-router'
</script>

<style scoped>
.home {
  min-height: 70vh;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  position: relative;
  text-align: center;
  background: linear-gradient(135deg, #f8fafc 60%, #ffe3e3 100%);
}

h1 {
  font-size: 2.2rem;
  margin-bottom: 16px;
  color: #d50000;
}

p {
  font-size: 1.15rem;
  margin-bottom: 32px;
  color: #333;
}

.actions {
  display: flex;
  gap: 20px;
  margin-bottom: 40px;
}

.main-btn {
  padding: 12px 28px;
  background: #ff1744;
  color: #fff;
  border-radius: 8px;
  font-size: 1.1rem;
  font-weight: bold;
  text-decoration: none;
  box-shadow: 0 2px 8px rgba(0,0,0,0.07);
  transition: background 0.2s;
}
.main-btn:hover {
  background: #d50000;
}

.bg-movie {
  position: absolute;
  bottom: 0;
  left: 0;
  width: 100%;
  height: 120px;
  background: url('https://images.unsplash.com/photo-1465101046530-73398c7f28ca?auto=format&fit=crop&w=900&q=80') center/cover no-repeat;
  opacity: 0.15;
  z-index: 0;
  pointer-events: none;
}
</style>