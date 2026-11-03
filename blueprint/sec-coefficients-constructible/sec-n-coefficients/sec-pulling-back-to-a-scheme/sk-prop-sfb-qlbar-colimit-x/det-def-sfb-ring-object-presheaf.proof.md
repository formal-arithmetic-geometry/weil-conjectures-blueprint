+++
kind = "proof"
of = "det-def-sfb-ring-object-presheaf"
+++
1. Define $\mu\colon P\otimes_pP\to P$ and $\eta\colon\underline{\mathbf Z}\to P$ objectwise by
   $\mu_{P(U)}$ and $\eta_{P(U)}$ of [det-def-sfb-ring-object-rings]. They are natural in $U$
   because the restriction maps of $P$ are ring homomorphisms, hence morphisms of ring objects of
   $\Ab$. The ring object axioms, the morphism conditions for a morphism of presheaves of rings, and
   commutativity are equalities of morphisms of presheaves, which may be checked at each $U$, where
   they are [det-def-sfb-ring-object-rings], because all structure maps of $\otimes_p$ are
   objectwise.
2. Sheafification is strong symmetric monoidal from $(\mathrm{PSh}(C,\Ab),\otimes_p)$ to
   $(\Sh(C,\Ab),\otimes)$ by [det-def-sfb-sheaf-tensor-structure], with unit
   $a(\underline{\mathbf Z})=\underline{\mathbf Z}$. So [det-def-sfb-ring-object-transport]
   (parts 1 and 2), applied to $F=a$ and the ring object $P$ of part 1, gives the ring object $aP$ with
   the stated multiplication and unit, its commutativity, and the functoriality.
