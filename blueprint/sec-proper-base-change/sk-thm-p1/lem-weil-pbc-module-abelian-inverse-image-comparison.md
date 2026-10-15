+++
id = "lem-weil-pbc-module-abelian-inverse-image-comparison"
kind = "lemma"
title = "Canonical module-to-abelian inverse-image comparison is invertible"
uses = ["def-pc-scheme", "def-weil-pbc-direct-image", "def-weil-pbc-etale-sheaves", "def-weil-pbc-etale-site", "def-weil-pbc-inverse-image"]
lean = ["AlgebraicGeometry.Etale.isIso_moduleAbelianInverseImageComparison"]
+++
Let $i:X\to Y$ be a morphism of schemes [def-pc-scheme] and $\Lambda$ a commutative ring. Let $J$ be a sheaf of $\Lambda$-modules on the small etale site of $Y$ [def-weil-pbc-etale-site], [def-weil-pbc-etale-sheaves]. Write $U_X,U_Y$ for the functors forgetting to abelian sheaves. For the inverse-image and direct-image adjunctions [def-weil-pbc-inverse-image], [def-weil-pbc-direct-image], the abelian adjoint of $U_Y(\eta^{\mathrm{Mod}}_J):U_YJ\to i_*U_X(i^{-1}_{\mathrm{Mod}}J)$ is an isomorphism $i^{-1}_{\mathrm{Ab}}U_YJ\xrightarrow{\sim}U_X(i^{-1}_{\mathrm{Mod}}J)$. This is the particular canonical comparison determined by the module adjunction unit, not merely existence of some isomorphism.
