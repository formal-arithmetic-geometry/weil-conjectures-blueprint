+++
id = "cor-weil-boundary-duality-discharge"
kind = "theorem"
title = "The finite-stage boundary input is a consequence"
lean = ["AlgebraicGeometry.Etale.nonempty_iso_leftDerivedUpperStar_verdierDual", "AlgebraicGeometry.Etale.hasBoundaryDuality"]
order = 2983
tags = ["latex:corollary"]
uses = ["def-weil-boundary-duality-input", "lem-weil-closed-costalk-duality", "lem-weil-duality-pairing", "thm-fix-general-biduality"]
+++
The boundary duality input of [def-weil-boundary-duality-input]
holds for every separated finite-type $Y/k$ and every finite stage
$A=A_{E,n}$. In particular the canonical evaluation-defined map

$$
\beta_L:i^*D_TL\longrightarrow D_ZRi^!L
$$

is an isomorphism for every closed immersion $i:Z\hookrightarrow T$
between the locally closed pieces in that definition.
