+++
id = "lem-kun-0f1h-sep-reduction"
kind = "lemma"
title = "Reduction to a separably closed ground field"
order = 2111
uses = ["def-kun-unbounded-exchange", "lem-kun-0f1c", "lem-kun-bc-base-change", "lem-kun-sep-closure-conservative"]
+++
Let $K$ be a field, let $j:U\to X$ be an open immersion of schemes
of finite type over $K$, and let $Y$ be a scheme of finite type
over $K$. Let $F$ be an abelian sheaf on $U_{\Et}$ whose stalks
are torsion of orders invertible in $K$. Form the cartesian square

$$
\begin{array}{ccc}
Y\times_KX&\xleftarrow{\;h\;}&Y\times_KU\\
\Big\downarrow{\scriptstyle q}&&\Big\downarrow{\scriptstyle p}\\
X&\xleftarrow{\;j\;}&U
\end{array}
$$

and let

$$
\beta:q^{-1}Rj_*F\longrightarrow Rh_*p^{-1}F
$$

be its exchange morphism, [def-kun-unbounded-exchange]. If the
analogous map $\beta_{K^{\mathrm{sep}}}$ in the square obtained by
extension of scalars from $K$ to $K^{\mathrm{sep}}$ is an
isomorphism, then $\beta$ is an isomorphism.
