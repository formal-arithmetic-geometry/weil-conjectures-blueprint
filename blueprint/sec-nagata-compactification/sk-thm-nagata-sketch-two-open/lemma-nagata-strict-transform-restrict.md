+++
id = "lemma-nagata-strict-transform-restrict"
kind = "lemma"
title = "Strict transform over the complement of the center"
order = 273
lean = ["AlgebraicGeometry.Scheme.IdealSheafData.isPullback_strictTransform_over_blowupMap"]
uses = ["def-nagata-global-blowup", "def-nagata-strict-transform", "prop-nagata-global-blowup-cover-independent"]
+++
Let $\mathcal I\subseteq\mathcal O_X$ be a quasi-coherent ideal with
center $C=V(\mathcal I)$, let $b\colon X'=\operatorname{Bl}_{\mathcal I}(X)\to X$
be the blow-up, and let $f\colon Y\to X$ be a morphism. Let
$\Omega\subseteq Y\times_XX'$ be the open subscheme lying over
$X\setminus C$ and let $\widetilde Y\hookrightarrow Y\times_XX'$ be the
strict transform of $f$ along the blow-up ([def-nagata-strict-transform]).
Then the part $\widetilde Y\times_{Y\times_XX'}\Omega$ of the strict
transform lying over $X\setminus C$, together with its projection to $Y$
and the map to $b^{-1}(X\setminus C)\xrightarrow{\sim}X\setminus C$, is a
fibre product of $f$ and the inclusion $X\setminus C\hookrightarrow X$.
Thus over $X\setminus C$ the strict transform is canonically
$Y\times_X(X\setminus C)$, compatibly with the projection to $Y$.
