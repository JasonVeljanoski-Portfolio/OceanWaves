<template>
  <!-- prettier-ignore -->
  <div ref="renderMath">
      <BaseTitle>
        Review on Linear Functions
      </BaseTitle>

      <p>
        A linear function is a function that graphs a straight line.
        <br><br>
        The general form of a linear function is
        $$y=mx+c$$
        Some common features that are associated with linear functions follow below.
      </p>
      
      <BaseColumns>
        <BaseColumn>
          <!-- COLUMN 1 GOES HERE -->
          <p>This is a linear function with a positive gradient.</p>
          <BaseImage width="medium">
            <img src="@/assets/images/MethodsUnit1/QuadraticRelationships/QuadRel.02.svg">
          </BaseImage>
        </BaseColumn>
        <BaseColumn>
          <!-- COLUMN 2 GOES HERE -->
          <p>Another linear function with a negative gradient.</p>
          <BaseImage width="medium">
            <img src="@/assets/images/MethodsUnit1/QuadraticRelationships/QuadRel.03.svg">
          </BaseImage>
        </BaseColumn>
      </BaseColumns>

      <p>The common features of linear functions are:</p>
      <ul>
        <li>One \(x\) intercept</li>
        <li>One \(y\) intercept</li>
        <li>Constant gradient (slope)</li>
      </ul>

      <BaseTitle>
        Quadratic Relationships
      </BaseTitle>

      <p>
        A quadratic function is a curve that is essentially shaped like a 'U'. These curves are often also named parabolas and they all posses similar properties.
        <br><br>
        The most basic quadratic relationship has the equation
        $$y={x}^{2}$$
        Let us create a table of values and graph the function to see what a quadratic looks like.
      </p>
      
      <!-- <AppModal :mini-player="true">
        <AppVideo
          video-id="204135196"
          color="blue"
        />
      </AppModal> -->
      <p>These points are plotted with a curve following through as shown below.</p>

      <BaseImage width="large">
        <img src="@/assets/images/MethodsUnit1/QuadraticRelationships/QuadRel.01.svg">
      </BaseImage>

      <p>The same way that \(y = x\) is the simplest linear function that exists, \(y = x^2\) is the simplest quadratic function. Notice that the highest power of the equation is two. This is the crucial factor that mathematically defines a quadratic function. </p>
      
      <BaseTitle>
        The Three Different Forms
      </BaseTitle>
      <p>All parabolas possess some common features. Study the graphic below to understand them.</p>
      <BaseImage width="large">
        <img src="@/assets/images/MethodsUnit1/QuadraticRelationships/QuadRel.04.svg">
      </BaseImage>

      <ul>
        <li>1: \(x\) intercepts</li>
        <li>2: \(y\) intercept</li>
        <li>3: Line of symmetry</li>
        <li>4: Turning Point</li>
      </ul>

      <br>

      <p>There exists three common forms in which we can mathematically represent the equation of a quadratic. These forms give different information about the features of a parabola.</p>

      <h3>General Form</h3>
      <BaseBlockQuote color="blue">$$y=a{x}^{2}+bx+c$$</BaseBlockQuote>
      <p>This form gives the vertical shift of a quadratic.</p>
      <h3>Turning Point Form</h3>
      <BaseBlockQuote color="blue"> $$y=a{(x-b)}^{2}+c$$</BaseBlockQuote>
      <p>This form gives the location of the turning point.</p>
      <h3>Intercept Form</h3>
      <BaseBlockQuote color="blue">$$y=a(x-b)(x-c)$$</BaseBlockQuote>
      <p>
        This form gives the location of the \(x\) intercepts.
        <br><br>
        If you expand the tuning point form and intercept form, it can be seen that the highest power is two thus proving that these forms represent the equation of a quadratic.
        <br><br>
        All these forms will be covered in more detail as the chapter progresses.
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
