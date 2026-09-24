+++
id = "lemma-nagata-comparison-restrict-proper-open"
kind = "lemma"
title = "Restriction of the comparison image over the proper-extension open"
order = 542
lean = ["AlgebraicGeometry.exists_prepared_keyDisjoint_twoOpenSide"]
uses = ["def-nagata-global-blowup-cover-comparison", "def-nagata-isomorphism-near-closure", "def-nagata-two-open-comparison-space", "def-nagata-two-open-improved-comparison", "lemma-nagata-proper-to-separated-target", "lemma-nagata-scheme-image-of-closed-immersion", "lemma-nagata-scheme-image-restrict-open", "prop-nagata-global-blowup-cover-independent"]
+++
For $\{i,j\}=\{1,2\}$, the canonical morphism

$$
V_{12}=V_1\times_UV_2\longrightarrow p_i^{-1}(V_i)
$$

is an isomorphism. Under this identification,
$p_i^{-1}(V_i)\to V_i$ is the base change of
$\psi_j\colon V_j\to U$ along $\psi_i\colon V_i\to U$.

## Proof

Restrict the scheme-theoretic image defining $X_{12}$ to the open target
$V_i\times_SX_j\subseteq X_i\times_SX_j$. The inverse image of this
open in $V_{12}$ is all of $V_{12}$, so
[lemma-nagata-scheme-image-restrict-open] identifies
$p_i^{-1}(V_i)$ with the scheme-theoretic image of

$$
V_{12}\longrightarrow V_i\times_SX_j.
$$

The map $V_{12}\to V_i\times_SV_j$ is the pullback of the diagonal
$U\to U\times_SU$; it is therefore a closed immersion because
$U\to S$ is separated. Composing with the open immersion
$V_i\times_SV_j\to V_i\times_SX_j$ shows that the displayed map is an
immersion. It is also proper: its composite to $V_i$ is the base change
of the proper morphism $\psi_j$, while
$V_i\times_SX_j\to V_i$ is separated; apply
[lemma-nagata-proper-to-separated-target]. A proper immersion is a
closed immersion, so
[lemma-nagata-scheme-image-of-closed-immersion] identifies its
scheme-theoretic image with $V_{12}$ itself.
The first projection of the fibre square is the displayed map to $V_i$,
and its second component is the map to $V_j$. The universal property of
the fibre product gives the inverse identification with the base change of
$\psi_j$ along $\psi_i$, so the description of the projection is exactly
the one asserted.
