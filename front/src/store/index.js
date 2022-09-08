import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    sampleInfos: []
  },
  getters: {
    getSampleInfo: (state) => (id) => {
      for (let i = 0; i < state.sampleInfos.length; ++ i) {
        if (state.sampleInfos[i].id == id) {
          return state.sampleInfos[i]
        }
      }
      return null
    }
  },
  mutations: {
    setSampleInfos(state, sampleInfos) {
      state.sampleInfos = sampleInfos
    }
  },
  actions: {
  },
  modules: {
  }
})
