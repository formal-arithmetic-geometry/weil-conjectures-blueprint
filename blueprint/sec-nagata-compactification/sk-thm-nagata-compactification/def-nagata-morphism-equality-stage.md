+++
id = "def-nagata-morphism-equality-stage"
kind = "definition"
title = "Stage of equality for two descended morphisms"
order = 54
lean = ["AlgebraicGeometry.morphismEqStage"]
uses = ["def-nagata-directed-finite-upper-bound", "def-nagata-qc-open-equality-stage", "lemma-nagata-filtered-colimit-finite-data"]
+++
Let $(S_\lambda)$ be a cofiltered inverse system of quasi-compact
quasi-separated schemes with affine transition morphisms and limit $S$, let
$X_{\lambda_0},Y_{\lambda_0}$ be of finite presentation over
$S_{\lambda_0}$, and let
$\varphi_{\lambda_0},\psi_{\lambda_0}\colon X_{\lambda_0}\to Y_{\lambda_0}$
be $S_{\lambda_0}$-morphisms with equal base change to $S$. Define
$\lambda_{\varphi=\psi}\geq\lambda_0$ to be a selected stage such that the
base changes of $\varphi_{\lambda_0}$ and $\psi_{\lambda_0}$ to
$S_\lambda$ agree for every $\lambda\geq\lambda_{\varphi=\psi}$.
