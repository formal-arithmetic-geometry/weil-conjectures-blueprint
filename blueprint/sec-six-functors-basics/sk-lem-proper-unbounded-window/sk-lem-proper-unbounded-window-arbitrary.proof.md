+++
kind = "proof"
of = "det-proper-unbounded-window-arbitrary"
+++
*Limit presentation.* By [sk-prop-pe-left-complete], $K\simeq R\varprojlim_n\tau_{\geq-n}K$. $Rp_*$ is right
adjoint to $p^*$, so it preserves products, and it is exact, so it preserves fibers; hence it preserves
derived limits of sequences: $Rp_*K\simeq R\varprojlim_nRp_*\tau_{\geq-n}K$.

*Eventual constancy.* The fibre of $\tau_{\geq-n-1}K\to\tau_{\geq-n}K$ is $\mathcal H^{-n-1}(K)[n+1]$, a sheaf
in degree $-n-1$. By [det-proper-unbounded-window-bounded-below], $Rp_*(\mathcal H^{-n-1}(K)[n+1])$ has
cohomology only in degrees $-n-1,\dots,2d-n$. From the long exact sequence, the transition map
$\mathcal H^q(Rp_*\tau_{\geq-n-1}K)\to\mathcal H^q(Rp_*\tau_{\geq-n}K)$ is an isomorphism as soon as $q$ and
$q+1$ lie outside $[-n-1,2d-n]$, i.e. for $n>2d-q+1$ (so that $q>2d-n$ and $q+1>2d-n$). The same holds for
$q-1$ for $n$ large.

*Milnor.* By [sk-prop-pe-milnor], there is an exact sequence of sheaves

$$
0\to R^1\varprojlim_n\mathcal H^{q-1}(Rp_*\tau_{\geq-n}K)\to\mathcal H^q(Rp_*K)\to\varprojlim_n\mathcal H^q(Rp_*\tau_{\geq-n}K)\to0.
$$

The tower in degree $q-1$ is eventually constant, so its $R^1\varprojlim$ vanishes (description as
$\coker(1-T)$ on the product, solved successively); the tower in degree $q$ is eventually constant, so its
limit is its eventual value. This gives the isomorphism.

*Consequences.* $\tau_{\geq-n}K$ is bounded below and lies in $\Dic(X,\Lambda)$, so
[det-proper-unbounded-window-bounded-below] gives $\mathcal H^q(Rp_*K)\in\IndCons(Y,\Lambda)$. If
$K\in\Dic^{\leq b}$ then so is $\tau_{\geq-n}K$, whence $\mathcal H^q(Rp_*K)=0$ for $q>b+2d+1$. An object of
$\Dic^{\geq a}$ is bounded below, so the lower bound is the bounded-below case.
