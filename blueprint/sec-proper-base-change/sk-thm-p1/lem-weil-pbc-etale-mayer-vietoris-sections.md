+++
id = "lem-weil-pbc-etale-mayer-vietoris-sections"
kind = "lemma"
title = "Sections of a two-open etale cover form an equalizer"
uses = ["def-pc-scheme", "def-weil-pbc-etale-site"]
lean = ["AlgebraicGeometry.Etale.etale_mayerVietoris_sections"]
order = 1733
+++
Let $X$ be a scheme [def-pc-scheme], $U,V\subseteq X$ open subschemes with $U\cup V=X$, and $F$ an abelian sheaf on the small étale site $X_{\Et}$ [def-weil-pbc-etale-site]. Let $a:F(X)\to F(U)\oplus F(V)$, $a(s)=(s|_U,s|_V)$, and $b:F(U)\oplus F(V)\to F(U\cap V)$, $b(s,t)=s|_{U\cap V}-t|_{U\cap V}$, all restrictions being along the open immersions. Then $a$ is injective and $\ker b=\operatorname{im}a$, i.e. $0\to F(X)\xrightarrow{a}F(U)\oplus F(V)\xrightarrow{b}F(U\cap V)$ is exact. No injectivity assumption on $F$ is needed.
