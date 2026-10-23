+++
kind  = "proof"
of    = "p-real-operations"
+++
Changing the decomposition-group map conjugates $F_x$ by some
$g\in\pi_1(C_0)$, and this is a conjugation inside $W(C_0)$: as
$\widehat{\mathbf Z}=\mathbf Z+e_x\widehat{\mathbf Z}$, one can write
$g=wF_x^t$ with $w\in W(C_0)$ and $t\in\widehat{\mathbf Z}$, where $F_x^t$ is
the image of the $t$-th power of the geometric Frobenius in the procyclic
group $\pi_1(x)$, which commutes with $F_x$; so $gF_xg^{-1}=wF_xw^{-1}$.
Hence $F_x$ is well defined up to conjugacy in $W(C_0)$.

Granted [prop-wf-weil-sheaf-representation-equivalence], the operations of
[def-real-weil-representation-operations] on
lisse Weil sheaves are *defined* by transport along the equivalence, so
only the local polynomial needs an argument. Iterating the Frobenius
structure map $e_x$ times on the stalk at $\bar x$, as in
[def-weil-local-frobenius-trace], realizes $F_x$ as $\rho$ of
any member of the degree-$e_x$ class supplied by $x$. A characteristic
polynomial is invariant under conjugation, so $\det(1-T\rho(F_x)\mid V)$ is
independent of the member chosen and agrees with the stalkwise $P_x$ of [sk-d-real-weights].
