+++
id = "sbc-thm-smooth-base-change"
kind = "theorem"
title = "Smooth base change"
order = 2032
uses = ["def-sbc-smooth-morphisms", "def-weil-pbc-scheme-conventions", "lemma-weil-pbc-direct-image-filtered-colimit", "lemma-weil-pbc-torsion-filtered-union", "sbc-def-base-change-map", "sbc-def-base-change-property", "sbc-def-base-change-square", "sbc-lem-base-change-composition", "sbc-lem-degree-zero-flat-base-change", "sbc-lem-etale-locality", "sbc-lem-rel-dim-one-induction", "lem-pc-smooth-characterization", "sbc-lem-smooth-geometrically-reduced", "sbc-thm-etale-local-normal-form"]
+++
Consider a cartesian diagram of
schemes

$$
\begin{array}{ccc}
X & \xleftarrow{\;h\;} & Y\\
f\big\downarrow & & \big\downarrow e\\
S & \xleftarrow{\;g\;} & T
\end{array}
$$

where $f$ is smooth and $g$ is
quasi-compact and
quasi-separated. Then

$$
f^{-1}R^qg_*\mathcal F=R^qh_*e^{-1}\mathcal F
$$

for any $q$ and any abelian sheaf $\mathcal F$ on $T_{\Et}$ all of
whose stalks at geometric points are torsion of orders invertible on
$S$, the isomorphism being the base-change map of
[sbc-def-base-change-map].
