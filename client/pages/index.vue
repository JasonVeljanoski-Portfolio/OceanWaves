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
    <TheStatsRack :confidence="confidence" :height="height" :period="period" :time="time" :graph="activeGraphItem" />
    <!-- <TheForecastStatRack v-show="showForecast" :stats="stats" /> -->

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
          activeTime: 'Forecast',
          graphitmes: ['Wave Height', 'Peak Period', 'Direction'],
          scaleitems: ['Forecast', 'Last Day', 'Last Week', 'Last Month'],
          upperbound: 50,
          componentKey: 0,
          time: 'Forecast',
          confidence: 0,
          height: 1,
          period: 2
      }
  },
  async asyncData({ $axios }) {
    const { data } = await $axios.$get('/oceanwaves')
    return { data: data.data, stats: data.summary, forecast: data.forecast }
  },
  mounted() {
    this.confidence = this.stats.forecast.confidence.waveHeight
    this.height = this.stats.forecast.height
    this.period = this.stats.forecast.period
  },
  methods: {
      forceRerender() {
        this.componentKey += 1
      },
      graphToggleHandler(event) {
          this.activeGraphItem = event
          this.reScale(this.activeTime)
      },
      reScale(event) {
        this.activeTime = event
        // FORECAST
        if ( event === 'Forecast' ) {

          // check which models confidence to display ('Wave Height', 'Peak Period', 'Direction' models)
          if ( this.activeGraphItem === 'Wave Height' ) {
            this.confidence = this.stats.forecast.confidence.waveHeight
            console.log(this.stats.forecast.confidence.waveHeight)
          }
          else if ( this.activeGraphItem === 'Peak Period' ) {
            this.confidence = this.stats.forecast.confidence.peakPeriod
            console.log(this.stats.forecast.confidence.peakPeriod)
          }
          else if ( this.activeGraphItem === 'Direction' ) {
            this.confidence = this.stats.forecast.confidence.direction
            console.log(this.stats.forecast.confidence.direction)
          }
          
          this.height = this.stats.forecast.height
          this.period = this.stats.forecast.period

        }
        else if ( event === 'Last Day' ) {  // LAST DAY


          // check which models confidence to display ('Wave Height', 'Peak Period', 'Direction' models)
          if ( this.activeGraphItem == 'Wave Height' ) {
            this.confidence = this.stats.waveHeight.confidence
            console.log(this.stats.waveHeight.confidence)
          }
          else if ( this.activeGraphItem == 'Peak Period' ) {
            this.confidence = this.stats.peakPeriod.confidence
            console.log(this.stats.peakPeriod.confidence)
          }
          else if ( this.activeGraphItem == 'Direction' ) {
            this.confidence = this.stats.direction.confidence
            console.log(this.stats.direction.confidence)
          }

          this.height = this.stats.waveHeight.day
          this. period = this.stats.peakPeriod.day

        }
        else if ( event === 'Last Week' ) {

          // check which models confidence to display ('Wave Height', 'Peak Period', 'Direction' models)
          if ( this.activeGraphItem == 'Wave Height' ) {
            this.confidence = this.stats.waveHeight.confidence
            console.log(this.stats.waveHeight.confidence)
          }
          else if ( this.activeGraphItem == 'Peak Period' ) {
            this.confidence = this.stats.peakPeriod.confidence
            console.log(this.stats.peakPeriod.confidence)
          }
          else if ( this.activeGraphItem == 'Direction' ) {
            this.confidence = this.stats.direction.confidence
            console.log(this.stats.direction.confidence)
          }
          
          this.height = this.stats.waveHeight.week
          this. period = this.stats.peakPeriod.week

        }
        else if ( event === 'Last Month' ) {

          // check which models confidence to display ('Wave Height', 'Peak Period', 'Direction' models)
          if ( this.activeGraphItem == 'Wave Height' ) {
            this.confidence = this.stats.waveHeight.confidence
            console.log(this.stats.waveHeight.confidence)
          }
          else if ( this.activeGraphItem == 'Peak Period' ) {
            this.confidence = this.stats.peakPeriod.confidence
            console.log(this.stats.peakPeriod.confidence)
          }
          else if ( this.activeGraphItem == 'Direction' ) {
            this.confidence = this.stats.direction.confidence
            console.log(this.stats.direction.confidence)
          }

          this.height = this.stats.waveHeight.month
          this. period = this.stats.peakPeriod.month

        }


        // if (event === this.scaleitems[0]) {
        //     this.showForecast = true
        //     return
        // }
        // else if (event === this.scaleitems[1]) {
        //     this.upperbound = 50  // rescale graph
        //     this.showForecast = false // reset
        // }
        // else if (event === this.scaleitems[2]) {
        //     this.upperbound = 350
        //     this.showForecast = false // reset
        // }
        // else if (event === this.scaleitems[3]) {
        //     this.upperbound = 1400
        //     this.showForecast = false // reset
        // }

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
