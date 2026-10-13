+++
id = "thm-pur-projective-bundle-formula"
kind = "theorem"
title = "Projective-bundle formula without purity"
order = 2326
uses = ["cor-kun-compact-kunneth", "cor-weil-pbc-geometric-fiber-finite", "def-coefficient-twists-detailed", "def-pur-conventions", "def-weil-derived-cohomology-sheaves", "def-weil-open-closed-recollement", "def-weil-scheme-morphism-properties", "lem-pur-divisor-class", "lem-pur-frame-independence", "lem-pur-kummer-additivity", "lem-pur-kunneth-supported", "prop-weil-proet-finite-proper-base-change", "thm-pur-rank-one-local-calculation", "thm-pur-rank-one-thom"]
+++
In the purity conventions of this chapter ([def-pur-conventions] fixed setting),
let $F$ be a
vector bundle of rank
$n+1$ on $B$, let $p:\mathbf P_B(F)\to B$, and put
$h_F=c_1(\mathcal O(1))$ of [lem-pur-kummer-additivity].
Then the morphism

$$
(1,h_F,\ldots,h_F^n):
\bigoplus_{a=0}^{n}\Lambda_B(-a)[-2a]
\xrightarrow{\ \sim\ }Rp_*\Lambda_{\mathbf P_B(F)}
$$

is an isomorphism, base-change compatible.
