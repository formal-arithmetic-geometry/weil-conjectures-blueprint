+++
id = "lem-sfb-modobj-kernels"
kind = "lemma"
title = "Kernels of module objects are computed in $\\mathcal C$"
order = 1554
uses = ["sk-def-sfb-module-objects"]
lean = ["CategoryTheory.Mod.isLimitKernelFork"]
+++
Let $\mathcal C$ be a preadditive monoidal category whose tensor product is additive in
each variable, and let $\mathcal R$ be a monoid object of $\mathcal C$. Let
$f\colon M\to N$ be a morphism of $\mathcal R$-module objects ([sk-def-sfb-module-objects])
whose underlying morphism has a kernel $\iota\colon K\to M$ in $\mathcal C$. Then there is
a unique morphism $\gamma_K\colon\mathcal R\otimes K\to K$ with
$\iota\circ\gamma_K=\gamma_M\circ(\mathcal R\otimes\iota)$. It is an action of
$\mathcal R$ on $K$, and $\iota\colon(K,\gamma_K)\to M$ is a kernel of $f$ in
$\Mod_{\mathcal R}(\mathcal C)$.
