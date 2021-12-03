<template>
    <div class="page-my-account">
        <div class="columns is-multiline">
            <div class="column is-12">
                <h1 class="title">My account</h1>
            </div>
             <div class="column is-12">
                <button @click="logout()" class="button blue">Log out</button>
            </div>
        </div>
    </div>
</template>

<script>
import axios from 'axios'
export default {
    name: 'MyAccount',
    methods: {
        logout() {
            axios.defaults.headers.common['Authorization'] = ""
            localStorage.removeItem("token")
            localStorage.removeItem("username")
            localStorage.removeItem("userid")
            this.$store.commit('removeToken')

            // redirect to home page upon logout
            this.$router.push('/')
        }
    }
}
</script>

<style scoped>
.blue {
  background-color: #1d4286;
}
.blue:hover {
    background-color: #0b4eca;
    color: white;
}
</style>