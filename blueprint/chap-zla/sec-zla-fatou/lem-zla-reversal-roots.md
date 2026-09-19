+++
id = "lem-zla-reversal-roots"
kind = "lemma"
title = "Reciprocal roots and reversal"
order = 1017
uses = ["def-zla-reversal"]
+++
For $P$ as in [def-zla-reversal], the polynomial $P^{\mathrm{rev}}$ is
monic, and for every field $\Omega$ containing $\mathbf Q$ and every
$\alpha\in\Omega^\times$,

$$
P(\alpha^{-1})=0
\quad\Longleftrightarrow\quad
P^{\mathrm{rev}}(\alpha)=0.
$$

## Proof

Monicity is the coefficient $c_0=1$ of $P$ read in top degree after reversal.
The equivalence is the defining identity
$P^{\mathrm{rev}}(\alpha)=\alpha^bP(\alpha^{-1})$ together with
$\alpha\neq0$.
