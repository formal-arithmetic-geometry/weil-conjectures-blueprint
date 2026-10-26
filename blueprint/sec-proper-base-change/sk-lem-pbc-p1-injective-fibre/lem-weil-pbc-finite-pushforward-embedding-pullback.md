+++
id = "lem-weil-pbc-finite-pushforward-embedding-pullback"
kind = "lemma"
title = "The inverse image of an embedding into finite pushforwards of constant sheaves is again such an embedding"
uses = ["def-weil-pbc-direct-image", "def-weil-pbc-etale-sheaves", "def-weil-pbc-inverse-image", "def-weil-pbc-scheme-conventions"]
lean = ["AlgebraicGeometry.Etale.exists_mono_biproduct_lowerStar_upperStar"]
order = 1557
+++
Let $\nu:X\to X'$ be a morphism of schemes [def-weil-pbc-scheme-conventions], $\Lambda$ a commutative ring and $F'$ a sheaf of $\Lambda$-modules on $X'_{\Et}$ [def-weil-pbc-etale-sheaves]. Let $n\ge0$ and, for $i=1,\dots,n$, let $f_i:Y_i\to X'$ be a finite morphism which is locally of finite presentation and $M_i$ a $\Lambda$-module, and let $\varphi:F'\hookrightarrow\bigoplus_{i=1}^nf_{i,*}\underline{M_i}$ be a monomorphism into the finite direct sum in $\Mod(X'_{\Et},\Lambda)$, where $\underline{M_i}$ is the constant sheaf of $\Lambda$-modules with value $M_i$ on $Y_{i,\Et}$ and $f_{i,*}$ is the direct image [def-weil-pbc-direct-image]. Then there are, for $i=1,\dots,n$, a finite morphism $g_i:Y'_i\to X$ locally of finite presentation (one may take the base change $Y'_i=Y_i\times_{X'}X$, $g_i$ the second projection) and a monomorphism of sheaves of $\Lambda$-modules $\nu^{-1}F'\hookrightarrow\bigoplus_{i=1}^ng_{i,*}\underline{M_i}$ in $\Mod(X_{\Et},\Lambda)$, with the same $M_i$, where $\nu^{-1}$ is the inverse image [def-weil-pbc-inverse-image].
