+++
id = "sk-prop-hilbert90"
kind = "proposition"
title = "Hilbert 90"
order = 883
uses = ["sk-def-av-pic", "sk-def-curve"]
lean = ["AlgebraicGeometry.Scheme.subsingleton_cohomologicalPicardGroup_of_field"]
tags = ["sketch"]
+++
Let $X$ be a scheme (e.g. $C$ as in [sk-def-curve]). The natural
maps are isomorphisms of abelian groups

$$
\{\text{invertible }\mathcal O_X\text{-modules}\}/{\cong}
\;\xrightarrow{\ \sim\ }\;
H^1(X_{\mathrm{Zar}},\mathcal O_X^\times)\;\xrightarrow{\ \sim\ }\;
H^1(X_{\Et},\mathbb G_m),
$$

the composite sending the class of an invertible module
$\mathcal L$ to the class of the $\mathbb G_m$-torsor
$\underline{\mathrm{Isom}}(\mathcal O_X,\mathcal L)$. In particular
$H^1(\Spec K,\mathbb G_m)=0$ for a field $K$.
