+++
id = "lem-kun-bc-kunneth-compat"
kind = "lemma"
title = "Cohomology of the base change map through the Kunneth identification"
order = 1770
uses = ["def-kun-kunneth-map", "def-kun-projective", "def-kun-unbounded-exchange", "lem-kun-0f14b", "lem-kun-leray-bdd", "lem-kun-open-immersion-restriction", "lem-kun-tensor-unit"]
+++
Let $K$ be a separably closed field, let $j:U\to X$ be an open
immersion of schemes of finite type over $K$, let $Y$ be a
projective scheme over $K$, and let
$F$ be a sheaf of $\kunZn$-modules on $U_{\Et}$ with $n$
invertible in $K$. Consider the diagram

$$
\begin{array}{ccc}
Y\times_KX&\xleftarrow{\;h\;}&Y\times_KU\\
\Big\downarrow{\scriptstyle q}&&\Big\downarrow{\scriptstyle p}\\
X&\xleftarrow{\;j\;}&U .
\end{array}
$$

Then $\RGamma$ of the base change map
$q^{-1}Rj_*F\to Rh_*p^{-1}F$ of
[def-kun-unbounded-exchange], under the Kunneth isomorphisms of
[lem-kun-0f14b] (applied to the pairs $(Y,X)$ and $(Y,U)$
with the constant coefficient $\underline{\kunZn}$) and the Leray
identification of [lem-kun-leray-bdd], is identified with the
identity of
$\RGamma(Y_{\Et},\underline{\kunZn})\kunotimes{\kunZn}\RGamma(U_{\Et},F)$.
