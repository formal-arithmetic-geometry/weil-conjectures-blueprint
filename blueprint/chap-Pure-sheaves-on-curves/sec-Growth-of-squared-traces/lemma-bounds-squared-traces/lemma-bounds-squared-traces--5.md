+++
id = "lemma-bounds-squared-traces--5"
kind = "lemma"
title = "Bounds for squared traces (5)"
name_showing = false
order = 1202006
aliases = ["bp-r371-5"]
lean = ["AlgebraicGeometry.WeilSheaf.l2Weight_eq_sub_of_traceEnergy_eq", "AlgebraicGeometry.WeilSheaf.traceEnergy_constantTwist"]
uses = ["definition-growth-squared-traces", "proposition-weights-under-usual-operations"]
+++
Let $F,F'$ be Weil sheaves on a $k_0$-scheme $X_0$, and let
$w\in\mathbf R$. If $S_n(F')=S_n(F)/q^{nw}$ for every
$n\in\mathbf N$, then $\nu(F')=\nu(F)-w$.

For $b\in\overline{\mathbf Q}_\ell^\times$ satisfying
$|\iota(b)|=q^{-w/2}$, with $\mathcal B_b$ as in
[proposition-weights-under-usual-operations], we have

$$
S_n(F\otimes\mathcal B_b)=\frac{S_n(F)}{q^{nw}}
\qquad(n\in\mathbf N),
$$

and consequently

$$
\nu(F\otimes\mathcal B_b)=\nu(F)-w
=\nu(F)+\lambda_\iota(b).
$$
