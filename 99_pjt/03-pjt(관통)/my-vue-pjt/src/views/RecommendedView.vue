<template>
  <div class="recommended-container" v-if="movie && weather">
    <h2>오늘의 서울 날씨: <span class="weather">{{ weather }}</span></h2>
    <p>추천 장르: <span class="genre">{{ genreName }}</span></p>
    <div class="movie-card">
      <img
        :src="getPosterURL(movie.poster_path)"
        alt="포스터"
        class="poster"
        @click="goToDetail(movie.id)"
        style="cursor:pointer"
      />
      <div class="info">
        <h3>{{ movie.title }}</h3>
        <p>{{ movie.overview }}</p>
        <p><strong>개봉일:</strong> {{ movie.release_date }}</p>
      </div>
    </div>
  </div>
  <div v-else class="loading">
    <p>추천 영화를 불러오는 중...</p>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { useRouter } from 'vue-router'
import axios from 'axios'

const router = useRouter()
const weather = ref(null)
const genreName = ref('')
const movie = ref(null)

const weatherGenreMap = {
  Rain: { id: 18, name: '드라마' },
  Clear: { id: 35, name: '코미디' },
  Clouds: { id: 53, name: '스릴러' },
  Snow: { id: 16, name: '애니메이션' },
  Mist: { id: 99, name: '다큐멘터리' },
  Thunderstorm: { id: 27, name: '공포' }
}

function getPosterURL(path) {
  return `https://image.tmdb.org/t/p/w500${path}`
}

function goToDetail(movieId) {
  router.push({ name: 'MovieDetailView', params: { movieId } })
}

onMounted(async () => {
  try {
    const weatherApiKey = import.meta.env.VITE_OPENWEATHER_API_KEY
    const weatherUrl = `https://api.openweathermap.org/data/2.5/weather?q=Seoul&appid=${weatherApiKey}&units=metric`
    const weatherRes = await axios.get(weatherUrl)
    const mainWeather = weatherRes.data.weather[0].main
    weather.value = mainWeather

    const genreObj = weatherGenreMap[mainWeather] || weatherGenreMap['Clear']
    genreName.value = genreObj.name

    const tmdbApiKey = import.meta.env.VITE_TMDB_API_KEY
    const tmdbUrl = `https://api.themoviedb.org/3/discover/movie?api_key=${tmdbApiKey}&with_genres=${genreObj.id}&language=ko-KR`
    const tmdbRes = await axios.get(tmdbUrl)
    const movies = tmdbRes.data.results

    if (movies.length > 0) {
      movie.value = movies[Math.floor(Math.random() * movies.length)]
    }
  } catch (e) {
    weather.value = null
    movie.value = null
  }
})
</script>

<style scoped>
.recommended-container {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  min-height: 70vh;
  text-align: center;
}

.weather, .genre {
  font-weight: bold;
  color: #ff1744;
}

.movie-card {
  display: flex;
  align-items: flex-start;
  background: #fff;
  border-radius: 12px;
  box-shadow: 0 2px 8px rgba(0,0,0,0.07);
  margin-top: 32px;
  padding: 24px;
  max-width: 700px;
}

.poster {
  width: 180px;
  height: 260px;
  object-fit: cover;
  border-radius: 8px;
  margin-right: 32px;
}

.info {
  flex: 1;
  text-align: left;
}

.loading {
  min-height: 70vh;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 1.2rem;
  color: #888;
}
</style>