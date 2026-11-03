+++
kind  = "proof"
of    = "lem-pur-projection-purity-agreement"
+++
Both maps are canonical and, by [thm-pur-composition-coherence]
and [prop-pur-affine-space-purity-compatibilities], they are
compatible with the tower of affine projections. It therefore suffices
to compare them after restriction to a geometric fiber of $Y$, where
both are determined by the integration that normalizes them: the
dualizing-object identification of [def-pur-smooth-purity-map] for
$p_d$ comes from the deformation of the diagonal $\Delta$ and the
standard-pair computation of [lem-pur-dnc-section-geometry](4) – the
diagonal of the standard pair $(\mathbf A^{2d}_Y,\Delta)$ has normal
bundle the trivial rank-$d$ bundle $T_{p_d}$, and the DNC invariance of
[thm-pur-dnc-invariance] is the identity on the standard pair – where
$0^*\omega_{\mathbf A^d/Y}\cong\Lambda(d)[2d]$ is the vector-bundle
purity of [cor-pur-vector-bundle-purity], the adjoint of the
integration $t_\pi$ of [def-amb-vector-integration]; on the trivial
bundle $t_\pi$ is the ordered affine-space integration, the iterate of
the projective-line trace normalized by $t_q(c_1(\mathcal O(1)))=1$.
The affinity-space purity of [cor-pur-affine-space-purity] is the
ordered composite of the affinity-line comparisons, each the adjoint of
the same projective-line-normalized trace. So both are normalized by the
same integration, the one sending the product of the Cartier classes of
the coordinate hyperplanes to $1$ (and the product of the Kummer
boundaries of the coordinates to $(-1)^d$). The two
assemblies differ only by the canonical reassociations of the package
(the Koszul signs are $+1$, since all shift factors are of even
degree, by [prop-pur-affine-space-purity-compatibilities]); hence
the maps agree.
