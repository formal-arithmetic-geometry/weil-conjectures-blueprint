+++
id = "def-sfb-derived-extend-subfield"
kind = "definition"
title = "The derived extension of scalars $T_{E,F}$"
order = 2295
uses = ["def-sfb-subfield-coefficient-map", "det-def-sfb-derived-extension-of-scalars"]
lean = ["AlgebraicGeometry.ProEtale.derivedExtendScalarsSubfield"]
+++
Let $\ell$ be a prime, $X$ a scheme and $E\le F$ finite extensions of $\mathbf Q_\ell$ inside
$\Qlb$. The derived extension of scalars

$$
T_{E,F}=F_X\otimes^{\mathrm L}_{E_X}-=L(\operatorname{Ext}_{E_X\to F_X})\colon
D(\Mod_{E_X})\longrightarrow D(\Mod_{F_X})
$$

is the derived extension of scalars of [det-def-sfb-derived-extension-of-scalars] along the
inclusion $E_X\to F_X$ of [def-sfb-subfield-coefficient-map].
