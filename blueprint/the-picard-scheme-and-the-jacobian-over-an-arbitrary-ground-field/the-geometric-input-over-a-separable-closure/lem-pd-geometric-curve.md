+++
id = "lem-pd-geometric-curve"
kind = "lemma"
title = "The geometric curve is a smooth projective geometrically integral curve"
order = 4710
lean = ["AlgebraicGeometry.Curve.baseChange_sepClosure_isSmoothProjective"]
uses = ["def-pd-separable-closure"]
+++
Let $k$ be a field and let $C$ be a smooth projective curve over $k$ which is
geometrically integral, of genus $g$. Then for a separable closure $k_s$
[def-pd-separable-closure] of $k$ the base change $C_{k_s}$ is a smooth
projective curve over the separably closed field $k_s$ which is
geometrically integral, of genus $g$.

## Proof

Smoothness and projectivity of a morphism are stable under base change, so
$C_{k_s}$ is a smooth projective curve over $k_s$, and $k_s$ is separably
closed by [def-pd-separable-closure].

Geometric integrality of $C_{k_s}$ over $k_s$ means that
$C_{k_s}\times_{k_s}\bar k_s$ is integral for an algebraic closure
$\bar k_s$ of $k_s$; that scheme is the base change $C_{\bar k_s}$ along the
composite $k\hookrightarrow k_s\hookrightarrow\bar k_s$, and it is integral
because $C$ is *geometrically* integral over $k$ and integrality is preserved
by base change along a field extension.

Finally $\dim C_{k_s}=\dim C=1$ and $g(C_{k_s})=g(C)$, by the base-change
invariance of the dimension and of coherent cohomology applied to the flat
extension $k\subseteq k_s$ and to $\mathcal{O}_C$.

Unresolved dependencies: def:pc-smooth-projective-curve, def:pc-geometrically-irreducible, def:pc-genus, def:pc-base-change, lem:pc-dim-base-change
