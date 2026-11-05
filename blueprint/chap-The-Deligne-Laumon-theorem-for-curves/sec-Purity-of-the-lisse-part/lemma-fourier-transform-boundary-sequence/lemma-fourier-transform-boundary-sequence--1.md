+++
id = "lemma-fourier-transform-boundary-sequence--1"
kind = "lemma"
title = "The Fourier correction sequence"
order = 1276001
aliases = ["bp-r393-1"]
lean = ["AlgebraicGeometry.WeilSheaf.LisseOnDenseOpen.FourierCorrection.fourierTransformExtensionByZeroIso", "AlgebraicGeometry.WeilSheaf.LisseOnDenseOpen.nonempty_fourierCorrection"]
+++
Let $\psi$ be nontrivial, let $j:U_0\hookrightarrow\mathbf A^1_{k_0}$
be a dense open, put $U=U_0\otimes_{k_0}\bar k_0$, and let $M$ be a nonzero irreducible lisse Weil
$\overline{\mathbf Q}_\ell$-sheaf on $U_0$ with no geometric irreducible
constituent of the form $\mathcal L_{\psi(ax)}|_{U}$ for $a\in\bar k_0$.
Fix a dense open $j':U'_0\hookrightarrow\mathbf A^{1\vee}_{k_0}$,
a lisse Weil sheaf $M'$ on $U'_0$, and an isomorphism
$\operatorname{FT}_\psi((j_*M)[1])\simeq(j'_*M')[1]$, as in
[proposition-fourier-transform-middle-extension]. No assumption on the
weights of $M$ is needed here; in [lemma-fourier-transform-boundary-sequence--2], $M$ is moreover pure of weight $w$.

Put $B=j_*M/j_!M$. There are Weil sheaves $G$ and $B'$ on the dual line
and isomorphisms
$\operatorname{FT}_\psi(j_!M)\simeq G$ and
$\operatorname{FT}_\psi(B)\simeq B'[1]$, together with a short exact sequence

$$
0\longrightarrow B'\longrightarrow G
\overset{g}{\longrightarrow} j'_*M'\longrightarrow0.
$$

Under the corresponding isomorphisms
$\operatorname{FT}_\psi(j_!M[1])\simeq G[1]$ and
$\operatorname{FT}_\psi(j_*M[1])\simeq(j'_*M')[1]$, the map $g[1]$
is the Fourier transform of the canonical map $j_!M[1]\to j_*M[1]$.
