+++
id = "def-nagata-relative-gluing-datum-descent"
kind = "definition"
title = "Finite-stage raw relative gluing datum"
order = 365
lean = ["AlgebraicGeometry.RelativeGluingDatum", "AlgebraicGeometry.RelativeAffinePresentation.ChartModels", "AlgebraicGeometry.RelativeAffinePresentation.chartModels", "AlgebraicGeometry.RelativeAffinePresentation.ChartModels.rawStage", "AlgebraicGeometry.RelativeAffinePresentation.ChartModels.rawDatum"]
uses = ["def-nagata-affine-fp-descent", "def-nagata-morphism-descent", "def-nagata-qc-open-descent", "def-nagata-relative-finite-affine-presentation", "lemma-nagata-affine-fp-descends", "lemma-nagata-morphism-descends", "lemma-nagata-qc-open-descends"]
+++
Let $(S_\lambda)$ be a cofiltered inverse system of quasi-compact
quasi-separated schemes with affine transition morphisms and limit $S$, and
let $X\to S$ be of finite presentation with $X$ quasi-separated. For a
scheme $T$, schemes $Y_a\to T$ and a morphism $B\to T$, a *relative gluing
datum* over $B$ consists of opens $V_{ab}$ of the charts
$Y_a\times_TB$ and $T$-morphisms $\psi_{ab}\colon V_{ab}\to Y_b$; the
associated overlap maps $V_{ab}\to Y_b\times_TB$ are $B$-morphisms.

Starting from $\mathsf R_X$:

1. select a common index $\lambda_1\geq\lambda_0$ and affine schemes $Y_a$
of finite presentation over $S_{\lambda_1}$ with
$Y_a\times_{S_{\lambda_1}}S\cong W_a$ (the descended chart algebras, as in
[lemma-nagata-affine-fp-descends]), and let
$\ell_a\colon Y_a\times_{S_{\lambda_1}}S\to X$ be the resulting open
immersions;
1. descend each overlap $\ell_a^{-1}(W_b)$, a quasi-compact open, to a
quasi-compact open at a stage $\mu_{ab}$ using
[lemma-nagata-qc-open-descends];
1. descend each overlap map $\ell_a^{-1}(W_b)\to Y_b$ over
$S_{\lambda_1}$ to a morphism from the descended overlap at a later stage
$\nu_{ab}\geq\mu_{ab}$, as in [lemma-nagata-morphism-descends].

Define $\lambda_{\mathrm{raw}}(X/S)$ to be a selected common bound of the
finitely many stages $\nu_{ab}$, and let
$\mathsf R_{X,\lambda_{\mathrm{raw}}}^{\mathrm{raw}}$ be the relative
gluing datum over $S_{\lambda_{\mathrm{raw}}}$ with charts
$Y_a\times_{S_{\lambda_1}}S_{\lambda_{\mathrm{raw}}}$ formed by the
descended overlaps and overlap maps transported to
$\lambda_{\mathrm{raw}}$.
