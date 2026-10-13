+++
id = "prop-sf-closed-unit-all-stages"
kind = "theorem"
title = "Closed direct image is fully faithful at every coefficient stage"
order = 2205
tags = ["latex:proposition"]
uses = ["def-weil-algebraically-closed-coefficients", "def-weil-derived-complete-integral-detailed", "def-weil-derived-direct-image", "def-weil-exceptional-inverse-image", "def-weil-rationalization-karoubi", "prop-sf-closed-immersion-unit", "prop-weil-open-closed-recollement-adjunctions", "prop-weil-pbc-direct-image-limits", "prop-weil-pbc-roos-triangle", "prop-weil-pbc-scalar-extension"]
+++
Let $i:Z\hookrightarrow X$ be a closed immersion of separated finite-type
$k$-schemes and let $\Lambda$ be one of the coefficient stages
$A_{E,n},\mathcal O_E,E,\Qlb$, with the categories $D^b_c(-,\Lambda)$ of
[def-weil-derived-complete-integral-detailed],
[def-weil-rationalization-karoubi],
[def-weil-algebraically-closed-coefficients] and the direct image
$i_*=Ri_*=Ri_!$ of [def-weil-derived-direct-image]. Then

$$
i_*:D^b_c(Z,\Lambda)\longrightarrow D^b_c(X,\Lambda)
$$

is fully faithful. Consequently, at every stage at which $i_*$ has a right
adjoint $Ri^!$ on these categories (the exceptional inverse image of
[def-weil-exceptional-inverse-image]), the adjunction unit is an isomorphism

$$
Q\xrightarrow{\ \sim\ }Ri^!i_*Q\qquad(Q\in D^b_c(Z,\Lambda)).
$$

At $\Lambda=A_{E,n}$ the right adjoint exists on the ambient categories and
this is [prop-sf-closed-immersion-unit].
