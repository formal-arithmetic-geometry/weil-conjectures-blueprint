+++
id = "proposition-composition-base-change-rf-shriek--2"
kind = "proposition"
title = "Associativity"
order = 516003
aliases = ["bp-r157-2"]
lean = ["AlgebraicGeometry.ProEtale.CondensedRing.boundedConstructibleLowerShriekComp_padicAlgCl_assoc"]
uses = ["proposition-composition-base-change-rf-shriek--1"]
+++
For $\Lambda=\Qbarl$ in the shared context and three composable
$k$-morphisms $X\xrightarrow fY\xrightarrow gZ\xrightarrow hT$, the
isomorphisms $C_{f,g}$ of [proposition-composition-base-change-rf-shriek--1]
are associative. For every $K\in\Dbc(X_{\mathrm{pro}\acute{e}t},\Qbarl)$,
$$
Rh_!\bigl(C_{f,g}(K)\bigr)\circ C_{gf,h}(K)
=
C_{g,h}(Rf_!K)\circ C_{f,hg}(K),
$$
after identifying $h(gf)$ with $(hg)f$.
