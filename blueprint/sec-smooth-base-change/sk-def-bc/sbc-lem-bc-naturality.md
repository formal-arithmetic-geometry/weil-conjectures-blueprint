+++
id = "sbc-lem-bc-naturality"
kind = "lemma"
title = "Naturality of the base-change map"
lean = ["AlgebraicGeometry.Etale.baseChange_naturality"]
order = 2069
uses = ["sbc-def-base-change-map", "sbc-def-base-change-square"]
+++
For a base-change square the
derived base-change maps $\operatorname{BC}_{f,g}(K)$ of
[sbc-def-base-change-map] are natural in $K$: for every morphism
$u:K\to K'$ in $D(T_{\Et},\Lambda)$ the square

$$
\begin{array}{ccc}
Lf^*Rg_*K & \xrightarrow{\ \operatorname{BC}_{f,g}(K)\ } & Rh_*Le^*K\\
\big\downarrow{\scriptstyle Lf^*Rg_*u} & & \big\downarrow{\scriptstyle Rh_*Le^*u}\\
Lf^*Rg_*K' & \xrightarrow{\ \operatorname{BC}_{f,g}(K')\ } & Rh_*Le^*K'
\end{array}
$$

is commutative.
