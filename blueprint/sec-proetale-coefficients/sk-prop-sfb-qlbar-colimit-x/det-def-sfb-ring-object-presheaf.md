+++
id = "det-def-sfb-ring-object-presheaf"
kind = "lemma"
title = "Presheaves of rings and their sheafifications are ring objects"
lean = ["CategoryTheory.Functor.monObjCompForget₂", "CategoryTheory.Functor.isMonHom_whiskerRight_forget₂", "CategoryTheory.Functor.isCommMonObj_compForget₂", "CategoryTheory.Sheaf.monObj_presheafToSheaf_obj", "CategoryTheory.Sheaf.isCommMonObj_presheafToSheaf_obj", "CategoryTheory.Sheaf.sheafifyRingPresheaf", "CategoryTheory.Functor.map.instIsMonHom"]
order = 1224
uses = ["det-def-sfb-ring-object-rings", "det-def-sfb-ring-object-transport", "det-def-sfb-sheaf-tensor-structure"]
+++
Let $C$ be a site as in [det-def-sfb-sheaf-tensor-structure] (for instance $X_{\mathrm{proét}}$
or the site of profinite sets), with abelian presheaves carrying the objectwise tensor product
$\otimes_p$ and abelian sheaves the tensor product
$\mathcal F\otimes\mathcal G=a(\mathcal F\otimes_p\mathcal G)$ of
[det-def-sfb-sheaf-tensor-structure].

1. A presheaf of rings $P$ on $C$ is a ring object of abelian presheaves, with multiplication and
   unit given at each $U$ by those of the ring $P(U)$ ([det-def-sfb-ring-object-rings]).
   A morphism of presheaves of rings is a morphism of ring objects. If all $P(U)$ are commutative,
   the ring object $P$ is commutative.
2. The sheafification $aP$ of the underlying abelian presheaf of $P$ is a ring object of
   $\Sh(C,\Ab)$, with multiplication $aP\otimes aP\cong a(P\otimes_pP)\xrightarrow{a\mu}aP$ and unit
   $\underline{\mathbf Z}=a(\underline{\mathbf Z})\xrightarrow{a\eta}aP$; it is commutative when all
   $P(U)$ are, and $a$ sends morphisms of presheaves of rings to morphisms of ring objects.
