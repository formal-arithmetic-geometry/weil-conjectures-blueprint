+++
id = "lem-weil-pbc-adjunct-counit-identity"
kind = "lemma"
title = "The adjunct of a morphism, composed with the counit, gives back the morphism"
refines = "proof/lem-weil-pbc-edge-map-base-change"
lean = ["CategoryTheory.Adjunction.eq_unit_comp_map_iff"]
tags = ["sheaf-dag", "mathlib", "stacks-0037"]
+++
Let $\mathcal C,\mathcal D$ be categories, $L:\mathcal C\to\mathcal D$ a functor left adjoint to $R:\mathcal D\to\mathcal C$ with unit $\eta:\mathrm{id}_{\mathcal C}\to RL$ and counit $\varepsilon:LR\to\mathrm{id}_{\mathcal D}$ (satisfying the triangle identities $\varepsilon_{LA}\circ L(\eta_A)=\mathrm{id}_{LA}$, $R(\varepsilon_B)\circ\eta_{RB}=\mathrm{id}_{RB}$). For objects $A$ of $\mathcal C$, $B$ of $\mathcal D$ and morphisms $\varphi:LA\to B$, $\psi:A\to RB$, one has $\psi=R(\varphi)\circ\eta_A$ if and only if $\varepsilon_B\circ L(\psi)=\varphi$. In particular the adjunct $\varphi^\sharp=R(\varphi)\circ\eta_A$ of $\varphi$ satisfies $\varepsilon_B\circ L(\varphi^\sharp)=\varphi$.
