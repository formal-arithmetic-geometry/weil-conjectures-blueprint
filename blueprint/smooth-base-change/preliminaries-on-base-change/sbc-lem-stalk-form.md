+++
id = "sbc-lem-stalk-form"
kind = "lemma"
title = "Stalk form of the base-change map"
order = 2772
uses = ["def-weil-pbc-scheme-conventions", "lemma-weil-pbc-geometric-stalk-conservative", "prop-weil-pbc-strict-henselization-stalk-formula", "sbc-def-base-change-map", "sbc-def-base-change-square"]
+++
Consider a base-change square
where $g:T\to S$ is
quasi-compact and
quasi-separated, let $\mathcal F\in\Ab(T_{\Et})$ and $q\geq0$. The
following are equivalent:

1. For every geometric point $\bar x$ of $X$ with image
$\bar s=f(\bar x)$ in $S$,
$$
H^q\bigl(\operatorname{Spec}\mathcal
O^{\mathrm{sh}}_{X,\bar x}\times_ST,\mathcal F\bigr)
=H^q\bigl(\operatorname{Spec}\mathcal
O^{\mathrm{sh}}_{S,\bar s}\times_ST,\mathcal F\bigr).
$$
1. The base-change map of [sbc-def-base-change-map]
$$
f^{-1}R^qg_*\mathcal F
\longrightarrow R^qh_*e^{-1}\mathcal F
$$
is an isomorphism.

(*Stacks Project, Lemma 59.86.5, [Tag `0EZU`](https://stacks.math.columbia.edu/tag/0EZU).*)

## Proof

Since $Y=X\times_ST$, the strict-local base changes satisfy
$\operatorname{Spec}\mathcal O^{\mathrm{sh}}_{X,\bar x}\times_XY =\operatorname{Spec}\mathcal O^{\mathrm{sh}}_{X,\bar x}\times_ST$; by
[prop-weil-pbc-strict-henselization-stalk-formula] the stalk at
$\bar x$ of $f^{-1}R^qg_*\mathcal F$ is
$H^q(\operatorname{Spec}\mathcal O^{\mathrm{sh}}_{S,\bar s}\times_ST,\mathcal F)$ and the stalk of
$R^qh_*e^{-1}\mathcal F$ is
$H^q(\operatorname{Spec}\mathcal O^{\mathrm{sh}}_{X,\bar x}\times_ST,\mathcal F)$, so (1) says exactly
that the stalk of the base-change map of
[sbc-def-base-change-map] at every geometric point $\bar x$ is an
isomorphism. Geometric stalks are conservative
([lemma-weil-pbc-geometric-stalk-conservative]), which is (2).
