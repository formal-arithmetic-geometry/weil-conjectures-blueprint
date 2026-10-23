+++
kind  = "proof"
of    = "lem-sc-canonical-degree"
+++
The module $\omega_C$ is invertible ([lem-sc-canonical-sheaf]). Serre
duality ([thm-sc-serre-duality-curve]) for the finite locally free module
$\mathcal O_C$, whose dual is $\mathcal O_C$, gives
$H^1(C,\mathcal O_C)^\vee\cong H^0(C,\omega_C)$ and
$H^0(C,\mathcal O_C)^\vee\cong H^1(C,\omega_C)$; hence
$\dim_kH^0(C,\omega_C)=g$ and $\dim_kH^1(C,\omega_C)=\dim_kH^0(C,\mathcal O_C)=1$.
Coherent cohomology on the one-dimensional Noetherian scheme $C$
vanishes in degrees $\ge2$ (Grothendieck vanishing), so
$\chi(\omega_C)=g-1$ and $\chi(\mathcal O_C)=1-g$, and by
[def-sc-pic0]

$$
\deg\omega_C=\chi(\omega_C)-\chi(\mathcal O_C)=(g-1)-(1-g)=2g-2 .
$$
