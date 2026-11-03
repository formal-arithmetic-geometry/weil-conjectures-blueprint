+++
kind  = "proof"
of    = "prop-av-tate-no-frobenius-fixed"
+++
In the finite-field setting of [d-ab-field], the fixed points of
$x\mapsto x^q$ in $\bar k$ are exactly $k_0$: every element of $k_0$ is a
root of $T^q-T$ (as $k_0^\times$ has order $q-1$), and this polynomial has
at most $q$ roots. Now let $P\in A=A_0(\bar k)$ with $\sigma P=P$. Choose
one of the finitely many affine charts $\operatorname{Spec}R$ of $A_0$,
$R=k_0[x_1,\dots,x_m]/I$, containing the image of $P$; since $\sigma$ acts
by coordinates over $k_0$, the point $\sigma P$ has the same image, and in
this chart $P$ is a $k_0$-algebra map $\varphi:R\to\bar k$ with
$\sigma\circ\varphi=\varphi$. Hence every $\varphi(x_i)$ lies in $k_0$, so
$P\in A_0(k_0)$ and there are at most $q^m$ such points in the chart.
Thus $A^\sigma=A_0(k_0)$ is a finite group.
Apply [lem-tate-module-no-fixed] to the abelian group $A$ and the automorphism
$\sigma$; it gives $(T_\ell A)^\sigma=0$ and $(V_\ell A)^\sigma=0$, and the
same for $F=\sigma^{-1}$.
