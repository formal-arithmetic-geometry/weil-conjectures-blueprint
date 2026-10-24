+++
kind  = "proof"
of    = "lem-sfb-qlbar-push-iso-proper"
uses = ["sk-prop-sfb-qlbar-colimit-x", "lem-sfb-subfield-push-iso", "lem-sfb-subfield-coefficient-map-comp", "sk-cor-pe-bounded-continuity"]
+++
Represent $K$ by a complex $K^\bullet$ of $E_X$-modules vanishing below some degree $a$. By
[sk-prop-sfb-qlbar-colimit-x], $\overline{\mathbf Q}_{\ell,X}=\operatorname{colim}_{F\ge E}F_X$ along the
inclusions, compatibly with the $E_X$-module structures
([lem-sfb-subfield-coefficient-map-comp]). Since all extensions of scalars involved are exact,
$T^X_{E,\Qlb}K$ is represented, after restriction of scalars to $E_X$ (which is conservative and
commutes with $Rf_*$), by the termwise filtered colimit
$\operatorname{colim}_F(F_X\otimes_{E_X}K^\bullet)$ of complexes all vanishing below $a$, and
likewise on $Y$ for $Rf_*K$; the comparison maps are compatible with the transition maps. At each
finite stage (Push) is an isomorphism ([lem-sfb-subfield-push-iso]). Since filtered colimits of
modules are exact, on the $q$-th cohomology sheaves (Push) for $E\subseteq\Qlb$ is therefore
identified with the canonical map

$$
\operatorname{colim}_FR^qf_*(F_X\otimes_{E_X}K^\bullet)\longrightarrow
R^qf_*\operatorname{colim}_F(F_X\otimes_{E_X}K^\bullet).
$$

As $f$ is proper, it is quasi-compact and quasi-separated, and the complexes have the common lower
bound $a$, so this map is an isomorphism by [sk-cor-pe-bounded-continuity]. Hence (Push) at $K$
is an isomorphism on all cohomology sheaves, so an isomorphism. The common lower bound is
essential: for unbounded complexes $Rf_*$ need not commute with the countable direct sums that
compute $\overline{\mathbf Q}_{\ell,X}\otimes_{E_X}-$, even for $f$ proper.
