+++
kind = "proof"
of = "proposition-dctf-x-qbar-2-colimit--3"
order = 648004
uses = ["lemma-continuity-ext-out-constructible-complex", "definition-sp-scalar-extension"]
+++
For (1), choose a finite field containing $E$ and $F$, and let $H$ run
over the finite subextensions containing it. This is a cofinal filtered
system. After restriction to $E_X$, the complex
$L_{\overline{\mathbf Q}_\ell}$ is represented by the filtered colimit
of complexes representing the $L_H$, with a common termwise lower
bound. The presentation and its compatibility with the scalar-extension
adjunctions are supplied by
`AlgebraicGeometry.ProEtale.exists_condensed_coefficient_complex_presentation`.

The continuity argument of [lemma-continuity-ext-out-constructible-complex]
is used first for a constructible module in degree zero, in every shift:
this is `AlgebraicGeometry.ProEtale.isIso_constructible_condensed_sheaf_hom_colimit`.
Dévissage along the finite cohomology tower of $K$ extends it to $K$,
using `AlgebraicGeometry.ProEtale.prop_of_boundedConstructibleModule`.
The adjoint of the given morphism therefore factors through one finite
stage. Transpose that factorization back by the extension-restriction
adjunction at that stage. Compatibility with transitivity of scalar
extension identifies its image with the original morphism.

For (2), the inclusion $H_X\to\overline{\mathbf Q}_{\ell,X}$ has an
$H_X$-linear retraction. It makes the unit of the derived
extension-restriction adjunction a monomorphism, so extension of scalars
is faithful, by
`AlgebraicGeometry.ProEtale.faithful_derivedExtendScalarsToPadicAlgCl`.
Thus $g=g'$ already over $H$; take $H'=H$.

Surjectivity in the displayed colimit follows from (1) with the same
initial field for both objects. For injectivity, move two representatives
to a common finite stage and apply (2).
