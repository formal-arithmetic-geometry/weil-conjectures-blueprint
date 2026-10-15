+++
kind = "proof"
of = "det-def-sfb-sheaf-tensor-local-iso"
+++
The equivalence of the two descriptions of $W$: $\Hom(g,H)\cong\Hom(a(g),H)$ for sheaves $H$, so
by Yoneda in $\Sh(C,\mathcal A)$, $a(g)$ is invertible if and only if $\Hom(g,H)$ is bijective for
all sheaves $H$.

1. Let $H$ be a sheaf. By the adjunction of [det-def-sfb-sheaf-tensor-presheaf],
   $\Hom(F\otimes_pg,H)\cong\Hom(g,[F,H])$ naturally. The presheaf $[F,H]$ is a sheaf by
   [det-def-sfb-sheaf-tensor-hom-sheaf], so this map is bijective, and $F\otimes_pg\in W$. The
   objectwise symmetry identifies $g\otimes_pF$ with $F\otimes_pg$, giving the second claim.
2. Write $g\otimes_ph=(F'\otimes_ph)\circ(g\otimes_pG)$. Both factors lie in $W$ by 1, and $W$
   is closed under composition.
3. The map is $\eta_F\otimes_p\eta_G$, with $\eta$ the unit of $a$, and $a(\eta_F)$, $a(\eta_G)$
   are isomorphisms; so 2 applies.
