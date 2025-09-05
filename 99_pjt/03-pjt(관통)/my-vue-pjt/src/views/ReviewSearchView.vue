<template>
  <div class="search-container">
    <div class="search-bar">
      <input v-model="keyword" placeholder="영화 제목을 입력하세요" />
      <button class="search-btn" @click="searchYoutube">검색</button>
    </div>
    <div class="results">
      <YoutubeCard
        v-for="video in videos"
        :key="video.id.videoId"
        :video="video"
        @open="openModal"
      />
    </div>
    <YoutubeReviewModal
      v-if="showModal"
      :videoId="selectedVideoId"
      @close="closeModal"
    />
  </div>
</template>

<script setup>
import { ref } from 'vue'
import YoutubeCard from '@/components/YoutubeCard.vue'
import YoutubeReviewModal from '@/components/YoutubeReviewModal.vue'

const keyword = ref('')
const videos = ref([])
const showModal = ref(false)
const selectedVideoId = ref(null)

async function searchYoutube() {
  if (!keyword.value) return
  const apiKey = import.meta.env.VITE_YOUTUBE_API_KEY
  const query = encodeURIComponent(keyword.value + ' trailer')
  const url = `https://www.googleapis.com/youtube/v3/search?part=snippet&type=video&q=${query}&key=${apiKey}&maxResults=5`
  try {
    const res = await fetch(url)
    const data = await res.json()
    videos.value = data.items || []
  } catch (e) {
    videos.value = []
  }
}

function openModal(videoId) {
  selectedVideoId.value = videoId
  showModal.value = true
}
function closeModal() {
  showModal.value = false
  selectedVideoId.value = null
}
</script>

<style scoped>
.search-container {
  display: flex;
  flex-direction: column;
  align-items: center;
  margin-top: 40px;
}

.search-bar {
  display: flex;
  align-items: center;
  justify-content: center;
  margin-bottom: 32px;
  gap: 12px;
}

input {
  padding: 8px 14px;
  font-size: 1rem;
  border: 1px solid #ccc;
  border-radius: 6px;
  outline: none;
  width: 260px;
}

.search-btn {
  padding: 8px 20px;
  font-size: 1rem;
  background: #ff1744;
  color: #fff;
  border: none;
  border-radius: 6px;
  cursor: pointer;
  font-weight: bold;
  transition: background 0.2s;
}
.search-btn:hover {
  background: #d50000;
}

.results {
  width: 100%;
  display: flex;
  flex-direction: column;
  align-items: center;
}
</style>