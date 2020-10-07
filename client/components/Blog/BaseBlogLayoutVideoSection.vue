<template>
  <div>
    <div class="title">Current Course - {{ currentLesson.name }}</div>
    <div class="course-wrapper">
      <nav class="smallitem video-nav">
        <ul>
          <li
            @click="
              updateCurrent(topic.name)
              setActive(index)
            "
            :class="{ active: isActive(index) }"
            v-for="(topic, index) in topics"
            :key="index"
          >
            <span class="vid-count">{{ index + 1 }}.</span>
            <div class="vid-content">
              <div class="vid-name">{{ topic.name }}</div>
              <div class="vid-runtime">Run Time: 10:09</div>
            </div>
          </li>
        </ul>
      </nav>
      <div class="bigitem">
        <div class="video-wrapper">
          <!-- <video width="560" height="315" controls controlsList="nodownload">
            <source
              v-if="currentLesson.videoLink"
              :src="currentLesson.videoLink"
              type="video/mp4"
            />
            Your browser does not support the video tag.
          </video> -->
          <iframe
            v-if="currentLesson.videoLink"
            :src="currentLesson.videoLink"
            width="560"
            height="315"
            frameborder="0"
            allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture"
            allowfullscreen
          />
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { mapGetters } from 'vuex'

export default {
  name: 'BaseBlogLayoutVideoSection',
  props: {
    topics: {
      type: Array,
      required: true,
      validator(value) {
        return typeof value === 'object'
      }
    }
  },
  data() {
    return {
      activeItem: 0
    }
  },
  computed: {
    ...mapGetters({
      // topics: 'courses/methods_unit_1/cosine_and_sine_rules/getTopics',
      currentLesson: 'courses/current_state/getCurrentTopic'
    })
  },
  // initialiseState on mounted so `currentLesson.videoLink` can have init state
  // note `currentLesson.videoLink` should be resolved befor html is rendered (i.e. on create) but this causes errors so v-if tag is placed in <video>
  // to block errors in the created stage
  // `currentLesson.videoLink` if not undefined should affect <video> thus, v-if exist in this tag
  mounted() {
    this.initialiseState()
  },
  methods: {
    updateCurrent(selectedTopic) {
      for (const topic of this.topics) {
        if (selectedTopic === topic.name) {
          this.$store.commit('courses/current_state/UPDATE_TOPIC', topic)
          break
        }
      }
    },
    /* Default to first topic as the current lesson */
    initialiseState() {
      this.$store.commit('courses/current_state/UPDATE_TOPIC', this.topics[0])
    },
    // show which menu item is active to apply style
    isActive(menuItem) {
      return this.activeItem === menuItem
    },
    // show which menu item is active to apply style
    setActive(menuItem) {
      this.activeItem = menuItem
    }
  }
}
</script>

<style lang="stylus" scoped>
@import '~static/css/main.styl'

+mobile()
  .video-nav
    order 1
  .course-wrapper
    flex-direction column

.video-nav
  background-color white
  overflow scroll
  border-bottom solid 1px $light-grey
  ul
    padding 0
  li
    border-bottom solid 1px $light-grey
    display flex
    align-items center
    list-style none
    cursor pointer
    width 100%
    height 80px
    background-color white
    .vid-count
      padding 10px
      font-size 32pt
    .vid-content
      padding 10px
      font-size 12pt
    .vid-name
      font-size 14pt
      font-weight bold
    .vid-runtime
      font-size 12pt

.video-nav li:hover
  background-color #efefef

.active
  background-color #efefef !important


.title
  display flex
  align-items center
  padding-left 30px
  width 100%
  height $header-height
  background-color $blue
  font-size 22pt
  font-style italic
  font-weight bold

.course-wrapper
  display flex

.video-wrapper
  display flex
  position relative
  width 100%
  padding-bottom 56.25%
  height 0
  iframe
    position absolute
    top 0
    left 0
    width 100%
    height 100%

.bigitem
  /* This will be 3x */
  /* big as the small item. */
  flex 3 0 0

.smallitem
  flex 1 0 0
</style>
