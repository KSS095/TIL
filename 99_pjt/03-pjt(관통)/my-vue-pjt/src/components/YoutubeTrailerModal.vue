<template>
  <div v-if="show" class="modal-overlay" @click.self="close">
    <div class="modal-content">
      <button class="close-btn" @click="close">X</button>
      <div v-if="videoId">
        <iframe
          width="560"
          height="315"
          :src="`https://www.youtube.com/embed/${videoId}`"
          frameborder="0"
          allow="autoplay; encrypted-media"
          allowfullscreen
        ></iframe>
      </div>
      <div v-else>
        <p>예고편을 찾을 수 없습니다.</p>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, watch } from 'vue'

const props = defineProps({
  show: Boolean,
  movieTitle: String
})
const emit = defineEmits(['close'])

const videoId = ref(null)

watch(() => props.show, async (val) => {
  if (val && props.movieTitle) {
    const apiKey = import.meta.env.VITE_YOUTUBE_API_KEY
    const query = encodeURIComponent(`${props.movieTitle} trailer`)
    const url = `https://www.googleapis.com/youtube/v3/search?part=snippet&type=video&q=${query}&key=${apiKey}&maxResults=1`
    try {
      const res = await fetch(url)
      const data = await res.json()
      if (data.items && data.items.length > 0) {
        videoId.value = data.items[0].id.videoId
      } else {
        videoId.value = null
      }
    } catch (e) {
      videoId.value = null
    }
  }
})

function close() {
  emit('close')
  videoId.value = null
}
</script>

<style scoped>
.modal-overlay {
  position: fixed;
  top: 0; left: 0; right: 0; bottom: 0;
  background: rgba(0,0,0,0.7);
  display: flex;
  align-items: center;
  justify-content: center;
  z-index: 1000;
}
.modal-content {
  background: #fff;
  padding: 24px;
  border-radius: 12px;
  position: relative;
  min-width: 320px;
}
.close-btn {
  position: absolute;
  top: 8px;
  right: 8px;
  background: #eee;
  border: none;
  border-radius: 4px;
  padding: 6px 12px;
  cursor: pointer;
}
</style>