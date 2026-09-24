+++
id = "lemma-weil-pbc-epsilon-pullback"
kind = "lemma"
title = "Comparison inverse image commutes with pullback"
order = 1810
uses = ["def-weil-pbc-comes-from-etale", "def-weil-pbc-epsilon-comparison", "lemma-weil-pbc-epsilon-inverse-image-exact", "lemma-weil-pbc-epsilon-scheme-naturality"]
+++
For $u:X\to Y$ and $L\in D^+(Y_{\mathrm{et}},A)$ there is a natural
isomorphism

$$
Lu^*\epsilon_Y^{-1}L\xrightarrow{\sim}
\epsilon_X^{-1}Lu^*L.
$$

It is compatible with identities, composition, and both horizontal maps in a
Cartesian square.

## Proof

Lemma [lemma-weil-pbc-epsilon-scheme-naturality] identifies the two
composite site functors. Their inverse images are therefore sheafifications
of the same presheaf left Kan extension, and the identity on that presheaf
induces the displayed isomorphism. The identity and composition coherence
proved there gives the corresponding equations and the two horizontal maps
in a Cartesian square. Exactness of $\epsilon^{-1}$ and K-flat replacement
extend these equations to derived pullback.
