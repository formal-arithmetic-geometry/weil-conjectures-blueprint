+++
id = "def-sbc-normal-dominant-galois"
kind = "definition"
title = "Integral, normal, dominant, Galois covers, and geometric connectedness"
order = 5107
lean = ["AlgebraicGeometry.Scheme.IsIntegral", "AlgebraicGeometry.Scheme.IsNormal", "AlgebraicGeometry.IsDominant", "AlgebraicGeometry.IsGaloisCover"]
+++
A scheme $S$ is *integral* if it is nonempty, reduced, and irreducible; it is
*normal* if it is integral and the local ring at every point is a normal
domain (a domain integrally closed in its fraction field). A morphism
$f:X\to Y$ is *dominant* if $f(X)$ is dense in $Y$.

A finite étale morphism $\pi:Z\to C$ is a *Galois cover with group $G$* if
$G$ acts on $Z$ over $C$ by finite étale automorphisms, the quotient is
$Z/G\cong C$, and $Z\to C$ is a $G$-torsor (the action is simply transitive
on every geometric fibre); the *deck group* of a Galois cover is the group of
its automorphisms over $C$. For a Galois cover with connected total space
this group is $G$, as [sbc-lem-galois-deck-group] records.

A morphism $f:X\to S$ has *geometrically connected fibres* if for every point
$s\in S$ the fibre $X_s$ is geometrically connected over $\kappa(s)$ (its
base change to every separably closed extension of $\kappa(s)$ is
connected). It has *geometrically reduced fibres* if for every point $s\in S$
the fibre $X_s$ is reduced after every separably closed extension of
$\kappa(s)$; equivalently, the corresponding property holds at every
geometric point.

Unresolved dependencies: def:weil-pbc-scheme-conventions
