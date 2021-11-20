<template>
  <div class="h-screen flex flex-col w-full items-center p-8 overflow-hidden pretty-bg">
    <header class="z-10 w-full">
      <h1 class="text-4xl font-bold text-center pt-6 pb-4 text-white brand">
        Foodability
      </h1>
    </header>
    <main class="border-2 border-green-600 rounded-lg w-full max-w-lg flex-grow mt-8 bg-white z-10 overflow-hidden relative">
      <Nuxt />
    </main>
  </div>
</template>

<style>
.pretty-bg {
  background: linear-gradient(to bottom, rgba(79, 80, 87, 0.52), rgba(4,120,87, 1.0) 50%), url('~/assets/bg.webp');
  background-size: cover;
  background-position: bottom;
  background-repeat: no-repeat;
}
.brand {
  font-family: Poppins, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Open Sans', 'Helvetica Neue', sans-serif;
}
</style>
