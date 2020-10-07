<template>
  <div @click="toggle" class="flexbox background">
    <!-- login form -->
    <form v-show="!isForgot" @click.stop @submit.prevent="submitForm">
      <div class="flexbox">
        <h1>Sign up.</h1>
        <div class="spacer" />
        <BaseIconCross @toggle="toggle" />
      </div>
      <!-- email -->
      <label for="username">Email</label>
      <input id="email" v-model="email" type="text" placeholder="Email" />
      <!-- password -->
      <label for="password">Password</label>
      <input
        id="password"
        v-model="password"
        type="password"
        placeholder="∗∗∗∗∗∗∗∗∗∗∗∗∗∗∗"
      />
      <!-- confirm password -->
      <label for="password">Confirm password</label>
      <input
        id="confirm-password"
        v-model="confirmPassword"
        type="password"
        placeholder="∗∗∗∗∗∗∗∗∗∗∗∗∗∗∗"
      />
      <!-- terms and conditions -->
      <div class="flexbox">
        <BaseCheckbox @toggle="toggleTermsChecked" />
        <span class="terms">
          I agree to the
          <a href="/terms" target="_blank">terms and conditions</a>.
        </span>
      </div>
      <button>Sign up</button>
      <span v-show="errorMsg.length !== 0" class="error">
        login unsuccessful - {{ errorMsg }}
      </span>
    </form>
  </div>
</template>

<script>
import { mapMutations } from 'vuex'
import BaseIconCross from '@/components/Utils/SVG/navigation/BaseIconCross'
import BaseCheckbox from '@/components/Utils/SVG/BaseCheckbox'
export default {
  name: 'TheFormLogin',
  components: {
    BaseIconCross,
    BaseCheckbox
  },
  data() {
    return {
      email: '',
      password: '',
      confirmPassword: '',
      termsChecked: false,
      errorMsg: '',
      isForgot: false
    }
  },
  methods: {
    ...mapMutations({ toggle: 'account.forms/toggleRegister' }),
    toggleForgot() {
      this.isForgot = !this.isForgot
    },
    toggleTermsChecked() {
      this.termsChecked = !this.termsChecked
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

form
  max-width 450px
  width 100%
  padding 25px
  margin 150px 0
  background-color: #f9f9f9
  box-shadow 0 0 20px 0 rgba(0, 0, 0, 0.2), 0 5px 5px 0 rgba(0, 0, 0, 0.24)

.terms
  font-size 10pt

a
  text-decoration none
  font-weight 400
  color $blue

// button style
button
  cursor pointer
  width 100%
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
