+++
kind  = "proof"
of    = "lem-a1-finite-boundary-weights"
+++
Here $Z=Z_0\times_{k_0}k$. Evaluation at geometric points gives, as in
the proof of [lem-a1-finite-boundary-cohomology],

$$
H_c^0(Z,\mathcal G)=\bigoplus_{x\in|Z_0|}\ \bigoplus_{z\mapsto x}\mathcal G_{\bar z},
$$

the inner sum running over the $\deg(x)=[\kappa(x):k_0]$ geometric points
$z$ of $Z$ over $x$. The Frobenius $F$ preserves each $x$-block, permuting
its $\deg(x)$ summands cyclically, and $F^{\deg(x)}$ acts on each summand
as $F_x$ on $\mathcal G_{\bar x}$. Hence the eigenvalues of $F$ on the
$x$-block are $\deg(x)$-th roots of eigenvalues of $F_x$: if $\alpha$ is
one of them, $|\iota(\alpha)|^{\deg(x)}\le q_x^{w/2}=q^{\deg(x)w/2}$ by
hypothesis, so $|\iota(\alpha)|\le q^{w/2}$, i.e. all eigenvalues of $F$
on $H_c^0(Z,\mathcal G)$ have weight at most $w$. So $H_c^0(Z,\mathcal G)$
is mixed of weights at most $w$ by [lem-a1-punctual-bound-module-mixed].
