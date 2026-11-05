+++
kind = "proof"
of = "corollary-trace-functions-direct-image-compact--1"
order = 1024002
uses = ["lemma-finite-morphisms", "proposition-composition-base-change-rf-shriek", "proposition-extension-zero-restriction-closed-subscheme", "proposition-properties-trace", "theorem-proper-pushforward-lefschetz-verdier", "proposition-frobenius-local-term-curve"]
+++
First establish the formula for finite étale morphisms, closed immersions,
and relative affine lines. In the finite étale case the stalk of the
direct image is a finite sum of stalks, as in [lemma-finite-morphisms].
Frobenius permutes the summands, and only the fixed summands contribute to
the trace. For a closed immersion, compactly supported base change
([proposition-composition-base-change-rf-shriek]) gives the original stalk
on the image and zero off the image. For a relative affine line, factor
the projection through the open immersion into the relative projective
line. The formula for the latter follows on each geometric fibre from
[theorem-proper-pushforward-lefschetz-verdier] and the Frobenius local-term
calculation [proposition-frobenius-local-term-curve]. These are the base
cases `shriekTraceFunctionAt_of_isFinite_of_etale`,
`shriekTraceFunctionAt_of_isClosedImmersion`, and
`shriekTraceFunctionAt_overProdMap_polyAffineProj` in the namespace
`AlgebraicGeometry.ProEtale.CondensedRing`.

The finite order of $e_X$ gives a nonempty stable open in every nonempty
source whose reduction has a finite étale map to an affine quotient.
Factor the map from this reduction to $Y_0$ through its graph, the finite
étale quotient, a closed embedding into affine space, and the coordinate
projections. The image lies in the fixed locus of a positive power of
$e_Y$, so the intervening automorphisms have finite order. Composition
of the base cases gives the formula on this reduction. Open–closed
dévissage then gives it on the stable open, proving
`shriekTraceFunctionGenericallyHolds`.

Now use Noetherian induction on the ranges of stable closed subschemes
of $X_0$. The empty scheme has no points and all its complexes are zero.
For a nonempty stable closed subscheme, choose the stable open just
constructed. Its reduced closed complement has strictly smaller range,
so the induction hypothesis applies there. The localization triangle
from [proposition-extension-zero-restriction-closed-subscheme], the
composition isomorphisms for $Rf_!$, and additivity of the alternating
trace ([proposition-properties-trace]) add the formulas on the two
pieces. This is `shriekTraceFunctionAt_of_isCompl`; the resulting
induction is `weilShriekTraceFunction_of_genericallyHolds`.

Finally write $m=n+1$ and the positive order of $e_X$ as $s+1$, apply
that induction theorem with `shriekTraceFunctionGenericallyHolds`, and
replace the finitely supported sum by the finite sum over the fibre.
The finiteness is supplied by `fintypeFrobeniusFixedPoints`, and the last
conversion is `finsum_eq_sum_of_fintype`. This proves
`weilShriekTraceFunction`; the absolute formula is subsequently obtained
by taking $Y_0=\operatorname{Spec}k$.
