+++
id = "def-nagata-qc-open-descent"
kind = "definition"
title = "Finite-stage model of a quasi-compact open"
order = 46
lean = ["AlgebraicGeometry.baseChangeQcOpenDescentStage", "AlgebraicGeometry.baseChangeQcOpenDescent"]
uses = ["def-nagata-basechanged-system", "def-nagata-directed-finite-upper-bound", "lemma-nagata-filtered-colimit-finite-data"]
+++
Let $(S_\lambda)$ be a cofiltered inverse system of schemes with affine
transition morphisms and limit $S$. Fix $\lambda_0$ and a morphism
$Y_{\lambda_0}\to S_{\lambda_0}$, form the base-changed system
$Y_\lambda=Y_{\lambda_0}\times_{S_{\lambda_0}}S_\lambda$ with limit
$Y=Y_{\lambda_0}\times_{S_{\lambda_0}}S$, and let $W\subseteq Y$ be a
quasi-compact open. Define $\lambda_W\geq\lambda_0$ and
$W_{\lambda_W}\subseteq Y_{\lambda_W}$ to be a selected stage and a
selected quasi-compact open of $Y_{\lambda_W}$ whose inverse image in $Y$
is $W$.
