+++
id = "sk-lem-nagata-density-normalization"
kind = "lemma"
title = "Passing to the schematic closure"
order = 1344
uses = ["sk-def-nagata-sketch-data", "sk-lem-nagata-sketch-closure", "sk-prop-sf-open-closed-triangle"]
lean = ["AlgebraicGeometry.ProEtale.CondensedRing.isIso_boundedConstructibleOpenImmersionLowerShriekRefinement", "AlgebraicGeometry.ProEtale.CondensedRing.isIso_boundedConstructibleOpenImmersionLowerShriekRefinementPushforward", "AlgebraicGeometry.ProEtale.CondensedRing.isIso_boundedConstructibleOpenImmersionLowerShriekRefinementPushforward_padicAlgCl", "AlgebraicGeometry.ProEtale.CondensedRing.boundedConstructibleLowerShriekRefinementIso"]
tags = ["sketch"]
+++
Let $X\xrightarrow{j}\overline X\xrightarrow{p}S$ be any compactification
([sk-def-nagata-sketch-data]) of separated schemes of finite type over a
field $k$ of positive characteristic different from $\ell$, and let
$i:Z\hookrightarrow\overline X$ be the schematic closure of $X$, with
$j_Z:X\hookrightarrow Z$ the induced open immersion
([sk-lem-nagata-sketch-closure]). Let $\Lambda$ be the condensed coefficient
ring of a finite extension $E/\Ql$ or of $\Qlb$, and use its pulled-back
coefficient sheaves on these schemes. For every
$K\in D^b_c(X,\Lambda)$ there are canonical identifications, in
$D^b_c(\overline X,\Lambda)$ and $D^b_c(S,\Lambda)$ respectively,

$$
j_!K\simeq i_*j_{Z,!}K,\qquad
Rp_*j_!K\simeq R(p\circ i)_*j_{Z,!}K.
$$

Thus replacing a compactification by the schematic closure of $X$ does not
change the expression $Rp_*j_!$ defining $Rf_!$; that expression needs only
an open immersion followed by a proper morphism.
