+++
id = "thm-galois-fundamental"
kind = "theorem"
title = "The fibre functor is an equivalence"
lean = ["AlgebraicGeometry.Scheme.FiniteEtale.equivalenceContAction", "AlgebraicGeometry.Scheme.FiniteEtale.equivalenceContAction_functor_obj_obj_V", "AlgebraicGeometry.Scheme.FiniteEtale.equivalenceContAction_functor_obj_obj_\u03c1_apply", "AlgebraicGeometry.Scheme.FiniteEtale.equivalenceContAction_functor_map_hom_hom"]
order = 984
uses = ["def-galois-fibre-functor", "lem-fet-galois-category", "lem-galois-aut-profinite", "lem-galois-transitive", "thm-galois-abstract-equivalence", "thm-galois-lc-etale"]
+++
Let $Y$ be connected with a geometric point $\bar y\to Y$. Then the
fibre functor induces an equivalence

$$
F_{\bar y}:\mathrm{F\acute Et}(Y)\xrightarrow{\ \sim\ }
\pi_1(Y,\bar y)\text{-}\mathbf{Set},
$$

and likewise on $\mathrm{FLC}(Y)$ under the identification of
[thm-galois-lc-etale], where
$\pi_1(Y,\bar y)=\operatorname{Aut}(F_{\bar y})$ carries the profinite
topology of [def-galois-fibre-functor]. The equivalence is compatible
with finite limits and colimits, and with base change along $Y'\to Y$ for
$Y'$ connected, where it corresponds to the passage to the open subgroup
of the fundamental group.
