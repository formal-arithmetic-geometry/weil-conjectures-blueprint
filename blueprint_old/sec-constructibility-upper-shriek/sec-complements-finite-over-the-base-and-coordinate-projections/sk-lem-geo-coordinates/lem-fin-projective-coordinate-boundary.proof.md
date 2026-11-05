+++
kind  = "proof"
of    = "lem-fin-projective-coordinate-boundary"
+++
The ideal defining $\mathbf A^1_S\setminus V_{\alpha r}$
contains a nonzero polynomial $P_{\alpha r}\in A[t]$.
Invert the finitely many nonzero leading coefficients and divide
by them, making these polynomials monic. On the reduced scheme
$Z\cap Y_\alpha$, every $P_{\alpha r}(t_{\alpha r})$
vanishes: it vanishes at all points and the coordinate ring is
reduced. Hence $Z\cap Y_\alpha$ is closed in

$$
\operatorname{Spec}
A[t_1,\ldots,t_{m_\alpha}]/
(P_{\alpha1}(t_1),\ldots,P_{\alpha m_\alpha}(t_{m_\alpha})).
$$

This algebra is finite over $A$, since products of powers below
the respective degrees generate it. Thus every geometric fiber
of every $Z\cap Y_\alpha$ has finitely many points.
The cover is finite, so the fibers of $Z\to S$ are finite.
As a closed subscheme of the projective $Y$, $Z$ is projective;
[lem-fin-projective-finite-fibres] proves finiteness.
