+++
kind = "proof"
of = "lemma-finite-cover-projective-space"
order = 388
+++
Recall that $\mathbf P^n$ parametrizes binary forms of degree $n$
up to scalars. The map $\sigma_n$ multiplies $n$ linear forms. Over a field
it is the quotient of $(\mathbf P^1)^n$ by the symmetric group. We use the coefficients of a product of binary linear forms:

$$
\prod_{i=1}^n(x_iT+y_iU)
=\sum_{j=0}^nF_jT^{n-j}U^j,\qquad
\sigma_n\bigl(([x_i:y_i])_i\bigr)=[F_0:\cdots:F_n].
$$

Every $F_j$ is homogeneous of degree one in each pair $(x_i,y_i)$.
The corresponding sections of $\mathcal O(1,\ldots,1)$ have no common
zero. Indeed, at a geometric point every linear factor is nonzero, and
hence so is their product. Therefore the sections define the stated morphism over any
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
$\sigma_n$ is nonempty, and $\sigma_n$ is surjective. Each geometric
fibre has at most $n!$ geometric points, namely the orderings of this
multiset. A scheme of finite type over a field with finitely many
geometric points is zero dimensional, so $\sigma_n$ is quasi-finite. A
proper quasi-finite morphism is finite [Stacks, [02LS](https://stacks.math.columbia.edu/tag/02LS)].
