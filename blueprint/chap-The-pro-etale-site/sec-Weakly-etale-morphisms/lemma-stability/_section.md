+++
id = "lemma-stability"
kind = "lemma"
title = "Stability"
order = 32
lean = ["AlgebraicGeometry.WeaklyEtale.instIsStableUnderBaseChangeScheme", "AlgebraicGeometry.WeaklyEtale.instIsMultiplicativeScheme", "AlgebraicGeometry.WeaklyEtale.instIsZariskiLocalAtSource", "AlgebraicGeometry.WeaklyEtale.instIsZariskiLocalAtTarget", "AlgebraicGeometry.WeaklyEtale.of_comp", "RingHom.IndEtale.isStableUnderBaseChange", "RingHom.IndEtale.comp", "AlgebraicGeometry.WeaklyEtale.hasRingHomProperty"]
uses = ["definition-ind-etale-pro-etale-weakly"]
+++
Weakly étale morphisms are stable under base change and composition,
and the property is local on source and target for the Zariski topology.
Every $X$-morphism between two weakly étale $X$-schemes is weakly
étale. Ind-étale ring maps are stable under base change and
composition. On affine charts, a morphism
$\operatorname{Spec}(B)\to\operatorname{Spec}(R)$ is weakly étale if and
only if both

$$
R\longrightarrow B,
\qquad B\otimes_RB\longrightarrow B
$$

are flat.
