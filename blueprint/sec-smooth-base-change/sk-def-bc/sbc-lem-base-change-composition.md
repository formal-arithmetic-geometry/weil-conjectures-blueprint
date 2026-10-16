+++
id = "sbc-lem-base-change-composition"
kind = "lemma"
title = "Base change for a composite square"
lean = ["AlgebraicGeometry.Etale.isIso_baseChange_app_of_paste_horiz", "AlgebraicGeometry.Etale.isIso_homologyFunctor_map_baseChange_app_of_paste_horiz", "AlgebraicGeometry.Etale.isIso_baseChangeHomologyMap_of_paste_horiz", "AlgebraicGeometry.Etale.BaseChangeProperty.comp"]
order = 1430
uses = ["lem-weil-pbc-exchange-identity-pasting", "sbc-def-base-change-map", "sbc-def-base-change-square"]
+++
Consider a tower of Cartesian diagrams of schemes

$$
\begin{array}{ccc}
W & \xrightarrow{j} & Z\\
i\big\downarrow & & \big\downarrow k\\
X & \xrightarrow{h} & Y\\
f\big\downarrow & & \big\downarrow e\\
S & \xrightarrow{g} & T
\end{array}
$$

and let $K\in D(T_{\Et})$. If

$$
f^{-1}Rg_*K\xrightarrow{\ \sim\ }Rh_*e^{-1}K
\quad\text{and}\quad
i^{-1}Rh_*e^{-1}K\xrightarrow{\ \sim\ }Rj_*k^{-1}e^{-1}K
$$

are isomorphisms, then
$(f\circ i)^{-1}Rg_*K\to Rj_*(e\circ k)^{-1}K$ is an isomorphism
(``the outer rectangle'') and the analogous statement holds
degreewise for an abelian sheaf $\mathcal F$ on $T_{\Et}$ and the maps
$R^q$.
