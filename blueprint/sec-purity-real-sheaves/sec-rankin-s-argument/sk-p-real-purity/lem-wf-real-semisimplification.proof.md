+++
kind  = "proof"
of    = "lem-wf-real-semisimplification"
+++
Let $V$ be the global Weil representation from the monodromy datum
of [def-wf-monodromy-data] and choose a composition
series $0=V_0\subsetneq\cdots\subsetneq V_t=V$ as in
[def-mg-weil-composition-series]. Under the lisse
sheaf–representation correspondence, the $V_i$ give Weil-stable lisse
subsheaves $\mathcal F_i$, and the semisimplification is
$\bigoplus_i\mathcal F_i/\mathcal F_{i-1}$ by
[def-mg-weil-semisimplification]. At a closed point $x$, the local
Frobenius of [def-weil-punctual-weights] acts through $\rho(F_x)$ by [p-real-operations], so it preserves this filtration.
In a basis adapted to it, its matrix is upper block triangular, with
diagonal blocks the local Frobenius matrices on the quotients
$\mathcal F_i/\mathcal F_{i-1}$. Therefore, by [p-linear-filtration],

$$
\det(1-tF_x\mid\mathcal F_{\bar x})
=\prod_i\det(1-tF_x\mid
(\mathcal F_i/\mathcal F_{i-1})_{\bar x}),
$$

which is exactly the characteristic polynomial of the direct-sum
semisimplification. Thus all local characteristic polynomials, and hence
$\iota$-reality in the sense of [def-wf-iota-real], are unchanged.
