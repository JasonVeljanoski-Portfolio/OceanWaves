<template>
  <div>
    <BaseContainer @itemtoggle="graphToggleHandler($event)" :rackitems="graphitmes" :description="activeGraphItem" logo-file-name="safeharbourMini.svg" width="100%">
    <div>

      <div class="flexbox queue">

        <h3>History Reports</h3>
        <div class="spacer" />
        <BaseToggleRack @toggle="reScale($event)" :items="scaleitems" />

      </div>

      <div :key="componentKey">
        <TheHistoryWaveHeight v-show="activeGraphItem === graphitmes[0]" :data="history.slice(0, upperbound)" />
        <TheHistoryPeakPeriod v-show="activeGraphItem === graphitmes[1]" :data="history.slice(0, upperbound)" />
        <TheHistoryDirection v-show="activeGraphItem === graphitmes[2]" :data="history.slice(0,upperbound)"/>
      </div>

    </div>
    </BaseContainer>
    <TheHistoryStatRack :stats="stats" :time="time" :graph="activeGraphItem" />


  </div>
</template>

<script>
// import { mapGetters, mapActions } from 'vuex'
import BaseContainer from '@/components/Utils/BaseContainer'
import BaseToggleRack from '@/components/Utils/BaseToggleRack'
import TheHistoryWaveHeight from '@/components/D3Visualisations/TheHistoryWaveHeight'
import TheHistoryPeakPeriod from '@/components/D3Visualisations/TheHistoryPeakPeriod'
import TheHistoryDirection from '@/components/D3Visualisations/TheHistoryDirection'
import TheOceanPeakPeriod from '@/components/D3Visualisations/TheOceanPeakPeriod'
import TheOceanRadar from '@/components/D3Visualisations/TheOceanRadar'
import TheHistoryStatRack from '@/components/SafeHarbourUtils/TheHistoryStatRack'

export default {
  name: 'D3Demos',
  components: {
    BaseContainer,
    BaseToggleRack,
    TheHistoryWaveHeight,
    TheHistoryPeakPeriod,
    TheHistoryDirection,
    TheOceanPeakPeriod,
    TheOceanRadar,
    TheHistoryStatRack
  },
  data() {
      return {
          activeGraphItem: 'Wave Height',
          graphitmes: ['Wave Height', 'Peak Period', 'Direction'],
          scaleitems: ['Last Day', 'Last Week', 'Last Month'],
          upperbound: 50,
          componentKey: 0,
          time: 'Last Day'
      }
  },
  async asyncData({ $axios }) {
    const { data } = await $axios.$get('/historywaves')
    return { history: data.history, stats: data.summary_history }
  },
  methods: {
      forceRerender() {
        this.componentKey += 1
      },
      graphToggleHandler(event) {
          this.activeGraphItem = event
      },
      reScale(event) {
        if (event === this.scaleitems[0]) {
            this.upperbound = 50  // rescale graph
        }
        else if (event === this.scaleitems[1]) {
            this.upperbound = 350
        }
        else if (event === this.scaleitems[2]) {
            this.upperbound = 1400
        }
        this.time = event     // update time for summary stats
        this.forceRerender()
      }
  }
//   methods: {
//     ...mapActions({
//       setDemoData: 'd3Demo/setDemoData', // map `this.setDemoData()` to `this.$store.dispatch('setDemoData')`
//       setOceanData: 'oceandata/setOceanData'
//     })
//   },
//   computed: {
//     ...mapGetters({
//       demoData: 'd3Demo/getDemoData',
//       oceanData: 'oceandata/getOceanData'
//     }),
//   },
}
</script>

<style lang="stylus" scoped>
@import '~static/css/main.styl'

h3
  margin 0

.spacer
  flex 1 1 auto

.queue
  padding 5px

.flexcontainer
   display flex
   align-items center
   justify-content center
   flex-flow row wrap
   align-content flex-end
</style>
