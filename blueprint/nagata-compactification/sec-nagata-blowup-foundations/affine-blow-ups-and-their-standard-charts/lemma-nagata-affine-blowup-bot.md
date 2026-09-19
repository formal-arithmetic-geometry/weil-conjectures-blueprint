+++
id = "lemma-nagata-affine-blowup-bot"
kind = "lemma"
title = "Blow-up of the zero ideal"
order = 209
uses = ["def-nagata-affine-blowup"]
+++
**Status.** Bypassed by the formalized route: the affine blow-up and its
charts are the construction `AlgebraicGeometry.AffineBlowup`, with
`AffineBlowup.chart` and
`AffineBlowup.isLocalization_away_map` supplying the chart algebra
and its localization coherence, so neither is rebuilt by hand.

The blow-up in the zero ideal is empty: the positive-degree part of its Rees
algebra vanishes, so the irrelevant ideal is zero and Proj has no points.

## Proof

If $I=0$, then $I^n=0$ for every $n>0$. Hence the irrelevant ideal of
$\mathcal R_A(0)$ is zero. A point of Proj would be a homogeneous prime not
containing the irrelevant ideal, which is impossible because every prime
contains zero.
