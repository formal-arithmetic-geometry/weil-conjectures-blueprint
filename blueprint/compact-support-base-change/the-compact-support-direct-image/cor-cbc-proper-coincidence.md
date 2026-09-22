+++
id = "cor-cbc-proper-coincidence"
kind = "theorem"
title = "Proper morphisms: compact supports equal direct image"
order = 6613
lean = ["AlgebraicGeometry.Etale.compactSupportExchange_eq_exchange_of_isProper"]
tags = ["latex:corollary"]
uses = ["def-compact-support-direct-image", "def-weil-pbc-derived-exchange", "def-cbc-exchange-map", "thm-cbc-finite-torsion"]
+++
For a proper $f:X\to Y$ and the canonical identification
$Rf_!\xrightarrow{\sim}Rf_*$ (the compactification $j=\operatorname{id}$,
$p=f$), the map $\Ex_!$ of [def-cbc-exchange-map] is the proper-base-change
exchange map; consequently the compact-support base change of
[thm-cbc-finite-torsion] specializes to proper base change for proper $f$.

## Proof

For $j=\operatorname{id}$ the extension-by-zero identification of
[def-cbc-exchange-map] is the identity, so $\Ex_!$ is the derived exchange map
for the proper $p=f$, by [def-cbc-exchange-map] and the identification
$Rf_!=Rf_*$ of the compact-support direct image.

Unresolved dependencies: def:weil-pbc-scheme-conventions
