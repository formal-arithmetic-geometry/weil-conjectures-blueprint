+++
id = "lemma-nagata-affine-blowup-complement"
kind = "lemma"
title = "Affine complement-of-center isomorphism"
order = 58
lean = ["AlgebraicGeometry.Scheme.IdealSheafData.isIso_blowupMap_restrict_of_ideal_eq_top"]
uses = ["def-nagata-affine-blowup", "def-nagata-affine-blowup-restriction-map", "def-nagata-affine-proj", "def-nagata-global-blowup", "def-nagata-global-blowup-glue-data", "def-nagata-global-blowup-local-model", "def-nagata-global-blowup-overlap-basic-map", "def-nagata-homogeneous-localization-degree-zero", "def-nagata-rees-algebra", "def-nagata-rees-localization-map", "def-nagata-rees-piece", "lemma-nagata-affine-blowup-restrict-cocycle", "lemma-nagata-affine-blowup-top", "lemma-nagata-global-blowup-overlap-basic", "lemma-nagata-localization-ideal-pow", "lemma-nagata-rees-degree-zero", "lemma-nagata-rees-piece-membership", "lemma-nagata-rees-piece-mul", "prop-nagata-affine-blowup-restrict", "prop-nagata-global-blowup-cover-independent", "prop-nagata-rees-graded"]
+++
Let $\mathcal I\subseteq\mathcal O_X$ be a quasi-coherent ideal and let
$V\subseteq X$ be an affine open with
$\Gamma(V,\mathcal I)=\Gamma(V,\mathcal O_X)$. Then the blow-up morphism
$\operatorname{Bl}_{\mathcal I}(X)\to X$ restricts to an isomorphism over
$V$.

## Proof

By [prop-nagata-global-blowup-cover-independent], the open immersion
$\iota_V$ identifies the local model
$\mathsf B_V(\mathcal I)=\operatorname{Bl}_{I_V}(\operatorname{Spec}A_V)$
with $b_{X,\mathcal I}^{-1}(V)$, compatibly with the morphisms to $V$.
Thus the restriction of the blow-up morphism over $V$ is identified with
the structure morphism
$\operatorname{Bl}_{I_V}(\operatorname{Spec}A_V)\to\operatorname{Spec}A_V\cong V$.
By hypothesis $I_V=\Gamma(V,\mathcal I)$ is the unit ideal of
$A_V=\Gamma(V,\mathcal O_X)$, so this structure morphism is an isomorphism
by [lemma-nagata-affine-blowup-top].
