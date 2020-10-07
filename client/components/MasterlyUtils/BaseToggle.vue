<template>
  <div>
    <!-- prettier-ignore -->
    <label @click="changeEvent($event)" :class="_color" class="switch" for="checkbox">
      <input ref="checker" v-model="state" type="checkbox" checked />
      <span ref="span" class="slider round"></span>
    </label>
    <slot />
  </div>
</template>

<script>
export default {
  name: 'BaseToggle',
  props: {
    color: {
      type: String,
      required: true,
      validator(value) {
        // hex, rgb(a) and red | green | blue
        const color = /red|green|blue|(#([\da-f]{3}){1,2}|(rgb|hsl)a\((\d{1,3}%?,\s?){3}(1|0?\.\d+)\)|(rgb|hsl)\(\d{1,3}%?(,\s?\d{1,3}%?){2}\))/gi
        const regex = new RegExp(color)
        return value.match(regex)
      }
    }
  },
  data() {
    return {
      state: true
    }
  },
  computed: {
    _color() {
      let color = this.color

      switch (color) {
        case 'red':
          color = '#ec6d5f'
          break
        case 'green':
          color = '#27c9b8'
          break
        case 'blue':
          color = '#2caaca'
          break
      }
      return color
    }
  },
  methods: {
    changeEvent(event) {
      this.$emit('toggle')
      this.state = !this.state
      const checkbox = this.$refs.checker
      const span = this.$refs.span
      if (checkbox.checked) span.style.background = this._color
      else span.style.background = ''
    },
    hexToRGB(hex) {
      const result = /^#?([a-f\d]{2})([a-f\d]{2})([a-f\d]{2})$/i.exec(hex)
      return result
        ? {
            r: parseInt(result[1], 16),
            g: parseInt(result[2], 16),
            b: parseInt(result[3], 16)
          }
        : null
    }
  }
}
</script>

<style lang="stylus" scoped>
@import '~static/css/main.styl'

.switch
  position relative
  display inline-block
  width 60px
  height 34px

.switch input
  opacity 0
  width 0
  height 0

.slider
  position absolute
  cursor pointer
  top 0
  left 0
  right 0
  bottom 0
  background-color #ccc
  -webkit-transition .4s
  transition .4s

.slider:before
  position absolute
  content ""
  height 26px
  width 26px
  left 4px
  bottom 4px
  background-color white
  -webkit-transition .4s
  transition .4s

// input:checked + .slider
//   background-color red

input:focus + .slider
  box-shadow 0 0 1px #2196F3

input:checked + .slider:before
  -webkit-transform translateX(26px)
  -ms-transform translateX(26px)
  transform translateX(26px)

/* Rounded sliders */
.slider.round
  border-radius 34px

.slider.round:before
  border-radius 50%
</style>
