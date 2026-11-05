+++
kind = "proof"
of = "theorem-purity-real-sheaves-curves"
order = 1167
uses = ["lemma-filtrations-spectra", "proposition-lattices-representations-normal-scheme", "theorem-rank-one-sheaves-have-finite", "corollary-rank-one-weights", "definition-monodromy-groups", "lemma-normality-geometric-monodromy", "proposition-central-element-arithmetic-monodromy-group", "lemma-determinant-weight-from-central-scalar", "proposition-bound-largest-determinant-weight"]
+++
We group the constituents by determinant weight and
place each group, tensored with the determinants of the groups of
larger weight, in an exterior power where it carries the largest
determinant weight. There Proposition [proposition-bound-largest-determinant-weight] bounds the
eigenvalues of the group by its own determinant weight, and the same
argument applied to the dual gives the reverse bound.

Let $\mathcal G$ be an $\iota$-real lisse Weil sheaf on the curve. We
first prove the assertion when the curve is affine. There, replacing
$\mathcal G$ by its semisimplification changes neither its local characteristic
polynomials nor its irreducible constituents, and it keeps the sheaf
real, so we may assume that $\mathcal G$ is semisimple and write

$$
\mathcal G=\bigoplus_{i=1}^t\mathcal G_i,
\qquad \gamma_1>\cdots>\gamma_t,
\qquad r_i=\operatorname{rank}\mathcal G_i,
$$

where $\mathcal G_i$ is the sum of the irreducible constituents with
determinant weight $\gamma_i$.

Fix $i$, and let us find the exterior power in which $\mathcal G_i$,
together with the determinants of $\mathcal G_1,\dots,\mathcal G_{i-1}$,
carries the largest determinant weight. To this end set $m=\sum_{j<i}r_j$, and put
$B=\sum_{j<i}r_j\gamma_j$.  By
Proposition [proposition-determinant-weights-tensor-operations](2), the largest determinant weight of a
constituent of $\bigwedge^{m+1}\mathcal G$ is $B+\gamma_i$.  Indeed,
it is obtained by taking $n_j=r_j$ for every $j<i$ and $n_i=1$, and
every other choice gives a smaller sum, because the $\gamma_j$ are
strictly decreasing.  Moreover, exterior powers of a real sheaf are real. Indeed,
their eigenvalues are the products of eigenvalues with distinct
indices, and complex conjugation permutes this multiset.  Hence
Proposition [proposition-bound-largest-determinant-weight] applies to $\bigwedge^{m+1}\mathcal G$.

The eigenvalues of $\mathcal G_i$ appear in
$\bigwedge^{m+1}\mathcal G$ not by themselves but multiplied by the
eigenvalues of the determinants of the groups of larger weight, and those
eigenvalues are known.
To make this precise, let $x$ be a closed point of the curve and $\alpha$ an eigenvalue of
$\operatorname{Frob}_x$ on $(\mathcal G_i)_{\bar x}$.
The decomposition of the exterior power of a direct sum shows that
$\bigwedge^{m+1}\mathcal G$ contains the summand

$$
(\det\mathcal G_1\otimes\cdots\otimes\det\mathcal G_{i-1})
\otimes\mathcal G_i.
$$

If $\beta_j$ is the eigenvalue of $\operatorname{Frob}_x$ on
$(\det\mathcal G_j)_{\bar x}$, then the product $\alpha\beta_1\cdots\beta_{i-1}$ is
an eigenvalue of $\operatorname{Frob}_x$ on the stalk of this summand
at $\bar x$. Since $\det\mathcal G_j$ is pure of weight $r_j\gamma_j$, we have
$|\iota(\beta_1\cdots\beta_{i-1})|^2=q_x^B$. Now
Proposition [proposition-bound-largest-determinant-weight] gives

$$
|\iota(\alpha)|^2q_x^B\le q_x^{B+\gamma_i},
\qquad |\iota(\alpha)|^2\le q_x^{\gamma_i}.
$$

For the reverse bound, note that the dual $\mathcal G^\vee$ is real as well, with determinant weights
$-\gamma_t>\cdots>-\gamma_1$. Applying the same argument to the
summand $\mathcal G_i^\vee$, we get
$|\iota(\alpha^{-1})|^2\le q_x^{-\gamma_i}$, and hence
$|\iota(\alpha)|^2=q_x^{\gamma_i}$. Since every
irreducible constituent of $\mathcal G$ is a summand of exactly one
$\mathcal G_i$, this proves the theorem on an affine curve.

On an arbitrary curve we restrict to an affine neighbourhood of a
given closed point $x$, which suffices because purity is a condition at
each closed point. It remains to check that the restriction changes neither the
constituents nor their determinant weights.
The neighbourhood is a nonempty open subscheme of a smooth geometrically
integral curve, so it is geometrically connected, and restriction to it preserves
irreducibility. Indeed, a connected finite étale cover of a normal connected
curve is integral, and hence remains connected after restriction to a dense
open. So the maps of geometric and of arithmetic fundamental groups are
surjective, and since restriction preserves the degree map, the map of Weil groups
is surjective too. Hence a subspace of the fibre is stable on the open
if and only if it is stable on the curve.

The restriction of a real sheaf is real, and by
Corollary [corollary-rank-one-weights] the determinant keeps its
weight. The affine case therefore applies at $x$, and since $x$ was
arbitrary, we obtain purity on the whole curve. Finally, the sheaf is mixed
because a composition series is a finite filtration with pure quotients.
