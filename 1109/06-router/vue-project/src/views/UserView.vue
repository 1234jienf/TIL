
<template>
    <div>
        <h1>UserView</h1>
        <h2>{{ userId  }}번 User 페이지</h2>
        <button @click="routeUpdate">100번 유저 페이지</button>
    </div>
</template>

<script setup>
import {ref} from 'vue'
import { useRoute, useRouter, onBeforeRouteLeave, onBeforeRouteUpdate } from 'vue-router';

onBeforeRouteLeave((to,from) => {
    const answer = window.confirm('정말 떠나실 건가요?')
    if (answer === false) {
        return false
    }
})

const routeUpdate = function() {
    router.push({ name: 'user', params: {id:100}})
}

onBeforeRouteUpdate((to,from) => {
    userId.value = to.params.id
})
const route = useRoute()
const userId = ref(route.params.id)

// 프로그래밍 방식 네비게이션
const router = useRouter()

const goHome = function() {
    // router.push({name:'home'})
    router.replace({name: 'home'})
}
</script>

<style scoped>

</style>