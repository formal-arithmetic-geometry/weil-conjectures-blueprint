+++
id = "proposition-purity-lisse-part-fourier-transform--1"
kind = "proposition"
title = "Purity of the lisse part in weight zero"
name_showing = false
order = 1280001
aliases = ["bp-r396-1"]
lean = ["AlgebraicGeometry.exists_isPunctuallyPureOfWeight_of_isFourierPartner_weight_zero"]
uses = ["definition-weights", "proposition-fourier-transform-middle-extension"]
+++
Let $k_0=\Fq$, let $\ell\ne\operatorname{char}(k_0)$ be prime, and fix
an embedding $\iota:\Qbarl\hookrightarrow\C$ and a nontrivial additive
character $\psi:k_0\to\Qbarl^\times$. Let
$j:U_0\hookrightarrow\mathbf A^1_{k_0}$ and
$j':U'_0\hookrightarrow\mathbf A^{1\vee}_{k_0}$ be nonempty dense opens.
Suppose that $M$ is a nonzero irreducible lisse Weil sheaf on $U_0$,
punctually $\iota$-pure of weight zero, and that none of its geometric
irreducible constituents is the restriction of
$\mathcal L_{\psi(ax)}$ for any $a\in\bar k_0$, including $a=0$.
If $M'$ is a lisse Weil sheaf on $U'_0$ with

$$
\operatorname{FT}_\psi((j_*M)[1])\simeq(j'_*M')[1],
$$

then $M'$ is punctually $\iota$-pure of some real weight $v$ on all of
$U'_0$.
