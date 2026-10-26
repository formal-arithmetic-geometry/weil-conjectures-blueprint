+++
id = "lem-galois-descent"
kind = "lemma"
title = "Effective etale descent for finite etale morphisms"
order = 1373
lean = ["AlgebraicGeometry.finiteEtaleDescent", "AlgebraicGeometry.FiniteEtaleDescentData"]
uses = ["def-galois-categories", "def-pd-descent-datum", "def-weil-pbc-scheme-conventions", "lem-weil-pbc-fpqc-descend-finite", "lem-weil-pbc-fpqc-finer-than-etale"]
+++
Let $g:Y'\to Y$ be a surjective etale morphism, and put
$Y''=Y'\times_YY'$, $Y'''=Y'\times_YY'\times_YY'$. Then base change
$P\mapsto P\times_YY'$, with its canonical descent datum, is an
equivalence from the category of finite etale $Y$-schemes to the category
of finite etale $Y'$-schemes $P'$ endowed with a descent datum
[def-pd-descent-datum], i.e. an isomorphism
$\varphi:p_1^*P'\cong p_2^*P'$ over $Y''$ satisfying
$p_{13}^*\varphi=p_{23}^*\varphi\circ p_{12}^*\varphi$ over $Y'''$, with
morphisms the $Y'$-morphisms compatible with the descent data.
