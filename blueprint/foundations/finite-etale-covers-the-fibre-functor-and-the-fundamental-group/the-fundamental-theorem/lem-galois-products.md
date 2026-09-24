+++
id = "lem-galois-products"
kind = "lemma"
title = "Products of Galois covers"
order = 2083
uses = ["def-galois-categories", "def-galois-object", "def-weil-pbc-scheme-conventions", "lem-fet-galois-category", "lem-galois-axioms", "lem-galois-object-degree"]
+++
Let $Y$ be connected with geometric point $\bar y$, and let $Q,Q'$ be
Galois covers. Then every connected component $Z$ of $Q\times_YQ'$ is
Galois over $Y$, and it dominates $Q$ and $Q'$.

## Proof

The product $Q\times_YQ'$ of the
Galois covers $Q,Q'$ of
[def-galois-object] is a finite etale $Y$-scheme, i.e. an object
of $\mathrm{F\acute Et}(Y)$ in the sense of
[def-galois-categories] with the fibre products of
[def-weil-pbc-scheme-conventions]; being finite etale over the
connected $Y$, its
connected components are open and closed and each of them surjects onto
$Y$, hence the projections from a component $Z$ to $Q$ and to $Q'$
are surjective, which is the domination statement. By
[lem-galois-axioms](6) applied in the Galois category
$\mathrm{F\acute Et}(Y)$ ([lem-fet-galois-category]) the group
$H=\operatorname{Aut}_Y(Q)\times\operatorname{Aut}_Y(Q')$ acts simply
transitively on the fibre
$F_{\bar y}(Q\times_YQ')=F_{\bar y}(Q)\times F_{\bar y}(Q')$, because each
factor does. For $z\in F_{\bar y}(Z)$ and any $z'\in F_{\bar y}(Z)$
there is a unique $h\in H$ with $h(z)=z'$; as both $z$ and $z'$
lie in the fibre of the connected component $Z$, and components are
determined by their fibres over the connected base $Y$, the element $h$
maps $Z$ to $Z$. Hence the stabilizer of $Z$ in $H$ acts
transitively on $F_{\bar y}(Z)$, so
$\#\operatorname{Aut}_Y(Z)\ge\#F_{\bar y}(Z)$, while
$\#\operatorname{Aut}_Y(Z)\le\#F_{\bar y}(Z)$ by
[lem-galois-axioms](6). Therefore equality holds and $Z$ is a
Galois cover by [lem-galois-object-degree].
