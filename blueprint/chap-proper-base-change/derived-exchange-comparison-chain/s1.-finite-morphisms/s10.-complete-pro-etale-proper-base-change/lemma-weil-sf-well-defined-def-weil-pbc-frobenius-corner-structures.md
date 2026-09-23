+++
id = "lemma-weil-sf-well-defined-def-weil-pbc-frobenius-corner-structures"
kind = "lemma"
title = "Well-definedness certificate for def:weil-pbc-frobenius-corner-structures"
order = 1875
uses = ["def-weil-pbc-frobenius-corner-structures", "lemma-weil-pbc-perfect-projection-formula", "lemma-weil-sf-well-defined-def-weil-pbc-frobenius-tower-datum", "lemma-weil-sf-well-defined-def-weil-pbc-level-map-arrows"]
+++
The tuple $(\Theta_{A,n},\Theta_{B,n},\Theta_{C,n},\Theta_{D,n})$ belongs to

$$
\operatorname{Iso}(\Phi_{Y'}A_n,A_n)\times
\operatorname{Iso}(\Phi_{Y'}B_n,B_n)\times
\operatorname{Iso}(\Phi_{Y'}C_n,C_n)\times
\operatorname{Iso}(\Phi_{Y'}D_n,D_n).
$$

This assertion records the four corner types and does not assert edge
equivariance.

## Proof

The certified tower datum makes $\kappa_g,\kappa_{g'},\beta_{f,n}, \beta_{f',E_n}$ and $\vartheta_n$ isomorphisms with the displayed
endpoints. Their ordered composites therefore give
$\vartheta_{E,n}$, $\Theta_{B,n}$ and $\Theta_{D,n}$ with the asserted
types. The level-arrow certificate and the perfect projection formula make
$h_n$ and $h'_n$ invertible. Conjugating $\Theta_{B,n}$ by $h_n$ and
$\Theta_{D,n}$ by $h'_n$ gives the asserted types for $\Theta_{A,n}$ and
$\Theta_{C,n}$. Edge equivariance remains the next lemma.
