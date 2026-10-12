+++
id = "sk-thm-sf-pf-adic"
kind = "theorem"
title = "Projection formula: the derived-complete stage"
order = 2433
uses = ["sk-def-sf-operations", "sk-prop-sf-pf-reduction"]
lean = ["AlgebraicGeometry.Etale.hasProjectionFormula_of_derivedCompleteIntegral"]
tags = ["sketch"]
+++
Let $E/\Ql$ be a finite extension inside $\Qlb$ with ring of integers
$\mathcal O_E$, let $f:X\to Y$ be a morphism of schemes admitting a
compactification, with $Rf_!$ formed from the chosen compactification, and
let $K\in D(X_{\Et},\mathcal O_E)$, $L\in D(Y_{\Et},\mathcal O_E)$ be
complexes of étale sheaves of $\mathcal O_E$-modules that are derived
complete with respect to the maximal ideal of $\mathcal O_E$ and of finite
Tor amplitude, with finite reductions $K_n,L_n$. Then the projection map

$$
\operatorname{PF}_{f,K,L}:Rf_!K\otimes^L L\longrightarrow Rf_!\bigl(K\otimes^L Lf^*L\bigr)
$$

is an isomorphism.
