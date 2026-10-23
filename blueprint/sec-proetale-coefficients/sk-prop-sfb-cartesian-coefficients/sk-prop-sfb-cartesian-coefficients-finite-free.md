+++
id = "det-prop-sfb-cartesian-coefficients-finite-free"
kind = "lemma"
title = "$\\mathcal O_{F,X}$ is finite free over $\\mathcal O_{E,X}$"
order = 1263
uses = ["det-def-sfb-condensed-ring", "det-def-sfb-pullback-from-point", "det-prop-sfb-qlbar-colimit-x-invert-ell", "lem-sfb-subfield-flat"]
+++
Let $E\subset F$ be finite extensions of $\mathbf Q_\ell$ inside $\Qlb$, of degree $d=[F:E]$, and
let $X$ be a scheme. Then a choice of $\cO_E$-basis $b_1,\dots,b_d$ of $\cO_F$ induces
isomorphisms of $\cO_{E,X}$-modules, resp. $E_X$-modules,
$$
\cO_{E,X}^{\,d}\xrightarrow{\ \sim\ }\cO_{F,X},\qquad E_X^{\,d}\xrightarrow{\ \sim\ }F_X,
\qquad (a_i)\mapsto\textstyle\sum_ia_ib_i ,
$$
compatible with the maps $\cO_{E,X}\to E_X$ and $\cO_{F,X}\to F_X$ and with inverse image
along morphisms of schemes. In particular $\cO_{F,X}$ and $F_X$ are flat
([lem-sfb-subfield-flat]).
