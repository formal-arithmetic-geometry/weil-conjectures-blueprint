+++
id = "lemma-nagata-affine-blowup-projective-embedding"
kind = "lemma"
title = "Closed immersion into relative projective space"
order = 246
lean = ["AlgebraicGeometry.AffineBlowup.isClosedImmersion_toProjectiveSpace"]
uses = ["def-nagata-affine-blowup-projective-embedding", "lemma-nagata-rees-polynomial-surjection", "prop-nagata-relative-proj-functoriality"]
+++
The constructed morphism $e_I$ is a closed immersion over
$\operatorname{Spec}(A)$.

## Proof

A surjective graded algebra map induces a closed immersion in the opposite
direction on Proj. The source of $\rho_I$ has Proj $\mathbf P^r_A$, and
its degree-zero map is the identity of $A$, so the closed immersion is over
$\operatorname{Spec}(A)$.
