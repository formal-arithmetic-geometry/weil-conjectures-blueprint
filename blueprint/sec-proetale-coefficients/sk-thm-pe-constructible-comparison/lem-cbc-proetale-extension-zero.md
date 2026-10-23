+++
id = "lem-cbc-proetale-extension-zero"
kind = "lemma"
title = "Extension by zero on the pro-etale site"
lean = ["AlgebraicGeometry.ProEtale.openImmersionLowerShriek", "AlgebraicGeometry.ProEtale.openImmersionLowerShriekUpperStarAdjunction", "AlgebraicGeometry.ProEtale.preservesFiniteLimits_openImmersionLowerShriek", "AlgebraicGeometry.ProEtale.nonempty_iso_mapDerivedCategory_upperStar_openImmersionLowerShriek", "AlgebraicGeometry.ProEtale.isZero_mapDerivedCategory_upperStar_openImmersionLowerShriek"]
order = 1050
uses = ["def-weil-extension-by-zero", "def-weil-pbc-derived-categories", "def-weil-pbc-proetale-site", "def-weil-pbc-scheme-conventions"]
+++
For an open immersion
$j:U\hookrightarrow X$, extension by zero on the small pro-etale
site (the functor $j_!$ of [def-weil-extension-by-zero])
is the exact left adjoint of $j^{-1}$ and acts degreewise on complexes. It
has the stalk prescription of the etale extension by zero: for a complex $K$
of pro-etale sheaves on $U$ and a morphism $s:T\to X$, for instance a
geometric point $\bar x$ of $X$,

$$
s^{-1}j_!K\cong
\begin{cases}
t^{-1}K,&s=j\circ t\text{ factors through }U,\\
0,&s(T)\cap U=\emptyset.
\end{cases}
$$

In particular $(j_!K)_{\bar x}=K_{\bar x}$ if $\bar x$ lies in $U$, and
$(j_!K)_{\bar x}=0$ if $\bar x$ lies in $X\setminus U$.
