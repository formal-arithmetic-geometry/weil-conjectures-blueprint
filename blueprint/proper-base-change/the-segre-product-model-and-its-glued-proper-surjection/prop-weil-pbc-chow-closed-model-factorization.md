+++
id = "prop-weil-pbc-chow-closed-model-factorization"
kind = "theorem"
title = "Closed model and factorization of the glued morphism"
order = 1099
lean = ["AlgebraicGeometry.ChowModification.isClosedImmersion_toProjectiveSpace", "AlgebraicGeometry.ChowModification.toProjectiveSpace_over"]
uses = ["lem-weil-pbc-chow-proper-surjective-isomorphism", "lem-weil-pbc-chow-product-image-model", "lem-weil-pbc-chow-segre-closed-immersion"]
+++
In the situation of [lem-weil-pbc-chow-proper-surjective-isomorphism], the
composite

$$
 i:X'\hookrightarrow\widetilde X\hookrightarrow Z
 \hookrightarrow\prod_{i=1}^m\mathbf P^{n_i}_Y
 \xrightarrow{\ s\ }\mathbf P^N_Y,\qquad N=\prod_{i=1}^m(n_i+1)-1,
$$

of the open immersion $X'\subseteq\widetilde X$, the closed immersion
$\widetilde X\hookrightarrow Z$ of
[lem-weil-pbc-chow-product-image-model], the product of the closed immersions
$Z_i\hookrightarrow\mathbf P^{n_i}_Y$, and the Segre embedding
([lem-weil-pbc-chow-segre-closed-immersion]) is a closed immersion, and
$f\circ\pi$ equals the composite of $i$ with $\mathbf P^N_Y\to Y$.

## Proof

By [lem-weil-pbc-chow-proper-surjective-isomorphism], $\pi$ is proper and
surjective and $\pi^{-1}(U)\xrightarrow{\sim}U$. The composite $i$ is a
composite of the open immersion $X'\subseteq\widetilde X$ with closed
immersions (the closed immersion $\widetilde X\hookrightarrow Z$, the product
of the closed immersions $Z_i\hookrightarrow\mathbf P^{n_i}_Y$, and the Segre
embedding), hence an immersion. Its source $X'$ is proper over $Y$: the
composite of the proper surjective $\pi$ with the proper $f$ is proper; its
target $\mathbf P^N_Y$ is separated over $Y$, so $i$ is proper, and a proper
immersion is a closed immersion. Finally $f\circ\pi$ and the composite of $i$
with $\mathbf P^N_Y\to Y$ are both the structure morphism of the $Y$-scheme
$X'$, since every morphism in the display is a morphism of $Y$-schemes, as in
the last paragraph of the proof of
[lem-weil-pbc-chow-proper-surjective-isomorphism].

Unresolved dependencies: def:weil-pbc-scheme-conventions, lem:weil-pbc-closed-immersion-products, lem:weil-pbc-proper-composition, lem:weil-pbc-proper-to-separated, lem:weil-pbc-proper-immersion-closed
