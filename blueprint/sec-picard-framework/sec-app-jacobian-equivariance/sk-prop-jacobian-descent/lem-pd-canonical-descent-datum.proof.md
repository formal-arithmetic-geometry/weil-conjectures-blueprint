+++
kind  = "proof"
of    = "lem-pd-canonical-descent-datum"
+++
Write $\theta_f$ for the bijection between the $T$-points of $V$ over
$f:T\to X$ and $F(T\xrightarrow{p\circ f}Y)$ given by the representation.
The transport is $\theta_{f_2}^{-1}\circ\theta_{f_1}$, which makes sense
because $f_1$ and $f_2$ define the same scheme $T$ over $Y$. Naturality in
$T$ holds because the $\theta_f$ are natural in $(T,f)$ and $F$ is a
functor. For $f_1=f_2$ the transport is the identity, and the cocycle
condition is [lem-pd-descent-cocycle]. So the transports form a descent
datum in transport form. By the Yoneda lemma this is the same as an
isomorphism $\varphi:\mathrm{pr}_0^*V\to\mathrm{pr}_1^*V$ over
$X\times_YX$ satisfying the cocycle condition of [def-pd-descent-datum]
([Stacks, Tag 023V](https://stacks.math.columbia.edu/tag/023V)): $\varphi$ is the transport for the universal pair
$\mathrm{pr}_0,\mathrm{pr}_1$.

For the special case, take $X=\Spec(k_s)$, $Y=\Spec(k)$ and
$F=\operatorname{Pic}^0_{C/k}$. By [cor-pd-pic0-base-change] the
restriction of $F$ to schemes over $\Spec(k_s)$ is
$\operatorname{Pic}^0_{C_s/k_s}$, which $J_s$ represents by
[thm-pd-geometric-pic0] and [def-sc-jacobian].
