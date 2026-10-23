+++
id = "thm-fd-generic-fourier-sheaf-pure"
kind = "theorem"
tags = ["latex:proposition"]
title = "The generic Fourier sheaf is pure of some weight"
order = 4004
uses = ["cor-wf-unramified-boundary-purity", "def-a1-constituent-nonexceptional", "def-fd-transform", "def-weil-punctual-weights", "def-wf-determinantal-weight", "def-wf-iota-real", "def-wf-middle-extension", "fin2-lem-lisse-dense-open", "lem-a1-constituent-nonexceptional-comparison", "lem-fd-constituent-nonexceptional-concentration", "lem-fd-realified-kernel-real", "lem-fd-realness-pushforward", "prop-a1-fourier-middle-extension", "prop-fd-zero-extension-comparison", "rem-dl-a1-conventions", "thm-rp-real-lisse-purity-affine"]
lean = ["AlgebraicGeometry.exists_isPunctuallyPureOfWeight_of_isFourierPartner"]
+++
In the conventions of [rem-dl-a1-conventions], let $\psi$ be a
nontrivial additive character of $k_0$, let
$j:U_0\hookrightarrow A_0=\mathbf A^1_{k_0}$ be a dense open immersion
and let $\mathcal M$ be a nonzero irreducible lisse Weil sheaf on $U_0$
(irreducible among lisse Weil sheaves: its only lisse Weil subsheaves are
$0$ and $\mathcal M$) which is constituent-nonexceptional in the sense of
[def-a1-constituent-nonexceptional] and punctually $\iota$-pure of
weight $w$. Let $j':U'_0\hookrightarrow A'_0$ be a dense open immersion
into the dual line and $\mathcal M'$ a lisse Weil sheaf on $U'_0$
(such data exist by [prop-a1-fourier-middle-extension]) with

$$
\operatorname{FT}_\psi\bigl((j_*\mathcal M)[1]\bigr)\cong(j'_*\mathcal M')[1].
$$

Then $\mathcal M'$ is punctually $\iota$-pure, on all of $U'_0$, of some
real weight $v$ (in the sense of [def-weil-punctual-weights]).
