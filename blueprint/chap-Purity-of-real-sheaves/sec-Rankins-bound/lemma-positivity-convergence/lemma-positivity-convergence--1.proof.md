+++
kind = "proof"
of = "lemma-positivity-convergence--1"
order = 1159002
uses = []
+++
Write $f_j=\sum_na_{j,n}t^n$ and $L=\sum_nA_nt^n$. A finite
subproduct containing $f_j$ is $f_jg$, where $g$ has nonnegative
coefficients and constant coefficient one. The term $a_{j,n}g_0$ in
the coefficient of $t^n$ is $a_{j,n}$, and all the other terms are
nonnegative. Thus every such subproduct dominates $f_j$
coefficientwise. These inequalities define a closed set in the
coefficientwise topology. Passing to the limit gives
$0\le a_{j,n}\le A_n$ for every $n$.

For $0\le r<\rad(L)$, the series $\sum_n|A_n|r^n$ converges, so
comparison gives convergence of $\sum_n|a_{j,n}|r^n$.
Taking all such $r$ proves $\rad(L)\le\rad(f_j)$; this is the
coefficient comparison in `PowerSeries.radius_le_radius_of_norm_coeff_le`.

For the second assertion, put $G=P^{-1}$. Since $P(0)\ne0$, the
formal identity $PG=1$ holds. If $|z|<\rad(G)$, the series for
$G(z)$ converges absolutely, and the series for $P(z)$ is finite.
Their Cauchy product therefore gives

$$
P(z)\sum_{n\ge0}[t^n]G\,z^n=1.
$$

Hence $P(z)\ne0$. Applying this over $\mathbf C$ to $P_j$ and using
$\rad(L)\le\rad(f_j)$ proves the last assertion.
