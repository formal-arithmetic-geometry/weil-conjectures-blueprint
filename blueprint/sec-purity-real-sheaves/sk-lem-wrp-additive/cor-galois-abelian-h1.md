+++
id = "cor-galois-abelian-h1"
kind = "theorem"
title = "Abelian case: torsors, characters and $H^1$"
lean = ["AlgebraicGeometry.Scheme.EtaleTorsor.existsUnique_fiber_map_vaddHom", "AlgebraicGeometry.Scheme.EtaleTorsor.monodromy", "AlgebraicGeometry.Scheme.EtaleTorsor.fiber_map_vaddHom_monodromy", "AlgebraicGeometry.Scheme.EtaleTorsor.monodromy_eq_of_isIsomorphic", "AlgebraicGeometry.Scheme.EtaleTorsor.isIsomorphic_of_monodromy_eq", "AlgebraicGeometry.Scheme.EtaleTorsor.exists_monodromy_eq", "AlgebraicGeometry.Scheme.EtaleTorsor.bijective_monodromy", "AlgebraicGeometry.Scheme.EtaleTorsor.monodromy_eq_of_classH1_eq", "AlgebraicGeometry.Scheme.EtaleTorsor.sheafHEquivContinuousMonoidHom", "AlgebraicGeometry.Scheme.EtaleTorsor.exists_equiv_sheafH_continuousMonoidHom", "AlgebraicGeometry.Scheme.EtaleTorsor.sheafHEquivContinuousMonoidHom_map"]
order = 3822
uses = ["def-galois-fibre-functor", "def-weil-pbc-finite-torsors", "lem-galois-axioms", "thm-galois-fundamental", "sbc-prop-torsors-h1", "thm-galois-torsor-h1"]
tags = ["latex:corollary"]
+++
Let $Y$ be connected with geometric point $\bar y$ and let $M$ be a
finite abelian group. Then there is a canonical bijection

$$
H^1(Y_{\Et},\underline M)\xrightarrow{\ \sim\ }
\operatorname{Hom}_{\mathrm{cont}}\bigl(\pi_1(Y,\bar y),M\bigr),
$$

given on torsors by choosing $p\in P_{\bar y}$ — a simply transitive
$M$-set — and sending $P$ to the continuous homomorphism $f_P$ with

$$
g\cdot p=p+f_P(g)\qquad(g\in\pi_1(Y,\bar y));
$$

the class of $P$ is independent of the choice of $p$ because $M$ is
abelian.
