<template>
  <div class="h-full flex flex-col w-full items-center p-8 overflow-hidden pretty-bg">
    <header class="z-10 w-full">
      <h1 class="text-3xl sm:text-4xl font-medium flex justify-center items-center pt-2 pb-1 sm:pt-6 sm:pb-4 text-white brand">
        <svg aria-hidden="true"
             focusable="false"
             data-prefix="fas"
             data-icon="leaf"
             class="h-10 w-10 mr-4"
             role="img"
             xmlns="http://www.w3.org/2000/svg"
             viewBox="0 0 576 512">
          <path fill="currentColor"
                d="M546.2 9.7c-5.6-12.5-21.6-13-28.3-1.2C486.9 62.4 431.4 96 368 96h-80C182 96 96 182 96 288c0 7 .8 13.7 1.5 20.5C161.3 262.8 253.4 224 384 224c8.8 0 16 7.2 16 16s-7.2 16-16 16C132.6 256 26 410.1 2.4 468c-6.6 16.3 1.2 34.9 17.5 41.6 16.4 6.8 35-1.1 41.8-17.3 1.5-3.6 20.9-47.9 71.9-90.6 32.4 43.9 94 85.8 174.9 77.2C465.5 467.5 576 326.7 576 154.3c0-50.2-10.8-102.2-29.8-144.6z"></path>
        </svg>
        Foodability
      </h1>
    </header>
    <main class="rounded-lg w-full max-w-lg flex-grow mt-8 bg-white z-10 overflow-hidden relative">
      <Nuxt />
    </main>
  </div>
</template>

<style>
#__nuxt, #__layout {
  height: 100%;
}
html, body {
  height: 100%;
}
.pretty-bg {
  background: linear-gradient(
      to bottom,
      rgba(79, 80, 87, 0.52),
      rgba(4, 120, 87, 1) 75%
    ),
    url("~/assets/bg.webp");
  background-size: cover;
  background-position: bottom;
  background-repeat: no-repeat;
}
.brand {
  font-family: Poppins, -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto,
    Oxygen, Ubuntu, Cantarell, "Open Sans", "Helvetica Neue", sans-serif;
}
</style>
