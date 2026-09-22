+++
id = "lem-sp-shift-identification"
kind = "lemma"
title = "Shift rule for derived functors"
order = 1731
lean = ["CategoryTheory.Functor.rightDerived_shift"]
uses = ["def-sp-left-exact-additive"]
+++
Let $v$ be a left exact additive [def-sp-left-exact-additive] functor, let
$K\in\operatorname{Ch}^+(\mathcal A)$ and let $q\in\mathbb Z$. Then the
derived functor commutes with the shift and the cohomology of a shifted
complex is the shifted cohomology:

$$
 \mathcal H^{p+q}\bigl(Rv(\mathcal H^qK[-q])\bigr)
 =\mathcal H^{p}\bigl(Rv(\mathcal H^qK)\bigr)
 =R^pv(\mathcal H^qK).
$$

## Proof

The derived functor of a left exact additive functor on
$\operatorname{Ch}^+$ is computed by applying the functor to a K-injective
resolution in the sense of [def-sp-kinjective-bridge]; K-injective complexes
are closed under shift, so the derived functor commutes with the shift
([def-sp-left-exact-additive]). Consequently the cohomology of the shifted
complex is the shifted cohomology, which is exactly the first displayed
identity; the second displayed identity is the definition $R^pv=\mathcal
H^p\circ Rv$ of [def-sp-left-exact-additive].
