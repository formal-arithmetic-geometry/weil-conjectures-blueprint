+++
kind = "proof"
of = "lemma-finite-quasi-finite-direct-images--1"
order = 1321004
uses = ["lemma-finite-morphisms", "proposition-composition-base-change-rf-shriek", "lemma-finite-quasi-finite-direct-images--3", "lemma-weights-exact-sequence", "proposition-weights-under-usual-operations"]
+++
Zariski's main theorem factors $g$ as a quasi-compact open immersion
$j:Z_0\hookrightarrow T_0$ followed by a finite morphism $p:T_0\to Y_0$.
The composition isomorphism of
[proposition-composition-base-change-rf-shriek] and the identification
of proper direct image with direct image with compact support give
$Rg_!F\simeq Rp_*j_!F$. Extension by zero is exact, and finite direct
image is exact by [lemma-finite-morphisms] and the comparison of
coefficients. Thus the higher direct images vanish. This is the
argument of `AlgebraicGeometry.isZero_higherLowerShriek_of_quasiFinite`.

Extension by zero preserves purity: its stalks are the original stalks
on the open and zero elsewhere. Applying it to a mixed filtration
therefore preserves mixedness and its upper bound. For the finite
direct image, Lean uses
`AlgebraicGeometry.WeilComplex.IsMixedOfWeightsAtMost.derivedLowerStar_of_isFinite`.
This reduces complexes to sheaves by truncation triangles and then
inducts on a mixed filtration. A pure quotient retains its weight by
[lemma-finite-quasi-finite-direct-images--3]; its derived finite direct
image is concentrated in degree zero. The triangles coming from the
filtration preserve the bound by [lemma-weights-exact-sequence].
Apply this to $j_!F$ in degree zero and transport the bound through
$Rg_!F\simeq Rp_*j_!F$. Taking degree-zero cohomology gives the assertion
on $R^0g_!F$, as in
`AlgebraicGeometry.WeilSheaf.IsMixedOfWeightsAtMost.higherLowerShriek_zero_of_quasiFinite`.
