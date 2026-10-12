+++
id = "def-sfb-derived-extend-comp-iso"
kind = "definition"
title = "Transitivity $T_{F,\\Qlb}\\circ T_{E,F}\\cong T_{E,\\Qlb}$"
order = 1706
uses = ["def-sfb-derived-extend-subfield", "def-sfb-derived-extend-to-qlbar"]
lean = ["AlgebraicGeometry.ProEtale.derivedExtendScalarsCompIso"]
+++
For a prime $\ell$, a scheme $X$ and finite extensions $E\le F$ of $\mathbf Q_\ell$ inside
$\Qlb$, there is a natural isomorphism

$$
T_{F,\Qlb}\circ T_{E,F}\;\cong\;T_{E,\Qlb}\colon D(\Mod_{E_X})\longrightarrow
D(\Mod_{\overline{\mathbf Q}_{\ell,X}})
$$

between the derived extensions of scalars of [def-sfb-derived-extend-subfield] and
[def-sfb-derived-extend-to-qlbar].
