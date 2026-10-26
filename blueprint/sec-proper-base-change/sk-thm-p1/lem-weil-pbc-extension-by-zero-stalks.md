+++
id = "lem-weil-pbc-extension-by-zero-stalks"
kind = "lemma"
title = "Geometric stalks of extension by zero along an open immersion"
uses = ["def-weil-pbc-extension-by-zero", "def-weil-pbc-geometric-stalks"]
lean = ["AlgebraicGeometry.Etale.openImmersionLowerShriekCompUliftSheafFiberIso", "AlgebraicGeometry.Etale.isZero_uliftSheafFiber_openImmersionLowerShriek_obj"]
order = 1734
+++
Let $\Lambda$ be a commutative ring ($\Lambda=\mathbf Z$ gives abelian sheaves), let $j:U\hookrightarrow X$ be an open immersion of schemes, let $F$ be a sheaf of $\Lambda$-modules on $U_{\Et}$ and $j_!F$ its extension by zero [def-weil-pbc-extension-by-zero], and let $\bar x:\operatorname{Spec}\Omega\to X$ be a geometric point. Stalks are taken as in [def-weil-pbc-geometric-stalks].
1. If the image of $\bar x$ lies in $j(U)$, then $\bar x$ factors uniquely as $\bar x=j\circ\bar u$ with $\bar u:\operatorname{Spec}\Omega\to U$, and the map sending the class of $s\in(j_{p!}F)(V)=F(V\xrightarrow{\varphi}U)$, for a pointed etale neighbourhood $(V,\bar v)$ of $\bar x$ with $V\to X$ factoring as $j\varphi$, to the class of $s$ in $F_{\bar u}$ (note $\varphi\bar v=\bar u$) induces an isomorphism $(j_!F)_{\bar x}\xrightarrow{\sim}F_{\bar u}$, natural in $F$ and $\Lambda$-linear.
2. If the image of $\bar x$ does not lie in $j(U)$, then $(j_!F)_{\bar x}=0$.
In short $(j_!F)_{\bar x}=F_{\bar u}$ for $\bar x=j\bar u$ in $U$ and $0$ for $\bar x$ in $X\setminus U$; this is the case of an open immersion of the formula $(j_!F)_{\bar x}=\bigoplus_{\bar u:\,j\bar u=\bar x}F_{\bar u}$ for etale $j$.
