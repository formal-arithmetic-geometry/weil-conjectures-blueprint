+++
kind = "proof"
of = "lemma-coordinate-projections"
order = 573
uses = ["lemma-coordinate-projections--1", "lemma-coordinate-projections--2"]
+++
Part (1) is a transcendence degree count. For part (2), note that a point
of $Z$ has all its coordinates in the finite sets of excluded values.
After shrinking $S$, these sets are cut out by monic polynomials, and
monic equations in every coordinate force finiteness.

(1) We use that the dimension of an integral scheme of finite type over a
field is the transcendence degree of its function field. Consider an
irreducible component of $X_{k(S)}\cap Y_\alpha$ with function field $L$.
If $t_{\alpha r}$ is algebraic over $k(S)$ on it, the component does
not meet the generic fibre of $t_{\alpha r}$, as it does not dominate
$\mathbf A^1_{k(S)}$. Otherwise $t_{\alpha r}$ is transcendental, and

$$
\operatorname{trdeg}_{k(S)(t_{\alpha r})}L
=\operatorname{trdeg}_{k(S)} L-1\leq n-1.
$$

The left-hand side is the dimension of the corresponding component of the
generic fibre of $t_{\alpha r}$, and every component of that generic
fibre arises in this way.

(2) Let $t$ be the coordinate of $\mathbf A^1_S$. The ideal of the
complement of $V_{\alpha r}$ contains a nonzero polynomial
$P_{\alpha r}\in\mathcal O(S)[t]$. Indeed, since $V_{\alpha r}$ is dense,
its complement is a proper closed subset of the integral scheme
$\mathbf A^1_S$, and its ideal is nonzero. After
inverting the leading coefficients of these finitely many polynomials, we
may assume that all of them are monic. The function
$P_{\alpha r}(t_{\alpha r})$ is zero in the coordinate ring of the reduced
affine scheme $Z\cap Y_\alpha$, because it vanishes at every point, $t_{\alpha r}$
mapping $Z\cap Y_\alpha$ into the complement of $V_{\alpha r}$. This ring is
therefore a quotient of

$$
\mathcal O(S)[t_{\alpha1},\ldots,t_{\alpha m_\alpha}]/
(P_{\alpha1}(t_{\alpha1}),\ldots,
P_{\alpha m_\alpha}(t_{\alpha m_\alpha})),
$$

which is generated as an $\mathcal O(S)$-module by the monomials whose
exponent in each variable is less than the degree of the corresponding
polynomial. Each $Z\cap Y_\alpha$ is thus finite over $S$, and
$Z\to S$ has finite fibres. As $Z$ is closed in the projective scheme $Y$,
the morphism $Z\to S$ is also proper, and a proper morphism with finite
fibres is finite [Stacks, [02LS](https://stacks.math.columbia.edu/tag/02LS)].
