+++
id = "prose-06-06"
kind = "hidden"
title = "Duality for the projective line (3)"
order = 547
+++
Over $S=\operatorname{Spec}\bar k$, (6.2) reads
$R\Gamma(\mathbf P^1_{\bar k},A)\simeq A\oplus A(-1)[-2]$.
Here the shift $[-2]$ places the second summand in degree $2$, so that it is
$H^2$, and the twist $(-1)$ records how Galois acts on $H^2$: the
Kummer map identifies $H^2$ with
$\operatorname{Pic}(\mathbf P^1)\otimes\mu_{\ell^r}^{\otimes-1}$, that is, with
$A(-1)$. Twisting by $(1)$ and shifting by $[2]$ therefore moves this summand to degree $0$ with trivial twist. The map $\operatorname{Tr}_p$ is the projection onto this summand, and it sends the class
of a point to $1$. It is the counit of
$Rp_*\dashv p^*(1)[2]$ in
Proposition [proposition-adjunction-projective-line]. After its lift to
$\mathcal O_E$ in Section [subsec-The-projective-line], it is also the trace
map $\operatorname{Tr}_p$ of $\mathbf P^1$ in
Section [sec-Compatibilities].

As a check of the twist, let us work over $\mathbf F_q$. The geometric
Frobenius acts by $1$ on $H^0$ and by $q$ on $H^2=A(-1)$. The
alternating sum of the traces is $1+q=\#\mathbf P^1(\mathbf F_q)$, as in
Corollary [corollary-point-counting-zeta-function].
