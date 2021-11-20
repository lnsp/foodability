export const state = () => ({
  tags: [],
  recipes: [],
  days: 5,
})

export const mutations = {
  tags(state, tags) {
    state.tags = tags
  },
  recipes(state, recipes) {
    state.recipes = recipes
  },
  days(state, days) {
    state.days = days
  }
}