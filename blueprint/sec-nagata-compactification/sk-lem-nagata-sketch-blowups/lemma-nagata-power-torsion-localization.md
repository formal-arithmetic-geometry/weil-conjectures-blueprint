+++
id = "lemma-nagata-power-torsion-localization"
kind = "lemma"
title = "Localization of power torsion"
order = 141
lean = ["Submodule.localized'_powTorsion"]
uses = ["def-nagata-power-torsion", "lemma-nagata-power-torsion-kernel-localization", "lemma-nagata-power-torsion-submodule"]
+++
Let $R$ be a ring, $M$ an $R$-module, $a\in R$, and let $S\subseteq R$ be a
multiplicative subset. Under the localization map $M\to S^{-1}M$, the
localization of $\Gamma_{(a)}(M)$ is the power-torsion submodule of
$S^{-1}M$ for the image of $a$:

$$
S^{-1}\Gamma_{(a)}(M)=\Gamma_{(a/1)}(S^{-1}M).
$$

## Proof

Localize the kernel description in
[lemma-nagata-power-torsion-kernel-localization]. Localization is flat,
so it preserves this kernel. The iterated localization $(M_s)_{a/1}$ is
canonically $M_{sa}$.

The power-torsion submodule is the kernel of the map
$N\to N_a$ by
[lemma-nagata-power-torsion-kernel-localization]. Localization at
$s$ is flat, hence carries this kernel to the kernel of
$N_s\to (N_s)_{a/1}$. The latter kernel is
$\Gamma_{(a/1)}(N_s)$, proving the first equality. The universal property
of the quotient then gives the displayed map; it is an isomorphism because
localization is exact and the localized kernel is exactly the target
torsion submodule. For $s,t$, both composites are induced by the same map
$N\to N_{st}$ and therefore agree by quotient and localization
extensionality.
