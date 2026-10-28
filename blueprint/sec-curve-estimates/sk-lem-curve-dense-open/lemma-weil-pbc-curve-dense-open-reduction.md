+++
id = "lemma-weil-pbc-curve-dense-open-reduction"
kind = "lemma"
title = "Dense-open localization reduction"
lean = ["AlgebraicGeometry.IsCurve.exists_dense_assertions_iff_lowerShriek"]
order = 1608
uses = ["def-constructible-constructible", "def-constructible-stratification", "def-weil-pbc-eight-curve-assertions", "prop-constructible-generic-constancy"]
+++
Let $X$ be a reduced separated curve of finite type over an algebraically
closed field $k$, let $\Lambda$ be a finite ring, $r$ a prime, and $F$ a
constructible sheaf of $\Lambda$-modules on $X_{\Et}$ with $rF=0$. There is
a dense open $j:U\hookrightarrow X$ whose connected components are
irreducible, such that $j^{-1}F$ is finite locally constant and the eight
assertions $\mathcal C_1,\dots,\mathcal C_8$ of
[def-weil-pbc-eight-curve-assertions] (vanishing, finiteness, invariance
under algebraically closed extension of $k$, and surjectivity of $H^2$ onto
opens) hold for $(X,F)$ if and only if they hold for $(X,j_!j^{-1}F)$.
