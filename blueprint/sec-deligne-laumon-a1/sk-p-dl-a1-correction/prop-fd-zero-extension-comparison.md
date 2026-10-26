+++
id = "prop-fd-zero-extension-comparison"
kind = "theorem"
tags = ["latex:proposition"]
title = "The zero-extension comparison"
order = 4005
uses = ["def-a1-constituent-nonexceptional", "def-fd-artin-schreier-sheaf", "def-fd-kernel", "def-fd-transform", "def-weil-punctual-weights", "def-wf-middle-extension", "lem-fd-as-trace", "lem-fd-first-formula", "lem-wf-boundary-semicontinuity", "prop-a1-fourier-middle-extension", "rem-dl-a1-conventions", "thm-fd-transform-well-defined"]
lean = ["AlgebraicGeometry.WeilSheaf.LisseOnDenseOpen.FourierCorrection", "AlgebraicGeometry.WeilSheaf.LisseOnDenseOpen.nonempty_fourierCorrection", "AlgebraicGeometry.WeilSheaf.LisseOnDenseOpen.FourierCorrection.isLisse", "AlgebraicGeometry.WeilSheaf.LisseOnDenseOpen.FourierCorrection.hasWeightsAtMost"]
+++
In the conventions of [rem-dl-a1-conventions], let $\psi$ be a
nontrivial additive character of $k_0$, let
$j:U_0\hookrightarrow A_0$ be a dense open immersion with finite
complement $S_0$, and let $\mathcal M$ be a nonzero irreducible lisse
Weil sheaf on $U_0$ (irreducible among lisse Weil sheaves: its only lisse
Weil subsheaves are $0$ and $\mathcal M$) which is constituent-nonexceptional in the sense of
[def-a1-constituent-nonexceptional] and punctually $\iota$-pure of
weight $w$. Let $j':U'_0\hookrightarrow A'_0$ be a dense open immersion
into the dual line and $\mathcal M'$ a lisse Weil sheaf on $U'_0$ such
that $\operatorname{FT}_\psi\bigl((j_*\mathcal M)[1]\bigr)\cong
(j'_*\mathcal M')[1]$ for the transform of [def-fd-transform] (such
data exist by [prop-a1-fourier-middle-extension]), and put

$$
\mathcal B:=j_*\mathcal M/j_!\mathcal M ,
$$

with $j_*$ the middle extension of [def-wf-middle-extension]. Then there
are Weil sheaves $\mathcal G$ and $\mathcal B'$ on the dual line $A'_0$
such that

$$
\operatorname{FT}_\psi\bigl(j_!\mathcal M[1]\bigr)\cong\mathcal G[1],
\qquad
\operatorname{FT}_\psi(\mathcal B)\cong\mathcal B'[1],
\qquad
0\longrightarrow\mathcal B'\longrightarrow\mathcal G\longrightarrow
j'_*\mathcal M'\longrightarrow0 .
$$

The correction $\mathcal B'$ is lisse on the entire dual line $A'_0$, and
it has weights at most $w$: for every closed point $y$ of $A'_0$ and
every eigenvalue $\alpha$ of the local Frobenius $F_y$ on
$\mathcal B'_{\bar y}$,

$$
|\iota(\alpha)|^2\le q_y^{\,w}.
$$

In particular the transform of $j_!\mathcal M[1]$ is a sheaf shifted by
one without assuming geometric irreducibility of $\mathcal M$ or
unramifiedness at infinity.
