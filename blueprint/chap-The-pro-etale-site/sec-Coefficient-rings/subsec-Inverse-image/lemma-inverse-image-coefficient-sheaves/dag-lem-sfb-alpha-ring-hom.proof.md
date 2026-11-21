+++
kind = "proof"
of = "dag-lem-sfb-alpha-ring-hom"
tags = ["sheaf-dag"]
uses = ["dag-def-sfb-pullback-from-point-comp-iso", "dag-sk-def-sfb-pullback-from-point-comp", "dag-lem-sfb-pullback-from-point-comp-monoidal"]
+++
1. By `def-sfb-alpha`, the map $\alpha_f$ is the component at $\Lambda$ of the canonical comparison $f^*\circ p_Y^*\cong p_X^*$. The comparison is the natural isomorphism of [dag-def-sfb-pullback-from-point-comp-iso], and [dag-sk-def-sfb-pullback-from-point-comp] identifies it with the monoidal comparison used in the Lean construction. Thus, writing $F=p_Y^*$, $G=f^*$, and $H=p_X^*$, the Lean term defining $\alpha_f$ is definitionally `Functor.compAlgHom F G (upperStarFromPointComp f).hom \Lambda`, i.e. the component `(upperStarFromPointComp f).hom.app \Lambda`; its source has the ring structure transported first along $F$ and then along $G$, while its target has the structure transported along $H$. (uses [dag-def-sfb-pullback-from-point-comp-iso], [dag-sk-def-sfb-pullback-from-point-comp])
2. The monoidality instance supplied by [dag-lem-sfb-pullback-from-point-comp-monoidal] is exactly the premise `NatTrans.IsMonoidal (upperStarFromPointComp f).hom`. Apply the Lean theorem `Functor.isMonHom_compAlgHom` (whose construction uses `Functor.monObjObj_comp` and `IsMonHom.of_eq`) to this monoidal natural transformation and the ring object $\Lambda$. By the transported-ring-object result `det-def-sfb-ring-object-transport`, the resulting component preserves both multiplication and the unit. Since that component is the map identified in the preceding step, it is precisely $\alpha_f:f^*\Lambda_Y\to\Lambda_X$, hence a morphism of ring objects. (uses [dag-lem-sfb-pullback-from-point-comp-monoidal], `det-def-sfb-ring-object-transport`)

Proof dependencies not drawn: `det-def-sfb-ring-object-transport`.
