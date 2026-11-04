+++
id = "theorem-smooth-base-change-all-admissible"
kind = "theorem"
title = "Smooth base change for all admissible coefficients"
order = 694
lean = ["AlgebraicGeometry.ProEtale.isIso_derivedBaseChangeMap_app_of_smooth", "AlgebraicGeometry.ProEtale.CondensedRing.isIso_baseChangeMap_app_of_smooth_of_finite", "AlgebraicGeometry.ProEtale.CondensedRing.isIso_baseChangeMap_app_padicIntegers_of_smooth", "AlgebraicGeometry.ProEtale.CondensedRing.isIso_boundedConstructibleBaseChange_of_smooth"]
+++
In (8.1), assume that all schemes are of finite type over $k$
and that $g$ is smooth. For every admissible coefficient ring

$$
\Lambda\in\{A,\mathbf Z_\ell,\mathcal O_E,\mathbf Q_\ell,E,\overline{\mathbf Q}_\ell\}
$$

and every $K\in D^b_{\mathrm{ctf}}(X,\Lambda)$, the
base change map (4.5) is an isomorphism

$$
g^*Rf_*K\xrightarrow{\sim}Rf'_*g'^*K.
\tag{8.2}
$$
