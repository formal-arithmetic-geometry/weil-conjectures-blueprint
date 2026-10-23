+++
id = "def-nagata-relative-stage-morphism-data"
kind = "definition"
title = "Finite-stage data for a morphism"
lean = ["AlgebraicGeometry.Scheme.Hom.NoetherianStageData", "AlgebraicGeometry.Scheme.Hom.noetherianStageData"]
order = 77
uses = ["def-nagata-noetherian-inverse-system"]
+++
Let $f\colon X\to S$ be a morphism and let $\mathsf N(X)$ and
$\mathsf N(S)$ be Noetherian approximations of $X$ and $S$
([def-nagata-noetherian-inverse-system]), with their limit projections
$X\to X_\lambda$ and $S\to S_\mu$. A finite-stage datum for this morphism consists of indices
$\lambda_X$ and $\lambda_S$ and a morphism
$\varphi_{\lambda_X,\lambda_S}\colon X_{\lambda_X}\to S_{\lambda_S}$
such that, after composing with the two limit projections, the map
$X\to S\to S_{\lambda_S}$ equals
$X\to X_{\lambda_X}\to S_{\lambda_S}$, and such that the comparison
$X\to X_{\lambda_X}\times_{S_{\lambda_S}}S$ induced by this equality is an
immersion.
