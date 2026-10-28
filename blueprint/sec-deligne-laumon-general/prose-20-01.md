+++
id = "prose-20-01"
kind = "hidden"
title = "Strategy for weights of direct images"
order = 4275
+++
In this section we prove Theorem [sk-cor-dl-general-complex]: for
every separated morphism of finite type $f$, the functor $Rf_!$
carries $D_{\leq w}(X_0)$ into $D_{\leq w}(Y_0)$. By the strategy of
Section “The weight bound and why it holds”, we must pass from the bound on a single curve
(Theorem [sk-cor-wft-curve-upper]) to families of curves. Applied fibre
by fibre, that bound controls each local eigenvalue of a direct image
sheaf. A weight bound in the sense of Definition [sk-d-real-weights]
also requires a finite filtration with pure quotients, however, and
the fibrewise bound does not produce one. The filtration comes from
Theorem [sk-i-dl-general-real], which says that real sheaves are
mixed. Along a relative affine curve only $H^1_c$ and $H^2_c$ occur in
the fibres, and their eigenvalues have different absolute values, so
the trace formula shows that the direct images of the real sheaf of
Proposition [sk-prop-wrp-real-envelope] attached to a pure sheaf are real,
hence mixed. By Noether normalization and
localization we then reduce an arbitrary morphism to relative affine
curves. In Section “Cohomology of smooth proper schemes and the Weil conjectures” the theorem gives the upper
bound in the purity of the cohomology of a smooth proper variety.

The proof of Theorem [sk-i-dl-general-real] restricts a sheaf to curves
and then reassembles it over strata and descends it along constant
extensions. For the reassembly and the descent we need that
quasi-finite direct images preserve weights; for the restriction we
need curves on which given lisse sheaves stay geometrically
irreducible.
