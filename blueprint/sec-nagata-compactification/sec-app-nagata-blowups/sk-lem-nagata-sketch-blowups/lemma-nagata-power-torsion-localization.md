+++
id = "lemma-nagata-power-torsion-localization"
kind = "lemma"
title = "Localization of power torsion"
order = 165
lean = ["Submodule.localized'_powTorsion"]
uses = ["def-nagata-power-torsion", "lemma-nagata-power-torsion-kernel-localization"]
+++
Let $R$ be a ring, $M$ an $R$-module, $a\in R$, and let $S\subseteq R$ be a
multiplicative subset. Under the localization map $M\to S^{-1}M$, the
localization of $\Gamma_{(a)}(M)$ is the power-torsion submodule of
$S^{-1}M$ for the image of $a$:

$$
S^{-1}\Gamma_{(a)}(M)=\Gamma_{(a/1)}(S^{-1}M).
$$
