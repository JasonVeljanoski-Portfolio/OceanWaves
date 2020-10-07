<template>
  <div :style="style" class="proof-container">
    <h5
      v-show="!isOpen"
      :style="textStyle"
      @click="toggleProof"
      class="proof-text"
    >
      Show Proof
    </h5>
    <h5
      v-show="isOpen"
      :style="textStyle"
      @click="toggleProof"
      class="proof-text"
    >
      Hide Proof
    </h5>
    <div :style="equStyle">
      <slot v-show="!isOpen" name="equation" />
    </div>
    <div v-show="isOpen">
      <div class="proof">
        <slot />
      </div>
      <h5 class="proof-qed">
        q.e.d
      </h5>
    </div>
  </div>
</template>

<script>
export default {
  name: 'BaseMathProof',
  data() {
    return {
      isOpen: false,
      style: '',
      equStyle: '',
      textStyle: {
        width: '100px'
      }
    }
  },
  methods: {
    toggleProof() {
      this.isOpen = !this.isOpen
      if (this.isOpen) {
        this.style = {
          'background-color': '#f4f5f7',
          border: '1px solid #e5e5e5'
        }
        this.equStyle = {
          display: 'none'
        }
        this.textStyle = {
          width: '85px'
        }
      } else {
        this.style = ''
        this.equStyle = ''
        this.textStyle = {
          width: '100px'
        }
      }
    }
  }
}
</script>

<style lang="stylus" scoped>
@import '~static/css/main.styl'

.proof-container
  overflow scroll

.proof-text
  padding 5px
  font-size 12px
  text-transform uppercase
  color #929395
  cursor pointer

.proof
  padding 20px 50px

.proof-qed
  text-align right
  padding 5px
  font-size 12px
  text-transform uppercase
  color #929395
</style>
