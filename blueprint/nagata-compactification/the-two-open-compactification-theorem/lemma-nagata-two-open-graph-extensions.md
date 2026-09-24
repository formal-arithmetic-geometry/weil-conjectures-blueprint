+++
id = "lemma-nagata-two-open-graph-extensions"
kind = "lemma"
title = "Properties of the chosen graph extensions"
order = 465
lean = ["AlgebraicGeometry.exists_prepared_twoOpenSide"]
uses = ["def-nagata-two-open-graph-extensions", "lemma-nagata-graph-extension"]
+++
Each replacement $X_i\to X_i^{\mathrm{old}}$ is $U_i$-admissible;
the resulting structural morphism $X_i\to S$ is proper;
$\psi_i$ is proper, extends the inclusion $U_i\hookrightarrow U$, satisfies
$\psi_i^{-1}(U_i)=U_i$, and is an isomorphism over $U_i$.

## Proof

For each $i$, [lemma-nagata-graph-extension] says that the selected
replacement $X_i\to X_i^{\mathrm{old}}$ is $U_i$-admissible and that its
associated map $\psi_i$ is proper, extends $U_i\hookrightarrow U$, has
inverse image $\psi_i^{-1}(U_i)=U_i$, and is an isomorphism there. The
old structural map $X_i^{\mathrm{old}}\to S$ is proper by the selected
compactification, while an admissible blow-up is proper. Their composite,
which is the structural map of the replacement, is therefore proper.
