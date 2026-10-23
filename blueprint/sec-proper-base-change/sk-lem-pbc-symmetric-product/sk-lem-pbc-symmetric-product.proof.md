+++
kind = "proof"
of = "sk-lem-pbc-symmetric-product"
uses = ["sk-lem-pbc-finite", "sk-lem-pbc-composition-cancellation", "sk-prop-av-pqf-finite"]
+++
Use the coefficients of a product of binary linear forms:

$$
\prod_{i=1}^n(x_iT+y_iU)=\sum_{j=0}^nF_jT^{n-j}U^j,\qquad
\sigma_n\bigl(([x_i:y_i])_i\bigr)=[F_0:\cdots:F_n].
$$

Every $F_j$ is homogeneous of degree one in each pair $(x_i,y_i)$. The
corresponding sections of $\mathcal O(1,\ldots,1)$ have no common zero: at a
geometric point every linear factor is nonzero, so their product is nonzero.
They therefore define the stated morphism over any $S$, and the construction
commutes with base change.

The elementary symmetric-polynomial description is visible on the target
chart $F_0\neq0$. Its preimage is the chart where every $x_i$ is invertible.
Over an affine base $\operatorname{Spec}(A)$ put $w_i=y_i/x_i$ and
$c_j=F_j/F_0$. The coordinate map is

$$
A[c_1,\ldots,c_n]\longrightarrow A[w_1,\ldots,w_n],\qquad
c_j\longmapsto e_j(w_1,\ldots,w_n).
$$

Each $w_i$ satisfies the monic equation

$$
W^n-c_1W^{n-1}+c_2W^{n-2}-\cdots+(-1)^nc_n=0.
$$

This makes the map finite on that chart.

Global finiteness follows from properness and finite fibres. The source is
proper over $S$ and the target is separated over $S$, so $\sigma_n$ is
proper, by the closed-graph argument. Over an algebraically closed field a
nonzero binary form of degree $n$ has a unique multiset of linear factors up
to nonzero scalars. Its fibre therefore has at most $n!$ geometric points,
given by their orderings. The fibres are of finite type over fields; having
finitely many geometric points makes them zero dimensional. Thus $\sigma_n$
is quasi-finite, and a proper quasi-finite morphism is finite
([sk-prop-av-pqf-finite]; Stacks Project, Tag 02LS). Factorization of binary
forms also shows that every geometric fibre is nonempty, so $\sigma_n$ is
surjective. This argument includes forms with a root at infinity.

The projection $(\mathbf P^1_S)^n\to S$ is a composite of $n$
projective-line projections over successive bases. It satisfies
$\mathrm{PBC}_\Lambda$ by the hypothesis and part (1) of
[sk-lem-pbc-composition-cancellation]. [sk-lem-pbc-finite] gives
$\mathrm{PBC}_\Lambda$ for $\sigma_n$. Part (2) of
[sk-lem-pbc-composition-cancellation] cancels $\sigma_n$ and gives
$\mathrm{PBC}_\Lambda$ for $\mathbf P^n_S\to S$. The case $n=0$ is the identity.
