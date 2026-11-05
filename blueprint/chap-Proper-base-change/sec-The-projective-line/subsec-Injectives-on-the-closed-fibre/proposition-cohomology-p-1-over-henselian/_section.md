+++
id = "proposition-cohomology-p-1-over-henselian"
kind = "proposition"
title = "Cohomology of $\\mathbf P^1$ over henselian rings"
order = 375
lean = ["AlgebraicGeometry.Etale.bijective_cohomologyMap_projectiveLine_residueField"]
uses = ["definition-torsion-sheaves"]
+++
Let $R$ be a henselian local ring with residue field $\kappa$. For every
torsion abelian sheaf $F$ on $\mathbf P^1_{R,\acute{e}t}$, restriction
induces isomorphisms, natural in $F$, with
$F_0=i^*F$,

$$
H^q(\mathbf P^1_R,F)\xrightarrow{\sim}
H^q(\mathbf P^1_\kappa,F_0)\qquad(q\geq0).
$$
