<template>
  <div class="p-6 flex flex-col items-between h-full">
    <div class="flex items-center gap-4">
      <div class="brand text-4xl font-black inline-block p-3 bg-green-700 w-16 h-16 text-white">
        IV.
      </div>
      <div class="text-xl">
        Go buy these items.
      </div>
    </div>
    <div class="grid grid-cols-1 gap-4 mt-4">
      <div v-for="item in shoppingList"
           :key="item">
        {{ item }}
      </div>
    </div>
    <div class="w-full my-4 border-b border-green-600" />
    <div class="flex items-center gap-4">
      <div class="brand text-4xl font-black inline-block p-3 bg-green-700 w-16 h-16 text-white">
        V.
      </div>
      <div class="text-xl">
        And start cooking!
      </div>
      <div class="grid grid-cols-1 gap-4 mt-4">
        <div v-for="recipe in recipes"
             :key="recipe">
          <a :href="recipe.url">{{ recipe.title }}</a>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      shoppingList: [],
      recipes: [],
    };
  },
  computed: {
    preference() {
      return this.$store.state.food.recipes;
    },
  },
  mounted() {
    this.fetch();
  },
  methods: {
    async fetch() {
      const response = await this.$axios.$post("/shop", {
        chosen: this.preference.chosen,
        excluded: this.preference.excluded,
      });
      this.shoppingList = response.shoppingList;
      this.recipes = response.recipes;
    },
  },
};
</script>
