+++
kind  = "proof"
of    = "lem-sfb-finite-upper-star-exact"
+++
$g^*$ is the composite of three functors: the inclusion of sheaves into presheaves, which
preserves limits; $\operatorname{Lan}_{b^{\mathrm{op}}}$; and sheafification, which is
left exact for a Grothendieck abelian $\mathcal A$. It remains to see that
$\operatorname{Lan}_{b^{\mathrm{op}}}$ is left exact. Its value at
$W\in Z_{\mathrm{proét}}$ is a colimit over the opposite of the category of pairs
$(V,\;W\to V\times_YZ)$. This category is cofiltered: it is nonempty ($V=Y$), and base
change preserves the finite limits of $Y_{\mathrm{proét}}$. So the colimit is filtered, and
filtered colimits are exact in the Grothendieck abelian category $\mathcal A$.

For $g$ weakly étale there is a shorter argument. Base change is then right adjoint to the
localization functor $(W\to Z)\mapsto(W\to Z\to Y)$, so $\operatorname{Lan}_{b^{\mathrm{op}}}$
is precomposition with the opposite of the localization functor, which preserves all
limits.

Right exactness holds because $g^*$ is a left adjoint
([def-sfb-finite-upper-lower-star-adjunction]).
