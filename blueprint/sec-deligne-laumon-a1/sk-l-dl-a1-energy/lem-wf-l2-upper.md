+++
id = "lem-wf-l2-upper"
kind = "lemma"
title = "The $L^2$-weight is at most the weight"
order = 2760
uses = ["def-weil-punctual-weights", "def-wf-l2-norm", "lem-wf-point-count-linear-growth"]
lean = ["AlgebraicGeometry.LAdicWeilSheaf.l2Weight_le_of_hasWeightsAtMost"]
+++
Let $X_0$ be a smooth geometrically connected affine curve over
$k_0=\mathbf F_q$, and let $\mathcal F$ be a lisse Weil sheaf of rank $r$
on $X_0$, punctually $\iota$-mixed of weights at most $w$.
Then

$$
\|\mathcal F\|\le w.
$$

## Proof

At $y\in X_0(k_m)$ the eigenvalues of the Frobenius $F_y^{(m)}$
are the $m/d(y)$-th powers of the local eigenvalues at the closed
point below, hence have modulus at most $q^{mw/2}$ by the punctual
bounds of [def-weil-punctual-weights]; therefore

$$
\|f_{\mathcal F}\|_m^2\le r^2\cdot\#X_0(k_m)\cdot q^{mw}
\le C\,q^{m(w+1)}
$$

for a constant $C$ (the point-count bound of the affine curve,
[lem-wf-point-count-linear-growth] of the basic-weight chapter). The
$\limsup$ in [def-wf-l2-norm] is therefore $0$ for
$\beta>w$, hence $\|\mathcal F\|\le w$.
