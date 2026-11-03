+++
kind  = "proof"
of    = "det-thm-sfb-proper-base-change-integral"
+++
(1) $K$ is derived complete if and only if
$\operatorname{R\lim}(\cdots\xrightarrow{\pi_E}K\xrightarrow{\pi_E}K)=0$. The functor $Rp_*$ is
a right adjoint, so it commutes with $\operatorname{R\lim}$, and it is $\cO_E$-linear, so it
carries this tower to the tower of multiplication by $\pi_E$ on $Rp_*K$; hence $Rp_*K$ is
derived complete. Reduction: $K\otimes^{\mathbf L}\cO_{E,X}/\pi_E=\operatorname{cone}(K\xrightarrow{\pi_E}K)$
since $\cO_{E,X}$ is $\pi_E$-torsion free, and the exact functor $Rp_*$ preserves cones and is
$\cO_E$-linear. The reduction $\bar K$ has torsion coefficients and is classical
([Stacks, Tag 09B1](https://stacks.math.columbia.edu/tag/09B1)), so $Rp_*\bar K$ is $\nu^*$ of the étale direct image ([Stacks, Tag 09A6](https://stacks.math.columbia.edu/tag/09A6)), which is
bounded constructible by [det-thm-sfb-proper-base-change-finite] (1) with $A=\cO_E/\pi_E$. By
[sk-prop-integral-criterion] (equivalently [sk-lem-integral-models] (2)),
$Rp_*K\in\Dbc(Y,\cO_E)$.

(2) This is [sk-lem-pe-derived-nakayama]. Directly: the exact sequences
$0\to\cO/\pi_E^{n-1}\to\cO/\pi_E^n\to\cO/\pi_E\to0$ give triangles showing by induction that
$C\otimes^{\mathbf L}\cO/\pi_E^n=0$ for all $n$; then $C\simeq\operatorname{R\lim}_nC\otimes^{\mathbf L}\cO/\pi_E^n=0$.

(3) The base change map $g^*Rp_*K\to Rp'_*g'^*K$ has derived complete source and target: $Rp_*K$
and $Rp'_*g'^*K$ are in $\Dbc$ by (1) and [sk-lem-integral-models] (3), and $g^*$ preserves
$\Dbc(-,\cO_E)$ by [sk-lem-integral-models] (3). Similarly for the projection formula map, using
that $\otimes^{\mathbf L}$ and $p^*$ preserve $\Dbc(-,\cO_E)$. All functors involved are exact
and $\cO_E$-linear, so they commute with reduction modulo $\pi_E$ (the cone of $\pi_E$), and
the reduction of each canonical map is the corresponding canonical map for the torsion
reductions, which is an isomorphism by [det-thm-sfb-proper-base-change-finite] (2), (3) with
$A=\cO_E/\pi_E$. So the cone of each map is derived complete (cones of maps between complete
objects are complete) with zero reduction, hence zero by (2).
