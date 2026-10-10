+++
id = "lem-galois-descent"
kind = "lemma"
title = "Effective etale descent for finite etale morphisms"
order = 964
uses = ["def-galois-categories", "def-weil-pbc-scheme-conventions", "lem-galois-glue"]
+++
Let $Y'\to Y$ be a surjective etale morphism with $Y'=\coprod_iY_i$,
and put $Y''=Y'\times_YY'$, $Y'''=Y'\times_YY'\times_YY'$. Then the
category of finite etale $Y$-schemes is equivalent to the category of
finite etale $Y'$-schemes $P'$ endowed with a descent datum, i.e. an
isomorphism $\varphi:p_1^*P'\cong p_2^*P'$ over $Y''$ satisfying
$p_{13}^*\varphi=p_{23}^*\varphi\circ p_{12}^*\varphi$ over $Y'''$.
