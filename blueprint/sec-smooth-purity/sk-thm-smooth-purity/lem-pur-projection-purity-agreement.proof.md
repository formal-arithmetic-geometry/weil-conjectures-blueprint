+++
kind  = "proof"
of    = "lem-pur-projection-purity-agreement"
+++
Both maps are canonical and, by [thm-pur-composition-coherence]
and [prop-pur-affine-space-purity-compatibilities], they are
compatible with the tower of affine projections. It therefore suffices
to compare them after restriction to a geometric fiber of $Y$, where
both are determined by the Kummer computation: the dualizing-object
identification of [def-pur-smooth-purity-map] for $p_d$ comes
from the deformation of the diagonal $\Delta$ and the standard-pair
computation of [lem-pur-dnc-section-geometry](4) – the diagonal
of the standard pair $(\mathbf A^{2d}_Y,\Delta)$ has normal bundle the
trivial rank-$d$ bundle $T_{p_d}$, and the DNC invariance of
[thm-pur-dnc-invariance] is the identity on the standard pair –
whose class, by
[lem-pur-dnc-section-geometry] and the definition of the
[def-pur-frame-class] (class of a frame), is the $d$-fold
exterior product of the rank-one Kummer boundaries, i.e. the
$d$-fold product of the affinity-line orientations; the affinity-space
purity of [cor-pur-affine-space-purity] is built from exactly the
same $d$-fold product of the affinity-line orientations. The two
assemblies differ only by the canonical reassociations of the package
(the Koszul signs are $+1$, since all shift factors are of even
degree, by [prop-pur-affine-space-purity-compatibilities]); hence
the maps agree.
