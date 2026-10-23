+++
id = "sbc-lem-bc-integral-base"
kind = "lemma"
title = "Integral base change on the source"
lean = ["AlgebraicGeometry.Etale.nonempty_arrowIso_baseChangeHomologyMap_comp", "AlgebraicGeometry.Etale.isIso_baseChangeHomologyMap_iff_of_isIntegralHom", "AlgebraicGeometry.Etale.isZero_of_isZero_lowerStar_obj"]
order = 2066
uses = ["lemma-weil-pbc-finite-direct-image-exact", "sbc-def-base-change-map", "sbc-def-base-change-property", "sbc-lem-integral-etale-direct-image-exact"]
+++
With $f:X\to S$ and $n$ as in [sbc-def-base-change-property] and some
$q\geq1$, consider
commutative
diagrams

$$
\begin{array}{ccccccc}
X & \xleftarrow{\;\;} & X' & \xleftarrow{\pi'} & X'' & &
Y\\
f\big\downarrow & & \big\downarrow f' & & \big\downarrow f'' & &
\big\downarrow e\\
S & \xleftarrow{\;\;} & S' & \xleftarrow{\;\pi\;} & S'' & &
T
\end{array}
$$

and the diagram with the outer
$h=h'\circ\pi''$, $g=g'\circ\pi$ (as horizontal composites), all squares
Cartesian, $g'$ quasi-compact and quasi-separated, and $\pi$ integral.
Let $\mathcal F$ be an abelian sheaf on $T_{\Et}$ annihilated by $n$.
If

$$
f'^{-1}R^qg_*\mathcal F\xrightarrow{\ \sim\ }R^qh_*e^{-1}\mathcal F
$$

is an isomorphism, then
$f''^{-1}R^qg'_*\mathcal F\to R^qh'_*e^{-1}\mathcal F$ is an
isomorphism.
