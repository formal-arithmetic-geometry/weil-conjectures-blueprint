+++
id = "prop-sf-pf-reduction"
kind = "theorem"
title = "Compatibility with finite reduction"
order = 2773
tags = ["latex:proposition"]
lean = ["AlgebraicGeometry.Etale.projectionMapOfCompactification_constantSingle", "AlgebraicGeometry.Etale.isIso_reductionModIdeal_map_projectionMapOfCompactification_iff", "AlgebraicGeometry.Etale.hasProjectionFormula_iff_reductionModIdeal"]
uses = ["def-sf-datum", "def-sf-pf", "lem-sf-reduction-compatibility", "lemma-weil-pbc-projection-formula-compactified", "lemma-weil-pbc-projection-formula-open-piece", "lemma-weil-pbc-projection-formula-proper-piece", "lem-amb-proper-coproducts-projection"]
+++
In the setting of [def-sf-datum], let $J\subseteq\Lambda$ be an ideal and let
$\rho$ be the reduction modulo $J$ of [lem-sf-reduction-compatibility]. Let
$c$ be a compactification of $f$ and let $\operatorname{PF}$ be the projection
transformation of [def-sf-pf] computed with $c$. For all
$K\in D(X_{\Et},\Lambda)$ and $L\in D(Y_{\Et},\Lambda)$:

1. the square

$$
\begin{array}{ccc}
\rho_Y\bigl(Rf^c_!K\otimes^L_\Lambda L\bigr)&\xrightarrow{\ \rho_Y(\operatorname{PF}_{f,K,L})\ }&
\rho_Y\,Rf^c_!\bigl(K\otimes^L_\Lambda Lf^*L\bigr)\\
\downarrow&&\downarrow\\
Rf^c_!K\otimes^L_\Lambda\rho_YL&\xrightarrow{\ \operatorname{PF}_{f,K,\rho_YL}\ }&
Rf^c_!\bigl(K\otimes^L_\Lambda Lf^*\rho_YL\bigr)\cong Rf^c_!\,\rho_X\bigl(K\otimes^L_\Lambda Lf^*L\bigr)
\end{array}
$$

commutes, where the left arrow is the associativity isomorphism, the right
arrow is the comparison of $Rf^c_!$ with $\rho$ of
[lem-sf-reduction-compatibility] (2), and the bottom right isomorphism is built
from the comparison of $Lf^*$ with $\rho$ of [lem-sf-reduction-compatibility]
(1) and associativity;
1. $\rho_Y(\operatorname{PF}_{f,K,L})$ is an isomorphism if and only if
$\operatorname{PF}_{f,K,\rho_YL}$ is;
1. the projection formula holds at $(K,L)$ if and only if it holds at
$(K,\rho_YL)$, and both hold.
