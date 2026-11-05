+++
id = "proposition-fourier-transform-middle-extension"
kind = "proposition"
title = "The Fourier transform of a middle extension"
order = 1264
lean = ["AlgebraicGeometry.exists_middleExtension_fourierTransform", "AlgebraicGeometry.WeilSheaf.IsNonexceptional"]
uses = ["definition-ind-etale-pro-etale-weakly", "lemma-stability", "definition-small-pro-etale-site", "proposition-pro-etale-coverings", "proposition-topos-functoriality", "example-locally-constant-functions-w-local", "proposition-sp-unique-adjoint", "lemma-artin-schreier-character-sheaf", "definition-compactification-refinement", "lemma-schematic-closure-uniqueness", "proposition-compactifying-union-two-opens", "lemma-affine-covers-dense-intersection"]
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
