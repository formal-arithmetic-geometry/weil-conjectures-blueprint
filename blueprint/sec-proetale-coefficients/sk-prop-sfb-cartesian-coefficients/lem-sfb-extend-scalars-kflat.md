+++
id = "lem-sfb-extend-scalars-kflat"
kind = "lemma"
title = "Extension of scalars preserves K-flat quasi-isomorphisms"
order = 1321
uses = ["det-def-sfb-change-of-scalars", "def-sfb-preserves-kflat-quasi-iso"]
lean = ["CategoryTheory.Mod.preservesKFlatQuasiIso"]
+++
Let $\mathcal C$ be a closed symmetric monoidal Grothendieck abelian category whose tensor
product is additive and which has functorial flat resolutions, and let
$\varphi\colon\mathcal R\to\mathcal S$ be a morphism of commutative ring objects of
$\mathcal C$. Let $s\colon P\to P'$ be a
quasi-isomorphism between K-flat complexes of $\mathcal R$-modules (K-flat for
$\otimes_{\mathcal R}$, [def-sfb-preserves-kflat-quasi-iso]). Then
$\mathcal S\otimes_{\mathcal R}s$ is a quasi-isomorphism of complexes of
$\mathcal S$-modules.
