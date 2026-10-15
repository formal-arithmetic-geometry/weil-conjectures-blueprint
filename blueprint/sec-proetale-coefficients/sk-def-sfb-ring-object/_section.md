+++
id = "sk-def-sfb-ring-object"
kind = "definition"
title = "Ring objects of abelian sheaves"
order = 850
uses = ["sk-def-sfb-sheaf-tensor"]
lean = ["CategoryTheory.MonObj", "AddCommGrpCat.ringMonObj", "CategoryTheory.Functor.monObjCompForget₂", "CategoryTheory.Sheaf.sheafifyRingPresheaf", "CategoryTheory.Sheaf.monObj_sheafCompose_obj", "CategoryTheory.Sheaf.isMonHom_sheafCompose_map"]
tags = ["sketch"]
+++
A *ring object* of a monoidal category $(\mathcal C,\otimes,\mathbf 1)$ is a monoid
object. It consists of an object $R$, a *multiplication* $\mu\colon R\otimes R\to R$ and
a *unit* $\eta\colon\mathbf 1\to R$, such that $\mu$ is associative,
$\mu\circ(\mu\otimes\mathrm{id})=\mu\circ(\mathrm{id}\otimes\mu)\circ\alpha_{R,R,R}$, and
$\eta$ is a two-sided unit, $\mu\circ(\eta\otimes\mathrm{id})=\lambda_R$ and
$\mu\circ(\mathrm{id}\otimes\eta)=\rho_R$. A *morphism of ring objects* is a morphism
compatible with the multiplications and the units. If $\mathcal C$ is braided, the ring
object $R$ is *commutative* when $\mu\circ\beta_{R,R}=\mu$.

Throughout, $\Ab$ carries the tensor product $\otimes_{\mathbf Z}$ with unit $\mathbf Z$.
Abelian presheaves carry the objectwise tensor product. Abelian sheaves on a site $C$
carry its sheafification, the tensor product of [sk-def-sfb-sheaf-tensor] (with $C$ as
there, e.g. $X_{\mathrm{proét}}$ or the site of profinite sets).

1. Every ring $R$ is a ring object of $\Ab$, with unit $\mathbf Z\to R$, $n\mapsto n\cdot1$,
   and multiplication $R\otimes_{\mathbf Z}R\to R$, $a\otimes b\mapsto ab$. A ring
   homomorphism is a morphism of ring objects. If $R$ is commutative, so is the ring
   object $R$.
2. A presheaf of rings $P$ on $C$ is, objectwise as in 1, a ring object of abelian
   presheaves, and a morphism of presheaves of rings is a morphism of ring objects. The
   sheafification $aP$ of the underlying abelian presheaf is a ring object of
   $\Sh(C,\Ab)$, commutative when all the rings $P(U)$ are.
3. The abelian sheaf underlying a sheaf of rings $\mathcal R$ on $C$ is a ring object of
   $\Sh(C,\Ab)$, commutative when all the rings $\mathcal R(U)$ are. A morphism of sheaves
   of rings is a morphism of ring objects.
