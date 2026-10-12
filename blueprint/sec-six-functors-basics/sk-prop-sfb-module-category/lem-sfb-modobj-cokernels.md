+++
id = "lem-sfb-modobj-cokernels"
kind = "lemma"
title = "Cokernels of module objects are computed in $\\mathcal C$"
order = 1555
uses = ["sk-def-sfb-module-objects"]
lean = ["CategoryTheory.Mod.isColimitCokernelCofork"]
+++
Let $\mathcal C$ be a preadditive monoidal category whose tensor product is additive in
each variable. Let $\mathcal R$ be a monoid object of $\mathcal C$ such that
$\mathcal R\otimes-$ preserves finite colimits. Let $f\colon M\to N$ be a morphism of
$\mathcal R$-module objects ([sk-def-sfb-module-objects]) whose underlying morphism has a
cokernel $\pi\colon N\to Q$ in $\mathcal C$. Then there is a unique morphism
$\gamma_Q\colon\mathcal R\otimes Q\to Q$ with
$\gamma_Q\circ(\mathcal R\otimes\pi)=\pi\circ\gamma_N$. It is an action of $\mathcal R$ on
$Q$, and $\pi\colon N\to(Q,\gamma_Q)$ is a cokernel of $f$ in
$\Mod_{\mathcal R}(\mathcal C)$.
