<template>
  <!-- prettier-ignore -->
  <div ref="renderMath">
      <BaseTitle>
        Derivation of the Sine rule
      </BaseTitle>

      <p>
        For any triangle with angles \(A\), \(B\) and \(C\) and corresponding opposite sides \(a\), \(b\) and \(c\), the sine rule is given by,
      </p>

      <BaseMathProof>
        <BaseBlockQuote 
          slot="equation"
          color="green" 
        >
          $$
          \frac { a }{ \sin  A } =\frac { b }{ \sin  B } =\frac { c }{ \sin  C } 
          $$
        </BaseBlockQuote>
        
        <p>
          To derive the sine rule, we must prove the formula for both acute and obtuse triangles. The sine rule will apply to all triangles if the rule is true for both of these cases.
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

            <p>
                To derive the formula, create a perpendicular height from angle \(B\) to side \(b\). 
                This is shown by the green dashed line. Expressing the height in terms of a side and the sine of an angle will lead to the formula of the sine rule. 
                Consider the acute triangle \(\text{$\triangle $ABC}\).
            </p>

            <BaseImage width="medium">
                <img src="@/assets/images/MethodsUnit1/CosineAndSineRules/CosAndSin.12.svg">
            </BaseImage>

            <p>
                First consider \(\text{$\triangle $ABD}\) 
                $$\begin{aligned} 
                \sin A &= \frac{\text{opposite}}{\text{hypotenuse}}=\frac{h}{c} \\ h &= c\sin A \tag{1} 
                \end{aligned}$$ 
                Now consider \(\text{$\triangle $CBD}\) 
                $$\begin{aligned} \sin C &= \frac{\text{opposite}}{\text{hypotenuse}}=\frac{h}{a} \\ h &= a\sin C \tag{2} 
                \end{aligned}$$ 
                Equating (1) and (2): 
                $$\begin{aligned} h &= h \\ c\sin A &= a\sin C \\ \frac { c }{ \sin{ C }} &= \frac{ a }{ \sin{ A }} \tag{3} 
                \end{aligned}$$
            </p>
            
            <p>
                To include angle \(B\) and side \(b\) in the relationship, construct another perpendicular height from angle \(A\) to side \(a\). 
                This is shown by the green dashed line in the graphic below.
            </p>

            <BaseImage width="medium">
                <img src="@/assets/images/MethodsUnit1/CosineAndSineRules/CosAndSin.13.svg">
            </BaseImage>

            <p>
                First consider \(\text{$\triangle $ABD}\) 
                $$\begin{aligned} \sin B &= \frac{\text{opposite}}{\text{hypotenuse}}=\frac{h}{c} \\ h &= c\sin B \tag{4} \end{aligned}$$
                Now consider \(\text{$\triangle $ACD}\) 
                $$\begin{aligned} \sin C &= \frac{\text{opposite}}{\text{hypotenuse}}=\frac{h}{b} \\ h &= b\sin C \tag{5} \end{aligned}$$ 
                Equating (4) and (5): 
                $$\begin{aligned} h &= h \\ c\sin B &= b\sin C \\ \frac { c }{ \sin{ C }} &= \frac{ b }{ \sin{ B }} \tag{6} \end{aligned}$$
                Thus by equating (3) and (6),
            </p>
            <BaseBlockQuote color="green" > $$\frac { a }{ \sin  A } =\frac { b }{ \sin  B } =\frac { c }{ \sin  C }$$ </BaseBlockQuote>
            </section>

        </transition>

        <transition name="fade">

            <section v-show="!flag">
            <BaseTitle>Derivation for Obtuse Triangles</BaseTitle>
            <p>
                To derive the formula, create a perpendicular height from angle \(B\) to the extension of side \(b\). This is shown by the green dashed line. Expressing the height in terms of a side and the sine of an angle will lead to the formula of the sine rule.
                <br><br>
                Consider obtuse triangle  \(\text{$\triangle $ABC}\)
            </p>
            <BaseImage width="medium">
                <img src="@/assets/images/MethodsUnit1/CosineAndSineRules/CosAndSin.10.svg">
            </BaseImage>
            <p>
                First consider \(\text{$\triangle $ABD}\) 
                $$\begin{aligned} \sin A &= \frac{\text{opposite}}{\text{hypotenuse}}=\frac{h}{c} \\ h &= c\sin A \tag{1} \end{aligned}$$
                Now consider \(\text{$\triangle $CBD}\) 
                $$\begin{aligned} \sin ({180}^{\circ}-C) &= \frac{\text{opposite}}{\text{hypotenuse}}=\frac{h}{a} \\ h &= a\sin ({180}^{\circ}-C) \\ h &= a\sin C \tag{2}  \end{aligned}$$
                Equating (1) and (2):
                $$\begin{aligned} h &= h \\ c\sin A &= a\sin C \\ \frac { c }{ \sin{ C }} &= \frac{ a }{ \sin{ A }} \tag{3} \end{aligned}$$
            </p>
            <p>
                To include angle \(B\) and side \(b\) in the relationship, construct another perpendicular height from angle \(A\) to the extension of side \(a\). This is shown by the green dashed line in the graphic below.
            </p>
            <BaseImage width="medium">
                <img src="@/assets/images/MethodsUnit1/CosineAndSineRules/CosAndSin.14.svg">
            </BaseImage>

            <p>
                First consider \(\text{$\triangle $ABD}\) 
                $$\begin{aligned} \sin B &= \frac{\text{opposite}}{\text{hypotenuse}}=\frac{h}{c} \\ h &= c\sin B \tag{4} \end{aligned}$$
                Now consider \(\text{$\triangle $ACD}\) 
                $$\begin{aligned} \sin \left({180}^{\circ}-C\right) &= \frac{\text{opposite}}{\text{hypotenuse}}=\frac{h}{b} \\ h &= b\sin ({180}^{\circ}-C) \\ h &= b\sin C\tag{5} \end{aligned}$$
                Equating (4) and (5): 
                $$\begin{aligned} h &= h \\ c\sin B &= b\sin C \\ \frac { c }{ \sin{ C }} &= \frac{ b }{ \sin{ B }} \tag{6}  \end{aligned}$$
                Thus by equating (3) and (6),
            </p>
            <BaseBlockQuote color="green" > $$\frac { a }{ \sin  A } =\frac { b }{ \sin  B } =\frac { c }{ \sin  C }$$ </BaseBlockQuote>
          </section>
        </transition>
      </BaseMathProof>

      <BaseTitle>
        When to use the Sine Rule
      </BaseTitle>

      <p>
        There are many formulas related to triangles including the area rule, sine rule and cosine rule and it is important to know when to use which formula to solve problems. The sine rule is used when we are given,
      </p>

      <ul>
        <li>
          two sides
        </li>
        <li>
          two angles
        </li>
      </ul>

      <p>
        <br>
        in which we are solving for one of these (i.e. our variable \(x\) counts as one of these sides or angles).
      </p>

      <BaseTitle>
        How to check if your solution looks reasonable
      </BaseTitle>

      <p>
        In tests and exams, this cool trick can be used to check if your solutions involving the sine rule looks reasonable.
        <br>
        Consider the two triangles below with different sized angles and sides.
      </p>

      <BaseColumns>
        <BaseColumn width="250px">
          <!-- COLUMN 1 GOES HERE -->
          <BaseImage width="small">
            <img src="@/assets/images/MethodsUnit1/CosineAndSineRules/CosAndSin.15.svg">
          </BaseImage>
        </BaseColumn>
        <BaseColumn width="250px">
          <!-- COLUMN 2 GOES HERE -->
          <BaseImage width="small">
            <img src="@/assets/images/MethodsUnit1/CosineAndSineRules/CosAndSin.16.svg">
          </BaseImage>
        </BaseColumn>
      </BaseColumns>

      <p>
        The graphic shows two triangles. One triangle has an angle and opposite side labelled '\(A\)' and '\(a\)' respectively and the other triangle has an angle and opposite side labelled '\(B\)' and '\(b\)' respectively. Notice that angle '\(A\)' is larger than '\(B\)' and side '\(a\)' is longer than '\(b\)'. We can conclude the following result in the statement below.
      </p>
      
      <BaseBlockQuote color="green">
        The largest angle in a triangle will always have the longest opposite side.
      </BaseBlockQuote>

      <p>
        This statement can be used to compare two sets of angles and opposite sides within a triangle. If you solved for one of these angles or sides and it does not agree with the statement above, then your solution must be incorrect. However, if the solution agrees with the statement then you can have good reason to beleive you are correct.
        <br>
        The sine rule uses the information of two angles and their opposite sides thus the fact above can be used to compare the validity of the solution. This fact only applies to the sine rule as the cosine rule does not possess enough information to compare the angles and sides in a triangle as we will soon find out.
      </p>
  </div>
</template>

<script>
import renderMathInElement from 'katex/dist/contrib/auto-render.js' // katex render math in element functionality
import BaseTitle from '@/components/Utils/BaseTitle'
import BaseImage from '@/components/Utils/BaseImage'
import BaseBlockQuote from '@/components/Utils/BaseBlockQuote'
import BaseMathProof from '@/components/MasterlyUtils/BaseMathProof'
import BaseToggle from '@/components/MasterlyUtils/BaseToggle'
import BaseColumns from '@/components/Utils/BaseColumns'
import BaseColumn from '@/components/Utils/BaseColumn'

export default {
  components: {
    BaseTitle,
    BaseImage,
    BaseBlockQuote,
    BaseMathProof,
    BaseToggle,
    BaseColumns,
    BaseColumn
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
