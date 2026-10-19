+++
id = "thm-chow-lemma"
kind = "theorem"
title = "Chow's lemma"
order = 1093
lean = ["AlgebraicGeometry.ChowModification", "AlgebraicGeometry.ChowModification.exists_dense_isIso_restrict", "AlgebraicGeometry.ChowModification.index", "AlgebraicGeometry.ChowModification.isImmersion_toProjectiveSpace", "AlgebraicGeometry.ChowModification.isProper_modificationMap", "AlgebraicGeometry.ChowModification.modificationMap", "AlgebraicGeometry.ChowModification.surjective_modificationMap", "AlgebraicGeometry.ChowModification.toProjectiveSpace", "AlgebraicGeometry.ChowModification.toProjectiveSpace_over"]
uses = ["def-nagata-affine-proj", "def-nagata-dense-compactification", "def-nagata-projective-space-base-change", "def-nagata-scheme-image-factor", "def-nagata-scheme-theoretic-image", "def-weil-pbc-scheme-conventions", "lem-chow-agree-on-dense-open", "lem-chow-closed-model", "lem-chow-glue", "lem-chow-graph", "lem-chow-preimage", "lem-chow-scheme-theoretic-closure", "lem-chow-segre", "lem-chow-tuple-immersion", "lem-weil-pbc-proper-closed-image", "lem-weil-pbc-proper-composition", "lem-weil-pbc-proper-immersion-closed", "lemma-nagata-dense-affine-cover-exists", "lemma-nagata-dense-flat-pullback", "lemma-nagata-immersion-open-in-scheme-image", "lemma-nagata-projective-space-base-change-proper", "lemma-nagata-projective-target-local", "lemma-nagata-scheme-image-ideal-qc"]
+++
Let $S$ be a noetherian scheme and let $f\colon X\to S$ be a separated morphism
of finite type. Then there are a finite set $N$, a scheme $X'$, a
morphism $\pi\colon X'\to X$ and an immersion $i\colon X'\to\mathbf P^N_S$
into the projective space over $S$ with homogeneous coordinates indexed by $N$
[def-nagata-projective-space-base-change], such that $i$ followed by the
structure morphism $\mathbf P^N_S\to S$ equals $f\circ\pi$, and

1. $\pi$ is proper and surjective, and
1. there is a dense open subscheme $U\subseteq X$ such that
$\pi^{-1}(U)\to U$ is an isomorphism.
