+++
id = "def-nagata-morphism-descent"
kind = "definition"
title = "Finite-stage model of a morphism"
order = 360
lean = ["AlgebraicGeometry.morphismDescentStage", "AlgebraicGeometry.morphismDescent"]
uses = ["def-nagata-affine-fp-descent", "def-nagata-directed-finite-upper-bound", "def-nagata-qc-open-descent", "lemma-nagata-filtered-colimit-finite-data"]
+++
Let $(S_\lambda)$ be a cofiltered inverse system of quasi-compact
quasi-separated schemes with affine transition morphisms and limit $S$. Let
$X_{\lambda_0},Y_{\lambda_0}$ be of finite presentation over
$S_{\lambda_0}$, write $X_\lambda=X_{\lambda_0}\times_{S_{\lambda_0}}S_\lambda$,
$Y_\lambda=Y_{\lambda_0}\times_{S_{\lambda_0}}S_\lambda$,
$X_{\lambda_0,S}=X_{\lambda_0}\times_{S_{\lambda_0}}S$ and
$Y_{\lambda_0,S}=Y_{\lambda_0}\times_{S_{\lambda_0}}S$, and let
$\varphi\colon X_{\lambda_0,S}\to Y_{\lambda_0,S}$ be an $S$-morphism.
Define $\lambda_\varphi\geq\lambda_0$ and

$$
\varphi_{\lambda_\varphi}\colon
X_{\lambda_\varphi}\longrightarrow Y_{\lambda_\varphi}
$$

to be a selected stage and a selected $S_{\lambda_\varphi}$-morphism whose
base change to $S$ is $\varphi$.
