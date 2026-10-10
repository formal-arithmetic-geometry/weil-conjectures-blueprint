+++
id = "def-nagata-strict-transform-closed-chart-model"
kind = "definition"
title = "Closed chart model of the global strict transform"
order = 156
uses = ["def-nagata-global-blowup", "def-nagata-strict-transform-chart-ring", "lemma-nagata-strict-transform-chart-localization-data"]
+++
Let $f\colon Y\to X$, let $\mathcal I$ be a finite-type quasi-coherent
ideal, and put $X'=\operatorname{Bl}_{\mathcal I}(X)$. Choose an affine
cover $V_i=\operatorname{Spec}(A_i)$ of $X$, finite generating sets for
$\mathcal I|_{V_i}$, and affine covers
$W_{ij}=\operatorname{Spec}(B_{ij})$ of $f^{-1}(V_i)$. Define
$Y^{\mathrm{st}}_{\mathrm{chart}}$ by gluing the affine schemes
$\operatorname{Spec}(C_{i,j,a}^{\mathrm{st}})$ and their quotient closed
immersions into the corresponding affine pieces of $Y\times_XX'$.
On an overlap, refine to basic opens in the chosen $W_{ij}$ and in the
blow-up chart. The transition maps are the localizations of
[lemma-nagata-strict-transform-chart-localization-data]; they preserve
the quotient ideals and satisfy the double- and triple-overlap identities.
These maps, together with the affine closed immersions, are the specified
scheme-glue datum.
