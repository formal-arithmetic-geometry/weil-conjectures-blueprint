+++
kind  = "proof"
of    = "sk-p-tensor"
+++
Apply [sk-p-central] to $V^{\mathrm{ss}}\oplus{V'}^{\mathrm{ss}}$, and let
$c_a$ and $d_b$ be the scalars by which its central element of degree $N$
acts on $A_a$ and $B_b$. The determinant weight is read off from the
central scalar ([sk-p-readout]), so

$$
\dw_\iota(A_a)=\lambda_\iota(c_a)/N,
\qquad
\dw_\iota(B_b)=\lambda_\iota(d_b)/N.
$$

The central element acts by $c_ad_b$ on $A_a\otimes B_b$, and hence on
every simple factor of this tensor product. These factors have finite
geometric determinant by hypothesis, so the same lemma shows that their
determinant weight is the asserted sum. Each $A_a\otimes B_b$ is nonzero
and therefore has a simple factor. Since [sk-r-linear-library] identifies
these factors with those of $V\otimes V'$, both assertions follow.

For the complement, if $\deg$ is trivial, all weights of representations
with finite geometric determinant vanish, since $\lambda$ kills elements
of finite order. Otherwise $\deg(W)=e\mathbf Z$ with $e>0$, and
$\deg_0=\deg/e$ is surjective with the same kernel $P$. Writing
$\gamma=u\gamma_0^m$ with $\deg_0(\gamma_0)=1$, $u\in P$ and
$m=\deg_0(\gamma)$, each weight at $\gamma$ is $m$ times the weight at
$\gamma_0$, because $\lambda$ kills the finite-order factor $\delta(u)$. So
the formula at $\gamma_0$, proved above, gives it at $\gamma$.
