+++
kind = "proof"
of = "lem-weil-pbc-module-abelian-inverse-image-comparison"
uses = ["def-weil-pbc-direct-image", "def-weil-pbc-inverse-image"]
+++
Write the inverse image [def-weil-pbc-inverse-image] as the left Kan extension of presheaves along the pullback of etale objects, followed by sheafification. The functor forgetting a sheaf of $\Lambda$-modules to its underlying abelian sheaf preserves colimits and limits; hence it commutes with left Kan extension and with sheafification, and we obtain an isomorphism $e:i^{-1}_{\mathrm{Ab}}U_YJ\xrightarrow{\sim}U_X(i^{-1}_{\mathrm{Mod}}J)$.

By naturality of the sheafification unit, the composite of the abelian sheafification unit with $e$ is the comparison map for the left Kan extensions followed by the underlying map of the module sheafification unit. Since the Kan extension comparison is compatible with the Kan extension units, it follows that the abelian adjoint of $e$ is the underlying map $U_Y(\eta^{\mathrm{Mod}}_J)$ of the module adjunction unit; here we use that the direct image [def-weil-pbc-direct-image] commutes with forgetting, as it is restriction of presheaves. Since passing to adjoints is a bijection on morphisms, the abelian adjoint of $U_Y(\eta^{\mathrm{Mod}}_J)$ is $e$, which is an isomorphism ([def-weil-pbc-inverse-image]).
