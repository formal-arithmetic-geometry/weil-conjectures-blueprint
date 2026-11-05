+++
kind = "proof"
of = "proposition-comparison-morphism-inverse-image--2"
order = 112005
uses = ["proposition-comparison-morphism-inverse-image--1"]
+++
Left Kan extension is left adjoint to restriction on presheaves, and
sheafification is left adjoint to the inclusion of sheaves. Combining
these adjunctions gives $\nu_X^*\dashv\nu_{X,*}$.

The inclusion $i_X$ is representably flat, as in the proof of
[proposition-comparison-morphism-inverse-image--1]. Its opposite therefore
has filtered comma categories for the pointwise left Kan extension.
Filtered colimits in $A$ are exact, so this left Kan extension preserves
finite limits. The inclusion of sheaves into presheaves and
sheafification also preserve finite limits. Their composite $\nu_X^*$
is thus left exact. As a left adjoint it preserves colimits, in particular
finite colimits, which proves exactness.
