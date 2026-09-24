+++
id = "lem-weil-pbc-h1-constructible-representation"
kind = "lemma"
title = "Finite-pushforward representation of an $H^1$ class"
order = 1657
uses = ["def-weil-pbc-constructible-complexes", "def-weil-pbc-scheme-conventions", "lem-weil-pbc-constructible-approximation", "lem-weil-pbc-constructible-finite-pushforward"]
+++
Let $I$ be an injective sheaf of $\mathbf F_r$-modules on $X=\mathbf P^1_A$.
Every class $c\in H^1(X_0,I_0)$ is the image of a finite tuple of classes
belonging to sheaves

$$
 (h_i)_*\underline{M_i},
$$

where $h_i:V_i\to X$ is finite and finitely presented and $M_i$ is a finite
$\mathbf F_r$-module.

## Proof

View $c$ as the isomorphism class of an $I_0$-torsor. It is trivial on a
quasi-compact etale cover, so choosing local origins gives a Cech cocycle with
finitely many components; [lem-weil-pbc-constructible-approximation] supplies
a constructible $\mathbf F_r$-module sheaf $F$, a map $F\to I$, and lifts of
the finitely many cocycle components and equations.
[lem-weil-pbc-constructible-finite-pushforward] gives a monomorphism
$F\hookrightarrow\bigoplus_i(h_i)_*\underline{M_i}$, and injectivity of $I$
extends the map $F\to I$ across it. The image of the lifted tuple in
$\bigoplus_iH^1(X_0,(h_i)_*\underline{M_i}|_{X_0})$ maps to $c$, as the Cech
complexes are compatible.
