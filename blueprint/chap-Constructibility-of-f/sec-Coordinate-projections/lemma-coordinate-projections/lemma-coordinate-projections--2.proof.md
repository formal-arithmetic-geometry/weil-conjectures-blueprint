+++
kind = "proof"
of = "lemma-coordinate-projections--2"
order = 573005
+++
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

*Source:* the proof of Lemma [lemma-coordinate-projections].
