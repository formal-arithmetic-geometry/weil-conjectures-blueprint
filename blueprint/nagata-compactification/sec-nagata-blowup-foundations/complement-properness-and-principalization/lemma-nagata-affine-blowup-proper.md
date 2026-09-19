+++
id = "lemma-nagata-affine-blowup-proper"
kind = "lemma"
title = "Properness of the affine blow-up"
order = 248
lean = ["AlgebraicGeometry.AffineBlowup.isProper_toSpec"]
uses = ["lemma-nagata-projective-is-proper", "prop-nagata-affine-blowup-projective"]
+++
If $I$ is finitely generated, the affine blow-up morphism is proper.

## Proof

It is projective by [prop-nagata-affine-blowup-projective], and is
therefore proper by [lemma-nagata-projective-is-proper].
