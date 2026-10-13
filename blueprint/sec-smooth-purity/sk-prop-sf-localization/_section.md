+++
id = "sk-prop-sf-localization"
kind = "proposition"
title = "Supported localization"
order = 2209
uses = ["sk-lem-sf-determination", "sk-prop-sf-closed-unit", "sk-prop-sf-open-closed-triangle"]
lean = ["AlgebraicGeometry.Etale.existsUnique_distTriang_supportedLocalization"]
tags = ["sketch"]
+++
Let $i:Z\hookrightarrow X$ be a closed immersion of schemes which admits a
compactification, and let $j:U\hookrightarrow X$ be an open immersion whose
image is the complement of the image of $i$. Let the coefficients be a
Grothendieck abelian category $\mathcal A$ with a closed symmetric monoidal
structure admitting functorial flat resolutions (for instance
$\Lambda$-modules), with the derived operations of [sk-def-sf-operations]; as
$i$ is proper, $Ri_!=Ri_*$. For every $L\in D(X_{\Et},\mathcal A)$
(unbounded), the counit of $Ri_!\dashv Ri^!$ and the unit of
$Lj^*\dashv Rj_*$ extend to a distinguished triangle

$$
Ri_!Ri^!L\longrightarrow L\longrightarrow Rj_*Lj^*L\xrightarrow{\ \delta_L\ }
Ri_!Ri^!L[1],
$$

and $\delta_L$ is the unique map $Rj_*Lj^*L\to Ri_!Ri^!L[1]$ making this
triangle distinguished.

Moreover, since the images of $i$ and $j$ are disjoint,
$\operatorname{Hom}((Ri_!B)[n],Rj_*C)=0$ for all $B\in D(Z_{\Et},\mathcal A)$,
$C\in D(U_{\Et},\mathcal A)$ and $n\in\mathbf Z$, and the triangle is natural in
$L$: for $f:L\to L'$ the triple $(Ri_!Ri^!f,f,Rj_*Lj^*f)$ is a morphism of
triangles, and it is the only one with middle component $f$.
