+++
id = "lemma-nagata-two-open-comparison-boundary"
kind = "lemma"
title = "The two descriptions of the comparison boundary agree"
order = 541
lean = ["AlgebraicGeometry.exists_prepared_keyDisjoint_twoOpenSide"]
uses = ["def-nagata-admissible-blowup", "def-nagata-compactifiable", "def-nagata-compactification", "def-nagata-global-blowup", "def-nagata-global-blowup-cover-comparison", "def-nagata-global-blowup-map", "def-nagata-isomorphism-near-closure", "def-nagata-scheme-image-factor", "def-nagata-scheme-theoretic-closure", "def-nagata-scheme-theoretic-image", "def-nagata-strict-transform", "def-nagata-two-open-boundary-loci", "def-nagata-two-open-comparison-boundary", "def-nagata-two-open-comparison-space", "def-nagata-two-open-graph-extensions", "def-nagata-two-open-improved-comparison", "def-nagata-two-open-prepared-boundaries", "lemma-nagata-admissible-blowup-over-open", "lemma-nagata-comparison-projections-proper", "lemma-nagata-diagonal-base-change", "lemma-nagata-immersion-open-in-scheme-image", "lemma-nagata-isomorphism-near-closure", "lemma-nagata-open-immersion-qc-over-separated-target", "lemma-nagata-prepared-boundaries", "lemma-nagata-proper-to-separated-target", "lemma-nagata-scheme-image-ideal-qc", "lemma-nagata-scheme-image-of-closed-immersion", "lemma-nagata-strict-transform-closure-characterization", "lemma-nagata-two-open-graph-extensions", "prop-nagata-global-blowup-cover-independent"]
+++
Inside $V_{12}$ one has

$$
Z_{12,2}=(p_2|_{V_{12}})^{-1}(Z_{2,2}).
$$

## Proof

Let $z=(v_1,v_2)$ be a point of $V_{12}=V_1\times_UV_2$. The fibre-product
equality gives $\psi_1(v_1)=\psi_2(v_2)=u\in U$. Since
$Z_{1,2}=V_1\times_UZ_2$ and $Z_{2,2}=V_2\times_UZ_2$, membership in either
inverse image is equivalent to $u\in Z_2$. Scheme-theoretically, both
sides are the pullback of the closed subscheme $Z_2\hookrightarrow U$ along
the equal composites $V_{12}\rightrightarrows U$. The canonical
associativity isomorphisms for fibre products therefore identify the two
closed subschemes.
