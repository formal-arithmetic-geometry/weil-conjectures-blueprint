+++
id = "lem-fd-transform-hc0-vanishing"
kind = "lemma"
title = "No compactly supported sections in the transform; the Kiehl–Weissauer property (b)"
order = 4242
uses = ["def-fd-transform", "def-weil-ordinary-compact-cohomology", "def-wf-tate-twist", "lem-fd-inversion", "lem-fd-stalk-at-origin"]
+++
Let $j:U_0\hookrightarrow\mathbf A^1_{k_0}$ be a dense open immersion and
let $\mathcal M$ be a lisse Weil sheaf on $U_0$. Then, for the
Fourier–Deligne transform and the
compact-support convention of
[def-weil-ordinary-compact-cohomology],

$$
H^0_c\bigl(\mathbf A^1_{k_0},\operatorname{FT}_\psi(j_!\mathcal M)\bigr)=0 .
$$

## Proof

Let $\mathcal G':=\operatorname{FT}_\psi(j_!\mathcal M)$. By the origin
stalk formula [lem-fd-stalk-at-origin], applied to the input
$\mathcal G'$ and the character $\psi^{-1}$, the fibre of the transform
of $\mathcal G'$ at the origin is

$$
\bigl(\operatorname{FT}_{\psi^{-1}}(\mathcal G')\bigr)_{0'}
=R\Gamma_c\bigl(\mathbf A^1_{k_0},\mathcal G'\bigr)[1],
$$

so its degree $(-1)$ cohomology is $H^0_c(\mathbf A^1_{k_0},\mathcal G')$. Fourier inversion [lem-fd-inversion] for the line
($r=1$) identifies
$\operatorname{FT}_{\psi^{-1}}\operatorname{FT}_\psi(j_!\mathcal M) \cong j_!\mathcal M(-1)$, the Tate twist of
[def-wf-tate-twist]; the right-hand side is a sheaf concentrated in
degree $0$, so its degree $(-1)$ cohomology vanishes. Hence
$H^0_c(\mathbf A^1_{k_0},\mathcal G')=0$.
