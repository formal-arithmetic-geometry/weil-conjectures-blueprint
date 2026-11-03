+++
id = "sk-p-dl-a1-middle"
kind = "proposition"
title = "The Fourier transform of a middle extension"
order = 738
lean = ["AlgebraicGeometry.WeilSheaf.IsNonexceptional", "AlgebraicGeometry.WeilSheaf.LisseOnDenseOpen.IsFourierPartner", "AlgebraicGeometry.exists_middleExtension_fourierTransform", "AlgebraicGeometry.isNonexceptional_of_isUnramifiedAtInfinity"]
uses = ["sk-i-restriction", "sk-lem-as-properties", "sk-lem-wft-curve-simples", "sk-p-dl-a1-perverse", "sk-thm-inversion"]
tags = ["sketch"]
+++
Suppose that $M$ is nonzero and irreducible, and that none of its
geometric irreducible constituents is the restriction of
$\mathcal L_{\psi(ax)}$ for some $a\in\bar k_0$ (the case $a=0$ being
the constant sheaf). Then there
are a dense open $j':U'_0\hookrightarrow\mathbf A^{1\vee}_{k_0}$
and a nonzero irreducible lisse Weil sheaf $M'$ on it such that

$$
\operatorname{FT}_\psi((j_*M)[1])\simeq(j'_*M')[1].
$$

The sheaf $M'$ is determined by
$M$ up to isomorphism and shrinking of $U'_0$, since it is the
restriction to $U'_0$ of $\mathcal H^{-1}\operatorname{FT}_\psi((j_*M)[1])$.
If $M$ is unramified at infinity and is not geometrically constant,
then no geometric constituent of $M$ is of the form
$\mathcal L_{\psi(ax)}$.
