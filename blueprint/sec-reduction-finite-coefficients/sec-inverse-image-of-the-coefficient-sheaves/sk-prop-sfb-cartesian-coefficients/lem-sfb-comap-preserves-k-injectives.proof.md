+++
kind  = "proof"
of    = "lem-sfb-comap-preserves-k-injectives"
+++
Let $I$ be a K-injective complex of $\Lambda'_X$-modules and $C$ an acyclic complex of
$\Lambda_X$-modules. By the adjunction $\operatorname{Ext}_{a_X}\dashv\operatorname{Res}_{a_X}$
([det-def-sfb-change-of-scalars]), applied termwise and passed to the homotopy category,
$\Hom_K(C,\operatorname{Res}_{a_X}I)\cong\Hom_K(\operatorname{Ext}_{a_X}C,I)$. The functor
$\operatorname{Ext}_{a_X}$ is exact (right exact as a left adjoint, left exact by assumption),
so $\operatorname{Ext}_{a_X}C$ is acyclic and the right side vanishes since $I$ is K-injective.
