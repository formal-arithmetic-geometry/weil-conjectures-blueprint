+++
id = "lemma-sheaves-finite-support-finite-morphisms--1"
kind = "lemma"
title = "Finite support and zero-dimensional cohomology"
name_showing = false
order = 1597001
aliases = ["bp-r498-1"]
lean = ["AlgebraicGeometry.Etale.subsingleton_H_of_isZero_upperStar", "AlgebraicGeometry.zero_dimensional_etale_cohomology"]
uses = []
+++
Let $X$ be a scheme and $U\subset X$ an open subset whose complement
is a finite set of closed points with separably closed residue fields.
If $F$ is an abelian sheaf on $X_{\acute{e}t}$ with $F|_U=0$, then
$H^q(X,F)=0$ for every $q>0$.

Let $C$ be a separated scheme of finite type over an algebraically
closed field $k$, with $\dim C\leq0$. Then $C$ has finitely many points.
For every abelian sheaf $G$ on $C_{\acute{e}t}$ one has $H^q(C,G)=0$
for $q>0$. Choose, for each $x\in C$, a geometric point
$s_x:\operatorname{Spec}\Omega_x\to C$ with image $x$, where $\Omega_x$
is algebraically closed. The canonical map given by germs of sections
is an isomorphism

$$
H^0(C,G)\xrightarrow{\ \sim\ }\prod_{x\in C}G_{s_x}.
$$

Since $C$ is finite, this product is also the direct sum of these stalks.
