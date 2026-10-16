+++
id = "pqf-lem-leray-lowdegree"
kind = "lemma"
title = "Low degree terms of the Leray spectral sequence"
lean = ["AlgebraicGeometry.Scheme.Modules.exists_leray_lowDegree_exact", "AlgebraicGeometry.Scheme.Modules.nonempty_rightDerived_one_iso_of_isZero"]
order = 549
uses = ["pqf-def-cohomology", "pqf-lem-leray"]
+++
Let $f:X\to Y$ be a morphism of schemes and $\mathcal F$ a
quasi-coherent $\mathcal O_X$-module. The low degree terms of the
spectral sequence of [pqf-lem-leray] give an exact sequence

$$
0\longrightarrow\mathrm H^1(Y,f_*\mathcal F)
\longrightarrow\mathrm H^1(X,\mathcal F)
\longrightarrow\mathrm H^0(Y,R^1f_*\mathcal F)
\longrightarrow\mathrm H^2(Y,f_*\mathcal F).
$$

In particular, if $R^1f_*\mathcal F=0$, then
$\mathrm H^1(X,\mathcal F)\cong\mathrm H^1(Y,f_*\mathcal F)$.
