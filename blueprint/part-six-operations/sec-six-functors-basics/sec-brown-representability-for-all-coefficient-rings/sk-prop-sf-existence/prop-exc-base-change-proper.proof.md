+++
kind  = "proof"
of    = "prop-exc-base-change-proper"
+++
The open-restriction argument; it needs neither the datum for $f_Z$ nor the
ambient localization triangle. Since $g$ and $g'$ are open immersions,
compact-support composition for $fg'=gf'$ gives

$$
Rf_!\,g'_!\simeq g_!\,Rf'_!.
$$

The functors $g_!$ and $g'_!$ are left adjoint to $g^*$ and $g'^*$, and
$Rf_!$, $Rf'_!$ are left adjoint to $Rf^{\times}$, $Rf'^{\times}$ on the
established constructible or localizing categories ([sk-thm-existence] (3)),
or on the ambient categories when $f$ and $f'$ carry the datum of
[def-weil-ambient-exceptional-adjoint]. Taking right adjoints of the displayed
isomorphism yields

$$
g'^*\,Rf^{\times}\simeq Rf'^{\times}\,g^*.
$$

Its transpose under $Rf'_!\dashv Rf'^{\times}$ is the composite of the
compact-support exchange with the counit of $Rf_!\dashv Rf^{\times}$, which is
the transpose of the canonical comparison $\beta$; hence this isomorphism is
$\beta$.
