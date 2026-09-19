+++
id = "lemma-nagata-flat-strict-transform-no-torsion"
kind = "lemma"
title = "Flatness kills the strict-transform torsion"
order = 340
uses = ["def-nagata-power-torsion", "lemma-nagata-chart-generator-regular"]
+++
**Status.** Bypassed by the formalized route: flat base change of strict
transforms is not used. The only strict-transform base-change fact the
route needs is the pullback square
`AlgebraicGeometry.isPullback_strictTransformOpen` over the
preserved open.

Let $A\to B$ be flat, let $I\subseteq A$ be an ideal, and let $a\in I$.
Then the $a$-power-torsion in
$B\otimes_AA[I/a]$ is zero.

## Proof

Multiplication by $a$ is injective on $A[I/a]$ by
[lemma-nagata-chart-generator-regular]. Tensor this injection with the
flat $A$-module $B$; multiplication by $a$ remains injective, and therefore
no nonzero element is killed by a power of $a$.
