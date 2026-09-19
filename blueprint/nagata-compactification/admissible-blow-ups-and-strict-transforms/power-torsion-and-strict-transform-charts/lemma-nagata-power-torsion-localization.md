+++
id = "lemma-nagata-power-torsion-localization"
kind = "lemma"
title = "Localization of power torsion"
order = 316
lean = ["Submodule.localized'_powTorsion"]
uses = ["lemma-nagata-power-torsion-kernel-localization"]
+++
Let $s\in R$. Under localization at $s$, the image of
$\Gamma_{(a)}(M)$ is
$\Gamma_{(a/1)}(M_s)$.

## Proof

Localize the kernel description in
[lemma-nagata-power-torsion-kernel-localization]. Localization is flat,
so it preserves this kernel. The iterated localization $(M_s)_{a/1}$ is
canonically $M_{sa}$.
