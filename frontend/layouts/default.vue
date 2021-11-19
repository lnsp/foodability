<template>
  <div class="h-screen bg-gray-100 flex flex-col p-8 overflow-hidden">
    <header class="z-10">
      <h1 class="text-4xl font-bold text-center pt-6 pb-4 text-white">
        Foodability
      </h1>
    </header>
    <main class="border-2 border-green-600 rounded-lg flex-grow mt-8 bg-white z-10">
      <Nuxt />
    </main>
    <div class="absolute -ml-8 mt-64 b-0 bg-green-600 w-full h-full z-0" />
    <div class="pretty-bg absolute -ml-8 -mt-8 h-72 z-0 w-full" />
  </div>
</template>

<style>
.pretty-bg {
  background: linear-gradient(to bottom, rgba(79, 80, 87, 0.52), rgba(5, 150, 105, 1.0)), url('~/assets/bg.jpg');
  background-size: cover;
  background-position: bottom;
  background-repeat: no-repeat;
}
</style>
