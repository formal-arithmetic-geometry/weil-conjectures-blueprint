+++
id = "thm-a1-fourier-t-exact"
kind = "theorem"
title = "The Fourier transform is perverse t-exact on the line"
order = 3093
uses = ["def-per-perverse-subcategories", "def-per-support-condition", "def-fd-transform", "def-wf-tate-twist", "rem-dl-a1-conventions", "thm-a1-curve-perverse-heart", "thm-fd-fourier-perverse", "thm-fd-transform-well-defined", "lem-fd-base-change", "lem-fd-stalk-formula", "lem-zl-affine-curve-range", "lem-a1-affine-hc2", "lem-fd-as-characters", "lem-fd-cohomology-affine-line-character", "lem-fd-inversion", "prop-base-linear"]
+++
In the conventions of [rem-dl-a1-conventions], let
$\operatorname{FT}_\psi$ be the Fourier–Deligne transform of
[def-fd-transform] from the line $A_0$ to the dual line $A'_0$, and
write $\mathrm{Perv}(A_0)$, $\mathrm{Perv}(A'_0)$ for the hearts of the
perverse t-structure of [thm-a1-curve-perverse-heart], built from the
classes ${}^pD^{\le0}$, ${}^pD^{\ge0}$ of
[def-per-perverse-subcategories]. Then $\operatorname{FT}_\psi$ is
t-exact:

$$
\operatorname{FT}_\psi\bigl({}^pD^{\le0}(A_0)\bigr)\subset{}^pD^{\le0}(A'_0),
\qquad
\operatorname{FT}_\psi\bigl({}^pD^{\ge0}(A_0)\bigr)\subset{}^pD^{\ge0}(A'_0),
$$

so it sends $\mathrm{Perv}(A_0)$ into $\mathrm{Perv}(A'_0)$, and
likewise $\operatorname{FT}_{\psi^{-1}}$ (from $A'_0$ to $A_0$) is
t-exact and sends $\mathrm{Perv}(A'_0)$ into $\mathrm{Perv}(A_0)$. This
sharpens the amplitude bound $[-1,1]$ of [thm-fd-fourier-perverse] to
amplitude $0$. Moreover, with the Tate twist of [def-wf-tate-twist],
the functors

$$
\operatorname{FT}_\psi:\mathrm{Perv}(A_0)\rightleftarrows\mathrm{Perv}(A'_0):
G:=\operatorname{FT}_{\psi^{-1}}(-)(1)
$$

are mutually quasi-inverse exact equivalences of abelian categories.
