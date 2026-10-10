+++
kind  = "proof"
of    = "sk-p-tensor"
+++
*Reduction to a pair of simple constituents.* Choose composition series
of $V$ and of $E$ ([sk-r-linear-library]); the products of their terms
filter $V\otimes E$ with subquotients the tensor products
$V_i\otimes E_j$ of their factors, so by the tensor-filtration statement
of [sk-r-linear-library] and Jordan–Hölder, the simple subquotient $Q$ is
a subquotient of some $V_i\otimes E_j$, where $V_i$ is a simple
subquotient of $V$ and $E_j$ one of $E$. By hypothesis $V_i$ and $E_j$
have finite geometric determinant. It remains to show
$\dw_\lambda(Q)=\dw_\lambda(V_i)+\dw_\lambda(E_j)$ for a simple
subquotient $Q$ of $V_i\otimes E_j$ with finite geometric determinant.

*Reduction to a degree datum.* If $\deg$ is trivial, then all three
weights vanish: the determinants take finitely many values on $W=P$, so
$\delta(\gamma)$ has finite order and $\lambda$ kills it ([sk-d-weights]).
Otherwise $\deg(W)=a\mathbf Z$ with $a>0$, and $\deg_0=\deg/a$ is
surjective with the same kernel $P$. Writing $\gamma=u\gamma_0^m$ with
$\deg_0(\gamma_0)=1$, $u\in P$ and $m=\deg_0(\gamma)$, each weight at
$\gamma$ is $m$ times the weight at $\gamma_0$, since $\lambda$ kills the
finite-order factor $\delta(u)$. So the formula at $\gamma_0$ implies it
at $\gamma$, and we may assume that $(W,\deg,\gamma)$ is a degree datum
([sk-d-monodromy]).

*The degree-datum case.* Apply [sk-p-central] to the semisimple
representation $V_i\oplus E_j$ and its own monodromy groups $G\supseteq H$,
obtaining a positive central pair $(N,z)$. The summands $V_i,E_j$ are
simple subquotients of this defining representation with finite
geometric determinant, so by [sk-p-readout] $z$ acts on them by scalars
$c_i,d_j$ with $\lambda(c_i)=N\dw_\lambda(V_i)$ and
$\lambda(d_j)=N\dw_\lambda(E_j)$. The map
$(a,b)\mapsto a\otimes b$ from block-diagonal matrices to
$\GL(V_i\otimes E_j)$ is a regular homomorphism ([sk-d-linear]); by
continuity it maps $G\supseteq H$ into the Zariski closures
$G'\supseteq H'$ of the images of $W\supseteq P$ in
$\GL(V_i\otimes E_j)$ (compare [sk-i-restriction]). Hence
$z'=z|_{V_i}\otimes z|_{E_j}=c_id_j$ lies in $H'F'^N$ for the Frobenius
$F'$ of $V_i\otimes E_j$, and it is central in $G'$, being a scalar. So
$(N,z')$ is a positive central pair for $V_i\otimes E_j$, acting on its
subquotient $Q$ by $c_id_j$. Applying [sk-p-readout] to $Q$ and the
multiplicative-to-additive rule of [sk-d-weights] gives
$$
\dw_\lambda(Q)=\frac{\lambda(c_id_j)}{N}=\dw_\lambda(V_i)+\dw_\lambda(E_j).
$$
Neither $V$, $E$ nor the tensor product is assumed semisimple.
