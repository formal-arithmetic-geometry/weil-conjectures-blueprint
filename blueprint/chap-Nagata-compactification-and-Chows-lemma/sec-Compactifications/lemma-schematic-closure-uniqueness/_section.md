+++
id = "lemma-schematic-closure-uniqueness"
kind = "lemma"
title = "Schematic closure"
order = 1409
lean = ["AlgebraicGeometry.IsImmersion.instIsOpenImmersionToImageOfQuasiCompact", "AlgebraicGeometry.Scheme.Hom.image", "AlgebraicGeometry.Scheme.Hom.ker_morphismRestrict", "AlgebraicGeometry.Scheme.Hom.ker_pullback_snd"]
+++
Let $i:U\to T$ be a quasi-compact immersion, with $T$ quasi-separated.
Its scheme-theoretic image $\overline U\subseteq T$ is a closed
subscheme, $U\to\overline U$ is an open immersion, and $U$ is
scheme-theoretically dense in $\overline U$. The formation of
$\overline U$ commutes with flat base change $T'\to T$, in particular
with restriction to opens of $T$.
