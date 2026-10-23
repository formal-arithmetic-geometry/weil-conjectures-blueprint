+++
id = "thm-galois-fundamental"
kind = "theorem"
title = "The fibre functor is an equivalence"
lean = ["AlgebraicGeometry.Scheme.FiniteEtale.equivalenceContAction", "AlgebraicGeometry.Scheme.FiniteEtale.equivalenceContAction_functor_obj_obj_V", "AlgebraicGeometry.Scheme.FiniteEtale.equivalenceContAction_functor_obj_obj_\u03c1_apply", "AlgebraicGeometry.Scheme.FiniteEtale.equivalenceContAction_functor_map_hom_hom"]
order = 1409
uses = ["def-galois-fibre-functor", "lem-fet-galois-category", "lem-galois-aut-profinite", "thm-galois-abstract-equivalence", "thm-galois-lc-etale"]
+++
Let $Y$ be connected with a geometric point
$\bar y:\operatorname{Spec}\Omega\to Y$, $\Omega$ separably closed, and
let $\pi_1(Y,\bar y)$ be a fundamental group of $F_{\bar y}$ as in
[def-galois-fibre-functor] (for instance
$\operatorname{Aut}(F_{\bar y})$). Then the fibre functor induces an
equivalence

$$
F_{\bar y}:\mathrm{F\acute Et}(Y)\xrightarrow{\ \sim\ }
\pi_1(Y,\bar y)\text{-}\mathbf{Set},
$$

sending $P$ to the finite set $|P_{\bar y}|$ with the given action of
$\pi_1(Y,\bar y)$ and a morphism to the induced map of geometric
fibres. Composing with the equivalence of [thm-galois-lc-etale], the
same holds for $\mathrm{FLC}(Y)$ in place of $\mathrm{F\acute Et}(Y)$.
Being an equivalence, it is compatible with finite limits and colimits.
