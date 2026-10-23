+++
id = "prop-a1-fourier-middle-extension"
kind = "theorem"
tags = ["latex:proposition"]
title = "Fourier transform of an irreducible middle extension"
order = 3996
uses = ["def-a1-constituent-nonexceptional", "def-fd-kernel", "def-fd-transform", "def-per-perverse-subcategories", "def-wf-middle-extension", "def-wf-tate-twist", "lem-fd-as-characters", "lem-fd-base-change", "lem-fd-first-formula", "lem-fd-inversion", "prop-a1-curve-perverse-simples", "prop-base-linear", "rem-dl-a1-conventions", "thm-a1-curve-perverse-heart", "thm-a1-fourier-t-exact"]
lean = ["AlgebraicGeometry.exists_middleExtension_fourierTransform"]
+++
In the conventions of [rem-dl-a1-conventions], let $\psi$ be a
nontrivial additive character of $k_0$, let
$j:U_0\hookrightarrow A_0$ be a dense open immersion and let
$\mathcal M$ be a nonzero irreducible lisse Weil sheaf on $U_0$ which is
constituent-nonexceptional in the sense of
[def-a1-constituent-nonexceptional]. Then there are a dense open
immersion $j':U'_0\hookrightarrow A'_0$ into the dual line and a nonzero
irreducible lisse Weil sheaf $\mathcal M'$ on $U'_0$ such that the
Fourier–Deligne transform of [def-fd-transform] of the middle extension
of [def-wf-middle-extension] satisfies

$$
\operatorname{FT}_\psi\bigl((j_*\mathcal M)[1]\bigr)\cong
(j'_*\mathcal M')[1].
$$
