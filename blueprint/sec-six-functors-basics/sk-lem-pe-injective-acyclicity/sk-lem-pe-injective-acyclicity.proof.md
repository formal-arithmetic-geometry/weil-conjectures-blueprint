+++
kind = "proof"
of = "sk-lem-pe-injective-acyclicity"
uses = ["det-pe-injective-acyclicity-reduction", "lem-weil-pbc-comparison-injective-acyclicity", "lem-weil-pbc-cech-criterion", "lem-weil-pbc-proetale-restriction-injectives"]
+++
It suffices to show that positive cohomology vanishes on affine étale objects
([det-pe-injective-acyclicity-reduction]). The restriction of $I$ to such an
object is injective, since restriction has an exact left adjoint, extension by
zero. On an affine base we use the basis of ind-étale affines: by the
compatible refinement of [sk-thm-pe-indetale-refinement], the Čech-acyclicity
criterion for a basis ([lem-weil-pbc-cech-criterion]) may be applied to finite
affine coverings by ind-étale maps.

Write each covering map as an inverse limit of affine étale maps over the
object being covered. By the affine evaluation formula of
[sk-prop-pe-comparison-morphism], the Čech complex of the covering is the
filtered colimit of the Čech complexes of these étale approximations. Each
finitely presented approximation descends to a common étale stage over the
base, is a covering after increasing that stage, and its nerve descends by
taking fibre products. Since $I$ is injective, each augmented Čech complex at a
finite stage has no positive cohomology. Filtered colimits are exact, so the
same holds for the pro-étale covering, and the criterion gives the required
vanishing ([lem-weil-pbc-comparison-injective-acyclicity]; the identification
of derived evaluation with cohomology on the slice is
[lem-weil-pbc-proetale-restriction-injectives]). This is the argument of
Stacks Project, Tag 099U; for module sheaves one uses free $\Lambda$-module
sheaves in the augmented resolution.
