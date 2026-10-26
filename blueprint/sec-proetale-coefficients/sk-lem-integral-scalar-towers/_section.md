+++
id = "sk-lem-integral-scalar-towers"
kind = "lemma"
title = "Perfect complexes over $\\cO_E$"
order = 1211
tags = ["sketch"]
+++
To make the local models of the $K_n$ compatible, we need two facts about complexes over
$\cO_E$: a compatible system of perfect complexes over the rings $\cO_E/\pi_E^n$ comes from a
single bounded finite free complex, and the images of the cohomology at finite levels
stabilize at a uniform rate.

1. **(1)** For $n\ge1$ let $M_n\in D(\cO_E/\pi_E^n)$ be perfect, with maps $M_{n+1}\to M_n$
   inducing isomorphisms $M_{n+1}\otimes^{\mathbf L}_{\cO_E/\pi_E^{n+1}}\cO_E/\pi_E^n\simeq M_n$.
   Then there is a bounded complex $P^\bullet$ of finite free $\cO_E$-modules with isomorphisms
   $P^\bullet/\pi_E^n\simeq M_n$ in $D(\cO_E/\pi_E^n)$, compatible with the transition maps.
2. **(2)** Let $Q^\bullet$ be a bounded complex of finite free $\cO_E$-modules, and let
   $\pi_E^e$ kill the torsion of $H^{q+1}(Q^\bullet)$. Then for $m\ge n+e$

   $$
   \operatorname{im}\bigl(H^q(Q^\bullet/\pi_E^m)\to H^q(Q^\bullet/\pi_E^n)\bigr)
   =\operatorname{im}\bigl(H^q(Q^\bullet)\to H^q(Q^\bullet/\pi_E^n)\bigr).
   $$

In (2) such an $e$ exists, since $\cO_E$ is a Noetherian discrete valuation ring and
$H^{q+1}(Q^\bullet)$ is finitely generated.
