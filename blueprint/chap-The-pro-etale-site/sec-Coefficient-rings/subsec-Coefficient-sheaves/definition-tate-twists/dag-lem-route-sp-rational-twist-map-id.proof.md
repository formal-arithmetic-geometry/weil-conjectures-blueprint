+++
kind = "proof"
of = "dag-lem-route-sp-rational-twist-map-id"
tags = ["sheaf-dag"]
+++
1. For $h:E\subseteq E$ the condensed inclusion is postcomposition with the identity, hence is the identity by `def-sfb-qlbar-subextension-map`. Its image under $p_X^*$ is the identity by the functor identity axiom and `def-sfb-coefficient-map`; thus $i_h=\mathrm{id}_{E_X}$. In the characterization of [dag-lem-route-sp-integers-map-exists-unique], $\mathrm{id}_{O_{E,X}}$ preserves unit and multiplication and satisfies $c_E\mathrm{id}=\mathrm{id}\,c_E$. Uniqueness gives $a_h=\mathrm{id}_{O_{E,X}}$. (uses `def-sfb-qlbar-subextension-map`, `def-sfb-coefficient-map`, `lem-route-sp-integers-map-exists-unique`)
2. For every $n\geq0$, [dag-lem-route-sp-ell-map-exists-unique] characterizes $b_{h,n}$ by $b_{h,n}r_{E,n}=r_{E,n}a_h$. Since step 1 gives $a_h=\mathrm{id}$, the identity of $B_{E,n,X}$ satisfies this equation: both sides are $r_{E,n}$. Its uniqueness gives $b_{h,n}=\mathrm{id}_{B_{E,n,X}}$. (uses `lem-route-sp-ell-map-exists-unique`)
3. By [dag-lem-route-sp-integral-twist-map-exists-unique], $g_h$ is the unique abelian-sheaf map whose composites with $p_{E,n}$ are $(b_{h,n}\otimes\mathrm{id}_{\mu_n})p_{E,n}$. Step 2 makes each right side $p_{E,n}$, since tensoring two identity maps is the identity (the tensor bifunctor identity axiom). The identity of $L_E$ has exactly these composites. Uniqueness gives $g_h=\mathrm{id}_{L_E}$. (uses `lem-route-sp-integral-twist-map-exists-unique`)
4. By [dag-lem-route-sp-rational-twist-map-exists-unique], $j_h$ is the unique abelian-sheaf map with $j_hq_E=q_E(i_h\otimes g_h)$. Steps 1 and 3 make the right side $q_E(\mathrm{id}\otimes\mathrm{id})=q_E$. The identity of $T_E$ satisfies the same equation, since $\mathrm{id}\,q_E=q_E$. Uniqueness therefore gives $j_h=\mathrm{id}_{T_E}$, as required. (uses `lem-route-sp-rational-twist-map-exists-unique`)

Proof dependencies not drawn: `def-sfb-qlbar-subextension-map`, `def-sfb-coefficient-map`, `lem-route-sp-integers-map-exists-unique`, `lem-route-sp-ell-map-exists-unique`, `lem-route-sp-integral-twist-map-exists-unique`, `lem-route-sp-rational-twist-map-exists-unique`.
