// vuex data
export const state = () => ({
    oceanData: []
  })
 
// synchronous way to update the state in our vuex store (synchronous setter)
export const mutations = {
    setOceanData(state, payload) {
        state.oceanData = payload
    }
}
  
// get item from state (getter)
export const getters = {
  getOceanData(state) {
    return state.oceanData
  }
}

// asynchronous way to update state (asynchronous setter)
export const actions = {

    async setOceanData(state, payload) {
        const { data } = await this.$axios.$get('/oceanwaves')
        state.commit('setOceanData', data)   // commit is to use the setter in mutations called 'setOceanData'
    }

}