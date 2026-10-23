+++
id = "lem-kun-0f14a"
kind = "lemma"
title = "Kunneth formula, one proper factor, integer coefficients"
order = 3188
uses = ["def-kun-kunneth-map", "def-kun-rgamma-unbounded", "def-pc-separably-closed", "def-kun-torsion-invertible", "def-weil-pbc-scheme-conventions", "lem-kun-0f0e", "lem-kun-0f0f", "lem-kun-kunneth-map-agrees", "lem-kun-leray-bdd", "lem-kun-proper-stability", "lem-kun-pullback-constant", "lem-kun-tensor-sym", "thm-weil-pbc-bounded-below"]
+++
Let $k$ be a separably closed
field. Let $X$ be a
proper scheme over $k$
and let $Y$ be a
quasi-compact and
quasi-separated scheme over $k$. If $E\in\Dplus(X_{\Et})$ has
torsion cohomology and
$K\in\Dplus(Y_{\Et})$, then the Kunneth map of
[def-kun-kunneth-map] for the square

$$
\begin{array}{ccc}
X\times_kY&\xrightarrow{\;\operatorname{pr}_2\;}&Y\\
\Big\downarrow{\scriptstyle \operatorname{pr}_1}&&\Big\downarrow{\scriptstyle a_Y}\\
X&\xrightarrow{\;a_X\;}&\Spec(k)
\end{array}
$$

$$
\kappa_{E,K}:
\RGamma(X_{\Et},E)\kunotimes{\mathbf Z}\RGamma(Y_{\Et},K)
\longrightarrow
\RGamma\bigl((X\times_kY)_{\Et},
\pr_1^{-1}E\kunotimes{\mathbf Z}\pr_2^{-1}K\bigr)
$$

is an isomorphism.
