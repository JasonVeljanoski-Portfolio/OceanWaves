<template>
  <!-- prettier-ignore -->
  <div ref="renderMath">
      <BaseTitle>
        What is the Unit Circle?
      </BaseTitle>


      <BaseImage width="medium">
        <img src="@/assets/images/MethodsUnit1/CosineAndSineRules/CosAndSin.02.svg">
      </BaseImage>

      <p>
        The unit circle is defined as a circle centred at the origin \((0,0)\) of the \(x−y\) plane and has a radius equal to one unit.
        Angles are measured starting \(0^\circ\) on the positive \(x\) axis where moving anti-clockwise will produce a positive angle and clockwise will produce a negative angle. The graphic above shows \(\theta\) to be a positive angle through this convention.
        The unit circle is used to help extend our current definitions for sine, cosine, and tangent to compliment for all angles of \(\theta\).
      </p>

      <BaseTitle> 
        Trigonometry and the Unit Circle
      </BaseTitle>

      <p>Main Notes:</p>
        <ul>
          <li>Cosine is the \(x\) component of a coordinate on the unit circle.</li>
          <li>Sine is the \(y\) component of a coordinate on the unit circle.</li>
          <li>Tangent is the \(y\) component of the coordinate where the \(x=1\) line intercepts the angle line.</li>
          <li>\(\tan \theta=\frac{\sin \theta}{\cos \theta}\)  (an alternate relationship for tangent)</li>
        </ul>

      <BaseImage width="medium">
        <img src="@/assets/images/MethodsUnit1/CosineAndSineRules/CosAndSin.02.svg">
      </BaseImage>

      <p>
        Visit the The Unit Circle section in the Cosine and Sine Rule’s playlist for a more in depth look at the unit circle.  <a href="#">Click here</a> to go straight there.
      </p>


    <!-- SECTION. Unit Circle in Radians -->
      <BaseTitle>
        The Unit Circle in Radians
      </BaseTitle>

      <p>
        We can interpret the unit circle in radians now that we are familiar with the concept of radian measure. To recap, radians are just a unit that we use to measure the size of an angle which has a different scale to degrees. This can be compared to how distance can be measured in both kilometres \((km)\) and miles \((mi)\). The great thing about radians is that its scaling system is optimised for the angles in a circle. The unit circle is used to define sine, cosine and tangent for any angle and because this definition is based on angles in a circle, it makes sense to talk about sine, cosine and tangent in radians. Using radians in these situations will make solutions to problems come out much nicer as a more appropriate scaling system is used.
        <br> <br>
        The graphic below shows the unit circle with coordinates at angles that are multiples of \(\frac{\pi}{6}\) and \(\frac{\pi}{4}\). The corresponding angles in degrees are also shown. Try to understand the relationship between the coordinates and the angles with sine, cosine and tangent.
      </p>

      <BaseImage width="medium">
        <img src="@/assets/images/MethodsUnit1/CosineAndSineRules/CosAndSin.02.svg">
      </BaseImage>

      <p>Reminder:</p>
        <ul>
          <li>Cosine is the \(x\) component of a coordinate on the unit circle.</li>
          <li>Sine is the \(y\) component of a coordinate on the unit circle.</li>
          <li>Tangent is related to both sine and cosine by \(\tan \theta=\frac{\sin \theta}{\cos \theta}\)</li>
        </ul>
        <br>
        <p>Visit the Radian Measure playlist for a more in depth look at the concept of radians.  <a href="#">Click here</a> go straight there.</p>

    <!-- SECTION. Exact Value Coordinates -->
      <BaseTitle>
        The Common Coordinates on the Unit Circle
      </BaseTitle>

      <p>
        We can interpret the unit circle in radians now that we are familiar with the concept of radian measure. To recap, radians are just a unit that we use to measure the size of an angle which has a different scale to degrees. This can be compared to how distance can be measured in both kilometres \((km)\) and miles \((mi)\). The great thing about radians is that its scaling system is optimised for the angles in a circle. The unit circle is used to define sine, cosine and tangent for any angle and because this definition is based on angles in a circle, it makes sense to talk about sine, cosine and tangent in radians. Using radians in these situations will make solutions to problems come out much nicer as a more appropriate scaling system is used.
        <br> <br>
        The graphic below shows the unit circle with coordinates at angles that are multiples of \(\frac{\pi}{6}\) and \(\frac{\pi}{4}\). The corresponding angles in degrees are also shown. Try to understand the relationship between the coordinates and the angles with sine, cosine and tangent.
      </p>

      <BaseImage width="medium">
        <img src="@/assets/images/MethodsUnit1/CosineAndSineRules/CosAndSin.02.svg">
      </BaseImage>

      <p>Reminder:</p>
        <ul>
          <li>Cosine is the \(x\) component of a coordinate on the unit circle.</li>
          <li>Sine is the \(y\) component of a coordinate on the unit circle.</li>
          <li>Tangent is related to both sine and cosine by \(\tan \theta=\frac{\sin \theta}{\cos \theta}\)</li>
        </ul>
        <p>Visit the Radian Measure playlist for a more in depth look at the concept of radians.  <a href="#">Click here</a> go straight there.</p>

      <BaseTitle>
        Deriving the Common Coordinates on the Unit Circle
      </BaseTitle>
  </div>
</template>

<script>
import renderMathInElement from 'katex/dist/contrib/auto-render.js' // katex render math in element functionality
import BaseTitle from '@/components/Utils/BaseTitle'
import BaseImage from '@/components/Utils/BaseImage'

export default {
  components: {
    BaseTitle,
    BaseImage
  },
  mounted() {
    renderMathInElement(this.$refs.renderMath)
  }
}
</script>
