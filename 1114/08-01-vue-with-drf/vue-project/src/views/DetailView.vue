<template>
  <div>
    <h1>Detail</h1>
    <p>제목: {{ article?.title }}</p>
    <p>내용: {{ article.content }}</p>
    <p>작성일: {{ article.created_at }}</p>
    <p>수정일: {{ article.updated_at }}</p>

  </div>
</template>

<script setup>
import axios from 'axios';
import { onMounted } from 'vue';
import { useCounterStore } from '../stores/counter';
import { useRoute } from 'vue-router';

const store = useCounterStore()
const route = useRoute()
const aricle = ref(null)

onMounted(() => {
  axios({
    method: 'get',
    url: `${store.API_URL}/api/v1/articles/${route.params.id}/`
  })
    .then((res) => {
      console.log(res.data)
    })
    .catch((err) => {
      console.log(err)
    })
})
</script>

<style>

</style>
