+++
id = "cor-nagata-flat-strict-transform-base-change"
kind = "theorem"
title = "Flat strict transform equals ordinary base change"
order = 341
tags = ["latex:corollary"]
uses = ["lemma-nagata-flat-strict-transform-no-torsion", "prop-nagata-strict-transform-closed-fiber-product"]
+++
**Status.** Bypassed by the formalized route: flat base change of strict
transforms is not used. The only strict-transform base-change fact the
route needs is the pullback square
`AlgebraicGeometry.isPullback_strictTransformOpen` over the
preserved open.

Let $f\colon Y\to X$ and let $\mathcal I$ be a finite-type quasi-coherent
ideal on $X$. If $f$ is flat, the strict transform in
$\operatorname{Bl}_{\mathcal I}(X)$ is all of
$Y\times_X\operatorname{Bl}_{\mathcal I}(X)$.

## Proof

On every affine blow-up chart the quotient is by the zero ideal, so the
closed immersion in
[prop-nagata-strict-transform-closed-fiber-product] is an isomorphism.
