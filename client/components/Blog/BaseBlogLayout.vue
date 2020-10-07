<template>
  <div>
    <BaseBlogLayoutVideoSection :topics="topics" />
    <BaseBlogLayoutContent :topics="topics">
      <slot />
    </BaseBlogLayoutContent>
  </div>
</template>

<script>
import BaseBlogLayoutVideoSection from '@/components/Blog/BaseBlogLayoutVideoSection'
import BaseBlogLayoutContent from '@/components/Blog/BaseBlogLayoutContent'

export default {
  name: 'CosineAndSineRulesPage',
  components: {
    BaseBlogLayoutVideoSection,
    BaseBlogLayoutContent
  },
  props: {
    topics: {
      type: Array,
      required: true,
      validator(value) {
        return typeof value === 'object'
      }
    }
  }
}
</script>

<style lang="stylus" scoped>
@import '~static/css/main.styl'
</style>
