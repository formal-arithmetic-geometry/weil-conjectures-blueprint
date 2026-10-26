+++
id = "thm-galois-lc-etale"
kind = "theorem"
title = "Finite locally constant sheaves and finite etale schemes"
lean = ["AlgebraicGeometry.Scheme.FiniteEtale.toFLC", "AlgebraicGeometry.Scheme.exists_finiteEtale_flc_equivalence", "AlgebraicGeometry.Scheme.finiteEtale_flc_preserves_torsors", "AlgebraicGeometry.Scheme.EtaleTorsor.exists_toSheafTorsor_equiv_of_iso"]
order = 1374
uses = ["def-galois-categories", "def-weil-pbc-finite-torsors", "lem-fet-locally-trivial", "lem-galois-descent"]
+++
In the situation of [def-galois-categories], the functor

$$
\mathrm{F\acute Et}(Y)\longrightarrow\mathrm{FLC}(Y),\qquad
P\longmapsto\underline{\operatorname{Hom}}_Y(-,P),
$$

where $\underline{\operatorname{Hom}}_Y(T,P)$ is the set of
$Y$-morphisms $T\to P$, is an equivalence of categories. It is
compatible with base change along every morphism $Y'\to Y$ and with the
fibre functors at geometric points with algebraically closed field, and,
for a finite abelian group $M$, it carries
finite etale $Y$-schemes $P$ which are surjective over $Y$ and carry a
simply transitive $M$-action ($\underline M\times P\to P\times_YP$ an
isomorphism) to the $M$-torsors of [def-weil-pbc-finite-torsors], and
conversely.
