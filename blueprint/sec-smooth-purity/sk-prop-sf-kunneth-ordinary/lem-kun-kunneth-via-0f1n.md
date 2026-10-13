+++
id = "lem-kun-kunneth-via-0f1n"
kind = "lemma"
title = "Compatibility of the Kunneth map with the projection-formula variant"
order = 2126
uses = ["def-kun-kunneth-map", "def-kun-separably-closed", "def-kun-unbounded-exchange", "lem-kun-03qu-sep-closed", "lem-kun-0f12", "lem-kun-0f1n", "lem-kun-inverse-image-monoidal", "lem-kun-leray-unbdd"]
+++
Let $k$ be a separably closed
field, $n\ge1$ invertible in $k$, and let $X$
and $Y$ be schemes of finite type over $k$. Let
$E\in D(X_{\Et},\kunZn)$ and $K\in D(Y_{\Et},\kunZn)$. Then
the Kunneth map $\kappa_{E,K}$ of
[def-kun-kunneth-map] for the product square is equal to the
composite

$$
\begin{aligned}
&\RGamma(X_{\Et},E)\kunotimes{\kunZn}\RGamma(Y_{\Et},K)\\
&\quad\xrightarrow[\Cref{lem-kun-0f12}]{\ \sim\ }
\RGamma\bigl(X_{\Et},E\kunotimes{\kunZn}\underline{\RGamma(Y_{\Et},K)}\bigr)\\
&\quad\xrightarrow{\ \RGamma(X_{\Et},\varphi)\ }
\RGamma\bigl((X\times_kY)_{\Et},
\pr_1^{-1}E\kunotimes{\kunZn}\pr_2^{-1}K\bigr),
\end{aligned}
$$

where $\varphi$ is the map of [lem-kun-0f1n] for the
diagram

$$
\begin{array}{ccccc}
X&\xleftarrow{\;=\;}&X&\xleftarrow{\;\pr_1\;}&X\times_kY\\
\Big\downarrow{}&&\Big\downarrow{}&&\Big\downarrow{\scriptstyle \pr_2}\\
\Spec(k)&\longleftarrow&\Spec(k)&\xleftarrow{\;=\;}&Y
\end{array}
$$

and the last arrow uses the Leray identification of
[lem-kun-leray-unbdd].
