<template>
  <div class="p-6 flex flex-col justify-between h-full">
    <div class="flex-grow">
      <div class="text-4xl font-black text-center">
        I.
      </div>
      <div class="text-xl mt-4">
        What would you like to eat?
      </div>
      <form @submit.prevent="add()">
        <input type="text" class="px-4 py-2 bg-gray-100 border-2 border-green-600 focus:border-green-900 w-full mt-4 rounded-lg" placeholder="banana" v-model="current">
      </form>
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
      <button class="bg-green-600 hover:bg-green-700 p-4 rounded-full text-white">
        <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M14 5l7 7m0 0l-7 7m7-7H3" />
        </svg>
      </button>
    </div>
  </div>
</template>

<script>
export default {
  data () {
    return {
      tags: ['pancakes', 'apple'],
      current: ''
    }
  },
  methods: {
    drop (tag) {
      const index = this.tags.indexOf(tag)
      this.tags.splice(index, 1)
    },
    add () {
      this.tags.push(this.current)
      this.current = ''
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
