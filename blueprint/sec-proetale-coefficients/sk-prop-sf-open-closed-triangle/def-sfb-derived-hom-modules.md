+++
id = "def-sfb-derived-hom-modules"
kind = "definition"
title = "Derived internal hom of module objects"
order = 1147
uses = ["def-sfb-derived-tensor-modules", "lem-sfb-derived-monoidal-closed"]
lean = ["AlgebraicGeometry.ProEtale.CondensedRing.derivedHom"]
+++
For a commutative condensed ring $\Lambda$ and a scheme $X$, the *derived internal hom*
$$
\RHom_{\Lambda_X}(-,-)\colon D(\Mod_{\Lambda_X})^{\mathrm{op}}\times D(\Mod_{\Lambda_X})\to D(\Mod_{\Lambda_X})
$$
is the internal hom of the closed monoidal structure on
$(D(\Mod_{\Lambda_X}),\otimes^{\mathrm L}_{\Lambda_X})$ [def-sfb-derived-tensor-modules],
[lem-sfb-derived-monoidal-closed].
