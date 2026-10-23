+++
id = "prop-weil-pbc-p1-acyclicity"
kind = "theorem"
title = "Acyclicity on the closed projective line"
lean = ["AlgebraicGeometry.Etale.subsingleton_H_projectiveLine_closedFibre_of_injective_of_one_lt", "AlgebraicGeometry.Etale.subsingleton_H_projectiveLine_closedFibre_of_injective"]
order = 1584
uses = ["def-weil-pbc-strict-henselian-setup", "lemma-weil-pbc-finite-direct-image-exact", "lemma-weil-pbc-finite-exchange", "lemma-weil-pbc-h1-constructible-representation", "lemma-weil-pbc-h1-torsor-comparison", "lemma-weil-pbc-injective-restriction-acyclicity"]
tags = ["latex:proposition"]
+++
Let $A$ be a strictly henselian local ring with residue field $\kappa$, and in the
setup of [def-weil-pbc-strict-henselian-setup] let $X=\mathbf P^1_A$ with closed
fibre $X_0=\mathbf P^1_\kappa$. For a prime $r$ and every injective sheaf $I$ of
$\mathbf F_r$-modules on $X_{\Et}$, the restriction $I_0$ is
$\Gamma(X_0,-)$-acyclic:

$$
 H^q(X_0,I_0)=0\qquad(q>0).
$$
