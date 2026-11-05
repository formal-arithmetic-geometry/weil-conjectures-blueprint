+++
id = "proposition-composition-base-change-rf-shriek--3"
kind = "proposition"
title = "Identity compatibility"
order = 516004
aliases = ["bp-r157-3"]
lean = ["AlgebraicGeometry.ProEtale.CondensedRing.boundedConstructibleLowerShriekComp_padicAlgCl_id_left", "AlgebraicGeometry.ProEtale.CondensedRing.boundedConstructibleLowerShriekComp_padicAlgCl_id_right"]
uses = ["proposition-composition-base-change-rf-shriek--1"]
+++
For $\Lambda=\Qbarl$ in the shared context, identify
$R(\mathrm{id}_X)_!$ with the identity by
$$
\epsilon_X:R(\mathrm{id}_X)_!\simeq R(\mathrm{id}_X)_*\simeq\mathrm{id}.
$$
For a $k$-morphism $f:X\to Y$ and
$K\in\Dbc(X_{\mathrm{pro}\acute{e}t},\Qbarl)$, the composition isomorphisms of
[proposition-composition-base-change-rf-shriek--1] satisfy
$$
Rf_!(\epsilon_X(K))\circ C_{\mathrm{id}_X,f}(K)=\mathrm{id}_{Rf_!K},
\qquad
\epsilon_Y(Rf_!K)\circ C_{f,\mathrm{id}_Y}(K)=\mathrm{id}_{Rf_!K},
$$
with the identifications $f\mathrm{id}_X=f$ and $\mathrm{id}_Yf=f$.
