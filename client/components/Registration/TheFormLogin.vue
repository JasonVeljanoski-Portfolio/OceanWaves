<template>
  <div @click="toggle" class="flexbox background">
    <!-- login form -->
    <form v-show="!isForgot" @click.stop @submit.prevent="submitForm">
      <div class="flexbox">
        <h1>Sign in.</h1>
        <div class="spacer" />
        <BaseIconCross @toggle="toggle" />
      </div>
      <label for="username">Email</label>
      <!-- email -->
      <input id="email" v-model="email" type="text" placeholder="Email" />
      <label for="password">Password</label>
      <!-- password -->
      <input
        id="password"
        v-model="password"
        type="password"
        placeholder="∗∗∗∗∗∗∗∗∗∗∗∗∗∗∗"
      />
      <div class="pad" />
      <div class="flexbox">
        <span @click="toggleForgot" class="forgot">Forgot Password?</span>
        <div class="spacer" />
        <button>Login</button>
      </div>
      <span v-show="errorMsg.length !== 0" class="error">
        login unsuccessful - {{ errorMsg }}
      </span>
    </form>

    <!-- forgot password form -->
    <form v-show="isForgot" @click.stop @submit.prevent="submitForm">
      <div class="flexbox">
        <h1>Reset your password.</h1>
        <div class="spacer" />
        <BaseIconCross @toggle="toggle" />
      </div>
      <span>TODO - handle reset password</span>
      <div class="pad" />
      <div class="flexbox">
        <span @click="toggleForgot" class="forgot">Back to login</span>
        <div class="spacer" />
        <button>Send Reset</button>
      </div>
    </form>
  </div>
</template>

<script>
import { mapMutations } from 'vuex'
import BaseIconCross from '@/components/Utils/SVG/navigation/BaseIconCross'

export default {
  name: 'TheFormLogin',
  components: {
    BaseIconCross
  },
  data() {
    return {
      email: '',
      password: '',
      errorMsg: '',
      isForgot: false
    }
  },
  methods: {
    ...mapMutations({ toggle: 'account.forms/toggleLogin' }),
    toggleForgot() {
      this.isForgot = !this.isForgot
    },
    submitForm() {
      this.errorMsg = '' // ensure previous error disapears, if any

      this.$axios
        .post(`/api/users`, {
          email: this.email,
          password: this.password
        })
        .then((res) => {
          // eslint-disable-next-line
          console.log(res)
          // close login modal when success
          // maybe show a success message
          // this.$emit('authenticate', res)
        })
        .catch((err) => {
          // eslint-disable-next-line
          console.log(err)
          this.errorMsg = err
        })
    }
  }
}
</script>

<style lang="stylus" scoped>
@import '~static/css/main.styl'

.background
  position fixed
  z-index 998
  top 0
  width 100%
  height 100%
  background-color rgba(0, 0, 0, 0.25)

.spacer
  flex 1 1 auto
  padding 5px

.pad
  padding-top 10px

form
  max-width 450px
  width 100%
  padding 25px
  margin 150px 0
  background-color: #f9f9f9
  box-shadow 0 0 20px 0 rgba(0, 0, 0, 0.2), 0 5px 5px 0 rgba(0, 0, 0, 0.24)

// button style
button
  cursor pointer
  width 150px
  border none
  background $blue
  color #fff
  margin 0 0 5px
  padding 10px
  font-size 15px

button:hover
  background $blue
  opacity 0.9
  -webkit-transition background 0.3s ease-in-out
  -moz-transition background 0.3s ease-in-out
  transition background-color 0.3s ease-in-out

button:active
  box-shadow inset 0 1px 3px rgba(0, 0, 0, 0.5)

// input styles
input[type="text"],
input[type="password"],
input[type="email"],
input[type="tel"],
input[type="url"],
textarea,
button[type="submit"]
  font 400 12px/16px "Roboto", Helvetica, Arial, sans-serif

fieldset
  border medium none !important
  margin 0 0 10px
  min-width 100%
  padding 0
  width 100%

input[type="text"],
input[type="email"],
input[type="tel"],
input[type="url"],
input[type="password"],
textarea
  width 100%
  border 1px solid #ccc
  background #fff
  margin 0 0 5px
  padding 10px

input[type="text"]:hover,
input[type="email"]:hover,
input[type="tel"]:hover,
input[type="password"]:hover,
input[type="url"]:hover,
textarea:hover
  -webkit-transition border-color 0.2s ease-in-out
  -moz-transition border-color 0.2s ease-in-out
  transition border-color 0.2s ease-in-out
  border 1px solid #aaa

textarea:focus,
input:focus
  border-color $blue !important

textarea, select, input, button
  outline none

.error
  color red
  font-style italic

.forgot
  font-weight 400
  width 200px
  cursor pointer
  color $navy

.forgot:hover
  color $grey
</style>
