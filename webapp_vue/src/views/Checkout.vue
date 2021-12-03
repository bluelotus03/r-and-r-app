<template>
    <div class="page-checkout">
        <div class="columns is-multiline">
            <div class="column is-12">
                <h1 class="title">Checkout</h1>
            </div>
            <div class="column is-12 box">
                <table class="table is-fullwidth">
                    <thead>
                        <tr>
                            <th>Product</th>
                            <th>Price</th>
                            <th>Quantity</th>
                            <th>Total</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr v-for="item in cart.items" v-bind:key="item.product.id">
                            <td>{{ item.product.name }}</td>
                            <td>{{ item.product.price }}</td>
                            <td>{{ item.quantity }}</td>
                            <td>{{ getItemTotal(item).toFixed(2) }}</td>
                        </tr>    
                    </tbody>
                    <tfoot>
                        <tr>
                            <td colspan="2">Total</td>
                            <td>{{ cartTotalLength }}</td>
                            <td>{{ cartTotalPrice.toFixed(2) }}</td>
                        </tr>
                    </tfoot>
                </table>
            </div>
            <div class="column is-12 box"> 
                <h2 class="subtitle">Shipping details</h2>
                <p class="has-text-grey mb-4">*All fields are required</p>
                <div class="columns is-multiline">
                    <div class="column is-6">
                            <div class="field">
                                <label>First Name*</label>
                                <div class="control">
                                    <input type="text" class="input" v-model="first_name">
                                </div>
                            </div>
                            <div class="field">
                                <label>Last Name*</label>
                                <div class="control">
                                    <input type="text" class="input" v-model="last_name">
                                </div>
                            </div>
                            <div class="field">
                                <label>Email*</label>
                                <div class="control">
                                    <input type="email" class="input" v-model="email">
                                </div>
                            </div>
                            <div class="field">
                                <label>Phone*</label>
                                <div class="control">
                                    <input type="email" class="input" v-model="phone">
                                </div>
                            </div>
                    </div>
                    <div class="column is-6">
                            <div class="field">
                                <label>Address*</label>
                                <div class="control">
                                    <input type="text" class="input" v-model="address">
                                </div>
                            </div>
                            <div class="field">
                                <label>Zipcode*</label>
                                <div class="control">
                                    <input type="text" class="input" v-model="zipcode">
                                </div>
                            </div>
                            <div class="field">
                                <label>State*</label>
                                <div class="control">
                                    <input type="email" class="input" v-model="state">
                                </div>
                            </div>
                    </div>   
                </div>
                <div class="notification is-danger mt-4" v-if="errors.length">
                        <p v-for="error in errors" v-bind:key="error">{{ error }}</p>
                </div>    
                <hr>
                <div id="card-element" class="mb-5"></div>    
                    <!-- if more than 0 items in cart, show button option to Pay with Stripe -->
                    <template v-if="cartTotalLength">
                        <hr>
                        <button class="button blue" @click="submitForm">Pay with Stripe</button>
                    </template>
            </div>
        </div>
    </div>
</template>

<script>
import axios from 'axios'

export default {
    name: 'Checkout',
    data() {
        return {
            cart: {
                items: []
            },
            stripe: {},
            card: {},
            first_name: '',
            last_name: '',
            email: '',
            phone: '',
            address: '',
            zipcode: '',
            state: '',
            errors: []
        }
    },
    mounted() {
        document.title = 'Checkout | R&R'
        this.cart = this.$store.state.cart
    },
    methods: {
        getItemTotal(item) {
            return item.quantity * item.product.price
        },
        submitForm() {
            this.errors = []
            if (this.first_name === '') {
                this.errors.push('Please enter First Name')
            }
            if(this.last_name === '') {
                this.errors.push('Please enter Last Name')
            }
            if(this.email === '') {
                this.errors.push('Please enter Email')
            }
            if(this.phone === '') {
                this.errors.push('Please enter Phone Number')
            }
            if(this.address === '') {
                this.errors.push('Please enter Address')
            }
            if(this.zipcode === '') {
                this.errors.push('Please enter Zipcode')
            }
            if(this.state === '') {
                this.errors.push('Please enter State')
            }
        }
    },
    computed: {
        cartTotalLength() {
            return this.cart.items.reduce((accumulator, currentVal) => {
                return accumulator += currentVal.quantity
                }, 0)
        },
        cartTotalPrice() {
            return this.cart.items.reduce((accumulator, currentVal) => {
                return accumulator += currentVal.product.price * currentVal.quantity
            }, 0)
        },
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