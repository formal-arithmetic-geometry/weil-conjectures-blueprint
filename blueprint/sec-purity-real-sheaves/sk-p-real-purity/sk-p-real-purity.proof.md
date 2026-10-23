+++
kind  = "proof"
of    = "sk-p-real-purity"
+++
We first prove the assertion on an affine curve. Replacing the sheaf
by its semisimplification does not change its local characteristic
polynomials ([sk-r-real-linear], [lem-wf-real-semisimplification]), so we may
write

$$
 \mathcal G=\bigoplus_{i=1}^t\mathcal G_i,
 \qquad \gamma_1>\cdots>\gamma_t,
 \qquad r_i=\operatorname{rank}\mathcal G_i,
$$

where $\mathcal G_i$ is the sum of the irreducible constituents with
determinant weight $\gamma_i$ ([def-rp-weight-blocks]).

Fix $i$, set $N=\sum_{j<i}r_j$, and put
$B=\sum_{j<i}r_j\gamma_j$. By [sk-p-exterior] and [sk-d-real-detweights]
(that is, by [sk-cor-walg-curve-calculus]), the largest determinant weight of a
constituent of $\bigwedge^{N+1}\mathcal G$ is $B+\gamma_i$. Indeed,
it is obtained by taking $n_j=r_j$ for every $j<i$ and $n_i=1$, and
every other choice gives a smaller sum, because the $\gamma_j$ are
strictly decreasing. Exterior powers of a real sheaf are real, since
their eigenvalues are the products of eigenvalues with distinct
indices and complex conjugation permutes this multiset
([lem-rp-exterior-reality]). Hence [sk-p-real-rankin] applies to
$\bigwedge^{N+1}\mathcal G$.

Let $\alpha$ be an eigenvalue on the stalk of $\mathcal G_i$ at $x$.
The decomposition of the exterior power of a direct sum shows that
$\bigwedge^{N+1}\mathcal G$ contains the summand

$$
 (\det\mathcal G_1\otimes\cdots\otimes\det\mathcal G_{i-1})
        \otimes\mathcal G_i.
$$

On it, $\alpha$ contributes the eigenvalue $\alpha$ times the
eigenvalues of $\det\mathcal G_j$ for $j<i$. These determinants are
pure of weights $r_j\gamma_j$ ([sk-cor-wrp-rankone-pure]), so the product of
the squares of their absolute values at $x$ is $q_x^B$. Consequently
[sk-p-real-rankin] gives

$$
 |\iota(\alpha)|^2q_x^B\le q_x^{B+\gamma_i},
 \qquad |\iota(\alpha)|^2\le q_x^{\gamma_i}.
$$

The dual $\mathcal G^\vee$ is real as well, with determinant weights
$-\gamma_t>\cdots>-\gamma_1$ ([sk-cor-walg-curve-calculus]). Applying the
same argument to the summand $\mathcal G_i^\vee$, we get
$|\iota(\alpha^{-1})|^2\le q_x^{-\gamma_i}$. Hence
$|\iota(\alpha)|^2=q_x^{\gamma_i}$, as required.

Now let the curve be arbitrary, and choose a closed point $x$ and an
affine open neighbourhood of $x$. This neighbourhood is geometrically
connected, being a nonempty open subscheme of a smooth geometrically
integral curve. Restriction to it preserves irreducibility. Indeed, a
connected finite étale cover of a normal connected curve is integral,
and hence remains connected after restriction to a dense open; thus the
maps of geometric and of arithmetic fundamental groups are surjective.
Since restriction preserves the degree map, the map of Weil groups is
surjective too, and so the invariant subspaces on the open are exactly
those on the curve ([lem-wf-dense-open-pi1-surjective], [sk-d-real-weil]).

The restriction of a real sheaf is real, and the determinant keeps its
weight by [sk-cor-wrp-rankone-pure]. Hence the affine case
applies at $x$, and since $x$ was arbitrary, we obtain purity on the
whole curve ([thm-rp-real-lisse-purity-affine]). Finally, a composition series
is a finite filtration with pure quotients, which proves that the sheaf is
mixed.
