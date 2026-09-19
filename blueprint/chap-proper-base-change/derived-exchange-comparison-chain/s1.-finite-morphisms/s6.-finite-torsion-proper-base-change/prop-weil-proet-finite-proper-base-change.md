+++
id = "prop-weil-proet-finite-proper-base-change"
kind = "theorem"
title = "Finite-torsion proper base change"
order = 750
tags = ["latex:proposition"]
uses = ["def-weil-pbc-derived-exchange", "lemma-weil-pbc-derived-exchange-coherence", "lemma-weil-pbc-torsion-assembly"]
+++
Let

$$
\begin{CD}
X'@>{g'}>>X\\
@V{f'}VV @VV{f}V\\
Y'@>{g}>>Y
\end{CD}
$$

be Cartesian with $f$ proper. For every torsion sheaf $F$ on
$X_{\mathrm{et}}$, the canonical exchange map

$$
g^{-1}Rf_*F\xrightarrow{\sim}Rf'_*g'^{-1}F
$$

is an isomorphism. These isomorphisms are natural in $F$, equal the identity
for identity squares, and commute with horizontal and vertical pasting.

## Proof

The torsion assembly proves the isomorphism in every cohomological degree for
the map constructed in S0. A morphism in $D^+$ is an isomorphism exactly when
all its cohomology sheaf maps are isomorphisms. Naturality, identity, and
pasting are the corresponding S0 coherence equations and survive each
devissage step. This is the expanded endpoint whose source locator is Tag
`095T`; that tag is not used as a proof leaf.
