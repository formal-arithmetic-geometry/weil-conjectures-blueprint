+++
kind  = "proof"
of    = "det-cor-coefficient-heart-ii-generation"
+++
*Converse.* $a_!L$ is constructible: on $S$ it restricts to $L$, lisse, and on the strata of
$X\smallsetminus S$ (choose a stratification of $X$ containing $S$ as a stratum) it
restricts to $0$. So $a_!L[n]\in\Dbc$, and $\Dbc$ is closed under cones
([det-cor-coefficient-heart-ii-triangulated]).

*Single sheaves.* Let $F$ be constructible, with filtration $0=F_0\subset\dots\subset F_m=F$
and $F_k/F_{k-1}\cong a_{k!}L_k$ ([det-lem-coefficient-heart-filtration]). A short exact
sequence $0\to F_{k-1}\to F_k\to a_{k!}L_k\to0$ gives a distinguished triangle
$F_{k-1}\to F_k\to a_{k!}L_k\xrightarrow{\delta}F_{k-1}[1]$, so $F_k$ is isomorphic to the cone
of $\delta[-1]\colon a_{k!}L_k[-1]\to F_{k-1}$. By induction on $k$, $F=F_m$ is obtained by
$m$ cones; and so is every shift $F[n]$.

*Complexes.* Induct on the number $c(K)$ of nonzero cohomology sheaves. If $c(K)=0$ then
$K=0$, the cone of $0\to0$. Otherwise let $q$ be the largest degree with $\mathcal H^q(K)\ne0$.
The truncation triangle $\tau_{<q}K\to K\to\mathcal H^q(K)[-q]\xrightarrow{\delta}\tau_{<q}K[1]$
exhibits $K$ as the cone of $\delta[-1]\colon\mathcal H^q(K)[-q-1]\to\tau_{<q}K$. Both
$\tau_{<q}K$ (with $c=c(K)-1$, and with constructible cohomology) and $\mathcal H^q(K)[-q-1]$
(a shifted constructible sheaf) are obtained by finitely many cones from $\mathcal G$, so
$K$ is as well.
