+++
id = "lem-sp-shift-identification"
kind = "lemma"
title = "Shift rule for derived functors"
order = 2110
lean = ["CategoryTheory.Functor.exists_rightDerived_shift_identification", "CategoryTheory.Functor.exists_rightDerived_shift_identification_nonneg", "CategoryTheory.Functor.isZero_rightDerived_shift_identification"]
uses = ["def-sp-kinjective-bridge", "def-sp-left-exact-additive", "lem-sp-kinjective-computes", "lem-weil-pbc-derived-functor-negative-vanishing"]
+++
Let $\mathcal A,\mathcal B$ be abelian categories, $\mathcal A$ with enough
injectives, let $v:\mathcal A\to\mathcal B$ be a left exact additive
[def-sp-left-exact-additive] functor, let
$K\in\operatorname{Ch}^+(\mathcal A)$ and let $q\in\mathbb Z$. Write
$\mathcal H^qK$ for the object $\mathcal H^q(K)$ placed in degree $0$. Then
the derived functor commutes with the shift and the cohomology of a shifted
complex is the shifted cohomology: for every $p\in\mathbb Z$ there are
isomorphisms, natural in $K$,

$$
 \mathcal H^{p+q}\bigl(Rv(\mathcal H^qK[-q])\bigr)
 \cong\mathcal H^{p}\bigl(Rv(\mathcal H^qK)\bigr),
$$

and for $p\geq0$ the right-hand side is identified naturally with
$R^pv(\mathcal H^q(K))$. For $p<0$ both sides vanish.
