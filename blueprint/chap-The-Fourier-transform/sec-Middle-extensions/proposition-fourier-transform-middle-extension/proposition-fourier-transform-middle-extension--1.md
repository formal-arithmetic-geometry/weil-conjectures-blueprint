+++
id = "proposition-fourier-transform-middle-extension--1"
kind = "proposition"
title = "A punctual transform forces a linear constituent"
name_showing = false
order = 1264001
aliases = ["bp-r391-1"]
lean = ["AlgebraicGeometry.WeilSheaf.LisseOnDenseOpen.exists_hasLinearArtinSchreierConstituent_of_iso", "AlgebraicGeometry.WeilSheaf.LisseOnDenseOpen.isEmpty_iso_fourierTransform_middleExtension_toComplex"]
uses = ["definition-lisse-sheaves", "definition-weil-structure", "lemma-artin-schreier-character-sheaf", "prose-16-06"]
+++
Let $k_0$ be a finite field, let $\ell\ne\operatorname{char}k_0$ be
prime, and let $\psi:k_0\to\overline{\mathbf Q}_\ell^\times$ be a
nontrivial additive character. Let $j:U_0\hookrightarrow\mathbf A^1_{k_0}$
be a dense open and $M$ a nonzero lisse Weil
$\overline{\mathbf Q}_\ell$-sheaf on $U_0$. If $G$ is a Weil sheaf of
finite support on the dual line and there is an isomorphism

$$
\operatorname{FT}_\psi((j_*M)[1])\simeq G[0],
$$

then some geometric irreducible constituent of $M$ is
$\mathcal L_{\psi(ax)}|_U$ for an $a\in\bar k_0$, where
$U=U_0\otimes_{k_0}\bar k_0$.

Consequently, if $M$ is also irreducible and none of its geometric
irreducible constituents is such a character, including $a=0$, there
is no such isomorphism for any Weil sheaf $G$ of finite support.
