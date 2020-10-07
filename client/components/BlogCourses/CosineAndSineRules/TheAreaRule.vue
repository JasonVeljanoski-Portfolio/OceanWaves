<template>
  <!-- prettier-ignore -->
  <div ref="renderMath">
      <BaseTitle>
        Convention used to Label a Triangle
      </BaseTitle>
      
      <p>
        In relation to triangles, we are going to investigate the area rule, sine rule and cosine rule. These formulas use specific symbols that correspond to sides and angles of a triangle. We must follow a common convention to label these sides and angles so that the formulas stay consistent and make sense.
        <br>
        Consider the graphic below.
      </p>
      
      <BaseImage width="medium">
        <img src="@/assets/images/MethodsUnit1/CosineAndSineRules/CosAndSin.08.svg">
      </BaseImage>

      <p>
        The convention used to labelling sides and angles of triangles is shown below.
      </p>
      <ul>
        <li>Angles are always written in capital letters</li>
        <li>Sides are always written in lower case letters</li>
        <li>Sides are oriented opposite their angle (e.g. side \(a\) is opposite angle \(A\)</li>
      </ul>

      <BaseTitle>
        Derivation of the Area Rule
      </BaseTitle>

      <p> 
        The following formula is the area rule for any triangle with an angle \(C\) between two sides \(a\) and \(b\) i.e. follow the convention used to labelling a triangle.
      </p>

      <BaseMathProof>
        <BaseBlockQuote 
          slot="equation"
          color="green" 
        >
          $$A = \frac{1}{2}ab\sin C$$
        </BaseBlockQuote>

        <p>
          To derive the area rule, we must prove the formula for both acute and obtuse triangles. The area rule will apply to all triangles if the rule is true for both of these cases.
        </p>

        <!--

          TOGGLE

        -->
        <BaseToggle
          @toggle="toggleButton()"
          color="green"
        >
          <div v-show="flag">Acute Proof</div>
          <div v-show="!flag">Obtuse Proof</div>
        </BaseToggle>

        <transition name="fade">

          <section v-show="flag">
            <BaseTitle>Derivation for Acute Triangles</BaseTitle>
            <!--<BaseBlockQuote color="green">$$A = \frac{1}{2}ab\sin C$$</BaseBlockQuote>-->
            <p>
              Consider acute triangle  \(\triangle ABC\). Finding an expression for the height \(h\) of the triangle will lead to the formula of the area rule for acute triangles.
            </p>

            <BaseImage width="medium">
              <img src="@/assets/images/MethodsUnit1/CosineAndSineRules/CosAndSin.12.svg">
            </BaseImage>

            <p>
              Consider \(\triangle CBD\)
              
              $$\begin{aligned}
              \sin C &= \frac{\text{opposite}}{\text{hypotenuse}} = \frac{h}{a}
              \\
              h &= a \sin C   \tag{1}
              \end{aligned}$$

              Notice that the base of the triangle is side \(b\)

              $$\begin{aligned}
              b = base    \tag{2}
              \end{aligned}$$

              Consider the formula:

              $$\begin{aligned}
              A = \frac{1}{2}\text{base}\cdot \text{height}   \tag{3}
              \end{aligned}$$

              Sub \((1)\) and \((2)\) into \((3)\)
              <BaseBlockQuote color="green">$$A = \frac{1}{2}ab\sin C$$</BaseBlockQuote>
            </p>
          </section>
        </transition>
        
        <transition name="fade">
          <section v-show="!flag">
            <BaseTitle>Derivation for Obtuse Triangles</BaseTitle>
            <p>
              An identical method as the above can be used to derive the area rule for obtuse triangles. Consider obtuse triangle  \(\triangle ABC\).
            </p>

            <BaseImage width="medium">
              <img src="@/assets/images/MethodsUnit1/CosineAndSineRules/CosAndSin.10.svg">
            </BaseImage>

            <p>Consider \(\triangle CBD\)</p>

            <ul>
              <li> \(\angle BCD\)  is \(180^\circ - C\) as it is the supplementary angle of \(C\).</li>
              <li> We will use this triangle to find an expression for the height \(h\) of \(\triangle ABC\).</li>
              <li> View the supplementary angles of sine section below to see how \(\sin(180^ \circ−C)=\sin C\).</li>
            </ul>

            <p>
              $$\begin{aligned}
              \sin \left(180^\circ - C\right) &= \frac{\text{opposite}}{\text{hypotenuse}} = \frac{h}{a}
              \\
              h &= a \sin\left(180^\circ - C\right)
              \\
              h &= \sin C     \tag{1}
              \end{aligned}$$

              Notice that the base of the triangle is side \(b\)
            
              $$\begin{aligned}
              b=base      \tag{2}
              \end{aligned}$$

              Consider the formula:

              $$\begin{aligned}
              A = \frac{1}{2}\text{base}\cdot \text{height}   \tag{3}
              \end{aligned}$$

              Sub \((1)\) and \((2)\) into \((3)\)
            </p>
            <BaseBlockQuote color="green">$$A = \frac{1}{2}ab\sin C$$</BaseBlockQuote>
          </section>
        </transition>

      </BaseMathProof>

      <BaseTitle>
        Supplementary Angles of Sine
      </BaseTitle>

      <p>
        Here we will discuss how \(\sin(180^\circ - C)=\sin C\) which is used to simplify the obtuse triangle proof.
        <br>
        Consider the graphic below of a unit circle with an arbitrary angle \(\phi\) and the angle \(180^ \circ - \phi\). Remember that sine of an angle is the value read off the \(y\) axis on the unit circle.
      </p>

      <ul>
        <li>\(\sin \phi\) is represented by the \(y\) value on the blue dashed line.</li>
        <li>\(\sin(180^\circ - \phi)\) is represented by the y value on the orange dashed line.</li>
      </ul>

      <BaseImage width="large">
        <img src="@/assets/images/MethodsUnit1/CosineAndSineRules/CosAndSin.11.svg">
      </BaseImage>

      <p>Notice that the orange and blue dashed lines meet at the same \(y\) value. Remember that the \(y\) value on the unit circle represents sine of the angle. This means \(\sin(180^\circ - \phi)= \sin \phi\).</p>
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
