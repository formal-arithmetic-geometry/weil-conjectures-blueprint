+++
id = "thm-nagata-blowup-universal-property"
kind = "theorem"
title = "[stacks-project]"
order = 354
lean = ["AlgebraicGeometry.Scheme.IdealSheafData.exists_lift_blowup", "AlgebraicGeometry.Scheme.IdealSheafData.hom_ext_of_isInvertible_comap"]
uses = ["def-nagata-blowup-universal-lift", "def-nagata-global-blowup-cover-comparison", "lemma-nagata-blowup-universal-exists", "lemma-nagata-blowup-universal-unique", "lemma-nagata-relative-proj-invertible-tensor-powers", "prop-nagata-global-blowup-cover-independent"]
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
