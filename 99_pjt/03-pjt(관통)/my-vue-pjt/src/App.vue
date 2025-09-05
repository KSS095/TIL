<template>
  <header>
    <nav class="nav-bar">
      <RouterLink class="nav-btn" :to="{ name: 'HomeView' }">Home</RouterLink>
      <RouterLink class="nav-btn" :to="{ name: 'MovieListView' }">Movies</RouterLink>
      <RouterLink class="nav-btn" :to="{ name: 'ReviewSearchView' }">Review Search</RouterLink>
      <RouterLink class="nav-btn" :to="{ name: 'RecommendedView' }">Today's Recommendation</RouterLink>
    </nav>
  </header>
  <RouterView />
</template>

<script setup>
import { RouterView, RouterLink } from 'vue-router'
</script>

<style scoped>
.nav-bar {
  display: flex;
  justify-content: center;
  align-items: center;
  gap: 24px;
  background: #fff;
  padding: 24px 0 16px 0;
  box-shadow: 0 2px 8px rgba(0,0,0,0.04);
}

.nav-btn {
  padding: 10px 28px;
  background: linear-gradient(90deg, #ff1744 60%, #ff8a65 100%);
  color: #fff;
  border-radius: 24px;
  font-size: 1.08rem;
  font-weight: bold;
  text-decoration: none;
  box-shadow: 0 2px 8px rgba(0,0,0,0.07);
  transition: background 0.2s, transform 0.2s;
  border: none;
  outline: none;
  cursor: pointer;
  letter-spacing: 1px;
  display: inline-block;
}

.nav-btn:hover,
.router-link-active.nav-btn {
  background: linear-gradient(90deg, #d50000 60%, #ff7043 100%);
  transform: scale(1.07);
  color: #fff;
}
</style>