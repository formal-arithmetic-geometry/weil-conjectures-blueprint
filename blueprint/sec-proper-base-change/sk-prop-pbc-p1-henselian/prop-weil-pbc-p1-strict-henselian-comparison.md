+++
id = "prop-weil-pbc-p1-strict-henselian-comparison"
kind = "theorem"
title = "Strictly henselian $\\mathbf P^1$ comparison"
lean = ["AlgebraicGeometry.Etale.bijective_cohomologyMap_projectiveLine_residueField"]
order = 1587
tags = ["latex:proposition"]
uses = ["def-weil-pbc-etale-sheaves", "def-weil-pbc-strict-henselian-setup", "lemma-weil-pbc-etale-degree-zero", "prop-weil-pbc-p1-acyclicity", "def-weil-pbc-torsion-etale-sheaf"]
+++
Let $A$ be a strictly henselian local ring with residue field $\kappa$, and in the
setup of [def-weil-pbc-strict-henselian-setup] let $X=\mathbf P^1_A$ with closed
fibre $X_0=\mathbf P^1_\kappa$. Let $\Lambda$ be a commutative ring. For every
sheaf $F$ of $\Lambda$-modules on $X_{\Et}$ which is torsion
[def-weil-pbc-torsion-etale-sheaf], restriction gives isomorphisms

$$
 H^q(X,F)\xrightarrow{\sim}H^q(X_0,F_0)
 \qquad(q\geq0).
$$
