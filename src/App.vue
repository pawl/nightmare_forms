<template>
  <v-app id="inspire">
    <v-content>
      <v-container
        class="fill-height"
        fluid
      >
        <v-row
          align="center"
          justify="center"
        >
          <v-col
            cols="12"
            sm="8"
            md="4"
          >
            <ProductDropdown/>
          </v-col>
        </v-row>
      </v-container>
    </v-content>
  </v-app>
</template>

<script>
import ProductDropdown from './components/ProductDropdown';

export default {
  name: 'App',

  components: {
    ProductDropdown,
  },

  data: () => ({
    //
  }),
};
</script>
