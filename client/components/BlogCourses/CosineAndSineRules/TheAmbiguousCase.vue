<template>
  <!-- prettier-ignore -->
  <div ref="renderMath">
      <BaseTitle>
        The Ambiguous Case
      </BaseTitle>

      <p>
        A unique feature of sine is that an obtuse angle (an angle between \(90^\circ\) and \(180^\circ\)) can have the same sine value as an acute angle (an angle between \(0^\circ\) and \(90^\circ\)). This concept has been briefly discussed in some sections above.
        <br><br>
        The graphic below shows this unique feature of sine.
      </p>

      <BaseImage width="large">
        <img src="@/assets/images/MethodsUnit1/CosineAndSineRules/CosAndSin.11.svg">
      </BaseImage>

      <ul>
        <li>Sine is the \(y\) component of a coordinate on the unit circle.</li>
        <li>The first quadrant contains all acute angles (angles between \(0^\circ\) and \(90^\circ\)).</li>
        <li>The second quadrant contains all obtuse angles (angles between \(90^\circ\) and \(180^\circ\)).</li>
        <br>
      </ul>

      <p>Notice that the angles \(\phi\) and \(180^\circ - \phi\) produce the same sine value. This concludes the following result.</p>

      <BaseBlockQuote color="green" > 
        $$
        \sin \phi = \sin \left(180^\circ - \phi \right)
        $$
      </BaseBlockQuote>

      <p>
        This relationship is relevant for angles that are between \(0^\circ\) and \(180^\circ\) (in the first and second quadrant) which is also the range of angles that a triangles angles can be. This resemblance between sine and a triangles angles is the corner stone that defines the ambiguous case.
      </p>

      <BaseTitle>
        Ambiguous Case in the Area Rule
      </BaseTitle>

      <p> 
        The area rule is given by: 
        
        $$\begin{aligned}
        A = \frac{1}{2}ab\sin C
        \end{aligned}$$
        
        Notice this formula contains \(\sin C\). We also know that

        $$
        \sin C = \sin \left(180^\circ - C \right)
        $$
        
        therefore the area rule can be rewritten as

        $$\begin{aligned}
        A = \frac{1}{2}ab\sin\left(180^\circ - C \right)
        \end{aligned}$$

        When we are given questions involving the area rule in which we have to solve for the angle (meaning we are given the area and the two side lengths), we must be conscious that the ambiguous case will always take effect meaning that there will be two solutions for the angle. One of the solutions will be \(C\) and the other will be \(180^\circ - C\).
      </p>

      <BaseTitle>
        Ambiguous Case in the Sine Rule
      </BaseTitle>

      <p>
        The sine rule is given by:
        $$ \frac { a }{ \sin  A } =\frac { b }{ \sin  B } =\frac { c }{ \sin  C } $$

        We also know that
        $$
        \sin C = \sin \left(180^\circ - C \right)
        $$
        therefore the sine rule can be rewritten as
        $$ \frac { a }{ \sin  \left(180^\circ - A \right) } =\frac { b }{ \sin \left(180^\circ - B \right) } =\frac { c }{ \sin  \left(180^\circ - C \right) } $$
 
        When we are given questions involving the sine rule in which we have to solve for an angle (meaning we are given one angle and two side lengths), we must be conscious that the ambiguous case can take effect on the solution. However, this extra solution may not always be valid.
        <br><br>
        Although this second possible solution is mathematically justified, it may not always apply to the context involving triangles. This is because the sum of angles in a triangle must always add to \(180^\circ\). If our second solution produces an angle that does not comply with this rule, the angle will not be valid as it is not supported by the context although the math works. 
        <br><br>
        Some simple steps below will show how to always account for the ambiguous case when completing problems in which you must solve for an angle using the sine rule.
      </p>

      <ol>
        <li>Find the 'normal' solution (acute angle) for \(\phi\)</li>
        <li>Calculate the obtuse angle \(180^\circ - \phi\)</li>
        <li>Test if the supplementary angle is valid for the context of triangles</li>
        <br>
      </ol>

      <p>
        All that is needed in order to test the validity of the obtuse angle solution is to use the fact that the sum of the angles in a triangle add to \(180^\circ\). 
        <br><br>
        If the sum of the given angle and obtuse angle is less than \(180^\circ\), then the obtuse angle will be a valid solution. There will exist two triangles that share the same information given in the problem.
        <br><br>
        If the sum of the given angle and obtuse angle is more than \(180^\circ\), then the obtuse angle will not be a valid solution as it is impossible to make a triangle with angles that add to more than \(180^\circ\). This means that only one triangle will exist that has the same information given in the problem.
      </p>

      <BaseTitle>
        There is NO Ambiguous Case in the Cosine Rule
      </BaseTitle>

      <p>
        Cosine does not have two angles that give the same cosine value in the first and second quadrant like sine and therefore there is no ambiguous case in the cosine rule. This means that there will always be only one solution for the angle if a problem asked to solve for the angle using the cosine rule.
        <br><br>
        The cosine rule is shown bellow for reference.
        $$\begin{aligned}
        c^2 = a^2 +b^2 -2ab\cos C
        \end{aligned}$$
        We can visually show how cosine does not possess the unique features of sine using the unit circle.
      </p>
      <BaseImage width="large">
        <img src="@/assets/images/MethodsUnit1/CosineAndSineRules/CosAndSin.18.svg">
      </BaseImage>

      <strong>REMINDER:</strong>
      <ul>
        <li>Sine is the \(y\) component of a coordinate on the unit circle.</li>
        <li>The first quadrant contains all acute angles (angles between \(0^\circ\) and \(90^\circ\)).</li>
        <li>The second quadrant contains all obtuse angles (angles between \(90^\circ\) and \(180^\circ\)).</li>
        <br>
      </ul>
      <p>
        It is clear by the graphic above that there will be no angle in the first quadrant that will have the same cosine value as an angle in the second quadrant. This means that the ambiguous case will not apply when using the cosine rule.
      </p>
  </div>
</template>

<script>
import renderMathInElement from 'katex/dist/contrib/auto-render.js' // katex render math in element functionality
import BaseTitle from '@/components/Utils/BaseTitle'
import BaseImage from '@/components/Utils/BaseImage'
import BaseBlockQuote from '@/components/Utils/BaseBlockQuote'

export default {
  components: {
    BaseTitle,
    BaseImage,
    BaseBlockQuote
  },
  mounted() {
    renderMathInElement(this.$refs.renderMath)
  }
}
</script>
