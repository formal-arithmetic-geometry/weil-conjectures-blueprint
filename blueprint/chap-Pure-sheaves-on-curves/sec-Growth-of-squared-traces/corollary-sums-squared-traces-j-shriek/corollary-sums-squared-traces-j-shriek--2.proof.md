+++
kind = "proof"
of = "corollary-sums-squared-traces-j-shriek--2"
order = 1211004
uses = ["theorem-weights-sums-squared-traces", "corollary-sums-squared-traces-j-shriek--1", "lemma-growth-finite-corrections"]
+++
Theorem [theorem-weights-sums-squared-traces] gives
$\nu(\mathcal G)=w$. The first inequality of
[corollary-sums-squared-traces-j-shriek--1] gives
$\nu(\mathcal G)\le\nu(j_*\mathcal G)$ by monotonicity of the growth
parameter. Lean uses
`AlgebraicGeometry.WeilSheaf.l2Weight_le_l2Weight_of_traceEnergy_le`,
which allows the two sheaves to live on different schemes.

Purity implies punctual weights $\le w$, so the second inequality
of [corollary-sums-squared-traces-j-shriek--1] applies. The estimate
`AlgebraicGeometry.WeilSheaf.l2Weight_le_max_of_traceEnergy_le_add`
underlying [lemma-growth-finite-corrections] gives

$$
\nu(j_*\mathcal G)\le\max\{\nu(\mathcal G),w-1\}=w.
$$

Indeed, for $\beta$ above both entries in the maximum, divide the
squared trace bound by $q^{n(\beta+1)}$: the term from $\mathcal G$
has limsup zero, and $Cq^{n(w-\beta-1)}$ tends to zero. Combining the
two inequalities proves the result.
