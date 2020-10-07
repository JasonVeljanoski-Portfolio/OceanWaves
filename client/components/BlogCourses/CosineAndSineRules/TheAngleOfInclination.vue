<template>
  <!-- prettier-ignore -->
  <div ref="renderMath"> 

      <BaseTitle>
        Angle of Inclination
      </BaseTitle>
      
      <BaseBlockQuote color="green" >The angle of inclination is the angle between a line and the positive \(x\) axis.</BaseBlockQuote>
      <p>Some examples follow below where \(\theta_i\) represents the angle of inclination.</p>
      <BaseColumns>
        <BaseColumn width="250px">
          <!-- COLUMN 1 GOES HERE -->
          <BaseImage width="medium">
            <img src="@/assets/images/MethodsUnit1/CosineAndSineRules/CosAndSin.19.svg">
          </BaseImage>
        </BaseColumn>
        <BaseColumn width="250px">
          <!-- COLUMN 2 GOES HERE -->
          <BaseImage width="medium">
            <img src="@/assets/images/MethodsUnit1/CosineAndSineRules/CosAndSin.20.svg">
          </BaseImage>
        </BaseColumn>
      </BaseColumns>

      <p>
        There exists a relationship between the gradient of a line and its angle of inclination.
        <br><br>
        Suppose we cut a section from a line and made a right triangle as shown below. Note that the angle of the triangle against the green line will be the angle of inclination as they are <strong>corresponding angles</strong>.
      </p>
      <BaseImage width="medium">
        <img src="@/assets/images/MethodsUnit1/CosineAndSineRules/CosAndSin.21.svg">
      </BaseImage>

      <p>
        Consider \(\tan \theta\)
    
        $$\begin{aligned}
        \tan \theta_i &= \frac{\text{opposite}}{\text{adjacent}} = \frac{\Delta y}{\Delta x}
        \\
        \tan \theta_i &= \frac{\Delta y}{\Delta x} \tag{1}
        \end{aligned}$$
    
        Consider the gradient \((m)\) of the line
        $$\begin{aligned}
        m &= \frac{\text{rise}}{\text{run}} = \frac{\Delta y}{\Delta x}
        \\
        m &= \frac{\Delta y}{\Delta x} \tag{2}
        \end{aligned}$$
        Now by equating \((1)\) and \((2)\):
      </p>
      <BaseBlockQuote color="green" >$$\tan \theta_i = m$$</BaseBlockQuote>
      <p>This concludes that the gradient of a line is equal to the tangent of its angle of inclination.</p>
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
