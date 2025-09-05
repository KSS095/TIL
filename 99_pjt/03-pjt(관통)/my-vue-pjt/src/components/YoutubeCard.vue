<template>
  <div class="youtube-card">
    <img
      :src="video.snippet.thumbnails.medium.url"
      alt="썸네일"
      class="thumbnail"
      @click="openModal"
      style="cursor:pointer"
    />
    <div class="info">
      <h4 class="title">{{ video.snippet.title }}</h4>
      <p class="desc">{{ video.snippet.description }}</p>
    </div>
  </div>
</template>

<script setup>
const props = defineProps({ video: Object })
const emit = defineEmits(['open'])

function openModal() {
  emit('open', props.video.id.videoId)
}
</script>

<style scoped>
.youtube-card {
  display: flex;
  align-items: flex-start;
  border: 1px solid #eee;
  border-radius: 8px;
  background: #fff;
  box-shadow: 0 2px 8px rgba(0,0,0,0.05);
  margin-bottom: 16px;
  padding: 16px;
  width: 100%;
  max-width: 900px; /* 더 넓게 */
  min-width: 400px;
}

.thumbnail {
  width: 180px;
  height: 120px;
  object-fit: cover;
  border-radius: 6px;
  margin-right: 24px;
}

.info {
  flex: 1;
  display: flex;
  flex-direction: column;
  justify-content: flex-start;
}

.title {
  font-size: 1.15rem;
  font-weight: bold;
  margin-bottom: 8px;
}

.desc {
  font-size: 1rem;
  color: #555;
}
</style>