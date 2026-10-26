+++
id = "cor-kun-compact-kunneth"
kind = "theorem"
title = "Künneth formula for compactly supported cohomology"
lean = ["AlgebraicGeometry.Etale.nonempty_iso_kunneth_compactSupport_of_isSepClosed"]
order = 3193
tags = ["latex:corollary"]
uses = ["def-compact-support-direct-image-detailed", "def-kun-kunneth-map", "def-weil-extension-by-zero", "thm-kun-0f1p"]
+++
Let $k$ be a separably closed
field, let $X$ and $Y$ be schemes of finite type over $k$, let
$n\ge1$ be an integer invertible in $k$, and let
$E\in D(X_{\Et},\kunZn)$, $K\in D(Y_{\Et},\kunZn)$. Choose
compactifications $j_X:X\hookrightarrow\overline X$ and
$j_Y:Y\hookrightarrow\overline Y$ over $k$, with $\overline X,\overline Y$
proper over $k$, and put
$R\Gamma_c(X_{\Et},E)=R\Gamma(\overline X_{\Et},j_{X,!}E)$ and similarly
for $Y$. Then the composite

$$
\begin{gathered}
R\Gamma_c(X_{\Et},E)\kunotimes{\kunZn}R\Gamma_c(Y_{\Et},K)
\\
\xrightarrow{\ \sim\ }
R\Gamma\bigl((X\times_kY)_{\Et},
\pr_1^{-1}j_{X,!}E\kunotimes{\kunZn}\pr_2^{-1}j_{Y,!}K\bigr)
\\
\xrightarrow{\ \sim\ }
R\Gamma_c\bigl((X\times_kY)_{\Et},
\pr_1^{-1}E\kunotimes{\kunZn}\pr_2^{-1}K\bigr)
\end{gathered}
$$

of the Künneth map of [thm-kun-0f1p] applied to $j_{X,!}E$ and
$j_{Y,!}K$ with the identification of the second line is an isomorphism;
the second arrow identifies
$\pr_1^{-1}j_{X,!}E\kunotimes{\kunZn}\pr_2^{-1}j_{Y,!}K$ with
$j_{X\times_kY,!}(\pr_1^{-1}E\kunotimes{\kunZn}\pr_2^{-1}K)$ along the
compactification $j_X\times_kj_Y$.
