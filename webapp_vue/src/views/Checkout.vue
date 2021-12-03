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

        if (this.cartTotalLength > 0) {
            this.stripe = Stripe('sk_test_51K2h1WHDcgh7mtUSuHauVtsQ5BeFiZRfeDXddTpAK4C86nBo8E7XDOpyDU6Tw2r1lNYWZlEaWw1aVlCogQ65usqY00JM4rGy6B')
            const elements = this.stripe.elements();
            this.card = elements.create('card', { hidePostalCode: true })
            this.card.mount('#card-element')
        }
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

            if (!this.errors.length) {
                this.$store.commit('setIsLoading', true)
                this.stripe.createToken(this.card).then(result => {
                    if (result.error) {
                        this.$store.commit('setIsLoading', false)
                        this.errors.push('Something went wrong with Stripe. Please try again.')
                        console.log(result.error.message)
                    } else {
                        this.stripeTokenHandler(result.token)
                    }
                })
            }
        },
        async stripeTokenHandler(token) {
        const items = []
            for (let i=0; i < this.cart.items.length; i++) {
                const item = this.cart.items[i]
                const obj = {
                    product: item.product.id,
                    quantity: item.quantity,
                    price: item.product.price * item.quantity
                }
                items.push(obj)
            }
            
            const data = {
                'first_name': this.first_name,
                'last_name': this.first_name,
                'email': this.email,
                'phone': this.phone,
                'address': this.address,
                'zipcode': this.zipcode,
                'state': this.state,
                'items': items,
                'stripe_token': token.id,
            }

            await axios
                .post('/api/v1/checkout', data)
                .then(response => {
                    this.$store.commit('clearCart')
                    this.$router.push('/cart/success')
                })
                .catch(error => {
                    this.errors.push('Something went wrong. Please try again.')
                    console.log(error)
                })

                this.$store.commit('setIsLoading', false)
        },
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