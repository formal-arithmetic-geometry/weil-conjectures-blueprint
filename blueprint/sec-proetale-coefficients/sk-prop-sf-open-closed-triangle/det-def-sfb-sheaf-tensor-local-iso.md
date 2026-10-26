+++
id = "det-def-sfb-sheaf-tensor-local-iso"
kind = "lemma"
title = "Objectwise tensoring preserves sheafification-isomorphisms"
lean = ["CategoryTheory.GrothendieckTopology.W", "CategoryTheory.GrothendieckTopology.W_iff", "CategoryTheory.GrothendieckTopology.W.whiskerLeft", "CategoryTheory.GrothendieckTopology.W.whiskerRight", "CategoryTheory.GrothendieckTopology.W.monoidal"]
order = 1135
uses = ["det-def-sfb-sheaf-tensor-hom-sheaf", "det-def-sfb-sheaf-tensor-presheaf"]
+++
In the situation of [det-def-sfb-sheaf-tensor-presheaf], let $a$ be sheafification of
$\mathcal A$-valued presheaves on $C$, left adjoint to the inclusion $\Sh(C,\mathcal A)\subseteq\mathrm{PSh}(C,\mathcal A)$,
and let $W$ be the class of morphisms $g$ of presheaves with $a(g)$ invertible. Equivalently, $g\in W$ if and only if
$\Hom(g,H)$ is bijective for every sheaf $H$.

1. If $g\in W$ and $F$ is a presheaf, then $F\otimes_pg\in W$ and $g\otimes_pF\in W$.
2. If $g\colon F\to F'$ and $h\colon G\to G'$ lie in $W$, then $g\otimes_ph\in W$.
3. For presheaves $F,G$, the morphism $F\otimes_pG\to aF\otimes_paG$ built from the units of
   $a$ lies in $W$; hence $a(F\otimes_pG)\to a(aF\otimes_paG)$ is an isomorphism.
