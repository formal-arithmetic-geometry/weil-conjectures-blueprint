+++
id = "def-sfb-modobj-restriction-equivalence"
kind = "definition"
title = "Restriction along an isomorphism is an equivalence"
order = 1152
uses = ["def-sfb-modobj-restriction"]
lean = ["CategoryTheory.Mod.comapEquivalenceOfIsIso"]
+++
Let $\mathcal C$ be a braided monoidal category that is closed, with equalizers and
coequalizers, such that $X\otimes-$ and $-\otimes X$ preserve colimits for every $X$. Let
$\varphi\colon\mathcal R\to\mathcal S$ be an isomorphism of monoid objects, with
$\mathcal R$ commutative. Then the restriction of scalars
$\operatorname{Res}_\varphi\colon\Mod_{\mathcal S}(\mathcal C)\to\Mod_{\mathcal R}(\mathcal C)$
([def-sfb-modobj-restriction]) is an equivalence of categories with quasi-inverse
$\operatorname{Res}_{\varphi^{-1}}$.
