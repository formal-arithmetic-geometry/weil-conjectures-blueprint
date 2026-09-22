+++
id = "prop-weil-pbc-cancellation"
kind = "theorem"
title = "Cancellation along a proper surjection"
order = 1081
lean = ["AlgebraicGeometry.Etale.isBaseChangeIso_of_comp_of_surjective"]
uses = ["lem-weil-pbc-retract-supplied", "lem-weil-pbc-grothendieck-spectral-sequence", "lem-weil-pbc-vanishing-descends-retract", "def-weil-pbc-property"]
+++
Let $X\xrightarrow{f}Y\xrightarrow{h}Z$ be proper, with $f$ surjective. If
$\mathrm{PBC}(f)$ and $\mathrm{PBC}(hf)$ hold, then $\mathrm{PBC}(h)$ holds.

## Proof

$\mathrm{PBC}(h)$ is equivalent to $\mathrm{IA}(h)$, so we prove
$\mathrm{IA}(h)$. Fix a base change $c:Z'\to Z$, write $Y'=Y\times_ZZ'$,
$X'=X\times_ZZ'$ with projections $b$, $a$, and base-changed maps $f'$, $h'$,
and fix a prime $r$ and an injective $\mathbf F_r$-module sheaf $I$ on $Y$. By
[lem-weil-pbc-retract-supplied], $b^{-1}I$ is a direct summand of
$b^{-1}f_*J$ for a suitable injective $J$ on $X$. The underived proper
exchange identifies $b^{-1}f_*J$ with $f'_*a^{-1}J$; $\mathrm{IA}_r(f)$ and
$\mathrm{IA}_r(hf)$ kill the higher direct images of $a^{-1}J$ along $f'$ and
$h'f'$, so the spectral sequence of
[lem-weil-pbc-grothendieck-spectral-sequence] collapses to the $q=0$ row and
yields $R^ph'_*(f'_*a^{-1}J)=0$ for $p>0$. Via the exchange identification
this is the vanishing for $b^{-1}f_*J$, and
[lem-weil-pbc-vanishing-descends-retract] descends it to the retract
$b^{-1}I$, proving $\mathrm{IA}_r(h)$.

Unresolved dependencies: def:weil-pbc-scheme-conventions, def:weil-pbc-injective-acyclicity, prop:weil-pbc-property-iff-acyclicity, lem:weil-pbc-underived-proper-exchange
