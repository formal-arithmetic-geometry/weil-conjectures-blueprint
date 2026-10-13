+++
id = "def-sfb-rationalization-quotient"
kind = "definition"
title = "The rationalization"
order = 1635
uses = ["def-sfb-rationalization-morphisms", "lem-sfb-torsion-triangulated"]
lean = ["CategoryTheory.Rationalization", "CategoryTheory.Rationalization.Q"]
+++
Let $\mathcal T$ be a triangulated category that is linear over a commutative ring $R$,
with $R$-linear shift functors, and let $M\subseteq R$ be a submonoid. The
*rationalization* $\mathcal T[M^{-1}]$ is the localization of $\mathcal T$ at the class
$W_M$ of [def-sfb-rationalization-morphisms], i.e. the Verdier quotient of $\mathcal T$ by
the triangulated subcategory of $M$-torsion objects [lem-sfb-torsion-triangulated]. It is
a triangulated category, and the localization functor
$Q\colon\mathcal T\to\mathcal T[M^{-1}]$ is triangulated.
