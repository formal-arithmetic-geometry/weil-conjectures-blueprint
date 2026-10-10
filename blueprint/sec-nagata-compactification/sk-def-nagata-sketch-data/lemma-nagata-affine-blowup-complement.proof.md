+++
kind  = "proof"
of    = "lemma-nagata-affine-blowup-complement"
uses = ["def-nagata-affine-blowup", "def-nagata-affine-blowup-restriction-map", "def-nagata-affine-proj", "def-nagata-global-blowup-glue-data", "def-nagata-global-blowup-local-model", "def-nagata-homogeneous-localization-degree-zero", "def-nagata-rees-algebra", "def-nagata-rees-localization-map", "def-nagata-rees-piece", "lemma-nagata-affine-blowup-top", "lemma-nagata-global-blowup-overlap-basic", "lemma-nagata-localization-ideal-pow", "lemma-nagata-rees-degree-zero", "lemma-nagata-rees-piece-membership", "lemma-nagata-rees-piece-mul", "prop-nagata-rees-graded"]
+++
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
