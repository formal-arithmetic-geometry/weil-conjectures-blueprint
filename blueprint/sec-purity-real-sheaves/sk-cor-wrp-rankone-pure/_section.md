+++
id = "sk-cor-wrp-rankone-pure"
kind = "corollary"
title = "Rank-one weights"
order = 3849
uses = ["sk-d-real-weights", "sk-p-real-rankone"]
lean = ["AlgebraicGeometry.WeilGroup.IsLisse.isPunctuallyPure_of_finrank_eq_one"]
tags = ["sketch"]
+++
Every rank-one lisse Weil sheaf on a smooth geometrically connected
curve is punctually $\iota$-pure ([sk-d-real-weights]). For $c=\chi(s)$ its
weight is $\lambda_\iota(c)=2\log_q|\iota(c)|$.

*Complement.* For any degree-one lift $s$ and $z=\chi(s)$, the functions
$w\mapsto z^{\deg w}$ and $\chi_{\mathrm{fin}}(w)=\chi(w)z^{-\deg w}$ are
characters, $\chi=\chi_{\mathrm{fin}}\cdot z^{\deg}$,
$\chi_{\mathrm{fin}}(s)=1$ and $\chi_{\mathrm{fin}}(W(U_0))=\chi(P)$
([det-p-rankone], [cor-wf-rank-one-degree-factorization-curve]).
