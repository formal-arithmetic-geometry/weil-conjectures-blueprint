+++
id = "lem-wf-l2-mixed-rigidity"
kind = "lemma"
title = "The $L^2$-weight of a mixed real lisse sheaf"
order = 3016
uses = ["def-weil-punctual-weights", "def-wf-iota-real", "def-wf-l2-norm", "lem-wf-l2-upper", "thm-rp-real-lisse-purity-affine", "thm-wf-l2-dictionary"]
+++
Let $\mathcal G\neq0$ be a lisse
real Weil sheaf on a smooth
geometrically connected affine curve, with a finite filtration whose
nonzero graded pieces are punctually pure.
Let $w(\mathcal G)$ be the maximum of their weights.
Then $\|\mathcal G\|=w(\mathcal G)$.

## Proof

Semisimplification preserves all local characteristic polynomials,
hence traces and the [def-wf-l2-norm] parameter.
By [thm-rp-real-lisse-purity-affine] its irreducible summands
are punctually pure in the sense of [def-weil-punctual-weights].
Group the summands of maximal weight $W=w(\mathcal G)$ into
$\mathcal A$, and the remaining summands into $\mathcal B$.
At each closed point the eigenvalues of $\mathcal A$ are exactly
those of the whole sheaf with modulus $q_x^{W/2}$.
Complex conjugation preserves modulus and the whole multiset by
[def-wf-iota-real]; thus $\mathcal A$ is real and pure.
By [thm-wf-l2-dictionary], $\|\mathcal A\|=W$.
If $\mathcal B=0$, this proves the result.
Otherwise let $W'<W$ bound its weights. By [lem-wf-l2-upper],
$\|\mathcal B\|\leq W'$, and also $\|\mathcal G\|\leq W$.

For any $b$ with $W'<b<W$, choose $c$ with $b<c<W$.
The definition of the supremum and the monotonicity of its defining
ratios show that
$\limsup_m\|f_{\mathcal A}\|_m^2/q^{m(c+1)}>0$.
There is consequently a subsequence on which
$\|f_{\mathcal A}\|_m\geq\epsilon q^{m(c+1)/2}$.
Meanwhile the bound $\|\mathcal B\|<b$ implies
$\|f_{\mathcal B}\|_m=o(q^{m(b+1)/2})$.
The triangle inequality in the finite-dimensional Euclidean space
of trace functions gives
$\|f_{\mathcal G}\|_m\geq\|f_{\mathcal A}\|_m-\|f_{\mathcal B}\|_m$.
On that subsequence its ratio at exponent $b$ is positive.
Therefore $\|\mathcal G\|\geq b$; letting $b\uparrow W$ proves equality.
