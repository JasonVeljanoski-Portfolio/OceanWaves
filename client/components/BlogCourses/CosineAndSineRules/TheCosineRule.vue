<template>
  <!-- prettier-ignore -->
  <div ref="renderMath">
      <BaseTitle>
        Derivation of the Cosine rule
      </BaseTitle>

      <p>
        For any triangle with angles \(A\), \(B\) and \(C\) and corresponding opposite sides \(a\), \(b\) and \(c\), the cosine rule is given by,
      </p>

      <BaseMathProof>
        <BaseBlockQuote 
          slot="equation"
          color="green" 
        >
          $$
          c^2 = a^2 + b^2 - 2ab\cos C
          $$
        </BaseBlockQuote>
        
        <p>
          To derive the cosine rule, we must prove the formula for both acute and obtuse triangles. The cosine rule will apply to all triangles if the rule is true for both of these cases.
        </p>
        
        <BaseToggle
          @toggle="toggleButton"
          color="green"
        >
          <div v-show="flag">Acute Proof</div>
          <div v-show="!flag">Obtuse Proof</div>
        </BaseToggle>

        <transition name="fade">
        <section v-show="flag">
          <BaseTitle>Derivation for Acute Triangles</BaseTitle>
          <p>Consider the acute triangle \(\text{$\triangle $ABC}\)</p>

          <BaseImage width="medium">
            <img src="@/assets/images/MethodsUnit1/CosineAndSineRules/CosAndSin.09.svg">
          </BaseImage>

          <p>
            First consider \(\text{$\triangle $CBD}\) 
            <br>
            Use the Pythagorean theorem 
            $$\begin{aligned} {h}^{2}+{x}^{2} &= {a}^{2} \tag{1} \end{aligned}$$ 

            Use cosine to find an expression for \(x\) 

            $$\begin{aligned} \cos C &= \frac{\text{adjacent}}{\text{hypotenuse}}=\frac{x}{a} \\ x &= a\cos C \tag{2} \end{aligned}$$ 

            Now consider \(\text{$\triangle $ABD}\) 
            <br>
            Use the Pythagorean theorem 

            $$\begin{aligned} {c}^{2} &= {h}^{2}+{(b-x)}^{2} \\ {c}^{2} &= {h}^{2}+{x}^{2}+{b}^{2}-2xb \tag{3} \end{aligned}$$

            Sub \((1)\) and \((2)\) into \((3)\)
          </p>
          
          <BaseBlockQuote color="green" > $$c^2 = a^2 + b^2 - 2ab\cos C$$ </BaseBlockQuote>
        </section>
        </transition>

        <transition name="fade">
        <section v-show="!flag">
          <BaseTitle>Derivation for Obtuse Triangles</BaseTitle>

          <p>Now consider the obtuse triangle \(\text{$\triangle $ABC}\)</p>

          <BaseImage width="medium">
            <img src="@/assets/images/MethodsUnit1/CosineAndSineRules/CosAndSin.17.svg">
          </BaseImage>

          <p>
            First consider \(\text{$\triangle $CBD}\) 
            <br>
            Use the Pythagorean theorem 

            $$\begin{aligned} {h}^{2}+{x}^{2} &= {a}^{2} \tag{1} \end{aligned}$$ 

            Use cosine to find an expression for \(x\) 

            $$\begin{aligned} \cos ({180}^{\circ}-C) &= \frac{\text{adjacent}}{\text{hypotenuse}}=\frac{x}{a} \\ x &= a\cos ({180}^{\circ}-C) \\ x &= -a\cos C \tag{2} \end{aligned}$$

            Now consider \(\text{$\triangle $ABD}\)
            <br>
            Use the Pythagorean theorem 

            $$\begin{aligned} {c}^{2} &= {h}^{2}+{(b+x)}^{2} \\ {c}^{2} &= {h}^{2}+{x}^{2}+{b}^{2}+2xb \tag{3} \end{aligned}$$

            Sub \((1)\) and \((2)\) into \((3)\)
          </p>

          <BaseBlockQuote color="green" > $$c^2 = a^2 + b^2 - 2ab\cos C$$ </BaseBlockQuote>
          
        </section>
        </transition>
      </BaseMathProof>

      <BaseTitle>
        Supplementary Angles of Cosine
      </BaseTitle>

      <p>
        Here we will discuss how \(\cos(180^\circ - C) = - \cos C\) which is used to simplify the obtuse triangle proof. 
        Consider the graphic below of a unit circle with an arbitrary angle \(\phi\) and the angle \(180^\circ - \phi\). 
        Remember that cosine of an angle is the value read off the \(x\) axis on the unit circle.
      </p>

      <BaseImage width="large">
        <img src="@/assets/images/MethodsUnit1/CosineAndSineRules/CosAndSin.18.svg">
      </BaseImage>

      <ul>
        <br>
        <li>\(\cos \phi\) is represented by the \(x\) value on the blue dashed line.</li>
        <li>\(\cos(180^\circ - \phi)\)  is represented by the \(x\) value on the orange dashed line.</li>
      </ul>
      <p>
        <br>
        Notice that the orange and blue dashed lines have the same distance from the origin but the orange is on the negative \(x\) axis and the blue is on the positive. This means they both have the same value but the orange is negative. This concludes that \(-\cos(180^\circ - \phi) = \cos \phi\), or by rearranging, \(\cos(180^\circ - C) = - \cos C\).
      </p>

      <BaseTitle>
        When to use the Cosine Rule
      </BaseTitle>

      <p>
        There are many formulas related to triangles including the area rule, sine rule and cosine rule and it is important to know when to use which formula. The cosine rule is used when we are given:
      </p>

      <ul>
        <li>three sides</li>
        <li>one angle</li>
        <br>
      </ul>

      <p>in which we are solving for one of these.</p>
  </div>
</template>

<script>
import renderMathInElement from 'katex/dist/contrib/auto-render.js' // katex render math in element functionality
import BaseTitle from '@/components/Utils/BaseTitle'
import BaseImage from '@/components/Utils/BaseImage'
import BaseBlockQuote from '@/components/Utils/BaseBlockQuote'
import BaseMathProof from '@/components/MasterlyUtils/BaseMathProof'
import BaseToggle from '@/components/MasterlyUtils/BaseToggle'

export default {
  components: {
    BaseTitle,
    BaseImage,
    BaseBlockQuote,
    BaseMathProof,
    BaseToggle
  },
  data() {
    return {
      flag: true,
      text: 'Acute Proof'
    }
  },
  mounted() {
    renderMathInElement(this.$refs.renderMath)
  },
  methods: {
    toggleButton() {
      this.flag = !this.flag
    }
  }
}
</script>
