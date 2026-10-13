+++
id = "sk-thm-fe"
kind = "theorem"
title = "Functional equation"
order = 3262
lean = ["AlgebraicGeometry.weilSign", "AlgebraicGeometry.WeilFunctionalEquation.alternatingProdEval_eq"]
uses = ["sk-def-roots", "sk-def-zeta", "sk-prop-reciprocity", "sk-thm-tracetodeterminant"]
tags = ["sketch"]
+++
With the notation of [sk-def-roots], set

$$
\chi=\sum_{i=0}^{2d}(-1)^{i}b_i,\qquad
\varepsilon=(-1)^{\chi}q^{-d\chi/2}\prod_{i=0}^{2d}D_i^{(-1)^{i}}\in\{1,-1\}.
$$

Then

$$
Z(X_0,q^{-d}T^{-1})=\varepsilon\,q^{d\chi/2}T^{\chi}Z(X_0,T).
$$

The sign $\varepsilon$ is the normalized functional-equation sign.
