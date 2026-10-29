+++
kind = "proof"
of = "sk-lem-geo-coordinates"
+++
(1) The dimension of an integral scheme of finite type over a field is the
transcendence degree of its function field. Consider an irreducible component
of $X_{k(S)}\cap Y_\alpha$ with function field $L$. If $t_{\alpha r}$ is
algebraic over $k(S)$ on it, then the component does not dominate
$\mathbf A^1_{k(S)}$ and does not meet the generic fibre of $t_{\alpha r}$.
Otherwise $t_{\alpha r}$ is transcendental, and

$$
\operatorname{trdeg}_{k(S)(t_{\alpha r})}L=\operatorname{trdeg}_{k(S)} L-1\leq n-1.
$$

The left-hand side is the dimension of the corresponding component of the
generic fibre of $t_{\alpha r}$, and every component of that generic fibre
arises in this way.

(2) Let $t$ be the coordinate of $\mathbf A^1_S$. The ideal of the closed
complement of $V_{\alpha r}$ contains a nonzero polynomial
$P_{\alpha r}\in\mathcal O(S)[t]$. After inverting the leading coefficients of
these finitely many polynomials, we may assume that all of them are monic.
Since $t_{\alpha r}$ maps $Z\cap Y_\alpha$ into the complement of
$V_{\alpha r}$, the function $P_{\alpha r}(t_{\alpha r})$ vanishes at every
point of the reduced affine scheme $Z\cap Y_\alpha$, and hence it is zero in
its coordinate ring. Therefore this ring is a quotient of

$$
\mathcal O(S)[t_{\alpha1},\ldots,t_{\alpha m_\alpha}]/
      (P_{\alpha1}(t_{\alpha1}),\ldots,P_{\alpha m_\alpha}(t_{\alpha m_\alpha})),
$$

which is generated as an $\mathcal O(S)$-module by the monomials whose exponent
in each variable is less than the degree of the corresponding polynomial. Thus
each $Z\cap Y_\alpha$ is finite over $S$, and $Z\to S$ has finite fibres. Since
$Z$ is closed in the projective scheme $Y$, the morphism $Z\to S$ is proper
with finite fibres, hence finite
[Stacks, Tag 02LS](https://stacks.math.columbia.edu/tag/02LS).
