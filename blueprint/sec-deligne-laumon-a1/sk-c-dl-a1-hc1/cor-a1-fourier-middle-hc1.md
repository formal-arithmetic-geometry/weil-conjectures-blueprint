+++
id = "cor-a1-fourier-middle-hc1"
kind = "theorem"
title = "Fourier bound for middle-extension cohomology"
order = 2782
tags = ["latex:corollary"]
uses = ["cor-fd-l2-plancherel-middle-extension", "cor-fd-origin-stationary-phase", "def-fd-nonexceptional", "def-weil-punctual-weights", "def-wf-fundamental-representation", "def-wf-middle-extension", "lem-a1-unramified-nonexceptional", "lem-wf-boundary-semicontinuity", "prop-a1-fourier-middle-extension"]
lean = ["AlgebraicGeometry.hasWeightsAtMost_compactlySupportedCohomology_one"]
+++
Let $\psi$ be a nontrivial additive character of $k_0$, let
$j:U_0\hookrightarrow\mathbf A^1_{k_0}$ be a dense open immersion and
let $\mathcal M$ be an irreducible lisse Weil sheaf on $U_0$, that is,
a nonzero lisse Weil sheaf whose only lisse Weil subsheaves are $0$ and
$\mathcal M$ (irreducibility among lisse sheaves; equivalently the Weil
group acts irreducibly on the geometric generic stalk). Assume that
$\mathcal M$ is punctually $\iota$-pure of weight
$w$ and nonexceptional: none of its geometric irreducible constituents
is the restriction $\mathcal L_{\psi(ax)}|_U$ of a linear
Artin–Schreier sheaf, for any $a\in k$, the value $a=0$ (the trivial
rank-one sheaf) included. Then
$H_c^1(\mathbf A^1_{k_0},j_*\mathcal M)$ has
weights at most $w+1$.
