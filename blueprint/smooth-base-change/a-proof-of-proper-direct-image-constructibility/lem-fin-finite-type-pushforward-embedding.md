+++
id = "lem-fin-finite-type-pushforward-embedding"
kind = "lemma"
title = "Finite-pushforward embeddings over a field"
order = 5189
lean = ["AlgebraicGeometry.Etale.IsConstructible.exists_embedding_finitePushforward_constant"]
uses = ["lem-fin-normal-generic-constant"]
+++
Let $X$ be of finite type over a field, and let $F$ be a constructible sheaf
of $\mathbf Z/N$-modules. There are finitely many finite maps
$h_i:Y_i\to X$, finite groups $M_i$ killed by $N$, and an injective map
$$
F\longrightarrow\bigoplus_i(h_i)_*\underline M_i.
$$

## Proof

Fix $x\in X$. The restriction of $F$ to $\operatorname{Spec}\kappa(x)$ is
finite locally constant. One member of a trivializing étale cover gives a
finite separable extension $K/\kappa(x)$ on which it becomes constant, say
$M$. Let $Z=\overline{\{x\}}_{\mathrm{red}}$, and normalize $Z$ in $K$. This
gives $h:Y\to Z\to X$, finite by the finiteness of normalization in a finite
extension. Its source is normal integral and Noetherian, with generic
inclusion $e:\operatorname{Spec}K\to Y$. Write $a=he$. The adjunction gives
$$
F\longrightarrow a_*a^*F\simeq h_*e_*\underline M\simeq h_*\underline M,
$$
where the last isomorphism is [lem-fin-normal-generic-constant].

At a geometric point above $x$, compose this map with evaluation at the
chosen generic geometric point of $Y$. The composite is the identity of
$F_{\bar x}=M$, by the unit–counit identity. Hence the displayed map is
injective at $\bar x$. It is a map of $\mathbf Z/N$-modules throughout.

Finitely many such $x$ suffice, by the finite-selection principle for
constructible sheaves on a Noetherian scheme.

Unresolved dependencies: def:weil-pbc-scheme-conventions, def:weil-pbc-constructible-complexes, def:weil-pbc-direct-image, def:weil-pbc-inverse-image, lem:fin-normalization-extension-finite, lem:weil-pbc-constructible-noetherian-finite-selection
