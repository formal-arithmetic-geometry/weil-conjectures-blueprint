+++
id = "lemma-weil-pbc-curve-dense-open-reduction"
kind = "lemma"
title = "Dense-open localization reduction"
order = 1246
uses = ["def-constructible-constructible", "def-constructible-stratification", "lemma-weil-pbc-curve-constructible-primary-reduction", "lemma-weil-pbc-eight-curve-devissage", "prop-constructible-generic-constancy"]
+++
Let $X$ be a reduced separated curve of finite type over an algebraically
closed field $k$, and let $F$ be a constructible sheaf of
$\mathbf F_\ell$-modules on $X_{\Et}$. There is a dense open immersion
$j:U\hookrightarrow X$ with $U=\coprod_aU_a$ a finite disjoint union of
irreducible opens and $G=j^{-1}F$ finite locally constant. With
$i:Z=X\setminus U\hookrightarrow X$, the complement $Z$ is a finite set of
closed points, and the sequence

$$
0\longrightarrow j_!G\longrightarrow F
\longrightarrow i_*i^{-1}F\longrightarrow0
$$

is exact. The eight assertions $\mathcal C_1,\dots,\mathcal C_8$ (vanishing,
finiteness, invariance under algebraically closed extension of $k$, and
surjectivity of $H^2$ onto opens) hold for $(X,F)$ if and only if they hold
for $(X,j_!G)$, and they hold for $(X,j_!G)$ if they hold for
$(X,j_{a,!}(G|_{U_a}))$ for every $a$, where $j_a:U_a\hookrightarrow X$.
