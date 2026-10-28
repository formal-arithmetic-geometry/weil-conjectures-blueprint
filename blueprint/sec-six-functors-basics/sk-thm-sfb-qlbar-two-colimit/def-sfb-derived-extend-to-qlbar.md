+++
id = "def-sfb-derived-extend-to-qlbar"
kind = "definition"
title = "The derived extension of scalars $T_{E,\\Qlb}$"
order = 2296
uses = ["def-sfb-subfield-to-qlbar-coefficient-map", "det-def-sfb-derived-extension-of-scalars"]
lean = ["AlgebraicGeometry.ProEtale.derivedExtendScalarsToPadicAlgCl"]
+++
Let $\ell$ be a prime, $X$ a scheme and $E$ a finite extension of $\mathbf Q_\ell$ inside $\Qlb$.
The derived extension of scalars

$$
T_{E,\Qlb}=\overline{\mathbf Q}_{\ell,X}\otimes^{\mathrm L}_{E_X}-=L(\operatorname{Ext}_{E_X\to\overline{\mathbf Q}_{\ell,X}})\colon
D(\Mod_{E_X})\longrightarrow D(\Mod_{\overline{\mathbf Q}_{\ell,X}})
$$

is the derived extension of scalars of [det-def-sfb-derived-extension-of-scalars] along the
inclusion $E_X\to\overline{\mathbf Q}_{\ell,X}$ of [def-sfb-subfield-to-qlbar-coefficient-map].
