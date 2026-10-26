+++
id = "lem-weil-pbc-inverse-image-stalk-germ"
kind = "lemma"
title = "Stalk of an inverse image, compatible with germs of pulled-back sections"
lean = ["AlgebraicGeometry.inverseImage_stalk_germ"]
order = 1840
uses = ["def-pc-scheme", "def-weil-geometric-point", "def-weil-pbc-abelian-etale-sheaves", "def-weil-pbc-inverse-image", "def-weil-pbc-direct-image", "def-weil-pbc-geometric-stalks"]
tags = ["stacks-03Q1"]
+++
Let $f:Y\to X$ be a morphism of schemes [def-pc-scheme], $\bar y:\operatorname{Spec}\Omega\to Y$ a geometric point [def-weil-geometric-point] and $\bar x=f\circ\bar y$ the image geometric point of $X$. Let $G$ be an abelian sheaf on $X_{\Et}$ [def-weil-pbc-abelian-etale-sheaves], $f^{-1}G$ its inverse image with unit $\eta_{f,G}:G\to f_*f^{-1}G$ [def-weil-pbc-inverse-image], so that for $U\to X$ etale $\eta_{f,G}(U):G(U)\to(f_*f^{-1}G)(U)=(f^{-1}G)(U\times_XY)$ [def-weil-pbc-direct-image]. Stalks are those of [def-weil-pbc-geometric-stalks]. There is an isomorphism of abelian groups
$$c_{f,\bar y,G}:(f^{-1}G)_{\bar y}\xrightarrow{\ \sim\ }G_{\bar x},$$
natural in $G$, such that for every pointed etale neighbourhood $(U,\bar u)$ of $\bar x$ and every $a\in G(U)$, with $(U\times_XY,(\bar u,\bar y))$ the induced pointed etale neighbourhood of $\bar y$,
$$c_{f,\bar y,G}\bigl(\text{germ of }\eta_{f,G}(U)(a)\text{ at }(U\times_XY,(\bar u,\bar y))\bigr)=\text{germ of }a\text{ at }(U,\bar u).$$
In particular, for $U=X$ and $a\in G(X)$: $c_{f,\bar y,G}\bigl((\eta_{f,G}(X)(a))_{\bar y}\bigr)=a_{\bar x}$.
