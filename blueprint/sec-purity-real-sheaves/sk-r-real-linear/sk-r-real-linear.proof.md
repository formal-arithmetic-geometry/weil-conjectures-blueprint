+++
kind  = "proof"
of    = "sk-r-real-linear"
uses = ["sk-p-linear-filtration", "sk-p-linear-spectra", "sk-d-real-weights"]
+++
*Semisimplification.* By [sk-p-linear-filtration], characteristic polynomials
multiply along a filtration by stable subspaces. A composition series has the
semisimplification as its associated graded, so each $P_x$ is unchanged. The
weights and the reality of [sk-d-real-weights] depend only on the $P_x$
([lem-wf-real-semisimplification]).

*Duality.* By [sk-p-linear-spectra] the eigenvalues of $f^\vee$ are the
$\alpha^{-1}$. Since $|\iota(\alpha^{-1})|=|\iota\alpha|^{-1}$, the weight
changes sign ([lem-tw-dual-negation], [lem-tw-multiplicativity]).

*Exterior powers.* By [sk-p-linear-spectra] the eigenvalues of $\bigwedge^sf$
are the products $\alpha_{i_1}\cdots\alpha_{i_s}$ over $i_1<\cdots<i_s$.
Complex conjugation permutes the multiset $\{\iota\alpha_i\}$, so it permutes
these products, and $\iota P_x(\bigwedge^s\mathcal F,T)$ has real coefficients
([lem-rp-exterior-reality]).
