+++
id = "thm-amb-vector-bundle-purity"
kind = "theorem"
title = "Vector-bundle purity before smooth orientation"
order = 3269
uses = ["cor-amb-affine-space-adjunction", "def-amb-vector-integration", "def-asd-vector-bundle-zero-section", "def-coefficient-twists-detailed", "def-weil-pbc-derived-categories", "lem-amb-etale-adjoint-locality", "lem-amb-proper-coproducts-projection", "lemma-weil-pbc-geometric-stalk-conservative", "thm-amb-etale-exceptional-adjoint"]
+++
Let $\pi:E\to S$ be a vector bundle of rank $d$
over a Noetherian scheme. For every complex $K$ of
etale $A$-modules on $S$, the adjoint of

$$
R\pi_!(\pi^*K(d)[2d])
\cong K\otimes_A^LR\pi_!A_E(d)[2d]
\xrightarrow{1\otimes t_\pi}K
$$

is an isomorphism

$$
\pi^*K(d)[2d]\xrightarrow{\sim}\pi^\times K.
$$

The notation refers to Tate twists, and vector-bundle integration.
