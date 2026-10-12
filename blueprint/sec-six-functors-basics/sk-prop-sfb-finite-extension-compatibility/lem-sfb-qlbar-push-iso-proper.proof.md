+++
kind  = "proof"
of    = "lem-sfb-qlbar-push-iso-proper"
uses = ["sk-prop-sfb-qlbar-colimit-x", "lem-sfb-subfield-push-iso", "lem-sfb-subfield-coefficient-map-comp"]
+++
By [sk-prop-sfb-qlbar-colimit-x], $\overline{\mathbf Q}_{\ell,X}=\operatorname{colim}_{F\ge E}F_X$ along the
inclusions, compatibly with the $E_X$-module structures
([lem-sfb-subfield-coefficient-map-comp]). Since all extensions of scalars involved are exact,
$T^X_{E,\Qlb}K\cong\operatorname{colim}_FF_X\otimes_{E_X}K$ (after restriction of scalars to
$E_X$), a filtered colimit of the finite-stage extensions of scalars, and likewise on $Y$; the
comparison maps are compatible with the transition maps. At each finite stage (Push) is an
isomorphism ([lem-sfb-subfield-push-iso]). Hence (Push) for $E\subseteq\Qlb$ is identified with
the canonical map

$$
\operatorname{colim}_FRf_*(F_X\otimes_{E_X}K)\longrightarrow
Rf_*\operatorname{colim}_F(F_X\otimes_{E_X}K).
$$

A countable filtered colimit in the derived category is computed from coproducts (as the cone of
the telescope map), so it suffices that $Rf_*$ commutes with coproducts. This is the input that
properness of $f$ supplies; for a non-proper $f$ the map is not an isomorphism in general.
