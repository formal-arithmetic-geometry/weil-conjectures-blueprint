+++
kind = "proof"
of = "det-sp-tower-evaluation-adjoint"
+++
*Well-defined.* The transitions are linear over the reduction maps: for
$r\geq n$ the identity $J\to J$ is linear over
$\mathcal O/\ell^{r+1}\to\mathcal O/\ell^r$ since both act through
$\mathcal O/\ell^n$; the maps into level $n-1$ and below are zero.

*Adjunction.* Let $\phi:C_\bullet\to r_nJ$ be a map of towers. Its components
for $r<n$ are zero. For $r\geq n$, compatibility with transitions gives
$\phi_r=\phi_n\circ(C_r\to C_n)$, the transition from level $r$ down to
level $n$ (the transitions of $r_nJ$ being identities). Conversely, for any
$\mathcal O_{E,T}/\ell^n$-linear $\psi:C_n\to J$, the family $\phi_r=0$ ($r<n$),
$\phi_r=\psi\circ(C_r\to C_n)$ ($r\geq n$) commutes with the transitions: for
$r\geq n$ by construction, and at $r=n-1$ because the target transition
$(r_nJ)_n\to(r_nJ)_{n-1}=0$ is zero. So
$\operatorname{Hom}(C_\bullet,r_nJ)=\operatorname{Hom}(C_n,J)$, naturally.

*Exactness.* Kernels and cokernels of towers are computed levelwise, and at
each level $r_n$ is either the identity (restriction of scalars, exact) or zero.

*Consequences.* A right adjoint of an exact functor preserves injectives. For
the embedding, the adjoint of $C_n\hookrightarrow J_n$ is a map
$C_\bullet\to r_nJ_n$, and the product of these maps is, at level $r$, the map
$C_r\to\prod_{n\leq r}J_n$ whose component $n=r$ is the monomorphism
$C_r\hookrightarrow J_r$; so it is a monomorphism at each level, hence a
monomorphism of towers (products of towers being levelwise, and only finitely
many factors being nonzero at each level).
