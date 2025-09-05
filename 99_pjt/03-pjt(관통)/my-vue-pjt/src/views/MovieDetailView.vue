<template>
  <MovieDetailInfo :movie="movie" v-if="movie" />
  <div v-if="movie" class="trailer-section">
    <h2>공식 예고편</h2>
    <button class="youtube-btn" @click="showModal = true" aria-label="유튜브 예고편 보기">
      <svg width="48" height="48" viewBox="0 0 48 48">
        <circle cx="24" cy="24" r="24" fill="#FF0000"/>
        <polygon points="20,16 34,24 20,32" fill="#fff"/>
      </svg>
    </button>
    <YoutubeTrailerModal
      :show="showModal"
      :movieTitle="movie.title"
      @close="showModal = false"
    />
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { useRoute } from 'vue-router'
import axios from 'axios'
import MovieDetailInfo from '@/components/MovieDetailInfo.vue'
import YoutubeTrailerModal from '@/components/YoutubeTrailerModal.vue'

const route = useRoute()
const movie = ref(null)
const showModal = ref(false)

onMounted(async () => {
  const apiKey = import.meta.env.VITE_TMDB_API_KEY
  const movieId = route.params.movieId
  const url = `https://api.themoviedb.org/3/movie/${movieId}?api_key=${apiKey}&language=ko-KR`
  const response = await axios.get(url)
  movie.value = response.data
})
</script>

<style scoped>
.trailer-section {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  margin-top: 32px;
  text-align: center;
}

.youtube-btn {
  background: none;
  border: none;
  cursor: pointer;
  margin-top: 12px;
  padding: 0;
  transition: transform 0.2s;
  display: flex;
  align-items: center;
  justify-content: center;
}
.youtube-btn svg {
  display: block;
}
.youtube-btn:hover {
  transform: scale(1.1);
}
</style>