+++
id = "lemma-finite-morphisms--1"
kind = "lemma"
title = "Finite morphisms (1)"
name_showing = false
order = 384001
aliases = ["bp-r116-1"]
lean = ["AlgebraicGeometry.Etale.lowerStarSheafFiberIsoPi", "AlgebraicGeometry.Scheme.Hom.GeometricFiber.finite"]
uses = []
+++
Let $A$ be a Grothendieck abelian category admitting sheafification on small
sites, and let $u:V\to W$ be finite. For an $A$-valued sheaf $F$ on
$V_{\acute{e}t}$ and a geometric point
$\bar w:\operatorname{Spec}(\Omega)\to W$, with $\Omega$ algebraically
closed, one has

$$
(u_*F)_{\bar w}
\simeq \prod_{\substack{\bar v:\operatorname{Spec}(\Omega)\to V\\
u\bar v=\bar w}}F_{\bar v}.
$$

The isomorphism is natural in $F$, and its components are the restriction
maps on germs. The product is finite. In particular, this applies to
abelian sheaves and to sheaves of modules over a constant coefficient ring.
