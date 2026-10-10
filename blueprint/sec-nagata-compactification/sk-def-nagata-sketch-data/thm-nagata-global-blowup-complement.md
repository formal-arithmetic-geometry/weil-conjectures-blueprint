+++
id = "thm-nagata-global-blowup-complement"
kind = "theorem"
title = "Complement of the center"
order = 59
lean = ["AlgebraicGeometry.Scheme.IdealSheafData.isIso_blowupMap_restrict_support_compl"]
uses = ["def-nagata-global-blowup", "lemma-nagata-affine-blowup-complement", "lemma-nagata-ideal-unit-off-support", "prop-nagata-global-blowup-cover-independent"]
+++
Let $\mathcal I\subseteq\mathcal O_X$ be a quasi-coherent ideal and let
$U=X\setminus V(\mathcal I)$. The restriction

$$
b_{X,\mathcal I}^{-1}(U)\longrightarrow U
$$

of the blow-up morphism is an isomorphism.

## Proof

Cover $U$ by affine opens $V\subseteq U$. Each such $V$ is disjoint from
$V(\mathcal I)$, so $\Gamma(V,\mathcal I)=\Gamma(V,\mathcal O_X)$ by
[lemma-nagata-ideal-unit-off-support], and the blow-up morphism restricts
to an isomorphism over $V$ by [lemma-nagata-affine-blowup-complement].
Being an isomorphism is local on the target, so
$b_{X,\mathcal I}^{-1}(U)\to U$ is an isomorphism.
