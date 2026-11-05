+++
id = "lemma-cohomology-modules-underlying-abelian--1"
kind = "remark"
title = "Acyclicity after forgetting coefficients"
name_showing = false
order = 312001
aliases = ["bp-r092-1"]
lean = ["AlgebraicGeometry.Scheme.isZero_rightDerived_globalSections_forget_of_injective"]
uses = []
+++
Let $X$ be a scheme, $\Lambda$ a commutative ring, and $I$ an injective
sheaf of $\Lambda$-modules on $X_{\acute{e}t}$. Write $I_{\mathrm{ab}}$
for its underlying abelian sheaf. Then

$$
R^{n+1}\Gamma(X_{\acute{e}t},I_{\mathrm{ab}})=0
\qquad(n\geq 0).
$$

To prove this, identify sheaves of $\Lambda$-modules with modules over
the constant ring sheaf. This equivalence preserves injectivity and
the underlying abelian sheaf. Exact sheafification makes the underlying
module presheaf of $I$ injective. The free module Čech chain complex of
a covering is exact in positive degrees; applying $\Hom(-,I)$ shows
that every positive Čech cocycle is a boundary. Forgetting coefficients
leaves the section groups, restriction maps, and differentials unchanged.

Apply the abelian Čech vanishing criterion using all étale objects and
all covering families. The collection is closed under the fibre
products in the Čech nerve, and each covering refines itself. Thus
positive derived evaluation of $I_{\mathrm{ab}}$ vanishes on every
étale object. Evaluation at the terminal object $X\to X$ is global
sections, which gives the assertion. This is the acyclicity argument
of [Stacks, [03FD](https://stacks.math.columbia.edu/tag/03FD)]; it does
not require $\Lambda$ to be flat over $\Z$, nor does it assert that
$I_{\mathrm{ab}}$ is injective.
