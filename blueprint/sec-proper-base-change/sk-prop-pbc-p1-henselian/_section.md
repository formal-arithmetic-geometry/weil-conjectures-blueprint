+++
id = "sk-prop-pbc-p1-henselian"
kind = "proposition"
title = "Henselian comparison for the projective line"
order = 1692
lean = ["AlgebraicGeometry.Etale.bijective_cohomologyMap_projectiveLine_residueField"]
uses = ["sk-lem-pbc-p1-injective-fibre", "sk-thm-pbc-henselian-h0"]
tags = ["sketch"]
+++
For a strictly henselian local ring $A$ with residue field $k$ and any torsion
abelian sheaf (or torsion sheaf of $\Lambda$-modules) $F$ on $\mathbf P^1_A$, restriction induces natural isomorphisms

$$
H^q(\mathbf P^1_A,F)\xrightarrow{\ \sim\ }H^q(\mathbf P^1_k,F_0)
\qquad(q\geq0).
$$
