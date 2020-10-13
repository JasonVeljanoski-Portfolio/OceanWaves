// vuex data
export const state = () => ({
    oceanData: [],
    historyData: []
  })
 
// synchronous way to update the state in our vuex store (synchronous setter)
export const mutations = {
    SET_OCEANDATA(state, payload) {
        state.oceanData = payload
    },
    SET_HISTORYDATA(state, payload) {
      state.historyData = payload
    }
}
  
// get item from state (getter)
export const getters = {
  getOceanData(state) {
    return state.oceanData
  },
  getHistoryData(state) {
    return state.historyData
  }
}

// asynchronous way to update state (asynchronous setter)
export const actions = {

    async loadItems ( { commit } ) {
      const { data } = await this.$axios.$get('/oceanwaves')
      commit( 'SET_OCEANDATA', data )
    },

    async loadHistoryItems ( { commit } ) {
      const { data } = await this.$axios.$get('/historywaves')
      commit( 'SET_HISTORYDATA', data )
    }

}