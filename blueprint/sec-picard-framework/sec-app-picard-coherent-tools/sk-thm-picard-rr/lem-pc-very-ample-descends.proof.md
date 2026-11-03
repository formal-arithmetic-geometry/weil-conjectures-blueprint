+++
kind  = "proof"
of    = "lem-pc-very-ample-descends"
+++
By definition of very ampleness there is an immersion
$i:X_K\to\mathbf P^N_K$ with $i^*\mathcal{O}_{\mathbf P^N}(1)=\mathcal{L}_K$; it
is given by the base-point-free sections $t_j=i^*x_j\in H^0(X_K,\mathcal{L}_K)$,
$j=0,\dots,N$, the pullbacks of the coordinates $x_j$. By
[lem-pc-flat-base-change-cohom],
$H^0(X_K,\mathcal{L}_K)=H^0(X,\mathcal{L})\otimes_kK$, so each $t_j$ is a finite
combination $t_j=\sum_ac_{ja}u_a$ with $c_{ja}\in K$ and
$u_a\in H^0(X,\mathcal{L})$. Let $V\subseteq H^0(X,\mathcal{L})$ be the
finite-dimensional $k$-span of the $u_a$. The sections in $V$ have no common
zero on $X$, since the $t_j\in V\otimes_kK$ have none on $X_K$; they define a
morphism $\psi:X\to\mathbf P(V)$ with $\psi^*\mathcal{O}_{\mathbf P(V)}(1)=\mathcal{L}$,
whose base change $\psi_K:X_K\to\mathbf P(V_K)$ is defined by the sections of
$V_K=V\otimes_kK$. The linear projection from $\mathbf P(V_K)$ to
$\mathbf P^N_K$ given by the $t_j$ is defined on an open subscheme containing
the image of $\psi_K$, and its composite with $\psi_K$ is $i$. Since $i$ is
an immersion and the projection is separated, $\psi_K$ is an immersion. As
$X$ is proper over $k$, $X_K$ is proper over $K$, so $\psi_K$ is proper, hence
a closed immersion. Closed immersions descend along
$\operatorname{Spec}K\to\operatorname{Spec}k$ ([Stacks, Tag 02L6]), so $\psi$
is a closed immersion and $\mathcal{L}=\psi^*\mathcal{O}_{\mathbf P(V)}(1)$ is very
ample. Finally a very ample module is ample ([def-sc-ample],
[lem-pc-very-ample-ample]).
