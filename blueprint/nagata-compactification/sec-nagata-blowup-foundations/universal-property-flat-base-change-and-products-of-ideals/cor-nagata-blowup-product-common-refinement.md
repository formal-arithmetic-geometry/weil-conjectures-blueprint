+++
id = "cor-nagata-blowup-product-common-refinement"
kind = "theorem"
title = "Common refinement by the product ideal"
order = 387
lean = ["AlgebraicGeometry.Scheme.IdealSheafData.exists_blowup_mul_iso"]
tags = ["latex:corollary"]
uses = ["def-nagata-blowup-product-domination-maps", "def-nagata-blowup-universal-graded-map", "def-nagata-blowup-universal-lift", "def-nagata-effective-cartier-ideal", "def-nagata-extended-ideal", "def-nagata-global-blowup", "def-nagata-global-blowup-cover-comparison", "def-nagata-global-blowup-map", "def-nagata-invertible-ideal", "def-nagata-scheme-image-factor", "def-nagata-scheme-theoretic-closure", "def-nagata-scheme-theoretic-image", "lemma-nagata-blowup-universal-exists", "lemma-nagata-blowup-universal-graded-map", "lemma-nagata-blowup-universal-unique", "lemma-nagata-cartier-total-transform-blowup", "lemma-nagata-ideal-invertible-product-factor", "lemma-nagata-invertible-ideal-mul", "lemma-nagata-invertible-product-factor", "lemma-nagata-localization-ideal-pow", "lemma-nagata-scheme-image-ideal-qc", "lemma-nagata-scheme-image-of-closed-immersion", "prop-nagata-global-blowup-cover-independent", "thm-nagata-blowup-principalizes-center", "thm-nagata-blowup-product-ideal", "thm-nagata-blowup-universal-property", "thm-nagata-global-blowup-complement"]
+++
The constructed $d_{\mathcal I}$ and $d_{\mathcal J}$ are morphisms over
$X$. If both ideals restrict to the unit ideal on an open $U$, the product
blow-up and both maps restrict to the identity over $U$.

## Proof

The maps are composites over $X$ by definition. On $U$, all three ideals
are the unit ideal, so all three blow-ups are identified with $U$ by the
complement theorem. The universal maps are unique over $U$, hence become
the identity under these identifications.
