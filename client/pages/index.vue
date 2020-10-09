<template>
  <div>
    <BaseContainer @itemtoggle="graphToggleHandler($event)" :rackitems="graphitmes" :description="activeGraphItem" logo-file-name="safeharbourMini.svg" width="100%">
    <div>

      <div class="flexbox queue">

        <h3>Forecast Reports</h3>
        <div class="spacer" />
        <BaseToggleRack @toggle="reScale($event)" :items="scaleitems" />

      </div>


      <div :key="componentKey">

        <div v-if="showForecast">
          <TheForecastWaveHeight :data="forecast" v-show="activeGraphItem === graphitmes[0]" />
          <TheForecastPeakPeriod :data="forecast" v-show="activeGraphItem === graphitmes[1]" />
          <TheForecastDirection :data="forecast" v-show="activeGraphItem === graphitmes[2]" />
        </div>
        <div v-else>
          <TheOceanWaveHeight v-show="activeGraphItem === graphitmes[0]" :data="data.slice(0, upperbound)" />
          <TheOceanPeakPeriod v-show="activeGraphItem === graphitmes[1]" :data="data.slice(0, upperbound)" />
          <TheOceanRadar v-show="activeGraphItem === graphitmes[2]" :data="data.slice(0,upperbound)"/>
        </div>
  
      </div>

    </div>
    </BaseContainer>
    <TheStatsRack v-if="!showForecast" :stats="stats" :time="time" :graph="activeGraphItem" />
    <TheForecastStatRack v-else :stats="stats" :time="time" :graph="activeGraphItem" />


  </div>
</template>

<script>
// import { mapGetters, mapActions } from 'vuex'
import BaseContainer from '@/components/Utils/BaseContainer'
import BaseToggleRack from '@/components/Utils/BaseToggleRack'
import TheForecastWaveHeight from '@/components/D3Visualisations/TheForecastWaveHeight'
import TheForecastPeakPeriod from '@/components/D3Visualisations/TheForecastPeakPeriod'
import TheForecastDirection from '@/components/D3Visualisations/TheForecastDirection'
import TheOceanWaveHeight from '@/components/D3Visualisations/TheOceanWaveHeight'
import TheOceanPeakPeriod from '@/components/D3Visualisations/TheOceanPeakPeriod'
import TheOceanRadar from '@/components/D3Visualisations/TheOceanRadar'
import TheStatsRack from '@/components/SafeHarbourUtils/TheStatsRack'
import TheForecastStatRack from '@/components/SafeHarbourUtils/TheForecastStatRack'

export default {
  name: 'D3Demos',
  components: {
    BaseContainer,
    BaseToggleRack,
    TheForecastWaveHeight,
    TheForecastPeakPeriod,
    TheForecastDirection,
    TheOceanWaveHeight,
    TheOceanPeakPeriod,
    TheOceanRadar,
    TheStatsRack,
    TheForecastStatRack
  },
  data() {
      return {
          showForecast: true,
          activeGraphItem: 'Wave Height',
          graphitmes: ['Wave Height', 'Peak Period', 'Direction'],
          scaleitems: ['12hr Forecast', 'Last Day', 'Last Week', 'Last Month'],
          upperbound: 50,
          componentKey: 0,
          time: 'Last Day',
      }
  },
  async asyncData({ $axios }) {
    const { data } = await $axios.$get('/oceanwaves')
    return { data: data.data, stats: data.summary, forecast: data.forecast }
  },
  methods: {
      forceRerender() {
        this.componentKey += 1
      },
      graphToggleHandler(event) {
          this.activeGraphItem = event
      },
      reScale(event) {

        // deal with forecast button separetly
        if (event === this.scaleitems[0]) {
            this.showForecast = true
            return 
        }
        
        // deal with normal day, week, month time scales
        this.showForecast = false // reset

        if (event === this.scaleitems[1]) {
            this.upperbound = 50  // rescale graph
        }
        else if (event === this.scaleitems[2]) {
            this.upperbound = 350
        }
        else if (event === this.scaleitems[3]) {
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
