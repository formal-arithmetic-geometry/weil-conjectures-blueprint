+++
id = "thm-nagata-blowup-universal-property"
kind = "theorem"
title = "[stacks-project]"
order = 354
lean = ["AlgebraicGeometry.Scheme.IdealSheafData.exists_lift_blowup", "AlgebraicGeometry.Scheme.IdealSheafData.hom_ext_of_isInvertible_comap"]
uses = ["def-nagata-affine-blowup", "def-nagata-affine-blowup-chart-map", "def-nagata-affine-blowup-restriction-map", "def-nagata-affine-proj", "def-nagata-blowup-universal-lift", "def-nagata-effective-cartier-ideal", "def-nagata-extended-ideal", "def-nagata-global-blowup", "def-nagata-global-blowup-affine-restriction-map", "def-nagata-global-blowup-cover-comparison", "def-nagata-global-blowup-glue-data", "def-nagata-global-blowup-local-model", "def-nagata-global-blowup-map", "def-nagata-global-blowup-overlap-basic-map", "def-nagata-homogeneous-localization-degree-zero", "def-nagata-invertible-ideal", "def-nagata-rees-algebra", "def-nagata-rees-localization-map", "def-nagata-rees-piece", "def-nagata-scheme-image-factor", "def-nagata-scheme-theoretic-closure", "def-nagata-scheme-theoretic-image", "lemma-nagata-blowup-universal-exists", "lemma-nagata-blowup-universal-unique", "lemma-nagata-chart-extended-ideal-principal", "lemma-nagata-diagonal-base-change", "lemma-nagata-global-blowup-local-maps-agree", "lemma-nagata-global-blowup-overlap-basic", "lemma-nagata-localization-ideal-pow", "lemma-nagata-rees-degree-one-element", "lemma-nagata-rees-degree-zero", "lemma-nagata-rees-generators-cover-proj", "lemma-nagata-rees-piece-membership", "lemma-nagata-rees-piece-mul", "lemma-nagata-relative-proj-invertible-tensor-powers", "lemma-nagata-scheme-image-ideal-qc", "lemma-nagata-scheme-image-of-closed-immersion", "prop-nagata-affine-blowup-chart", "prop-nagata-global-blowup-cover-independent", "prop-nagata-proj-standard-open", "prop-nagata-rees-graded"]
+++
Under the data of [def-nagata-blowup-universal-lift], the constructed
map $\widetilde f$ is the unique $X$-morphism from $Y$ to
$\operatorname{Bl}_{\mathcal I}(X)$ inducing the chosen invertible
quotient. Thus the blow-up is final among such $X$-schemes.

## Proof

Existence is [lemma-nagata-blowup-universal-exists], and uniqueness
among $X$-morphisms inducing the specified quotient is
[lemma-nagata-blowup-universal-unique]. Together these are exactly the
asserted final-object property.
