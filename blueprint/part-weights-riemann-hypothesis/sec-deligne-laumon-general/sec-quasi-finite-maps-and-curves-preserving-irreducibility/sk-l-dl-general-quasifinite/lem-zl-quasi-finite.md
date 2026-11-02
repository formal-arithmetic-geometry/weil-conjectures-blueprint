+++
id = "lem-zl-quasi-finite"
kind = "lemma"
title = "Quasi-finite direct images: exactness, weight bounds and purity"
order = 4277
lean = ["AlgebraicGeometry.isZero_higherLowerShriek_of_quasiFinite", "AlgebraicGeometry.WeilSheaf.isZero_higherLowerShriek_and_isMixedOfWeightsAtMost_of_quasiFinite", "AlgebraicGeometry.HasDirectImageWeightBound.of_locallyQuasiFinite", "AlgebraicGeometry.WeilSheaf.IsMixedOfWeightsAtMost.higherLowerShriek_zero_of_quasiFinite", "AlgebraicGeometry.WeilSheaf.HasWeightsAtMost.higherLowerShriek_zero_of_quasiFinite", "AlgebraicGeometry.WeilSheaf.IsPunctuallyPureOfWeight.higherLowerShriek_zero_of_quasiFinite"]
uses = ["def-weil-complex-weights", "def-weil-punctual-weights", "def-weil-weil-sheaf-complex", "det-def-sfb-bounded-constructible", "prop-functor-package", "sk-def-sf-weil-complexes", "det-def-sfb-module-lower-shriek", "sk-lem-coefficient-heart", "sk-d-real-weights"]
+++
Let $g:Z_0\to Y_0$ be a separated, quasi-finite morphism of finite type
of $k_0$-schemes, with $Y_0$ separated of finite type over $k_0$.
Let $\mathcal F$ be a constructible $\Qlb$-Weil sheaf on $Z_0$, i.e. an
object of $\Cons(Z,\Qlb)$ ([sk-lem-coefficient-heart]) with a Weil
structure ([def-weil-weil-sheaf-complex]), and let $w\in\mathbf R$.

1. $R^ig_!\mathcal F=0$ for every $i>0$.
1. $Rg_!$ carries $D_{\le w}(Z_0)$ into $D_{\le w}(Y_0)$
   ([def-weil-complex-weights]); here $D_{\le w}$ consists of Weil
   complexes with underlying object in $\Dbc(-,\Qlb)$
   ([det-def-sfb-bounded-constructible], [sk-def-sf-weil-complexes]).
1. If $\mathcal F$ is $\iota$-mixed of weights at most $w$, then so is
   $g_!\mathcal F=R^0g_!\mathcal F$.
1. If every local Frobenius eigenvalue of $\mathcal F$ at every closed
   point has weight at most $w$, then the same holds for
   $g_!\mathcal F$.
1. If $\mathcal F$ is punctually $\iota$-pure of weight $w$
   ([def-weil-punctual-weights]), then so is $g_!\mathcal F$. In
   particular, for a finite map $g$ the direct image $g_*\mathcal F$ of a
   punctually pure sheaf of weight $w$ is punctually pure of weight $w$.
