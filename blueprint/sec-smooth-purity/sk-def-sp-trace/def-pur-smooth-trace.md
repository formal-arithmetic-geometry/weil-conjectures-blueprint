+++
id = "def-pur-smooth-trace"
kind = "definition"
title = "Smooth trace"
lean = ["AlgebraicGeometry.Etale.smoothPurityTrace", "AlgebraicGeometry.Etale.homEquiv_smoothPurityTrace", "AlgebraicGeometry.Etale.smoothPurityTrace_naturality"]
order = 2365
uses = ["def-coefficient-twists-detailed", "def-pur-conventions", "def-sbc-smooth-morphisms", "def-weil-exceptional-adjoint-admissibility", "def-weil-pbc-proetale-site", "def-weil-scheme-morphism-properties"]
+++
Work in the purity conventions of [def-pur-conventions], let
$A=A_{E,n}$, and let $f:X\to Y$ be a smooth separated morphism of
relative dimension $d$. The *smooth trace* is the composite

$$
\operatorname{Tr}_f^{\mathrm{sm}}:
Rf_!\Lambda_X(d)[2d]
\xrightarrow{\ Rf_!(\gamma_{f,\Lambda_Y})\ }
Rf_!Rf^!\Lambda_Y
\xrightarrow{\ \operatorname{Tr}_f\ }\Lambda_Y,
$$

where $\operatorname{Tr}_f$ is the counit of the adjunction
$Rf_!\dashv Rf^!$ of
[def-weil-exceptional-adjoint-admissibility]; for
$K\in D^b_{ctf}(Y,\Lambda)$ the coefficient-valued smooth trace is

$$
\operatorname{Tr}^{\mathrm{sm}}_{f,K}:
Rf_!Lf^*K(d)[2d]
\xrightarrow{\ Rf_!(\gamma_{f,K})\ }
Rf_!Rf^!K
\xrightarrow{\ \operatorname{Tr}_{f,K}\ }K.
$$
