+++
id = "lemma-nagata-extend-admissible-blowup"
kind = "lemma"
title = "Property of the extended admissible blow-up, [stacks-project]"
order = 442
lean = ["AlgebraicGeometry.IsAdmissible.exists_extend", "AlgebraicGeometry.IsAdmissible.exists_extend_of_disjoint", "AlgebraicGeometry.Scheme.IdealSheafData.exists_finiteType_comap_eq_of_disjoint"]
uses = ["def-nagata-extended-admissible-blowup", "def-nagata-global-blowup-cover-comparison", "lemma-nagata-affine-image-kernel-flat", "lemma-nagata-extend-finite-type-ideal", "lemma-nagata-scheme-image-flat-base-change", "prop-nagata-global-blowup-cover-independent", "thm-nagata-blowup-flat-base-change"]
+++
The constructed morphism
$\mathsf{ExtBl}_{X,W,U}(\mathcal J)\to X$ is $U$-admissible, and its
restriction to $W$ is canonically the given blow-up
$\operatorname{Bl}_{\mathcal J}(W)\to W$.

## Proof

By [lemma-nagata-extend-finite-type-ideal], the ideal
$\mathcal I_X(\mathcal J)$ is finite type, restricts to $\mathcal J$ on
$W$, and restricts to the unit ideal on $U$. Its blow-up is therefore
$U$-admissible. The open immersion $W\to X$ is flat, so
[thm-nagata-blowup-flat-base-change] identifies the pullback of the
constructed blow-up with $\operatorname{Bl}_{\mathcal J}(W)$. On an
affine chart, that comparison is induced degreewise by the canonical map
from the pullback of the Rees algebra to the Rees algebra of the restricted
ideal; it sends every standard chart generator to itself. Hence the local
comparisons commute with restriction to basic overlaps and glue to the
stated canonical isomorphism. Over $U\cap W$ both ideals are the unit
ideal, so the same formula is the selected identity of the two trivial
blow-ups. This also verifies compatibility with the chosen admissibility
isomorphism.
