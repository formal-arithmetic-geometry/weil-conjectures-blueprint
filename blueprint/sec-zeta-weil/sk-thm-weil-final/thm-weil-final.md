+++
id = "thm-weil-final"
kind = "theorem"
title = "Weil conjectures for a smooth proper variety"
order = 4154
lean = ["AlgebraicGeometry.Scheme.weil_conjectures"]
uses = ["def-weil-point-counts-zeta", "def-weil-smooth-proper-cohomological-family", "prop-euler-product", "thm-weil-final-betti", "thm-weil-final-functional-equation", "thm-weil-final-integrality", "thm-weil-final-rationality", "thm-weil-final-rh"]
+++
Let $k_0$ be a finite field with $q$ elements, let $X_0$ be a scheme over
$k_0$ whose structure morphism $X_0\to\Spec k_0$ is smooth of relative
dimension $d$, proper and geometrically integral, and let $Z(X_0,T)\in\mathbf Q[[T]]$
be its point-count zeta series. Then there are polynomials
$P_0,\dots,P_{2d}\in\mathbf Z[T]$ such that:

1. (*Factorization.*) $P_i(0)=1$ for every $i$, $P_0(T)=1-T$,
$P_{2d}(T)=1-q^dT$, and
$$
Z(X_0,T)\prod_{\substack{0\leq i\leq2d\\ i\text{ even}}}P_i(T)
=\prod_{\substack{0\leq i\leq2d\\ i\text{ odd}}}P_i(T)
\quad\text{in }\mathbf Q[[T]].
$$
1. (*Functional equation.*) For every $0\leq i\leq2d$, the multiset of
complex roots of $P_{2d-i}$ is the image of the multiset of complex roots
of $P_i$ under $z\mapsto(q^dz)^{-1}$; equivalently, $\alpha\mapsto q^d/\alpha$
maps the reciprocal roots of $P_i$ bijectively, with multiplicity, onto
those of $P_{2d-i}$.
1. (*Riemann hypothesis.*) For every $0\leq i\leq2d$, every complex root
$z$ of $P_i$ satisfies $|z|=q^{-i/2}$; equivalently, every reciprocal root
of $P_i$ has absolute value $q^{i/2}$.
