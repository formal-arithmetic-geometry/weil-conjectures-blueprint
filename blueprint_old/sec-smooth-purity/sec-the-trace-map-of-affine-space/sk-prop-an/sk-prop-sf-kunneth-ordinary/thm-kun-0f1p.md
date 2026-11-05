+++
id = "thm-kun-0f1p"
kind = "theorem"
title = "Kunneth formula, etale cohomology"
lean = ["AlgebraicGeometry.Etale.isIso_kunnethMap_of_isSepClosed", "AlgebraicGeometry.Etale.nonempty_iso_kunneth_of_isSepClosed"]
order = 3164
uses = ["def-kun-kunneth-map", "def-pc-separably-closed", "lem-kun-0f10", "lem-kun-0f12", "lem-kun-0f1n", "lem-kun-cd-sep-closed-point", "lem-kun-kunneth-via-0f1n", "lem-kun-leray-unbdd"]
+++
Let $k$ be a separably closed
field and let $X$ and $Y$ be schemes of finite type over $k$.
Let $n\ge1$ be an integer invertible in $k$. Then for
$E\in D(X_{\Et},\kunZn)$ and $K\in D(Y_{\Et},\kunZn)$ the
Kunneth map of [def-kun-kunneth-map]

$$
\kappa_{E,K}:\RGamma(X_{\Et},E)\kunotimes{\kunZn}\RGamma(Y_{\Et},K)
\longrightarrow
\RGamma\bigl((X\times_kY)_{\Et},
\pr_1^{-1}E\kunotimes{\kunZn}\pr_2^{-1}K\bigr)
$$

is an isomorphism.
