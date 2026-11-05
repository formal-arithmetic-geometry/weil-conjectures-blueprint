+++
kind = "proof"
of = "proposition-fourier-transform-perverse-heart--3"
order = 1260006
uses = ["proposition-fourier-inversion", "proposition-fourier-transform-perverse-heart--2"]
+++
Fourier inversion gives an equivalence on Weil complexes, and
[proposition-fourier-transform-perverse-heart--2] identifies the inverse
image of the curve perverse object property with that same property.
Restrict the equivalence to these full subcategories. In Lean this is
the application of `congrFullSubcategory`
inside the proof of `AlgebraicGeometry.simple_fourierTransform_obj`;
the restricted equivalence then preserves simple objects. No separate
exactness or Frobenius-descent argument enters this step.
