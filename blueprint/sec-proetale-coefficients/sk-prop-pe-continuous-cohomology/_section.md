+++
id = "sk-prop-pe-continuous-cohomology"
kind = "proposition"
title = "Continuous cohomology as pro-étale cohomology"
order = 1086
lean = ["AlgebraicGeometry.ProEtale.isHomotopyLimit_mapCone_Q_of_epi", "CategoryTheory.Pretriangulated.IsHomotopyLimit.map", "AlgebraicGeometry.Scheme.continuousH", "AlgebraicGeometry.Scheme.ProEt.nonempty_continuousH_addEquiv_H_limit", "DerivedCategory.shortExact_milnor_of_isHomotopyLimit", "AlgebraicGeometry.Scheme.ProEt.bijective_extLimitToLimit_of_isMittagLeffler"]
uses = ["sk-prop-pe-replete", "sk-prop-sf-comparison", "sk-def-pe-classical-definition", "sk-prop-pe-milnor"]
tags = ["sketch"]
+++
Let $X$ be a scheme and $(F_n)$ an inverse system of abelian sheaves on
$X_{\Proet}$ which are classical, with epimorphic transition maps. Put
$F=\varprojlim_nF_n$ in the pro-étale topos. Then, in the derived category of
abelian groups,

$$
R\Gamma(X_{\Proet},F)\simeq R\varprojlim_nR\Gamma(X_{\Proet},F_n).
$$

If $F_n=\nu_X^*F_{n,\Et}$, its cohomology is the continuous étale cohomology of the
system $(F_{n,\Et})$: $H^i(X_{\Proet},F)\cong H^i_{\mathrm{cont}}(X,(F_{n,\Et}))$ for
all $i$, where $H^i_{\mathrm{cont}}$ are the right derived functors of
$(G_n)\mapsto\Gamma(X_{\Et},\varprojlim_nG_n)$, taken on the abelian category of
inverse systems.

For every $q$ there is a natural exact sequence

$$
0\longrightarrow\varprojlim\nolimits^1_nH^{q-1}(X_{\Proet},F_n)\longrightarrow
H^q(X_{\Proet},F)\longrightarrow\varprojlim_nH^q(X_{\Proet},F_n)\longrightarrow0.
$$

The first term need not vanish, since epimorphic transitions between the sheaves
$F_n$ do not make the transitions between their cohomology groups surjective. It
vanishes when the groups $H^{q-1}(X_{\Proet},F_n)$ satisfy the Mittag-Leffler
condition, for instance when they are finite, since descending chains of images
then stabilize at each level.
