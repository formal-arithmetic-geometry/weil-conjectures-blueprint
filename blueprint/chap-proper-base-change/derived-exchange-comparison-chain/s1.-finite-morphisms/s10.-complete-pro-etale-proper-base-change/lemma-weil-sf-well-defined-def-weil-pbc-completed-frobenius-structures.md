+++
id = "lemma-weil-sf-well-defined-def-weil-pbc-completed-frobenius-structures"
kind = "lemma"
title = "Well-definedness certificate for def:weil-pbc-completed-frobenius-structures"
order = 892
uses = ["def-weil-pbc-completed-frobenius-structures", "lemma-weil-pbc-frobenius-product-cone-limit", "lemma-weil-sf-well-defined-def-weil-pbc-completed-base-change-map"]
+++
The pair $(\Theta_S,\Theta_T)$ belongs to

$$
\operatorname{Iso}(\Phi_{Y'}S,S)\times
\operatorname{Iso}(\Phi_{Y'}T,T),
$$

and $tWs$ belongs to $\operatorname{Hom}(S,T)$. This certificate records
the completed types but not the equivariance equation for $tWs$.

## Proof

The product-cone lemma supplies isomorphisms
$\Theta_{A,\infty}:\Phi_{Y'}A_\infty\to A_\infty$ and
$\Theta_{D,\infty}:\Phi_{Y'}D_\infty\to D_\infty$, together with
$W:A_\infty\to D_\infty$. The preceding certificate gives the
isomorphisms $s:S\to A_\infty$ and $t:D_\infty\to T$. Conjugating the two
limit structures by $s$ and $t$ yields the displayed pair of isomorphism
types, and the endpoints of $s,W,t$ give $tWs:S\to T$. The next lemma
proves the equivariance equation.
