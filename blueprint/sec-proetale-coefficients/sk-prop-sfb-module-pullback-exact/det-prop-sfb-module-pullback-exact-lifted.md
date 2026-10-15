+++
id = "det-prop-sfb-module-pullback-exact-lifted"
kind = "lemma"
title = "Lifts of exact functors to module objects are exact"
uses = ["lem-sfb-modobj-abelian", "lem-sfb-modobj-kernels", "lem-sfb-modobj-cokernels", "lem-sfb-modobj-forget-faithful"]
+++
Let $\mathcal C$ and $\mathcal D$ be abelian monoidal categories whose tensor products are additive in
each variable. Let $\mathcal R$ be a monoid object of $\mathcal C$ and $\mathcal S$ a monoid object of
$\mathcal D$ such that $\mathcal R\otimes-$ and $\mathcal S\otimes-$ are right exact, so that
$\Mod_{\mathcal R}(\mathcal C)$ and $\Mod_{\mathcal S}(\mathcal D)$ are abelian
([lem-sfb-modobj-abelian]); write $U_{\mathcal R}$, $U_{\mathcal S}$ for the forgetful functors. Let
$F\colon\mathcal C\to\mathcal D$ be an additive exact functor and
$G\colon\Mod_{\mathcal R}(\mathcal C)\to\Mod_{\mathcal S}(\mathcal D)$ a functor with
$U_{\mathcal S}\circ G=F\circ U_{\mathcal R}$. Then $G$ is additive and exact; in particular it preserves
finite limits and finite colimits.
