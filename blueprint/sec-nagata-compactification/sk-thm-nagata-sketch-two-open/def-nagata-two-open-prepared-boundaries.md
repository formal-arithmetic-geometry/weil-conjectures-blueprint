+++
id = "def-nagata-two-open-prepared-boundaries"
kind = "definition"
title = "Prepared ambient schemes with separated boundary closures"
order = 369
lean = ["AlgebraicGeometry.TwoOpenSide.Prepared"]
uses = ["def-nagata-separate-constructible-closed", "def-nagata-two-open-boundary-loci", "def-nagata-two-open-graph-extensions"]
+++
For $\{i,j\}=\{1,2\}$, the $i$-th side is *prepared* if its self boundary
$\overline Z_{i,i}$ and its forbidden boundary $\overline Z_{i,j}$ (the
closures in $X_i$ of $\psi_i^{-1}(U\setminus U_j)$ and
$\psi_i^{-1}(U\setminus U_i)$) are disjoint.

To prepare the sides, define

$$
X_i^{\mathrm{prep}}
=\mathsf{CSepBl}_{V_i}(Z_{i,i},Z_{i,j})
$$

and transport $V_i$, $U_i$, and $\psi_i$ along the chosen isomorphism over
$V_i$. Replace $X_i$ by $X_i^{\mathrm{prep}}$ and let
$\overline Z_{i,k}$ denote the closure of the transported $Z_{i,k}$ in the
new $X_i$.
