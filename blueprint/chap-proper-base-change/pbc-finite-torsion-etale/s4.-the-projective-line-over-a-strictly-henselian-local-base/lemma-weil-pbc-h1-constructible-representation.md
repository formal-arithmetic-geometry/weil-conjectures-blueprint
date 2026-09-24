+++
id = "lemma-weil-pbc-h1-constructible-representation"
kind = "lemma"
title = "Constructible representation of an $H^1$ class"
order = 1728
uses = ["lemma-weil-pbc-constructible-approximation", "lemma-weil-pbc-constructible-finite-pushforward"]
+++
For an injective sheaf $I$ of $\mathbf F_\ell$-modules on $\mathbf P^1_A$,
every class
$c\in H^1(X_0,I_0)$ admits finite $\mathbf F_\ell$-modules $M_i$, finite finitely presented
morphisms $h_i:V_i\to X$, and a map
$\bigoplus_i(h_i)_*\underline{M_i}\to I$ such that $c$ is the image of a
tuple of classes in
$\bigoplus_iH^1(X_0,(h_i)_*\underline{M_i}|_{X_0})$.

## Proof

View $c$ as the isomorphism class of an $I_0$-torsor. It is trivial on an
etale cover; quasi-compactness of $X_0$ selects finitely many members
$U_a\to X_0$. Choosing local origins gives a Cech cocycle
$z=(z_{ab})$ with

$$
z_{ab}\in I_0(U_a\times_{X_0}U_b),\qquad
z_{bc}-z_{ac}+z_{ab}=0
$$

on every triple overlap. There are finitely many sections and equations.
Constructible approximation therefore supplies a constructible sheaf $F$, a
map $\alpha:F\to I$, and lifts $\widetilde z_{ab}\in F_0(U_{ab})$
satisfying the same equations and mapping to $z_{ab}$.

The finite-pushforward lemma gives a monomorphism
$\iota:F\hookrightarrow F'=\bigoplus_{i=1}^r(h_i)_*\underline{M_i}$.
Injectivity of $I$ extends $\alpha$ across $\iota$ to a map
$\psi:F'\to I$. The sheaf square and the three relevant terms of the Cech
complex form the commuting three-row diagram

$$
\begin{CD}
F @>{\iota}>> F' @>>> \operatorname{coker}(\iota)\\
@V{\alpha}VV @V{\psi}VV @VVV\\
I @= I @>>> 0\\[2pt]
@VVV @VVV @VVV\\
\prod_a I_0(U_a) @>{d^0}>>
\prod_{a,b} I_0(U_{ab}) @>{d^1}>>
\prod_{a,b,c} I_0(U_{abc}).
\end{CD}
$$

Here the bottom vertical maps mean restriction followed by the indicated
Cech cochain inclusion; commutativity in degrees $0,1,2$ follows from
functoriality of restriction. The cocycle $\iota(\widetilde z)$ defines
$c'\in H^1(X_0,F'_0)$ and $\psi_0(c')=c$.

Finite direct sums commute with $H^1$, while exact finite direct image and
Leray give

$$
H^1(X_0,F'_0)=
\bigoplus_{i=1}^rH^1(X_0,(h_i)_*\underline{M_i}|_{X_0})
=\bigoplus_{i=1}^rH^1((V_i)_0,\underline{M_i}).
$$

Thus $c'$ is the required finite tuple, and the displayed map $F'\to I$
sends that tuple to the original class.
