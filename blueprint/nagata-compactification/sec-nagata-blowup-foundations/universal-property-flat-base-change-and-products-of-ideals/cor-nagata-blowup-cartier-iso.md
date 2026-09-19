+++
id = "cor-nagata-blowup-cartier-iso"
kind = "theorem"
title = "Blow-up of an effective Cartier center"
order = 280
lean = ["AlgebraicGeometry.Scheme.IdealSheafData.isIso_blowupMap_of_isInvertible"]
tags = ["latex:corollary"]
uses = ["def-nagata-invertible-ideal", "thm-nagata-blowup-universal-property"]
+++
Let $X$ be a scheme. If $\mathcal I$ is an invertible ideal on $X$, then
$b_{X,\mathcal I}$ is an isomorphism.

## Proof

The identity of $X$ lifts to the blow-up by the universal property. Compose
this lift with the blow-up map in both orders and use uniqueness.
