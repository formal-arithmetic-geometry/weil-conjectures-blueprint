+++
id = "lem-wf-boundary-coinvariant-lower-bound"
kind = "lemma"
title = "Lower bound on the coinvariants at the boundary"
order = 2847
uses = ["d-real-boundary", "def-weil-punctual-weights", "def-wf-middle-extension", "lem-tw-dual-negation", "lem-wf-boundary-semicontinuity", "p-linear-spectra"]
+++
Let $X_0$ be a smooth geometrically connected affine curve over
$k_0=\mathbf F_q$, let $j:U_0\hookrightarrow X_0$ be a dense open
immersion with finite complement $S_0$, and let $\mathcal F$ be lisse
of rank $r\geq1$ on $U_0$, punctually
$\iota$-pure of weight $w$. Then for every $s\in S_0$ and every
eigenvalue $\alpha$ of the local Frobenius $F_s$ on the
*coinvariants* $\bigl(\mathcal F_{\bar\eta}\bigr)_{I_s}$ of the
local geometric generic stalk under the inertia group $I_s$ of [d-real-boundary],

$$
|\iota(\alpha)|^2\geq q_s^{w}.
$$

Thus the boundary *invariants* are bounded above and the boundary
*coinvariants* are bounded below by the same quantity $q_s^w$.

## Proof

The linear dual $\mathcal F^\vee$ is lisse on $U_0$, and by
[lem-tw-dual-negation] it is punctually $\iota$-pure of weight
$-w$; with the trivial filtration $0\subset\mathcal F^\vee$ it is
therefore punctually $\iota$-mixed of weights at most $-w$ in the
sense of [def-weil-punctual-weights]. The boundary semicontinuity
of [lem-wf-boundary-semicontinuity], applied to $\mathcal F^\vee$
with $\beta=-w$, gives that every eigenvalue $\beta_j$ of $F_s$ on
the boundary stalk $\bigl(j_*\mathcal F^\vee\bigr)_{\bar s}$ of the
middle extension satisfies
$|\iota(\beta_j)|^2\leq q_s^{-w}$.

That boundary stalk is the space of $I_s$-invariants of the local
geometric generic stalk of $\mathcal F^\vee$, and for a
finite-dimensional module $W$ over a group $G$ one has the standard
identification

$$
\bigl(W^\vee\bigr)^{G}=\bigl(W_{G}\bigr)^{\vee},
$$

the invariants of the dual being the dual of the coinvariants: a
functional fixed by $G$ is precisely one vanishing on the span of the
differences $gw-w$, that is on the kernel of the projection
$W\to W_G$. Applying this with $W=\mathcal F_{\bar\eta}$ and
$G=I_s$, the boundary stalk of $\mathcal F^\vee$ is
$\bigl((\mathcal F_{\bar\eta})_{I_s}\bigr)^\vee$. Its Frobenius
eigenvalues are the inverses ([p-linear-spectra]) of the eigenvalues $\alpha$ of $F_s$ on
$(\mathcal F_{\bar\eta})_{I_s}$, so the bound above reads
$|\iota(\alpha^{-1})|^2\leq q_s^{-w}$, i.e. $|\iota(\alpha)|^2\geq q_s^{w}$ for every such $\alpha$.
