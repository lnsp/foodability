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
    <div class="h-0 overflow-y-scroll flex-grow mt-4 border-t border-b border-gray-200 bg-white">
    <table class="table-auto w-full">
      <tr v-for="item in shoppingList"
           :key="item" class="hover:bg-gray-100 border border-gray-200">
        <td class="py-1 pl-1 text-right">{{ item.weight }}</td><td class="pr-2">{{ item.unit }}</td><td class="py-1 px-1 ">{{ item.name }}</td><td v-if="item.usedby" class="text-right"><span class="text-xs mr-2 px-2 py-1 rounded text-white bg-green-600 p-1 text-right">{{ item.usedby }}</span></td>
      </tr>
    </table>
    </div>
    <div class="flex items-center gap-4 mt-4">
      <div class="brand text-4xl font-black inline-block p-3 bg-green-700 w-16 h-16 text-white">
        V.
      </div>
      <div class="text-xl">
        And start cooking!
      </div>
    </div>
    <div class="flex-grow h-0 overflow-y-auto border border-gray-200 p-2 mt-4 bg-white">
      <ol class="grid grid-cols-1 gap-4 mt-4">
        <li v-for="(recipe, index) in recipes"
             :key="recipe" class="flex ">
          <span class="flex-shrink-0 text-right block w-6 text-lg mr-2">{{ index }}.</span>
          <a :href="recipe.url" target="_blank" rel="noreferrer noopener" class="flex items-center hover:underline hover:text-green-700"><span>{{ recipe.title }}</span></a>
        </li>
      </ol>
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
      return this.$store.state.food.recipes
    },
    uid() {
      return this.$store.state.food.uid
    }
  },
  mounted() {
    this.fetch();
  },
  methods: {
    async fetch() {
      const response = await this.$axios.$post("/shop", {
        recipes: this.preference,
        uid: this.uid,
      })
      this.shoppingList = response.shoppingList
      this.recipes = response.recipes
    },
  },
};
</script>
