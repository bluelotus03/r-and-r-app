<template>
    <div class="page-sign-up">
        <div class="column is-4 is-offset-4">
            <h1 class="title">Log in</h1>
            <form @submit.prevent="submitForm">
                <div class="field">
                    <label>Username</label>
                    <div class="control">
                        <input type="text" class="input" v-model="username">
                    </div>
                </div>
                <div class="field">
                    <label>Password</label>
                    <div class="control">
                        <input type="password" class="input" v-model="password">
                    </div>
                </div>
                <div class="notification is-danger" v-if="errors.length">
                    <p v-for="error in errors" v-bind:key="error">{{ error }}</p>
                </div>    
                <div class="field">
                    <div class="control">
                        <button class="button blue">Log in</button>
                    </div>
                </div>
                <hr>
                Don't have an account? <router-link to="/sign-up">Sign up</router-link>

            </form>
        </div>
    </div>
</template>

<script>
import axios from 'axios'
import { toast } from 'bulma-toast'

export default {
    name: 'LogIn',
    data() {
        return {
            username: '',
            password: '',
            errors: []
        }
    },
    mounted() {
        document.title = 'Log In | R&R'
    },
    methods: {
        async submitForm() {
            // reset authorization 
            axios.defaults.headers.common['Authorization'] = ""

            // remove token from local storage
            localStorage.removeItem("token")

            const formData = {
                username: this.username,
                password: this.password,
            } 

            await axios
                .post("/api/v1/token/login", formData) 
                .then(response => {
                    const token = response.data.auth_token
                    this.$store.commit('setToken', token)
                    axios.defaults.headers.common['Authorization'] = "Token " + token
                    localStorage.setItem("token", token)
                    const toPath = this.$route.query.to || '/cart'

                    // redirect to cart upon login     
                    this.$router.push(toPath)
                })
                .catch(error => {
                    if (error.response) {
                        for(const property in error.response.data) {
                            this.errors.push(`${property}: ${error.response.data[property]}`)
                        }
                        console.log(JSON.stringify(error.response.data))
                    } else {
                        this.errors.push('Something went wrong. Please try again')
                        console.log(JSON.stringify(error))
                    }
                })
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