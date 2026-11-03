+++
id = "det-cor-picard-pic-sheaf"
kind = "corollary"
title = "Picard functor is an fppf sheaf"
order = 598
uses = ["def-pc-picard-functor", "det-thm-picard-descent"]
lean = ["AlgebraicGeometry.picardFunctor", "AlgebraicGeometry.isSheaf_picardFunctorNormalized"]
+++
Let $f\colon X\to S$ be a morphism of schemes.
$\Pic_{X/S}$ is an fppf (hence Zariski) sheaf, being by
[def-pc-picard-functor] an fppf sheafification. If in addition $f$ has a
section $\sigma$ and $\cO_T\to f_{T,*}\cO_{X_T}$ is an isomorphism for
all $T\in\Ob((\Sch/S)_{fppf})$, then
$\Pic_{X/S,\sigma}(T)=\ker\sigma_T^*$ is an fppf (hence Zariski) sheaf
as well.

These hypotheses are satisfied for a smooth projective curve over a field
with a rational point. The presheaf $T\mapsto\Pic(X_T)$ itself is in
general *not* an fppf sheaf: [det-thm-picard-descent] (D1) makes descent
data effective, but unnormalized glueing isomorphisms between the local
modules need not satisfy the cocycle condition. Repairing that is exactly
what the sheafification in [def-pc-picard-functor] and the
$\sigma$-normalization do.
