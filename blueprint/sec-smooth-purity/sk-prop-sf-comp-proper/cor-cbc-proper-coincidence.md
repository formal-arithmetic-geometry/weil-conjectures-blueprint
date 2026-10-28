+++
id = "cor-cbc-proper-coincidence"
kind = "theorem"
title = "Proper morphisms: compact supports equal direct image"
order = 3206
tags = ["latex:corollary"]
uses = ["def-cbc-exchange-map", "def-compact-support-direct-image-detailed", "def-weil-pbc-derived-exchange", "def-weil-pbc-scheme-conventions", "thm-cbc-finite-torsion"]
lean = ["AlgebraicGeometry.Etale.nonempty_iso_rightDerivedLowerShriek_rightDerivedLowerStar"]
+++
For a proper
$f:X\to Y$ and the canonical identification
$Rf_!\xrightarrow{\sim}Rf_*$ of
[def-compact-support-direct-image-detailed] (the compactification
$j=\operatorname{id}$, $p=f$), the map $\operatorname{Ex}_!$
of [def-cbc-exchange-map] is the proper-base-change exchange map
of [def-weil-pbc-derived-exchange]; consequently the
compact-support base change of
[thm-cbc-finite-torsion] specializes to proper base change for
proper $f$.
