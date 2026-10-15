+++
kind = "proof"
of = "det-def-sfb-qlbar-condensed-subextensions"
+++
1. By induction it suffices to treat $n=2$. Let $E_2=\mathbf Q_\ell(b_1,\dots,b_m)$ (finitely many
   generators exist since $E_2$ is finite-dimensional). Then $E_1E_2=E_1(b_1,\dots,b_m)$, and a basis
   of $E_2$ over $\mathbf Q_\ell$ spans $E_1E_2$ over $E_1$, because the $E_1$-span of $E_2$ is a
   ring that is finite-dimensional over the field $E_1$ and a domain, hence a field containing $E_1$
   and the $b_j$. So $[E_1E_2:E_1]\le[E_2:\mathbf Q_\ell]$ and
   $[E_1E_2:\mathbf Q_\ell]=[E_1E_2:E_1][E_1:\mathbf Q_\ell]\le[E_1:\mathbf Q_\ell][E_2:\mathbf Q_\ell]$.
   The empty compositum is $\mathbf Q_\ell$ itself, so the poset is nonempty, and any two elements
   have an upper bound.
2. Each $x\in\Qlb$ is algebraic over $\mathbf Q_\ell$, so $\mathbf Q_\ell(x)$ is a finite
   subextension; for a finite set take the compositum of these, by 1.
