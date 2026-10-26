+++
id = "lem-exc-closed-localization"
kind = "lemma"
title = "Closed-site operations under weakly etale localization"
lean = ["AlgebraicGeometry.ProEtale.squareLowerStarIso", "AlgebraicGeometry.ProEtale.localizationRestrictionBaseChangeMap", "AlgebraicGeometry.ProEtale.isIso_localizationRestrictionBaseChangeMap_of_isPullback", "AlgebraicGeometry.ProEtale.mateEquiv_localizationRestrictionBaseChangeMap", "AlgebraicGeometry.ProEtale.isIso_baseChangeMap_of_isPullback", "AlgebraicGeometry.ProEtale.upperStarComp"]
order = 1091
uses = ["def-weil-pbc-cartesian-square", "def-weil-pbc-proetale-operations", "lem-weil-pbc-proetale-restriction-injectives"]
+++
Consider a cartesian square [def-weil-pbc-cartesian-square]
$$
\begin{array}{ccc}
W' & \xrightarrow{\;w'\;} & Z\\
{\scriptstyle g'}\downarrow & & \downarrow{\scriptstyle g}\\
W & \xrightarrow{\;w\;} & X
\end{array}
$$
with $w$ (hence $w'$) weakly etale and $g$ an arbitrary morphism, for
instance a closed immersion $Z\hookrightarrow X$. For pro-etale sheaves, the
inverse images along $w$ and $w'$ are restrictions to the slices over $W$ and
$W'$. The base change map
$$
 w^*g_*\longrightarrow g'_*w'^*
$$
is an isomorphism, and it corresponds, under the adjunctions $w^*\dashv w_*$
and $w'^*\dashv w'_*$, to the identification $g_*w'_*\cong w_*g'_*$ of direct
images along the two composites of the square. The two composites of inverse
images agree, $w'^*g^*\cong g'^*w^*$, both being identified with the inverse
image along the diagonal of the square. In particular restriction to $W$
commutes with the underived direct image along a closed immersion,
compatibly with the units and counits of these adjunctions.
