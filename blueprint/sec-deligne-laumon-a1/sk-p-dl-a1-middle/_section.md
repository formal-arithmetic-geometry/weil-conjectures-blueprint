+++
id = "sk-p-dl-a1-middle"
kind = "proposition"
title = "Irreducible middle extensions under Fourier"
order = 3054
uses = ["sk-d-dl-a1-setup", "sk-i-dl-a1-local", "sk-thm-inversion"]
lean = ["AlgebraicGeometry.LAdicWeilSheaf.IsNonexceptional", "AlgebraicGeometry.LAdicWeilSheaf.LisseOnDenseOpen.IsFourierPartner", "AlgebraicGeometry.exists_middleExtension_fourierTransform", "AlgebraicGeometry.isNonexceptional_of_isUnramifiedAtInfinity"]
tags = ["sketch"]
+++
Let $\psi$ be nontrivial. Call a nonzero irreducible lisse Weil sheaf $M$ on $U_0$
*nonexceptional* if none of its geometric irreducible constituents
is $\mathcal L_{\psi(ax)}|_U$, for any $a\in k$, including $a=0$.
For such $M$, there are a dense open $j':U'_0\hookrightarrow A'_0$ and
a nonzero irreducible lisse Weil sheaf $M'$ with

$$
\DLAFT_\psi((j_*M)[1])\simeq(j'_*M')[1].
$$

If $M$ is unramified at infinity and not geometrically constant, it is
nonexceptional.
