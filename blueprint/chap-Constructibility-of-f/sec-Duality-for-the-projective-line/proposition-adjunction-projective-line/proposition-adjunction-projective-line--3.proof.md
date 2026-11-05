+++
kind = "proof"
of = "proposition-adjunction-projective-line--3"
order = 553004
uses = ["proposition-adjunction-projective-line--1", "lemma-cohomology-projective-line-trace", "definition-projection-formula-map", "proposition-composition-base-change-rf-shriek", "proposition-forgetting-supports-composition"]
+++
First transport base change for the projective-line trace through
$Rp_!\simeq Rp_*$, using the trace convention $t_p=-\operatorname{Tr}_p$ of
[proposition-adjunction-projective-line--1]. Base change for the trace
in [lemma-cohomology-projective-line-trace] also holds after negation.
This identifies the pullback of $t_p$ with compact-support base
change followed by the Tate-object comparison and $t_{p'}$.

Expand both counits as the inverse projection map followed by the trace.
The projection map commutes with base change, and the identification
$p^*K(1)[2]\simeq\Lambda(1)[2]\otimes_\Lambda^{\mathbf L}p^*K$ commutes with
pullback. Combining these squares with the trace square gives the claimed
equality. This is
`AlgebraicGeometry.Etale.lowerShriekTraceCounit_twistShift_baseChange`
with twist $1$.

For a normalized Tate twist, choose a normalized Kummer class inducing
it. Apply [proposition-adjunction-projective-line--1] over $S$ and $S'$,
then replace their counits by the trace counits. The equality just proved
supplies the compatibility in
`AlgebraicGeometry.Etale.projectiveLineAdjunctionBaseChange_of_isNormalized`.
