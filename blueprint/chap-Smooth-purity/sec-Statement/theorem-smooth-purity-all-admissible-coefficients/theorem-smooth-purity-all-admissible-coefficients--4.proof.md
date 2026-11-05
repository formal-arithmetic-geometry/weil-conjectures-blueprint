+++
kind = "proof"
of = "theorem-smooth-purity-all-admissible-coefficients--4"
order = 730009
uses = ["theorem-smooth-purity-all-admissible-coefficients--2", "theorem-smooth-purity-all-admissible-coefficients--9", "proposition-six-operations-change-coefficients", "proposition-composition-open-restriction-compactifications-f", "theorem-smooth-base-change-classical-torsion", "theorem-proper-base-change-classical-pro"]
+++
Apply [theorem-smooth-purity-all-admissible-coefficients--2] with $E=\mathbf Q_\ell$ and extend scalars to $\overline{\mathbf Q}_\ell$. The comparisons for the integral Tate twist and for $f^!$ give an isomorphism at the constant object. Choose an invertible lift of the finite orientations if one exists, and otherwise choose this isomorphism. For an open immersion of relative dimension zero use the usual identification $f^!\overline{\mathbf Q}_\ell\simeq\overline{\mathbf Q}_\ell$. Finally factor $f$ through its open image and transport the orientation using composition for $f^!$. Every map used in this transport is invertible.

For the tensor product map, use dévissage by the generators $Rg_*Rj_*L$, where $g$ is a closed immersion, $j$ an open immersion, and $L$ dualizable. The map is an isomorphism for $L$ by the projection formula. Its compatibility with exceptional base change, the unit case of [theorem-smooth-purity-all-admissible-coefficients--9], and dualizability of the relative dualizing complex transfer this to the open and closed direct images. Ordinary smooth base change is used for the open step and proper base change for the closed step. Stability under shifts and distinguished triangles gives the assertion for every bounded constructible $K$.

The dualizability used here follows from the integral isomorphism and monoidal extension of scalars. This is the route of `AlgebraicGeometry.ProEtale.CondensedRing.isIso_upperShriekUnitTensorMap_of_smooth`.
