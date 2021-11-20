<template>
  <div class="p-6 flex flex-col justify-between h-full">
    <div class="flex items-between">
      <div class="flex items-center gap-4">
        <div class="brand text-4xl font-black inline-block p-3 bg-green-700 w-16 h-16 text-white">
          III.
        </div>
        <div class="text-xl">
          Choose your favorite meals.
        </div>
      </div>
    </div>
    <div class="flex flex-wrap gap-2 mt-4">
        <div v-for="tag in recommended"
             :key="tag"
             class="bg-green-700 text-sm px-2 py-1 text-white rounded flex items-center w-min">
          <span>{{ tag }}</span>
        </div>
    </div>
    <div class="my-4 flex-grow h-0 overflow-y-scroll p-2 border-t border-b border-green-600">
      <div class="grid gap-4 grid-cols-2 sm:grid-cols-3">
        <div v-for="recipe in filtered"
             :key="recipe.title"
             class="cursor-pointer overflow-hidden relative rounded-lg border-2 flex flex-col bg-gray-100 transform transition hover:opacity-100"
             :class="isChosen(recipe) ? ['border-green-500', 'scale-105'] : ['border-gray-400', 'opacity-75']"
             @click="toggle(recipe)">
          <button class="absolute  bg-white z-10 rounded-br-lg t-0 r-0 m-auto w-8 h-8 flex justify-center items-center transition hover:bg-red-600 hover:text-white"
                  @click="exclude(recipe)">
            <svg xmlns="http://www.w3.org/2000/svg"
                 class="h-5 w-5"
                 fill="none"
                 viewBox="0 0 24 24"
                 stroke="currentColor">
              <path stroke-linecap="round"
                    stroke-linejoin="round"
                    stroke-width="2"
                    d="M6 18L18 6M6 6l12 12" />
            </svg>
          </button>

          <img class="h-24 object-cover filter z-0"
               :class="{ 'grayscale': !isChosen(recipe) }"
               :src="recipe.image">
          <div class="text-gray-900 p-2 z-10 text-center">
            {{ recipe.title }}
          </div>
        </div>
      </div>
    </div>
    <div class="flex justify-center gap-4">
      <button class="bg-gray-400 hover:bg-gray-500 p-4 rounded-full text-white group"
              @click="fetch">
        <svg xmlns="http://www.w3.org/2000/svg"
             class="h-6 w-6 group-hover:animation-spin"
             fill="none"
             viewBox="0 0 24 24"
             stroke="currentColor">
          <path stroke-linecap="round"
                stroke-linejoin="round"
                stroke-width="2"
                d="M4 4v5h.582m15.356 2A8.001 8.001 0 004.582 9m0 0H9m11 11v-5h-.581m0 0a8.003 8.003 0 01-15.357-2m15.357 2H15" />
        </svg>
      </button>
      <button class="bg-green-600 hover:bg-green-700 p-4 rounded-full text-white justify-self-end"
              @click="next">
        <svg xmlns="http://www.w3.org/2000/svg"
             class="h-6 w-6"
             fill="none"
             viewBox="0 0 24 24"
             stroke="currentColor">
          <path stroke-linecap="round"
                stroke-linejoin="round"
                stroke-width="2"
                d="M14 5l7 7m0 0l-7 7m7-7H3" />
        </svg>
      </button>
    </div>
  </div>
</template>

<script>
export default {
  transition: "fade",
  computed: {
    uid() {
      return this.$store.state.food.uid
    },
    chosenTags() {
      return this.$store.state.food.tags
    },
    chosenDays() {
      return this.$store.state.food.days
    },
    filtered () {
      return this.recipes.filter(r => this.excluded.indexOf(r.title) === -1)
    }
  },
  mounted() {
    this.fetch();
  },
  data() {
    return {
      recommended: [],
      excluded: [],
      chosen: [],
      recipes: [],
    };
  },
  methods: {
    exclude(recipe) {
      this.excluded.push(recipe.title);
      const chosenIndex = this.chosen.indexOf(recipe.title);
      if (chosenIndex !== -1) {
        this.chosen.splice(chosenIndex, 1);
      }
      console.log(recipe, this.excluded)
    },
    toggle(recipe) {
      const index = this.chosen.indexOf(recipe.title);
      if (index !== -1) {
        this.chosen.splice(index, 1);
      } else {
        this.chosen.push(recipe.title);
      }
    },
    async fetch() {
      const response = await this.$axios.$post("/plan", {
        uid: this.uid,
        tags: this.chosenTags,
        recipes: {
          excluded: this.excluded,
          chosen: this.chosen,
        },
        days: this.chosenDays
      });
      this.recommended = response.recommended
      this.recipes = response.recipes
    },
    isExcluded (recipe) {
      return this.excluded.includes(recipe.title)
    },
    isChosen (recipe) {
      return this.chosen.includes(recipe.title)
    },
    next() {
      // TODO: Send recipes to backend
      this.$store.commit("food/recipes", {
        excluded: this.excluded,
        chosen: this.chosen,
      });
      this.$router.push("/shopping-list");
    },
  },
};
</script>

<style>
.fade-enter-active,
.fade-leave-active {
  transition: opacity 0.25s;
}
.fade-enter, .fade-leave-to /* .fade-leave-active below version 2.1.8 */ {
  opacity: 0;
}
</style>
