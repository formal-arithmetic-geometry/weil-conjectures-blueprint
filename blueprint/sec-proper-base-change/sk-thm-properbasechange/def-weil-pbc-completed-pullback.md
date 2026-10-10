+++
id = "def-weil-pbc-completed-pullback"
kind = "definition"
title = "Completed pullback"
order = 1261
uses = ["def-weil-pbc-adic-coefficient-datum", "def-weil-pbc-complete-coefficient-datum", "def-weil-pbc-derived-inverse-limit", "def-weil-pbc-proetale-operations"]
+++
For $g:T'\to T$, levelwise inverse image on strict tower complexes has a
total left derived functor

$$
 Lg^*_{\operatorname{Tow}}:
 D(\operatorname{Tow}_{A}(T))
 \longrightarrow D(\operatorname{Tow}_{A}(T')).
$$

Its $n$-th evaluation on the reduction tower $K_\bullet$ of
[def-weil-pbc-adic-coefficient-datum] is $Lg_n^*K_n$. For a derived complete
$K$, define

$$
 Lg^*_{\mathrm{comp}}K
   =\Rlim\bigl(Lg^*_{\operatorname{Tow}}K_\bullet\bigr)
   =R\varprojlim_n\bigl(Lg^*K\otimes^L_\Lambda\Lambda/I^n\bigr)
 \quad\text{in }D(T'_{\Proet},A).
$$

The comparison from ordinary pullback is the completion map of $Lg^*K$.
