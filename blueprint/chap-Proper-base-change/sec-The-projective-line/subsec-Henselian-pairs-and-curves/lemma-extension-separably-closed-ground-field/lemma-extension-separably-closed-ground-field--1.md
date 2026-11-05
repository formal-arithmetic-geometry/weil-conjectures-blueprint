+++
id = "lemma-extension-separably-closed-ground-field--1"
kind = "lemma"
title = "Passage from algebraically closed to separably closed fields"
name_showing = false
order = 364001
aliases = ["bp-r110-1"]
lean = ["AlgebraicGeometry.IsCurve.bijective_cohomologyMap_of_isSepClosed_of_isAlgClosed"]
uses = ["definition-torsion-sheaves"]
+++
Fix a commutative ring $\Lambda$. Suppose that for every extension
$K\subseteq K'$ of algebraically closed fields, every proper $K$-scheme
$D$ with $\dim D\leq1$, and every torsion sheaf $G$ of $\Lambda$-modules
on $D_{\acute{e}t}$, pullback induces an isomorphism

$$
H^q(D_{\acute{e}t},G)\xrightarrow{\sim}
H^q((D_{K'})_{\acute{e}t},G|)
\qquad(q\geq0).
$$

Then the same assertion holds for separably closed fields. More
explicitly, let $k\subseteq k'$ be separably closed fields, let $C$ be
proper over $k$ with $\dim C\leq1$, and let $F$ be a torsion sheaf of
$\Lambda$-modules on $C_{\acute{e}t}$. For any cartesian square with
vertical maps $C\to\operatorname{Spec}k$ and
$C'\to\operatorname{Spec}k'$, lower map
$\operatorname{Spec}k'\to\operatorname{Spec}k$, and upper map
$\iota':C'\to C$, the natural map

$$
H^q(C_{\acute{e}t},F)\xrightarrow{\sim}
H^q(C'_{\acute{e}t},\iota'^*F)
\qquad(q\geq0)
$$

is an isomorphism. Here torsion means torsion of the underlying abelian
groups of the geometric stalks, as in [definition-torsion-sheaves], and
all cohomology groups are computed after forgetting the module structure.
