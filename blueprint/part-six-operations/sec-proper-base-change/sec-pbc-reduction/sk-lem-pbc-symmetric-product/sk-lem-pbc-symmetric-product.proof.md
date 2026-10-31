+++
kind = "proof"
of = "sk-lem-pbc-symmetric-product"
uses = ["sk-lem-pbc-finite", "sk-lem-pbc-composition-cancellation", "sk-prop-av-isogeny"]
+++
The idea is that $\mathbf P^n$ parametrizes binary forms of degree $n$
up to scalars, and $\sigma_n$ multiplies $n$ linear forms. Over a field
this is the quotient of $(\mathbf P^1)^n$ by the symmetric group, so it
is finite and surjective, and then $\mathrm{PBC}_\Lambda$ for $\mathbf P^n$ follows by
cancelling $\sigma_n$.
We first construct $\sigma_n$ and check that it is finite and surjective.
We use the coefficients of a product of binary linear forms:

$$
\prod_{i=1}^n(x_iT+y_iU)
=\sum_{j=0}^nF_jT^{n-j}U^j,\qquad
\sigma_n\bigl(([x_i:y_i])_i\bigr)=[F_0:\cdots:F_n].
$$

Every $F_j$ is homogeneous of degree one in each pair $(x_i,y_i)$.
The corresponding sections of $\mathcal O(1,\ldots,1)$ have no common
zero, since at a geometric point every linear factor is nonzero, and
hence so is their product. Therefore they define the stated morphism over any
$S$, and the construction commutes with base change.

For example, on the chart $F_0\ne0$ of the target, whose preimage is the
chart where every $x_i$ is invertible, the coordinates $c_j=F_j/F_0$ pull
back to the elementary symmetric polynomials in the $w_i=y_i/x_i$, as in
the classical description of $\mathbf A^n$ as the quotient of
$\mathbf A^n$ by the symmetric group.

Finiteness of $\sigma_n$ follows from properness and finiteness of
the fibres. Since the source is proper over $S$ and the target is separated over
$S$, the morphism $\sigma_n$ is proper. Over an algebraically closed
field, a nonzero binary form of degree $n$ is a product of $n$ linear
forms $x_iT+y_iU$, and these are unique up to order and up to
multiplying each by a nonzero constant. Here a factor with $x_i=0$ is a
multiple of $U$ and corresponds to the point $[0:1]$. In other words, the form determines the multiset of
points $[x_i:y_i]\in\mathbf P^1$. Hence every geometric fibre of
$\sigma_n$ is nonempty, so that $\sigma_n$ is surjective, and has at
most $n!$ geometric points, namely the orderings of this multiset. The fibres are
of finite type over fields with finitely many geometric
points, hence zero dimensional. Thus $\sigma_n$ is quasi-finite, and a proper
quasi-finite morphism is finite [Stacks, Tag 02LS](https://stacks.math.columbia.edu/tag/02LS).

The projection $(\mathbf P^1_S)^n\to S$ is a composite of $n$
projections of projective lines over successive bases, so it satisfies
$\mathrm{PBC}_\Lambda$ by the hypothesis on projective lines and
Lemma [sk-lem-pbc-composition-cancellation](i).
By Lemma [sk-lem-pbc-finite], $\mathrm{PBC}_\Lambda$ holds for $\sigma_n$. Cancelling $\sigma_n$ by
Lemma [sk-lem-pbc-composition-cancellation](ii), we obtain
$\mathrm{PBC}_\Lambda$ for $\mathbf P^n_S\to S$. The case $n=0$ is the identity.
