+++
kind = "proof"
of = "sk-lem-sp-tower-levels"
+++
Evaluation at $n$ has an exact right adjoint $r_n$: for an
$\mathcal O_{E,T}/\ell^n$-module sheaf $J$,

$$
(r_nJ)_r=\begin{cases}
J,&r\geq n,\ \text{with scalars restricted along }
\mathcal O_{E,T}/\ell^r\to\mathcal O_{E,T}/\ell^n,\\
0,&r<n,
\end{cases}
$$

with identity transition maps from level $n$ on and zero maps below it. It is
right adjoint to evaluation because a map of towers $C_\bullet\to r_nJ$ is
determined by its component $C_n\to J$.

Embed each $C_n$ into an injective $\mathcal O_{E,T}/\ell^n$-module sheaf
$J_n$. By adjunction this gives a monomorphism
$C_\bullet\hookrightarrow\prod_{n\geq1}r_nJ_n$; at level $r$ only the factors
with $n\leq r$ are nonzero, and one of them is the embedding into $J_r$. If
$C_\bullet$ is injective the monomorphism splits, so $C_r$ is a direct summand of
a finite product of the sheaves $J_n$ with $n\leq r$.

An injective module sheaf over any of these rings is acyclic for sections over
every object of $T_{\mathrm{proét}}$. This is a property of the underlying abelian
sheaf, so restriction of scalars does not affect it, and finite products and
direct summands preserve it. Hence every component of an injective tower is
$g_*$-acyclic. Since evaluation is exact, evaluating a bounded below injective
resolution of $C_\bullet$ computes $Rg_{*,\mathcal O_E/\ell^n}C_n$.
