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
        v-model="model"
        :items="items"
        :loading="isLoading"
        color="white"
        hide-no-data
        hide-selected
        item-text="Description"
        item-value="API"
        label="Drinks"
        placeholder="Start typing to Search"
        prepend-icon="mdi-database-search"
        return-object
      ></v-autocomplete>
    </v-card-text>
    <v-divider></v-divider>
    <v-expand-transition>
      <v-list v-if="model">
        <v-list-item
          v-for="(field, i) in fields"
          :key="i"
        >
          <v-list-item-content>
            <v-list-item-title v-text="field.value"></v-list-item-title>
            <v-list-item-subtitle v-text="field.key"></v-list-item-subtitle>
          </v-list-item-content>
        </v-list-item>
      </v-list>
    </v-expand-transition>
    <v-card-actions>
      <v-spacer></v-spacer>
      <v-btn
        :disabled="!model"
        color="grey darken-3"
        @click="model = null"
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
      entries: [],
      isLoading: false,
      model: null,
    }),

    computed: {
      fields () {
        if (!this.model) return []

        return Object.keys(this.model).map(key => {
          return {
            key,
            value: this.model[key] || 'n/a',
          }
        })
      },
      items () {
        return this.entries.map(entry => {
          const Description = entry.name.length > this.descriptionLimit
            ? entry.name.slice(0, this.descriptionLimit) + '...'
            : entry.name

          return Object.assign({}, entry, { Description })
        })
      },
    },
    created() {
      axios.get('api/products/')
           .then(response => {
             this.entries = response.data
           })
           .catch(err => {
             console.log(err)
           })
           .finally(() => (this.isLoading = false))
    }
  }
</script>
