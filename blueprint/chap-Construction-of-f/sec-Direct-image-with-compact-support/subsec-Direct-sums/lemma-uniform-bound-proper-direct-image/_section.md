+++
id = "lemma-uniform-bound-proper-direct-image"
kind = "lemma"
title = "A uniform bound for proper direct image"
order = 483
lean = ["AlgebraicGeometry.ProEtale.CondensedRing.properLowerStarHeartHypotheses_continuousMapRingObj", "AlgebraicGeometry.ProEtale.CondensedRing.properLowerStarHeartHypotheses_padicAlgClRingObj"]
uses = ["definition-ind-etale-pro-etale-weakly", "lemma-stability", "definition-small-pro-etale-site", "proposition-topos-functoriality", "example-locally-constant-functions-w-local", "definition-constructible-sheaves"]
+++
Let $p:X\to Y$ be proper, and let $d$ be an integer bounding the
dimensions of all geometric fibres of $p$ (for instance $d=\dim X$). For
$M\in\IndCons(X,\Lambda)$,

$$
R^qp_*M=0\quad(q>2d+1),\qquad R^qp_*M\in\IndCons(Y,\Lambda)\quad(q\geq0),
$$

and $R^qp_*:\IndCons(X,\Lambda)\to\IndCons(Y,\Lambda)$ preserves arbitrary
direct sums.
