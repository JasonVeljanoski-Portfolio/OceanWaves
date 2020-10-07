<template>
  <!-- prettier-ignore -->
  <div class="flex">
      <div id="content" class="bigitem page-content">
        <transition name="fade">
          <slot />
        </transition>
      </div>
      <nav class="smallitem page-nav">
        <ul>
          <li class="list-title">{{ currentLesson.name }}</li>
          <li
            v-for="(header, index) in currentLesson.headings"
            :key="index"
            @click="selectItem(index)"
            :class="{ active: index === activeItem }"
          >
            <a :href="`#${createForgivingID(header)}`" class="list-item">
              {{ header }}
            </a>
          </li>
        </ul>
      </nav>
      <aside class="smallitem page-ads">
        adverts here
      </aside>
    </div>
</template>

<script>
import { mapGetters } from 'vuex'
import 'katex/dist/katex.min.css' // katex css

export default {
  name: 'BaseBlogLayoutContent',
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
      activeItem: null // keep track of active item in v-for
    }
  },
  computed: {
    ...mapGetters({
      currentLesson: 'courses/current_state/getCurrentTopic'
    })
  },
  created() {
    this.getSluggiest()
  },
  mounted() {
    window.addEventListener('scroll', this.findActiveNavCallback)
  },
  updated() {
    this.setHeaders()
  },
  destroyed() {
    window.removeEventListener('scroll', this.findActiveNavCallback)
  },
  methods: {
    /* get the sluggiest slug i.e. A/B/C --> C */
    getSluggiest() {
      let route = this.$route.path.split('/')
      route = route[route.length - 1]
      for (const key in this.courses) {
        const _obj = this.courses[key]
        // when objs slug matches this route
        if (_obj.slug === route) {
          this.course = _obj
          break
        }
      }
    },
    createForgivingID(str) {
      return str
        .trim()
        .toLowerCase()
        .split(' ')
        .join('_')
    },
    /* Loop all <h1> </h1> and set an ID to them */
    setHeaders() {
      // get all the headings in the content
      const headings = document.getElementsByTagName('h1')

      let i = 0
      // loop through each header and give a forgiving ID
      // ID should match a.href in side nav so header jumping is possible
      for (i; i < headings.length; i++) {
        const _header = headings[i]
        const _forgivingID = this.createForgivingID(_header.innerHTML)
        _header.setAttribute('id', _forgivingID) // set id for _header element. This links to anchors href
      }
    },
    /* update selected item to index of v-for */
    selectItem(index) {
      this.activeItem = index
      const navs = this.$el.getElementsByClassName('list-item') // get all navs

      let i = 0
      for (i; i < navs.length; i++) {
        navs[i].classList.remove('active')
      }
    },
    /* callback that checks which anchor is in the middle 200px of the screen and applies active class to it */
    findActiveNavCallback() {
      const els = this.$el.getElementsByClassName('anchor') // get all anchors
      const navs = this.$el.getElementsByClassName('list-item') // get all navs
      const middle = window.innerHeight / 2
      let i = els.length - 1
      // find the anchor closest to the top of page
      for (i; i >= 0; i--) {
        const offsetY = els[i].getBoundingClientRect().top
        // ************REFACTOR 100 *********
        if (offsetY >= middle - 100 && offsetY <= middle + 100) {
          let j = 0
          // add active class to active anchor, deactivate others
          for (j; j < navs.length; j++) {
            if (j === i) navs[j].classList.add('active')
            else {
              navs[j].classList.remove('active')
              this.activeItem = -1 // set active item to impossibl value
            }
          }
        }
      }
    }
  }
}
</script>

<style lang="stylus" scoped>
@import '~static/css/main.styl'

.flex
  display flex

.bigitem
   /* This will be 3x */
   /* big as the small item. */
   flex 3 0 0

.smallitem
  flex 1 0 0

+mobile()
  .page-nav,
  .page-ads
    display none

.page-ads
  padding-top "calc(1 * %s)" % $header-height

// page navigation
.page-nav
  padding-top "calc(1 * %s)" % $header-height
  order -1
  ul
    position sticky
    position -webkit-sticky /* Safari */
    top "calc(%s + 20px)" % $header-height
    list-style-type none
    margin 0
    padding-left 10px
    padding-right 10px
    padding-bottom 10px
  .list-title
    margin-bottom 10px
    font-size 14pt
    text-transform uppercase
    color $navy
    font-weight 600
  .list-item
    margin-bottom 5px
    font-size 12pt
    cursor pointer
    text-decoration inherit
    color inherit

.list-item:hover
  font-weight 600
  color $blue

.active
  font-weight 600
  color $blue !important

.page-nav,
.page-ads
   transition opacity 0.5s ease-in-out

.page-content
  padding 20px

.page-content:hover ~ .page-nav,
.page-content:hover ~ .page-ads
  transition-delay 1s
  opacity 0.5
</style>
