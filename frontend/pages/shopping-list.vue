<template>
  <div class="p-6 flex flex-col items-between h-full">
    <div class="">
      <div class="text-4xl font-black text-center">
        III.
      </div>
      <div class="text-xl mt-4 text-center">
        Go shop these.
      </div>
    </div>
      <div class="grid grid-cols-1 gap-4 mt-4">
        <div v-for="item in items" :key="item">
          {{ item }}
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  data () {
    return {
      items: [
        '500g flour',
        '25g backing powder',
        '100g salt',
        '250g sugar',
        '1 liter milk',
        '6 eggs',
        '100g butter'
      ]
    }
  }
}
</script>
