export const state = () => ({
  tags: [],
  recipes: [],
  days: 5,
  uid: '',
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
  },
  uid(state, uid) {
    state.uid = uid
  }
}