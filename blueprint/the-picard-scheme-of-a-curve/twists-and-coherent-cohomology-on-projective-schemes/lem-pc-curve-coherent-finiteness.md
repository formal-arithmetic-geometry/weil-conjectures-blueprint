+++
id = "lem-pc-curve-coherent-finiteness"
kind = "lemma"
title = "Coherent cohomology of a smooth projective curve over an algebraically closed field"
order = 4330
lean = ["AlgebraicGeometry.Curve.finiteDimensional_cohomology_of_isCoherent"]
uses = ["def-pc-smooth-projective-curve", "lem-pc-projective-curve-finite-projection"]
+++
Let $k$ be an algebraically closed field, let $X$ be a smooth projective
curve [def-pc-smooth-projective-curve] over $k$, and let $\mathcal F$ be a
coherent $\mathcal O_X$-module. Then $H^i(X,\mathcal F)$ is a
finite-dimensional $k$-vector space for $i=0,1$, and vanishes for
$i\ge2$.

## Proof

By [lem-pc-projective-curve-finite-projection], choose a finite morphism
$u:X\to\mathbf P^1_k$. If $W=\operatorname{Spec}(R)\subset\mathbf P^1_k$ is
affine, then $u^{-1}(W)=\operatorname{Spec}(B)$ with $B$ finite over $R$.
The restriction of $\mathcal F$ is $\widetilde M$ for a finite $B$-module
$M$: this is the affine characterization of coherence on the locally
Noetherian scheme $X$. Hence $M$ is finite over $R$, so
$u_*\mathcal F|_W=\widetilde M$ is coherent. (The same finite module
calculation on principal opens gives the restriction maps; thus no
finite-type-over-$R$ module is being mistaken for a finite $R$-module.)

For every affine $W\subset\mathbf P^1_k$, its inverse image is affine;
therefore higher cohomology of $\mathcal F$ on $u^{-1}(W)$ vanishes by
affine vanishing. The Leray spectral sequence of $u$ then has
$R^q u_*\mathcal F=0$ for $q>0$ and gives canonical isomorphisms
$$
 H^i(X,\mathcal F)\cong H^i(\mathbf P^1_k,u_*\mathcal F).
$$
The right side is finite-dimensional for $i=0,1$ by the coherent
finiteness on $\mathbf P^1$ of the divisors chapter, and is zero for
$i\ge2$ by the vanishing lemma there. This proves all assertions.

Unresolved dependencies: pqf-def-coherent, pqf-lem-coherent-ft-locnoeth, pqf-lem-affine-vanishing, pqf-lem-leray, lem:sc-p1-coherent-finite, lem:sc-p1-hi-vanishing
