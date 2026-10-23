+++
id = "sk-lem-pbc-p1-injective-fibre"
kind = "lemma"
title = "Acyclicity on the closed projective line"
order = 1575
lean = ["AlgebraicGeometry.Etale.subsingleton_H_projectiveLine_closedFibre_of_injective"]
uses = ["sk-thm-pbc-henselian-h0", "sk-lem-pbc-finite"]
tags = ["sketch"]
+++
Let $A$ be a strictly henselian local ring with maximal ideal $\mathfrak m$ and
residue field $k$. Set

$$
X=\mathbf P^1_A,\qquad X_0=\mathbf P^1_k,\qquad i:X_0\hookrightarrow X,
$$

and for a sheaf $G$ on $X_{\Et}$ write $G_0=i^{-1}G$.

If $r$ is a prime, not necessarily invertible on $A$, and $I$ is an injective sheaf of $\mathbf F_r$-modules on $X_{\Et}$, then
$H^q(X_0,I_0)=0$ for every $q>0$.
