+++
id = "lemma-nearby-cycles-constant-family"
kind = "lemma"
title = "Nearby cycles of a constant family"
order = 1627
lean = ["AlgebraicGeometry.ProEtale.CondensedRing.isIso_deformationModel_bot_unit_of_smooth", "AlgebraicGeometry.ProEtale.CondensedRing.isIso_deformationModel_bot_unit_of_smooth_finiteCoefficient", "AlgebraicGeometry.ProEtale.CondensedRing.NearbyCyclesModel.Hom.map_unit_comp_pullbackExchange_app"]
+++
For a separated $k$-scheme $Y$ of finite type and
$L\in\Dbc(Y,A)$, the specialization map

$$
\sigma_Y(L):L\longrightarrow
R\Psi_{Y\times S}(L_\eta)
$$

is an isomorphism. It is natural in $L$, and it is compatible with the
base change maps above in the following sense.

1. If $f:Y'\to Y$ is proper and $L'\in\Dbc(Y',A)$, then the composite
   of $Rf_*\sigma_{Y'}(L')$ with the base change map for proper direct
   image is $\sigma_Y(Rf_*L')$, where $(Rf_*L')_\eta$ is identified with
   $Rf_{\eta*}(L'_\eta)$ by proper base change.
2. If $f:Y'\to Y$ is smooth, then the composite of $f^*\sigma_Y(L)$
   with the base change map for pullback is $\sigma_{Y'}(f^*L)$.
