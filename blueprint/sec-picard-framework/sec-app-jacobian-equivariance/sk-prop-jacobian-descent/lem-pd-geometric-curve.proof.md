+++
kind  = "proof"
of    = "lem-pd-geometric-curve"
+++
Smoothness and projectivity of a morphism are stable under base change
([def-pc-base-change]), so $C_{k_s}$ is a
[def-pc-smooth-projective-curve] over $k_s$, and $k_s$ is separably closed
by [def-pd-separable-closure]. Geometric
integrality of $C_{k_s}$ over $k_s$ means that $C_{k_s}\times_{k_s}\bar k_s$ is
integral for an algebraic closure $\bar k_s$ of $k_s$
([def-pc-geometrically-irreducible]); that scheme is the base change
$C_{\bar k_s}$ along the composite $k\hookrightarrow k_s\hookrightarrow\bar k_s$,
and it is integral because $C$ is *geometrically* integral over $k$ and
integrality is preserved by base change along a field extension. Finally
$\dim C_{k_s}=\dim C=1$ and $g(C_{k_s})=g(C)$ for the
[def-pc-genus], by [lem-pc-dim-base-change] applied to the flat
extension $k\subseteq k_s$ and to $\mathcal{O}_C$.
