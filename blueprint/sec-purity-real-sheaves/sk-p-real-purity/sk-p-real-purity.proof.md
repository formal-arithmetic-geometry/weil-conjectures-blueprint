+++
kind  = "proof"
of    = "sk-p-real-purity"
+++
The idea is to group the constituents by determinant weight and to
place each group, tensored with the determinants of the groups of
larger weight, in an exterior power where it carries the largest
determinant weight. [sk-p-real-rankin] then bounds the
eigenvalues of the group by its own determinant weight, and the
determinant of the group gives the reverse bound.
Let $\mathcal G$ be an $\iota$-real lisse Weil sheaf on the curve. We
first prove the assertion when the curve is affine. Replacing
$\mathcal G$ by its semisimplification changes neither its local characteristic
polynomials nor its irreducible constituents, and it keeps the sheaf
real ([sk-r-real-linear], [lem-wf-real-semisimplification]), so we may
assume that $\mathcal G$ is semisimple and write

$$
 \mathcal G=\bigoplus_{i=1}^t\mathcal G_i,
 \qquad \gamma_1>\cdots>\gamma_t,
 \qquad r_i=\operatorname{rank}\mathcal G_i,
$$

where $\mathcal G_i$ is the sum of the irreducible constituents with
determinant weight $\gamma_i$ ([def-rp-weight-blocks]).

Fix $i$, set $N=\sum_{j<i}r_j$, and put
$B=\sum_{j<i}r_j\gamma_j$. By the exterior formula (2) of
[sk-prop-walg-determinant-weights], the largest determinant weight of a
constituent of $\bigwedge^{N+1}\mathcal G$ is $B+\gamma_i$. Indeed,
it is obtained by taking $n_j=r_j$ for every $j<i$ and $n_i=1$, and
every other choice gives a smaller sum, because the $\gamma_j$ are
strictly decreasing. Exterior powers of a real sheaf are real, since
their eigenvalues are the products of eigenvalues with distinct
indices and complex conjugation permutes this multiset
([lem-rp-exterior-reality]). Hence [sk-p-real-rankin] applies to
$\bigwedge^{N+1}\mathcal G$.

Let $x$ be a closed point of the curve and $\alpha$ an eigenvalue of
$\operatorname{Frob}_x$ on $(\mathcal G_i)_{\bar x}$.
The decomposition of the exterior power of a direct sum shows that
$\bigwedge^{N+1}\mathcal G$ contains the summand

$$
 (\det\mathcal G_1\otimes\cdots\otimes\det\mathcal G_{i-1})
        \otimes\mathcal G_i.
$$

Let $\beta_j$ be the eigenvalue of $\operatorname{Frob}_x$ on
$(\det\mathcal G_j)_{\bar x}$. Then $\alpha\beta_1\cdots\beta_{i-1}$ is
an eigenvalue of $\operatorname{Frob}_x$ on the stalk of this summand
at $\bar x$. Since $\det\mathcal G_j$ is pure of weight $r_j\gamma_j$
([sk-cor-wrp-rankone-pure], [sk-d-real-detweights]), we have
$|\iota(\beta_1\cdots\beta_{i-1})|^2=q_x^B$. Applying
[sk-p-real-rankin], we get

$$
 |\iota(\alpha)|^2q_x^B\le q_x^{B+\gamma_i},
 \qquad |\iota(\alpha)|^2\le q_x^{\gamma_i}.
$$

Every eigenvalue of $\operatorname{Frob}_x$ on $(\mathcal G_i)_{\bar x}$
therefore has $|\iota(\alpha)|^2\le q_x^{\gamma_i}$. Their product is the
eigenvalue of $\operatorname{Frob}_x$ on $(\det\mathcal G_i)_{\bar x}$,
which is pure of weight $r_i\gamma_i$, so the squares of their absolute
values multiply to $q_x^{r_i\gamma_i}$. Hence every inequality is an
equality, and $|\iota(\alpha)|^2=q_x^{\gamma_i}$, as required.

Now let the curve be arbitrary. We reduce to the affine case by
restricting to an affine neighbourhood of a given closed point $x$.
This neighbourhood is geometrically connected, being a nonempty open
subscheme of a smooth geometrically integral curve, and restriction to
it preserves irreducibility. To see this, recall that a connected
finite étale cover of a normal connected curve is integral, and
hence remains connected after restriction to a dense open. Thus the
maps of geometric and of arithmetic fundamental groups are surjective.
Since restriction preserves the degree map, the map of Weil groups is
surjective too, and so a subspace of the fibre is stable on the open
if and only if it is stable on the curve ([lem-wf-dense-open-pi1-surjective],
[sk-d-real-weil]).

The restriction of a real sheaf is real, and the determinant keeps its
weight by [sk-cor-wrp-rankone-pure]. Hence the affine case
applies at $x$, and since $x$ was arbitrary, we obtain purity on the
whole curve ([thm-rp-real-lisse-purity-affine]). Finally, a composition series
is a finite filtration with pure quotients, and so the sheaf is mixed.
