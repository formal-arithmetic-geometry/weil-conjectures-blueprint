+++
id = "lem-fd-character-parametrization"
kind = "lemma"
title = "Parametrization of the additive characters"
order = 2916
uses = ["def-fd-additive-character", "lem-fd-character-orthogonality"]
+++
For $k_0=\mathbf F_q$, every nondegenerate additive character of
$k_0$ is $\psi_a(x)=\psi(ax)$ for a unique $a\in k_0^\times$.

## Proof

Both $\psi$ and the given character $\psi'$ are nontrivial
homomorphisms of the cyclic group $(k_0,+)$, so $\psi'=\psi_a$ for
some $a\in k_0^\times$ (two nontrivial characters of a cyclic group
differ by the multiplication of the argument by the unique
$a=\psi'-\psi$-ratio); uniqueness of $a$ is the orthogonality of
[lem-fd-character-orthogonality], which separates the
$\psi_a$ for distinct $a$.
