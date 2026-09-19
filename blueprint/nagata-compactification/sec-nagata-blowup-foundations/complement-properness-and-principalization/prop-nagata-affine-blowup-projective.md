+++
id = "prop-nagata-affine-blowup-projective"
kind = "theorem"
title = "Projectivity of the affine blow-up"
order = 247
lean = ["AlgebraicGeometry.AffineBlowup.exists_isClosedImmersion_comp_projectiveSpaceOverAffineToSpec"]
tags = ["latex:proposition"]
uses = ["def-nagata-projective-morphism", "lemma-nagata-affine-blowup-projective-embedding"]
+++
If $I$ is finitely generated, the affine blow-up morphism

$$
\operatorname{Bl}_I(\operatorname{Spec}(A))
\longrightarrow\operatorname{Spec}(A)
$$

is projective.

## Proof

Choose finitely many generators of $I$. By
[lemma-nagata-affine-blowup-projective-embedding], the blow-up is a
closed subscheme of a finite-dimensional projective space over
$\operatorname{Spec}(A)$. The composite of a closed immersion with
$\mathbf P^r_A\to\operatorname{Spec}(A)$ is projective.
