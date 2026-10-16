+++
id = "sbc-lem-etale-locality"
kind = "lemma"
title = "Etale locality of the base-change map"
lean = ["AlgebraicGeometry.Etale.isIso_homologyFunctor_map_baseChange_app_of_etale_cover", "AlgebraicGeometry.Etale.isIso_baseChange_app_of_etale_cover", "AlgebraicGeometry.Etale.isIso_baseChangeHomologyMap_of_etale_cover", "AlgebraicGeometry.Etale.isIso_baseChangeMap_app_of_etale_cover", "AlgebraicGeometry.Etale.BaseChangeProperty.of_etale_cover", "AlgebraicGeometry.Etale.isIso_derivedBaseChangeMapPlus_of_etale"]
order = 1429
uses = ["def-weil-pbc-direct-image", "def-weil-pbc-etale-site", "sbc-def-base-change-map", "sbc-def-base-change-square"]
+++
Consider a base-change square
and let $\{U_i\to X\}$ be an etale covering such that $U_i\to S$ factors
as $U_i\to V_i\to S$ with $V_i\to S$ etale; form the associated
Cartesian diagrams

$$
\begin{array}{ccc}
U_i & \xleftarrow{h_i} & U_i\times_XY\\
f_i\big\downarrow & & \big\downarrow e_i\\
V_i & \xleftarrow{g_i} & V_i\times_ST,
\end{array}
$$

and put $\mathcal F_i=\mathcal F|_{V_i\times_ST}$ and
$K_i=K|_{V_i\times_ST}$ for a sheaf $\mathcal F$ resp. a complex $K$
on $T_{\Et}$.

1. If $f_i^{-1}g_{i,*}\mathcal F_i=h_{i,*}e_i^{-1}\mathcal F_i$ for
all $i$, then $f^{-1}g_*\mathcal F=h_*e^{-1}\mathcal F$.
1. If $f_i^{-1}Rg_{i,*}K_i=Rh_{i,*}e_i^{-1}K_i$ for all $i$, then
$f^{-1}Rg_*K=Rh_*e^{-1}K$.
1. If $\mathcal F$ is an abelian sheaf and
$f_i^{-1}R^qg_{i,*}\mathcal F_i=R^qh_{i,*}e_i^{-1}\mathcal F_i$
for all $i$, then
$f^{-1}R^qg_*\mathcal F=R^qh_*e^{-1}\mathcal F$.
