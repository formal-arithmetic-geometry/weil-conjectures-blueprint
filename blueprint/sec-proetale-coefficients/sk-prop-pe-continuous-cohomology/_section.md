+++
id = "sk-prop-pe-continuous-cohomology"
kind = "proposition"
title = "Continuous cohomology as pro-étale cohomology"
order = 1094
lean = ["AlgebraicGeometry.ProEtale.isHomotopyLimit_mapCone_Q_of_epi", "CategoryTheory.Pretriangulated.IsHomotopyLimit.map", "DerivedCategory.shortExact_milnor_of_isHomotopyLimit"]
uses = ["sk-prop-pe-replete", "sk-prop-pe-milnor", "sk-prop-sf-comparison"]
tags = ["sketch"]
+++
Let $X$ be a scheme and $(F_n)$ an inverse system of abelian sheaves on
$X_{\Proet}$ with epimorphic transition maps. Put
$F=\varprojlim_nF_n$ in the pro-étale topos. Then, in the derived category of
abelian groups,

$$
R\Gamma(X_{\Proet},F)\simeq R\varprojlim_nR\Gamma(X_{\Proet},F_n).
$$

For every $q$ there is a natural exact sequence

$$
0\longrightarrow\varprojlim\nolimits^1_nH^{q-1}(X_{\Proet},F_n)\longrightarrow
H^q(X_{\Proet},F)\longrightarrow\varprojlim_nH^q(X_{\Proet},F_n)\longrightarrow0.
$$

The first term need not vanish, since epimorphic transitions between the sheaves
$F_n$ do not make the transitions between their cohomology groups surjective. It
vanishes when the groups $H^{q-1}(X_{\Proet},F_n)$ are finite, since descending
chains of images then stabilize at each level.
