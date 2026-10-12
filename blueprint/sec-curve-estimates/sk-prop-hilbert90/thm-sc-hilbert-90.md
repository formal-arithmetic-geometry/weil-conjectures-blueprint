+++
id = "thm-sc-hilbert-90"
kind = "theorem"
title = "Hilbert 90 for a scheme"
order = 888
uses = ["def-sc-gm-torsor", "def-sc-invertible-module", "lem-sc-line-bundle-torsor", "lem-sc-torsor-h1"]
+++
Let $X$ be a scheme (for instance a curve $C$ as in
[def-sc-curves]). The set of isomorphism classes of invertible
$\mathcal O_X$-modules ([def-sc-invertible-module]) is an
abelian group under $\otimes$, and the natural maps are isomorphisms
of abelian groups

$$
\{\text{invertible }\mathcal O_X\text{-modules}\}/{\cong}
\;\xrightarrow{\ \sim\ }\;
H^1(X_{\mathrm{Zar}},\mathcal O_X^\times)\;\xrightarrow{\ \sim\ }\;
H^1(X_{\Et},\mathbf G_m),
$$

the first sending $\mathcal L$ to the Zariski torsor
$\underline{\operatorname{Isom}}(\mathcal O_X,\mathcal L)$, the second
being the comparison map induced by the morphism of sites
$\varepsilon:X_{\Et}\to X_{\mathrm{Zar}}$ and
$\varepsilon^{-1}\mathcal O_X^{\times}\to\mathbf G_m$, and the
composite sending the class of $\mathcal L$ to the class of the
$\mathbf G_m$-torsor
$\underline{\operatorname{Isom}}(\mathcal O_{X_{\Et}},\mathcal L_{\Et})$.
