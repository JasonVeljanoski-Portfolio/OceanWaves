<template>
  <ul class="icon-list flexbox">
    <a
      v-if="hasFacebook"
      :href="linkFacebook"
      target="_blank"
      class="icon-item"
    >
      <BaseIconFacebook />
    </a>
    <a
      v-if="hasInstagram"
      :href="linkInstagram"
      target="_blank"
      class="icon-item"
    >
      <BaseIconInstagram />
    </a>
    <a
      v-if="hasLinkedin"
      :href="linkLinkedin"
      target="_blank"
      class="icon-item"
    >
      <BaseIconLinkedin />
    </a>
    <a v-if="hasTwitter" :href="linkTwitter" target="_blank" class="icon-item">
      <BaseIconTwitter />
    </a>
    <a v-if="hasYoutube" :href="linkYoutube" target="_blank" class="icon-item">
      <BaseIconYoutube />
    </a>
  </ul>
</template>

<script>
import BaseIconFacebook from '@/components/Utils/SVG/social/BaseIconFacebook'
import BaseIconInstagram from '@/components/Utils/SVG/social/BaseIconInstagram'
import BaseIconLinkedin from '@/components/Utils/SVG/social/BaseIconLinkedin'
import BaseIconTwitter from '@/components/Utils/SVG/social/BaseIconTwitter'
import BaseIconYoutube from '@/components/Utils/SVG/social/BaseIconYoutube'

export default {
  name: 'BaseSocialMedia',
  components: {
    BaseIconFacebook,
    BaseIconInstagram,
    BaseIconLinkedin,
    BaseIconTwitter,
    BaseIconYoutube
  },
  props: {
    hasFacebook: {
      type: Boolean,
      require: true,
      validator(value) {
        return typeof value === 'boolean'
      }
    },
    hasInstagram: {
      type: Boolean,
      require: true,
      validator(value) {
        return typeof value === 'boolean'
      }
    },
    hasLinkedin: {
      type: Boolean,
      require: true,
      validator(value) {
        return typeof value === 'boolean'
      }
    },
    hasTwitter: {
      type: Boolean,
      require: true,
      validator(value) {
        return typeof value === 'boolean'
      }
    },
    hasYoutube: {
      type: Boolean,
      require: true,
      validator(value) {
        return typeof value === 'boolean'
      }
    },
    linkFacebook: {
      type: String,
      require: false,
      default: 'https://www.facebook.com',
      validator(value) {
        // value must match a web link or '/' (the default value)
        const web = /^https?:\/\/(.*)/gi
        const regex = new RegExp(web)
        return value.match(regex)
      }
    },
    linkInstagram: {
      type: String,
      require: false,
      default: 'https://www.instagram.com',
      validator(value) {
        // value must match a web link or '/' (the default value)
        const web = /^https?:\/\/(.*)/gi
        const regex = new RegExp(web)
        return value.match(regex)
      }
    },
    linkLinkedin: {
      type: String,
      require: false,
      default: 'https://www.linkedin.com',
      validator(value) {
        // value must match a web link with http or https or '/' (the default value)
        const web = /^https?:\/\/(.*)/gi
        const regex = new RegExp(web)
        return value.match(regex)
      }
    },
    linkTwitter: {
      type: String,
      require: false,
      default: 'https://www.twitter.com',
      validator(value) {
        // value must match a web link or '/' (the default value)
        const web = /^https?:\/\/(.*)/gi
        const regex = new RegExp(web)
        return value.match(regex)
      }
    },
    linkYoutube: {
      type: String,
      require: false,
      default: 'https://www.youtube.com',
      validator(value) {
        // value must match a web link or '/' (the default value)
        const web = /^https?:\/\/(.*)/gi
        const regex = new RegExp(web)
        return value.match(regex)
      }
    }
  }
}
</script>

<style lang="stylus" scoped>
@import '~static/css/main.styl'

.spacer
  flex 1 1 auto

.icon-list
  flex-flow row wrap
  list-style none
  padding 0
  margin 0

.icon-item
  margin 0 5px
  text-decoration none

.icon-item:hover
  cursor pointer
  opacity 0.9
</style>
