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
      <div v-for="item in items"
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
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      items: [
        "500g flour",
        "25g backing powder",
        "100g salt",
        "250g sugar",
        "1 liter milk",
        "6 eggs",
        "100g butter",
      ],
    };
  },
};
</script>
