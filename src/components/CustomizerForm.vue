<template>
  <v-card class="elevation-12">
    <v-toolbar
      color="primary"
      dark
      flat
    >
      <v-toolbar-title>Drink Lab</v-toolbar-title>
    </v-toolbar>
    <v-card-text>
      Choose a drink, add your modifications, and share with your friends.
    </v-card-text>
    <v-card-text>
      <v-autocomplete
        v-model="baseProduct"
        :items="baseProducts"
        :loading="isLoading"
        color="white"
        hide-no-data
        hide-selected
        item-text="name"
        item-value="id"
        label="Drinks"
        placeholder="Start typing to Search"
        prepend-icon="mdi-database-search"
        return-object
      ></v-autocomplete>
    </v-card-text>
    <v-divider></v-divider>
    <v-expand-transition>
      <div class="pa-2" v-if="baseProduct">
        <v-radio-group
          v-model="customizedProduct.size"
          v-if="baseProduct.allowed_sizes.length"
          label="Size:">
          <v-radio
            v-for="allowedSize in baseProduct.allowed_sizes"
            :key="allowedSize"
            :label="allowedSize.name"
            :value="allowedSize.id"
          ></v-radio>
        </v-radio-group>

        <v-radio-group
          v-model="customizedProduct.ice"
          v-if="baseProduct.allowed_ice.length"
          label="Ice:">
          <v-radio
            v-for="allowedIce in baseProduct.allowed_ice"
            :key="allowedIce"
            :label="allowedIce.name"
            :value="allowedIce.id"
          ></v-radio>
        </v-radio-group>

        <v-radio-group
          v-model="customizedProduct.room"
          v-if="baseProduct.allowed_room.length"
          label="Room:">
          <v-radio
            v-for="allowedRoom in baseProduct.allowed_room"
            :key="allowedRoom"
            :label="allowedRoom.name"
            :value="allowedRoom.id"
          ></v-radio>
        </v-radio-group>
      </div>
    </v-expand-transition>
    <v-card-actions>
      <v-spacer></v-spacer>
      <v-btn
        :disabled="!baseProduct"
        @click="shareCustomizedProduct()"
        color="primary"
      >
        Share
        <v-icon right>mdi-share</v-icon>
      </v-btn>
      <v-btn
        :disabled="!baseProduct"
        @click="baseProduct = null"
      >
        Clear
        <v-icon right>mdi-close-circle</v-icon>
      </v-btn>
    </v-card-actions>
  </v-card>
</template>

<script>
  import axios from 'axios';

  export default {
    data: () => ({
      descriptionLimit: 60,
      baseProducts: [],
      isLoading: false,
      baseProduct: null,
      customizedProduct: {
        size: null,
        room: null,
        ice: null,
        milk: null,
        sweeteners: [],
        espresso_shots: [],
        toppings: [],
        flavors: [],
        juices: [],
        teas: [],
      },
    }),
    methods: {
      shareCustomizedProduct: function () {
        // TODO: POST customized product to endpoint
        alert('Hello ' + this.customizedProduct.size + '!')
      }
    },
    computed: {},
    created() {
      axios.get('api/products/')
           .then(response => {
             this.baseProducts = response.data
           })
           .catch(err => {
             console.log(err)
           })
           .finally(() => (this.isLoading = false))
    }
  }
</script>
