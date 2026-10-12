+++
kind  = "proof"
of    = "lem-sfb-qlbar-flat"
uses = ["sk-prop-sfb-qlbar-colimit-x", "lem-sfb-subfield-flat", "lem-sfb-subfield-coefficient-map-comp"]
+++
By [sk-prop-sfb-qlbar-colimit-x], $\overline{\mathbf Q}_{\ell,X}=\operatorname{colim}_{F\ge E}F_X$, a filtered
colimit along the inclusions, compatibly with the $E_X$-module structures
([lem-sfb-subfield-coefficient-map-comp]). The relative tensor product commutes with colimits
in each variable, so $\overline{\mathbf Q}_{\ell,X}\otimes_{E_X}M\cong\operatorname{colim}_FF_X\otimes_{E_X}M$.
Each $F_X\otimes_{E_X}-$ is exact ([lem-sfb-subfield-flat]), and filtered colimits are exact in
the Grothendieck abelian category $\Mod_{\overline{\mathbf Q}_{\ell,X}}$ (equivalently, on underlying abelian
sheaves), so the colimit is exact.
