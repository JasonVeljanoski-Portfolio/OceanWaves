<template>
  <div class="flexcontainer">
    <BaseStatTile
      :title="`12hr Forecast Confidence Score`"
      :number="84.0"
      :gtThreshold="90"
      :ltThreshold="89"
      description="This confidence comes from being very confident about our results."
      tag="%"
    />
    <BaseStatTile
      :title="`Max Wave Height in 12hr Forecast`"
      :number="100.1"
      :gtThreshold="1"
      :ltThreshold="0.94"
      :flip="true"
      description="This is the max [time] wave height. More stuff goes here..."
      tag="m"
    />
    <BaseStatTile
      :title="`Max Wave Period in 12hr Forecast`"
      :number="100.2"
      :gtThreshold="24"
      :ltThreshold="20"
      :flip="true"
      description="This is the max [time] wave period. More stuff goes here..."
      tag="s"
    />
  </div>
</template>

<script>
import { mapGetters } from 'vuex'
import BaseStatTile from '@/components/SafeHarbourUtils/BaseStatTile'

export default {
  name: 'CoursesPage',
  components: {
    BaseStatTile
  },
  props: {
    stats: {
        type: Object,
        required: true,
        default: 0,
        validator(value) {
            return typeof value === 'object'
        }
    }
  },
  data() {
      return {
          statTimeObj: this.stats.day,
          statConfidenceVal: this.stats.confidence.waveHeight
      }
  },
  mounted() {
      this.renderStats
  },
  computed: {
    renderStats() {
        // TIME VALUE
        if (this.time === 'Last Day')
            this.statTimeObj = this.stats.day
        else if (this.time === 'Last Week')
            this.statTimeObj = this.stats.week
        else if (this.time === 'Last Month')
            this.statTimeObj = this.stats.month    
        
        // CONFIDENCE SCORE
        if (this.graph === 'Wave Height')
            this.statConfidenceVal = this.stats.confidence.waveHeight
        else if (this.graph === 'Peak Period')
            this.statConfidenceVal = this.stats.confidence.peakPeriod
        else if (this.graph === 'Direction')
            this.statConfidenceVal = this.stats.confidence.direction
    }
  },
  watch: {
    time: function () {
      this.renderStats
    },
    graph: function() {
        this.renderStats
    }
  },
}
</script>

<style lang="stylus" scoped>
@import '~static/css/main.styl'

.flexcontainer
   display flex
   align-items center
   justify-content center
   flex-flow row wrap
   align-content flex-end
</style>
