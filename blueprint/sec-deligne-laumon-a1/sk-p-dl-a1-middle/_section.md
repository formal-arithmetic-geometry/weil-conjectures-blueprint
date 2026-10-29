+++
id = "sk-p-dl-a1-middle"
kind = "proposition"
title = "The Fourier partner"
order = 4214
uses = ["sk-i-restriction", "sk-lem-as-properties", "sk-lem-wft-curve-simples", "sk-p-dl-a1-perverse", "sk-thm-inversion"]
lean = ["AlgebraicGeometry.WeilSheaf.IsNonexceptional", "AlgebraicGeometry.WeilSheaf.LisseOnDenseOpen.IsFourierPartner", "AlgebraicGeometry.exists_middleExtension_fourierTransform", "AlgebraicGeometry.isNonexceptional_of_isUnramifiedAtInfinity"]
tags = ["sketch"]
+++
Let $M$ be an irreducible lisse Weil sheaf on a dense open
$j:U_0\hookrightarrow\mathbf A^1_{k_0}$ of a line. We call $M$
*Fourier-generic* (or *nonexceptional*) if none of its geometric
irreducible constituents is the restriction of the character sheaf
$\mathcal L_{\psi(ax)}$ of [sk-lem-as-properties] for some
$a\in\bar k_0$ (the case $a=0$ being the constant sheaf).

If $M$ is nonzero, irreducible and Fourier-generic, there
are a dense open $j':U'_0\hookrightarrow\mathbf A^{1\vee}_{k_0}$
and a nonzero irreducible lisse Weil sheaf $M'$ on it such that

$$
 \operatorname{FT}_\psi((j_*M)[1])\simeq(j'_*M')[1].
$$

We call $M'$ the *Fourier partner* of $M$.
If $M$ is unramified at infinity and is not geometrically constant,
then it is Fourier-generic.
