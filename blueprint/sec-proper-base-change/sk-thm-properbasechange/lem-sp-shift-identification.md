+++
id = "lem-sp-shift-identification"
kind = "lemma"
title = "Shift rule for derived functors"
order = 1260
uses = ["def-sp-kinjective-bridge", "def-sp-left-exact-additive", "lem-sp-kinjective-computes"]
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
