<template>
    <div class="page-success">
        <div class="columns is-multiline">
            <div class="column is-12">
                <h1 class="title">Thank you!</h1>
                <p>Please allow up to 48 hours to process your order.</p>
            </div>
        </div>
    </div>
</template>

<script>
export default {
    name: 'Success',
    mounted() {
        document.title = 'Success | R&R'
    },
}
</script>