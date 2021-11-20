<template>
  <div class="p-6 flex flex-col justify-between h-full">
    <div class="flex-grow">
      <div class="flex items-center">
      <div class="brand text-4xl font-black inline-block p-3 bg-green-700 w-16 h-16 text-white">
        I.
      </div>
      <div class="text-xl ml-4 items-center">
        I would like to eat for
        <input type="number" v-model="numberOfDays" class="mx-3 border-2 bg-gray-100 rounded-lg border-green-600 px-4 py-2 text-lg w-16 text-center">
        days.
      </div>
      </div>
      <div class="w-full my-4 border-b border-green-600" />
      <div class="flex items-center gap-4">
      <div class="brand text-4xl font-black inline-block p-3 bg-green-700 w-16 h-16 text-white">
        II.
      </div>
      <div class="text-xl">
        I especially like
      </div>
      <form @submit.prevent="add()">
        <input type="text" class="px-4 py-2 bg-gray-100 border-2 border-green-600 focus:border-green-900 w-full rounded-lg" placeholder="banana" v-model="current">
        <div class="text-xs text-red-500 mt-2" v-if="error(current)">
          {{ error(current) }}
        </div>
      </form>
      </div>
      <transition-group name="fade" tag="div" class="flex flex-wrap mt-4 gap-2">
        <div v-for="tag in tags" :key="tag" class="bg-green-700 hover:bg-green-800 text-sm px-2 py-1 text-white rounded flex items-center w-min">
          <span>{{ tag }}</span>
          <button class="p-1 cursor-pointer" @click.prevent="drop(tag)">
            <svg xmlns="http://www.w3.org/2000/svg" class="ml-3 h-4 w-4" fill="none" viewBox="0 0 24 24" stroke="currentColor">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12" />
            </svg>
          </button>
        </div>
      </transition-group>
    </div>
    <div class="flex justify-center mb-4">
      <button class="bg-green-600 hover:bg-green-700 p-4 rounded-full text-white" @click="next">
        <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M14 5l7 7m0 0l-7 7m7-7H3" />
        </svg>
      </button>
    </div>
  </div>
</template>

<script>
export default {
  transition: 'fade',
  data () {
    return {
      available: [],
      tags: ['pancakes', 'apple'],
      current: '',
      numberOfDays: 5
    }
  },
  mounted() {
    // fetch tags from api
    this.fetchTags()
  },
  methods: {
    async fetchTags () {
      let response = await this.$axios.$get('/all-tags')
      this.tags = response.tags
    },
    drop (tag) {
      const index = this.tags.indexOf(tag)
      this.tags.splice(index, 1)
    },
    add () {
      this.tags.push(this.current)
      this.current = ''
    },
    error (tag) {
      if (this.tags.includes(tag)) {
        return 'Tag already exists.'
      }
    },
    next () {
      // TODO: Trigger /fetch-recipes call in backend
      this.$router.push('/recipes')
    }
  }
}
</script>

<style scoped>
.fade-enter-active, .fade-leave-active {
  transition: opacity .25s;
}
.fade-enter, .fade-leave-to /* .fade-leave-active below version 2.1.8 */ {
  opacity: 0;
}
</style>
