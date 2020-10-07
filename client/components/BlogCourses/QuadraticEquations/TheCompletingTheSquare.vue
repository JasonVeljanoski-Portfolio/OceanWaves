<template>
  <!-- prettier-ignore -->
  <div ref="renderMath">
      <BaseTitle>Completing The Square</BaseTitle>
      
      <p>
        Sometimes we have quadratic equations in the general form in which it is difficult or sometimes impossible to factorise into intercept form. This is a consequence of some quadratics that never intercept the \(x\) axis or do not factorise into whole numbers.
        <br><br>
        All parabolas have a turning point therefore can all be expressed in the turning point form. We can use a process called completing the square to convert quadratics from general form to the turning point form. This process is useful to know as it leads to an alternative method to finding the roots (\(x\) intercepts) of a quadratic especially when it is difficult to factorise from the general form to the intercept form.
        <br><br>
        The process of completing the square is shown below.
        <br><br>
        Start with the general form.
       
        $$\begin{aligned} y &= ax^{2}+bx+c \end{aligned}$$
      </p>

      <ol>
        <li>
          <strong>Make the coefficient in front of the \(x\) equal to one.</strong>
          <br><br>
          This can be acheived by dividing both sides of the equation by \(a\).
          $$\begin{aligned} \frac{y}{a} &= x^{2}+\frac{b}{a}x+\frac{c}{a} \end{aligned}$$
        </li>
        <li>
          <strong>Put the values containing an \(x\) in parenthesis.</strong>
          <br><br>
          Our eventual goal is to add a constant inside the parenthesis that will produce a perfect square binomial. Structuring the equation in this way will make things look neater.
          $$\begin{aligned} \frac{y}{a} &= \left(x^{2}+\frac{b}{a}x \right)+\frac{c}{a} \end{aligned}$$
        </li>
        <li>
          <strong>Find the value that  will make the contents inside the parenthesis factor into a perfect square binomial.</strong>
          <br><br>
          In order to find this value, consider the perfect square binomial \({(x+p)}^{2}\). We can expand this using the crab claw method.

          $${(x+p)}^{2}={x}^{2}+2px+{p}^{2}$$

          We want to convert \(\left(x^{2}+\frac{b}{a}x \right)\) into the form \({x}^{2}+2px+{p}^{2}\). Notice that the \({p}^{2}\) part is missing.
          <br><br>
          A way to find an expression for \({p}^{2}\) is to match the \(2px\) part with our \(\left(x^{2}+\frac{b}{a}x \right)\) expression. We will then have an equation to solve for \(p\).

          $$\begin{aligned}2px &= \frac{b}{a}x\\2p &= \frac{b}{a}\\ p &= \frac{b}{2a} \end{aligned}$$

          Our constant needs to be of the form \({p}^{2}\). Lets square our expression of \(p\).

          $$\frac{b^2}{4a^2}$$

          Adding this value inside the parenthesis will make the expression factorable into a perfect square binomial. In order to not change the equation, we must subtract the same value.

          $$\begin{aligned} \frac{y}{a} &= \left(x^{2}+\frac{b}{a}x+\frac{b^2}{4a^2}\right)+\frac{c}{a}-\frac{b^2}{4a^2} \end{aligned}$$

          Solve for \(y\) and simplify.

          $$\begin{aligned} \frac{y}{a} &= \left(x+\frac{b}{2a}\right)^2+\frac{4ac-b^2}{4a^2} \\ y &= a\left(x+\frac{b}{2a}\right)^2+\frac{4ac-b^2}{4a} \\ &= a\left(x+\frac{b}{2a}\right)^2+c-\frac{b^2}{4a} \end{aligned}$$

          <BaseBlockQuote color="blue">$$ax^2+bx+c=a\left(x+\frac{b}{2a}\right)^2+\left(c-\frac{b^2}{4a}\right)$$</BaseBlockQuote>

          We have successfully converted the general form expression into the turning point form.
        </li>
      </ol>
  </div>
</template>

<script>
import renderMathInElement from 'katex/dist/contrib/auto-render.js' // katex render math in element functionality
import BaseTitle from '@/components/Utils/BaseTitle'
import BaseBlockQuote from '@/components/Utils/BaseBlockQuote'

export default {
  components: {
    BaseTitle,
    BaseBlockQuote
  },
  mounted() {
    renderMathInElement(this.$refs.renderMath)
  }
}
</script>
