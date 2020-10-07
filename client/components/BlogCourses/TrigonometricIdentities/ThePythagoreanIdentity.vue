<template>
  <!-- prettier-ignore -->
  <div ref="renderMath"> 
      <BaseTitle>
        Derivation of the Pythagorean identity
      </BaseTitle>

      <p>The Pythagorean identity relates sine and cosine to the Pythagorean theorem. You can see that we can derive this identity just with a few facts about the unit circle.</p>

      <BaseMathProof>
        <BaseBlockQuote 
          slot="equation"
          color="green" 
        >
          $$\cos ^2 \theta + \sin^2 \theta = 1$$
        </BaseBlockQuote>

        <BaseImage width="large">
          <img src="@/assets/images/MethodsUnit1/TrigonometricIdentities/TrigIden.01.svg">
        </BaseImage>
        
        <p>
          Consider the right triangle in the unit circle presented in the graphic.
          <br>
          Use the Pythagorean theorem.

          $$\begin{aligned}
          x^2 + y^2 &= 1^2
          \\
          x^2 + y^2 &= 1
          \end{aligned}$$

          We know \(\cos \theta = x\) and \(\sin \theta = y\) from the unit circle definition of sine and cosine. Let us replace the values of \(x\) and \(y\). This will result in the Pythagorean identity.
        </p>
        <BaseBlockQuote color="green" > $$\cos ^2 \theta + \sin^2 \theta = 1$$ </BaseBlockQuote>
      </BaseMathProof>
  </div>
</template>

<script>
import renderMathInElement from 'katex/dist/contrib/auto-render.js' // katex render math in element functionality
import BaseTitle from '@/components/Utils/BaseTitle'
import BaseImage from '@/components/Utils/BaseImage'
import BaseBlockQuote from '@/components/Utils/BaseBlockQuote'
import BaseMathProof from '@/components/MasterlyUtils/BaseMathProof'

export default {
  components: {
    BaseTitle,
    BaseImage,
    BaseBlockQuote,
    BaseMathProof
  },
  mounted() {
    renderMathInElement(this.$refs.renderMath)
  }
}
</script>
