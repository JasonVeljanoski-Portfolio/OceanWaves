<template>
  <nuxt-link :to="`/${$route.name}/${slug}`" class="nav-item">
    <div class="tile">
      <section class="content">
        <div class="img-container">
          <BaseBlogTileArt
            :title="coursetitle"
            :subtitle="title"
            :color="color"
          />
        </div>
        <div class="title">{{ title }}</div>
        <!-- prettier-ignore -->
        <p class="description">{{ description }}</p>
      </section>
      <section class="footer">
        <div class="flexbox stats-box">
          <BaseIconPencile />
          <div class="stats">
            <p>{{ numberOfLessons }} Lessons</p>
            <p>{{ videoLength }} hours</p>
          </div>
          <BaseIconDifficulty :difficulty="difficulty" class="pad" />
        </div>
        <div class="footer-text flexbox">
          <span :style="_color">Start Course</span>
        </div>
      </section>
    </div>
  </nuxt-link>
</template>

<script>
import BaseIconDifficulty from '@/components/Utils/SVG/BaseIconDifficulty'
import BaseIconPencile from '@/components/Utils/SVG/BaseIconPencile'
import BaseBlogTileArt from '@/components/Blog/BaseBlogTileArt'

export default {
  name: 'BaseBlogTile',
  components: {
    BaseIconDifficulty,
    BaseIconPencile,
    BaseBlogTileArt
  },
  // image should have 16:9 aspect ratio
  props: {
    coursetitle: {
      type: String,
      required: true,
      validator(value) {
        return typeof value === 'string'
      }
    },
    title: {
      type: String,
      required: true,
      validator(value) {
        return typeof value === 'string'
      }
    },
    color: {
      type: String,
      required: false,
      default: '#ccc',
      validator(value) {
        // hex, rgb(a) and red | green | blue
        const color = /red|green|blue|(#([\da-f]{3}){1,2}|(rgb|hsl)a\((\d{1,3}%?,\s?){3}(1|0?\.\d+)\)|(rgb|hsl)\(\d{1,3}%?(,\s?\d{1,3}%?){2}\))/gi
        const regex = new RegExp(color)
        return value.match(regex)
      }
    },
    description: {
      type: String,
      required: true,
      validator(value) {
        return typeof value === 'string'
      }
    },
    difficulty: {
      type: String,
      required: true,
      validator(value) {
        return typeof value === 'string'
      }
    },
    numberOfLessons: {
      type: Number,
      required: true,
      validator(value) {
        return typeof value === 'number'
      }
    },
    videoLength: {
      type: String,
      required: true,
      validator(value) {
        // value must match a time in the form hh:mm:ss
        const time = /^(\d+):(\d+):(\d+)$/gi
        const regex = new RegExp(time)
        return value.match(regex)
      }
    },
    slug: {
      type: String,
      required: true,
      validator(value) {
        // typical slug regex
        const link = /^[a-z0-9]+(?:-[a-z0-9]+)*$/gi
        const regex = new RegExp(link)
        return value.match(regex)
      }
    }
  },
  computed: {
    _color() {
      let col = this.color

      switch (col) {
        case 'red':
          col = '#ec6d5f'
          break
        case 'green':
          col = '#27c9b8'
          break
        case 'blue':
          col = '#2caaca'
          break
      }

      // const rgb = this.hexToRGB(color)

      return {
        // 'border-left-color': color,
        color: col,
        opacity: 0.6
      }
    }
  }
}
</script>

<style lang="stylus" scoped>
@import '~static/css/main.styl'

$w = 300px
$h = 500px
$footer-txt-height = 50px

$footer-wrap-brkpnt = 313px     // mobile
mobile()
  @media (max-width: $footer-wrap-brkpnt)
    {block}

.nav-item
  text-decoration none
  color $grey

.tile
  margin 10px
  min-height $h
  max-width $w
  border solid 1px $border-color
  cursor pointer
  transition: transform 0.5s ease

.tile:hover
  transform scale(1.01, 1.01)
  span
    opacity 1 !important

.content
  width 100%

.img-container
  // background-color red
  // width 90%
  // padding-bottom 56.25% // 16:9 aspect ratio

.title
  color $navy
  font-size 16pt
  font-weight 600
  padding 15px 15px 0 15px
  // background-color yellow

.description
  text-align left
  line-height normal
  margin-top 10px
  font-size 11pt
  color $grey
  padding 15px 15px 0 15px

.stats
  text-align center
  p
    line-height normal
    margin 0
    color $grey
    font-size 12pt

.stats p:first-child
  font-weight 400
  font-size 16px
  color $grey

.stats-box
  height $footer-txt-height
  flex-wrap wrap
  justify-content flex-start

.footer
  width 100%
  bottom 0
  left 0
  height 90px

.pad
  padding-left 10px

.footer-text
  height $footer-txt-height
  background-color $border-color
  font-size 16px
  font-weight 400

.tile
  position relative

.content
  padding-bottom "calc(2 * %s)" % $footer-txt-height

.footer
  position absolute
  bottom 0
  width 100%
  height "calc(2 * %s)" % $footer-txt-height

+mobile()
  .content
    padding-bottom "calc(3 * %s)" % $footer-txt-height
  .footer
    height "calc(3 * %s)" % $footer-txt-height
  .stats-box
    height "calc(2 * %s)" % $footer-txt-height
</style>
