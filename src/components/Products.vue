<template>
  <div class="hello">
    <h3>Products in Database</h3>
    <p v-if="products.length === 0">No Products</p>
    <div class="product" v-for="(product, index) in products" :key="index">
        <p class="product-index">[{{index}}]</p>
        <p class="product-name" v-html="product.name"></p>
    </div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: "Products",
  data() {
    return {
      products: []
    }
  },
  created() {
    axios.get('api/products/').then(response => {
      this.products = response.data
    })
  }
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.product {
  margin: 0 auto;
  max-width: 30%;
  text-align: left;
  border-bottom: 1px solid #ccc;
  padding: 1rem;
}

.product-index {
  color: #ccc;
  font-size: 0.8rem;
  /* margin-bottom: 0; */
}
</style>
