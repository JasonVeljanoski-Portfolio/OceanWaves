<template>
  <!-- prettier-ignore -->
  <div ref="renderMath">
      <BaseTitle>The Quadratic Formula</BaseTitle>
      
      <p>The roots of a quadratic equation in the general form, \(ax^{2}+bx+c=0\), is given by the quadratic formula.</p>
            
      <BaseMathProof>
        <BaseBlockQuote 
          slot="equation"
          color="blue" 
        >
          $$x=\frac{-b\pm\sqrt{b^2-4ac}}{2a} \:\:when\:\:ax^2+bx+c=0$$
        </BaseBlockQuote>

        <p>
          Starting with the general form, let us complete the square.

          $$\begin{aligned} y &= ax^{2}+bx+c \end{aligned}$$

          Make the coefficient in front of the \(x\) equal one.

          $$\begin{aligned} \frac{y}{a} &= x^{2}+\frac{b}{a}x+\frac{c}{a} \end{aligned}$$

          We are going to put the values containing an \(x\) in parenthesis.

          $$\begin{aligned} \frac{y}{a} &= \left(x^{2}+\frac{b}{a}x \right)+\frac{c}{a} \end{aligned}$$

          Now lets complete the square by adding \(\frac{b^2}{4a^2}\) inside the parenthesis. We must subtract the same value to not change the equation.

          $$\begin{aligned} \frac{y}{a} &= \left(x^{2}+\frac{b}{a}x+\frac{b^2}{4a^2}\right)+\frac{c}{a}-\frac{b^2}{4a^2} \end{aligned}$$

          Solve for \(y\) and simplify.

          $$\begin{aligned} \frac{y}{a} &= \left(x+\frac{b}{2a}\right)^2+\frac{4ac-b^2}{4a^2} \\ y &= a\left(x+\frac{b}{2a}\right)^2+\frac{4ac-b^2}{4a} \end{aligned}$$

          Now that we have completed the square, we must solve for the \(x\) intercepts in order to obtain the quadratic formula. This is achieved by making \(y=0\) and solving for \(x\). 

          $$\begin{aligned} y &= 0 \\ a\left(x+\frac{b}{2a}\right)^2+\frac{4ac-b^2}{4a} &= 0 \\ a\left(x+\frac{b}{2a}\right)^2 &= \frac{b^2-4ac}{4a} \\ \left(x+\frac{b}{2a}\right)^2 &= \frac{b^2-4ac}{4a^2} \\ \left(x+\frac{b}{2a}\right) &= \pm\sqrt{\frac{b^2-4ac}{4a^2}} \\ &= \frac{\pm\sqrt{b^2-4ac}}{2a} \\ x &= \frac{-b}{2a}\pm\frac{\sqrt{b^2-4ac}}{2a} \end{aligned}$$
        </p>

        <BaseBlockQuote color="blue">$$x=\frac{-b\pm\sqrt{b^2-4ac}}{2a} \:\:\text{when}\:\:ax^2+bx+c=0$$</BaseBlockQuote>
        
      </BaseMathProof>

      <BaseTitle>The Discriminant</BaseTitle>

      <p>The discriminant (\(\Delta\)) is the value under the square root sign in the quadratic formula.</p>

      <BaseBlockQuote color="blue">$$\Delta =b^2-4 a c$$</BaseBlockQuote>
    
      <p>The importance of the discriminant is that it tells us how many solutions of \(x\) we will have when solving the quadratic formula or in other words, how many \(x\) intercepts a parabola will have.</p>

      <!-- COLUMN 1 GOES HERE -->
      <h4>Positive Discriminant</h4>

      <BaseBlockQuote color="blue">
        $$b^2-4 a c>0$$
        <p class="center">There will be two solutions of \(x\) if the discriminant is positive.</p>
      </BaseBlockQuote>
    
      <p>Consider a positive discriminant and the quadratic formula. The square root of a positive number is positive and because there exists a \(\pm\) in front of the square root sign in the quadratic formula, there will be two solutions of \(x\).</p>

      <!-- COLUMN 2 GOES HERE -->
      <h4>Negative Discriminant</h4>

      <BaseBlockQuote color="blue">
        $$b^2-4 a c&lt;0$$
        <p class="center">There will be no real solutions of \(x\) if the discriminant is negative.</p>
      </BaseBlockQuote>
    
      <p>Consider a negative discriminant and the quadratic formula. The square root of a negative number obtains no real solutions therefore no real values of \(x\) will exist.</p>

      <!-- COLUMN 3 GOES HERE -->
      <h4>Zero Discriminant</h4>

      <BaseBlockQuote color="blue">
        $$b^2-4 a c=0$$
        <p class="center">There will be one solution of \(x\) if the discriminant is zero.</p>
      </BaseBlockQuote>
    
      <p>
        When the discriminant is zero, the quadratic formula will simplify to:
        $$x=-\frac{b}{2 a}$$
        Notice that this expression is the equation of the line of symmetry for a parabola given in the general form.
        <br><br>
        Remember that the only time a parabola can have one \(x\) intercept is when the turning point touches the \(x\) axis. As the \(x\) component of the turning point is the equation of the line of symmetry, it makes sense that the quadratic formula simplifies in this way.
      </p>
  </div>
</template>

<script>
import renderMathInElement from 'katex/dist/contrib/auto-render.js' // katex render math in element functionality
import BaseTitle from '@/components/Utils/BaseTitle'
import BaseBlockQuote from '@/components/Utils/BaseBlockQuote'
import BaseMathProof from '@/components/MasterlyUtils/BaseMathProof'

export default {
  name: 'TheUnitCircle',
  components: {
    BaseTitle,
    BaseBlockQuote,
    BaseMathProof
  },
  mounted() {
    renderMathInElement(this.$refs.renderMath)
  }
}
</script>

<style lang="stylus" scoped>
.center
  text-align center
</style>
