<template>
  <router-link :to="{ name: 'MovieDetailView', params: { movieId: movie.id } }">
    <div class="card">
      <img :src="getPosterURL(movie.poster_path)" class="card-img-top" alt="영화 포스터">
      <div class="card-body">
        <h5 class="card-title">{{ movie.title }}</h5>
        <p class="card-text">{{ movie.overview }}</p>
      </div>
    </div>
  </router-link>
</template>

<script setup>
import { defineProps } from 'vue'

defineProps({
  movie: Object
})

const getPosterURL = (posterPath) => {
  return `https://image.tmdb.org/t/p/w500${posterPath}`
}
</script>

<style scoped>
.card {
  width: 250px;
  border: 1px solid #eee;
  border-radius: 8px;
  overflow: hidden;
  box-shadow: 0 2px 8px rgba(0,0,0,0.05);
  background: #fff;
  display: flex;
  flex-direction: column;
}

.card-img-top {
  width: 100%;
  height: 350px;
  object-fit: cover;
  display: block;
}

.card-body {
  flex: 1;
  padding: 16px;
  display: flex;
  flex-direction: column;
}

.card-title {
  font-size: 1.1rem;
  margin-bottom: 8px;
}

.card-text {
  font-size: 0.95rem;
  color: #555;
}
</style>