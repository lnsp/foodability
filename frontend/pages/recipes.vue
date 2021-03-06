<template>
  <div class="p-6 flex flex-col justify-between h-full">
    <div class="flex items-between">
      <div class="flex items-center gap-4">
        <div class="brand flex-shrink-0 text-4xl font-black inline-block p-3 bg-green-700 w-16 h-16 text-white">
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
    <div class="my-4 flex-grow h-0 flex relative">
      <div class="h-full flex-grow overflow-y-scroll rounded-xl shadow-xl p-3  border-green-600 bg-white">
        <div class="grid gap-3 grid-rows-auto auto-rows-fr">
          <div v-for="recipe in filtered"
               :key="recipe.title"
               class="cursor-pointer overflow-hidden relative h-24 rounded-xl border-2 flex flex-row justify-between items-center bg-gray-100 transform transition hover:opacity-100"
               :class="isChosen(recipe) ? ['border-green-500', 'bg-green-100', 'shadow-lg'] : ['border-gray-400', 'opacity-75']"
               @click="toggle(recipe)">
            <div class="flex gap-4 items-center h-full">
              <img class="flex-shrink-0 h-full w-16 sm:w-24 object-cover filter z-0"
                   :class="{ 'grayscale': !isChosen(recipe) }"
                   :src="recipe.image"
                   v-if="recipe.image">
              <div class="text-gray-900 mx-2 text-sm">
                {{ recipe.title }}
              </div>
            </div>
            <button class="w-8 h-8 flex flex-shrink-0 justify-center items-center transition rounded-lg  mr-4 hover:bg-green-600 hover:text-white"
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
          </div>
        </div>
      </div>
      <div class="flex flex-col px-2 gap-2 relative w-20 flex-shrink-0  h-full text-green-900">
        <div class="p-2 w-full" v-if="waste.absolute">
          <div class=""><span class="text-lg font-bold">{{ waste.absolute }}</span><span class="text-xs">kg</span></div>
          <div class="text-xs">abs. waste</div>
        </div>
        <div class="mx-2 w-full border-b border-green-700" v-if="waste.relative" />
        <div class="p-2 w-full" v-if="waste.relative">
          <div class=""><span class="text-lg font-bold">{{ waste.relative }}</span><span class="text-xs">%</span></div>
          <div class="text-xs">rel. waste</div>
        </div>
        <div class="mx-2 w-full border-b border-green-700" v-if="waste.plastic" />
        <div class="p-2 w-full" v-if="waste.plastic">
          <div class=""><span class="text-lg font-bold">{{ waste.plastic }}</span><span class="text-xs">cm&sup2;</span></div>
          <div class="text-xs">plastic</div>
        </div>
        <div class="mx-2 w-full border-b border-green-700" v-if="waste.metal" />
        <div class="p-2 w-full" v-if="waste.metal">
          <div class=""><span class="text-lg font-bold">{{ waste.metal }}</span><span class="text-xs">cm&sup2;</span></div>
          <div class="text-xs">metal</div>
        </div>
        <div class="mx-2 w-full border-b border-green-700" v-if="waste.carton" />
        <div class="p-2 w-full" v-if="waste.carton">
          <div class=""><span class="text-lg font-bold">{{ waste.carton }}</span><span class="text-xs">cm&sup2;</span></div>
          <div class="text-xs">carton</div>
        </div>
        <div class="mx-2 w-full border-b border-green-700" v-if="waste.glass" />
        <div class="p-2 w-full" v-if="waste.glass">
          <div class=""><span class="text-lg font-bold">{{ waste.glass }}</span><span class="text-xs">cm&sup2;</span></div>
          <div class="text-xs">glass</div>
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
      return this.$store.state.food.uid;
    },
    chosenTags() {
      return this.$store.state.food.tags;
    },
    chosenDays() {
      return this.$store.state.food.days;
    },
    filtered() {
      return this.recipes.filter((r) => this.excluded.indexOf(r.title) === -1);
    },
  },
  mounted() {
    this.fetch();
    //this.recipes = [
    //  {'title': 'ass', 'image': 'https://bilderspeiseplan.studentenwerk-dresden.de/m9/202012/252587.jpg'},{'title':'condesa'},{'title':'mensa'}
    //]
  },
  data() {
    return {
      recommended: [],
      excluded: [],
      chosen: [],
      recipes: [],
      waste: {
        absolute: '2.5',
        relative: '12',
        plastic: '2.3',
        metal: '4.5',
        carton: '8.9',
        glass: '12',
      }
    };
  },
  methods: {
    exclude(recipe) {
      this.excluded.push(recipe.title);
      const chosenIndex = this.chosen.indexOf(recipe.title);
      if (chosenIndex !== -1) {
        this.chosen.splice(chosenIndex, 1);
      }
      console.log(recipe, this.excluded);
    },
    toggle(recipe) {
      const index = this.chosen.indexOf(recipe.title);
      if (index !== -1) {
        this.chosen.splice(index, 1);
      } else {
        this.chosen.push(recipe.title);
      }
    },
    async fetchWaste() {
      let selected = this.recipes
        .filter((x) => !this.isExcluded(x))
        .map((x) => x.title);
      let response = await this.$axios.$post("/waste", {
        uid: this.uid,
        recipes: selected,
      })

      this.waste.absolute = response.waste.absolute
      this.waste.relative = response.waste.relative
      this.waste.plastic = response.packaging.plastic
      this.waste.metal = response.packaging.metal
      this.waste.carton = response.packaging.carton
      this.waste.glass = response.packaging.glass
    },
    async fetch() {
      const response = await this.$axios.$post("/plan", {
        uid: this.uid,
        tags: this.chosenTags,
        recipes: {
          excluded: this.excluded,
          chosen: this.chosen,
        },
        days: this.chosenDays,
      });
      this.recommended = response.recommended;
      this.recipes = response.recipes;
      this.fetchWaste()
    },
    isExcluded(recipe) {
      return this.excluded.includes(recipe.title);
    },
    isChosen(recipe) {
      return this.chosen.includes(recipe.title);
    },
    next() {
      let selected = this.recipes
        .filter((x) => !this.isExcluded(x))
        .map((x) => x.title);
      this.$store.commit("food/recipes", selected);
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
