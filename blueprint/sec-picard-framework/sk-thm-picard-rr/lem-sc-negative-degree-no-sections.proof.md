+++
kind  = "proof"
of    = "lem-sc-negative-degree-no-sections"
+++
The scheme $C$ is connected, since the field $H^0(C,\mathcal O_C)=k$ has
no nontrivial idempotents, and its local rings are regular
([lem-sc-smooth-regular]), hence domains; so $C$ is integral. Suppose
$s\in H^0(C,\mathcal M)$ is nonzero. Locally $s=f\,e$ for a generator $e$
of $\mathcal M$ and a function $f$, which is nonzero on every nonempty open
($C$ is integral), hence a non-zero-divisor. So the zero scheme $D$ of $s$,
locally $V(f)$, is an effective Cartier divisor
([def-nagata-invertible-ideal]), and $s$ identifies
$\mathcal O_C(D)=\mathcal I_D^\vee$ ([def-pc-divisor-line-bundle]), locally
$f^{-1}\mathcal O_C$, with $\mathcal M$ via $f^{-1}u\mapsto u\,e$. By
[lem-pc-degree-base-change](2),
$\deg\mathcal M=\deg\mathcal O_C(D)=\dim_kH^0(D,\mathcal O_D)\ge0$, a
contradiction.
