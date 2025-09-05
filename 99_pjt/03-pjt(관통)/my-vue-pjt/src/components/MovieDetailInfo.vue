<template>
  <div class="detail-container" v-if="movie">
    <img :src="getPosterURL(movie.poster_path)" alt="영화 포스터" class="detail-poster">
    <div class="detail-info">
      <h1>{{ movie.title }}</h1>
      <p><strong>개봉일:</strong> {{ movie.release_date }}</p>
      <p><strong>평점:</strong> {{ movie.vote_average.toFixed(1) }}</p>
      <p><strong>장르:</strong> 
        <span v-for="genre in movie.genres" :key="genre.id" class="genre-tag">
          {{ genre.name }}
        </span>
      </p>
      <hr>
      <h3>줄거리</h3>
      <p>{{ movie.overview }}</p>
    </div>
  </div>
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
.detail-container {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  min-height: 70vh;
  text-align: center;
}

.detail-poster {
  width: 300px;
  height: 450px;
  object-fit: cover;
  margin-bottom: 24px;
}

.detail-info {
  max-width: 600px;
}

.genre-tag {
  display: inline-block;
  background: #eee;
  border-radius: 12px;
  padding: 2px 10px;
  margin: 0 4px;
  font-size: 0.95rem;
}
</style>