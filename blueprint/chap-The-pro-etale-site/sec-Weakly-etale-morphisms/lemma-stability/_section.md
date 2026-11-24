+++
id = "lemma-stability"
kind = "lemma"
title = "Stability"
order = 32
lean = ["AlgebraicGeometry.WeaklyEtale.instIsStableUnderBaseChangeScheme", "AlgebraicGeometry.WeaklyEtale.instIsMultiplicativeScheme", "RingHom.WeaklyEtale.comp", "AlgebraicGeometry.WeaklyEtale.instIsZariskiLocalAtSource", "AlgebraicGeometry.WeaklyEtale.instIsZariskiLocalAtTarget", "AlgebraicGeometry.WeaklyEtale.of_comp", "AlgebraicGeometry.WeaklyEtale.of_comp_eq", "RingHom.IndEtale.isStableUnderBaseChange", "RingHom.IndEtale.comp", "Algebra.weaklyEtale_iff", "AlgebraicGeometry.WeaklyEtale.hasRingHomProperty", "AlgebraicGeometry.weaklyEtale_SpecMap_algebraMap_iff"]
uses = ["definition-ind-etale-pro-etale-weakly"]
+++
[Weakly étale](@definition-ind-etale-pro-etale-weakly) morphisms are stable under base change and composition,
and the property is local on source and target for the Zariski topology.
Every $X$-morphism between two [weakly étale](@definition-ind-etale-pro-etale-weakly) $X$-schemes is [weakly
étale](@definition-ind-etale-pro-etale-weakly). [Ind-étale](@definition-ind-etale-pro-etale-weakly) ring maps are stable under base change and
composition. On affine charts, a morphism
$\operatorname{Spec}(B)\to\operatorname{Spec}(R)$ is [weakly étale](@definition-ind-etale-pro-etale-weakly) if and
only if both

$$
R\longrightarrow B,
\qquad B\otimes_RB\longrightarrow B
$$

are flat.
