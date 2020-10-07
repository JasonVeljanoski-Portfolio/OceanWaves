<template>
  <!-- prettier-ignore -->
  <div ref="renderMath"> 
      <BaseTitle>
        The Right Triangle
      </BaseTitle>

      <p>
        A triangle containing a right angle has powerful properties as the sides can be related by the Pythagorean theorem and their ratios are the basis of trigonometry.
      </p>

      <BaseImage width="medium">
        <img src="@/assets/images/MethodsUnit1/CosineAndSineRules/CosAndSin.01.svg">
      </BaseImage>

      <ul>
        <li>The hypotenuse is the longest side of a right triangle</li>
        <li>The adjacent side is always between angle \(\theta\) and the right angle</li>
        <li>The opposite side is always opposite the angle \(\theta\)</li>
      </ul>

      <BaseTitle>
        Pythagorean Theorem
      </BaseTitle>

      The Pythagorean theorem relates the sides of a right triangle.

      <BaseBlockQuote color="green">
        In any right triangle, the sum of the square of the adjacent and opposite sides is equal to the square of the hypotenuse.
      </BaseBlockQuote>

      <p>
        This can be incorporated into a mathematical formula.
        <br> <br>
        For a right triangle with adjacent and opposite sides measured as \(a\) and \(b\) respectively and the length of the hypotenuse is \(c\), the theorem can be expressed as:
      </p>

      <BaseBlockQuote color="green">
        $$c^2 = a^2 + b^2$$
      </BaseBlockQuote>

      <BaseTitle>
        Trigonometry
      </BaseTitle>

      <BaseColumns>
        <BaseColumn>
          <!-- COLUMN 1 GOES HERE -->
          <p style="text-align: center; font-weight: bold;">SOH</p>
          <BaseBlockQuote color="green">
            $$
            \begin{aligned}
            \sin \theta &= \frac{\text{opposite}}{\text{hypotenuse}} 
            \end{aligned}
            $$
          </BaseBlockQuote>
        </BaseColumn>
        <BaseColumn>
          <!-- COLUMN 2 GOES HERE -->
          <p style="text-align: center; font-weight: bold;">CAH</p>
          <BaseBlockQuote color="green">
            $$
            \begin{aligned}
            \cos \theta &= \frac{\text{adjacent}}{\text{hypotenuse}} 
            \end{aligned}
            $$
          </BaseBlockQuote>
        </BaseColumn>
        <BaseColumn>
          <!-- COLUMN 3 GOES HERE -->
          <p style="text-align: center; font-weight: bold;">TOA</p>
          <BaseBlockQuote color="green">
            $$
            \begin{aligned}
            \tan \theta &= \frac{\text{opposite}}{\text{adjacent}}  
            \end{aligned}
            $$
          </BaseBlockQuote>
        </BaseColumn>
      </BaseColumns>

      <p>
        SOH CAH TOA requires the use of an adjacent, opposite and hypotenuse side thus it should be clear that a right triangle must be constructed in order to define sine, cosine and tangent of \(\theta\). In order to sustain a right triangle, \(\theta\) must be between \(0^{\circ}\) and \(90^{\circ}\)  \(\left(0^{\circ}&lt;\theta&lt;90^{\circ}\right)\).
        Our definitions for sine, cosine and tangent break down when \(\theta\) is beyond this domain. This is because we can no longer define a hypotenuse, adjacent and opposite side to manipulate their ratios using SOH CAH TOA in order to find sine, cosine and tangent of \(\theta\). At the moment we are restricted to finding trigonometric values for angles between \(0^{\circ}\) and \(90^{\circ}\). 
        We want to extend our current trigonometric definitions to compliment for angles beyond this domain. This can be achieved by investigating the unit circle.
      </p>
  </div>
</template>

<script>
import renderMathInElement from 'katex/dist/contrib/auto-render.js' // katex render math in element functionality
import BaseTitle from '@/components/Utils/BaseTitle'
import BaseImage from '@/components/Utils/BaseImage'
import BaseBlockQuote from '@/components/Utils/BaseBlockQuote'
import BaseColumns from '@/components/Utils/BaseColumns'
import BaseColumn from '@/components/Utils/BaseColumn'

export default {
  components: {
    BaseTitle,
    BaseImage,
    BaseBlockQuote,
    BaseColumns,
    BaseColumn
  },
  mounted() {
    renderMathInElement(this.$refs.renderMath)
  }
}
</script>
