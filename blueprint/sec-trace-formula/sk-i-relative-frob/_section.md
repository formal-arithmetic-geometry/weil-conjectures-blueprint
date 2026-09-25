+++
id = "sk-i-relative-frob"
kind = "section"
title = "Relative Frobenius"
order = 2361
uses = ["sk-d-relative-frob", "sk-d-setup"]
+++
*Proposition (sketch).*

The map $r_m$ of the factorization is a finite
universal homeomorphism.

## Proof

Affine-locally the absolute $q^m$-power Frobenius is $a\otimes b\mapsto a^{q^m}\otimes b^{q^m}$ on the two tensor factors, so it factors through
$r_m$ followed by the base Frobenius in either order, which is the
factorization of [sk-d-relative-frob]. For universal bijectivity, a map
out of the relevant tensor product to a test ring is determined by its two
components, and a component satisfying $\beta(v(a))=\alpha(a)^p$ lifts
uniquely by $b\mapsto\beta(b)^{1/p}$, a ring map restricting to $\alpha$.
The argument is local on the base and on the test scheme, so $r_m$ is a
universal homeomorphism. Finiteness is the finiteness of relative
Frobenius for a finite-type morphism, iterated and base changed.

Uses: [sk-d-relative-frob], [sk-d-setup]
