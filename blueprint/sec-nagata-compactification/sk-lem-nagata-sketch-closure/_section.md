+++
id = "sk-lem-nagata-sketch-closure"
kind = "lemma"
title = "Schematic closure and uniqueness"
order = 24
uses = ["sk-def-nagata-sketch-data"]
lean = ["AlgebraicGeometry.Scheme.Hom.image", "AlgebraicGeometry.IsImmersion.instIsOpenImmersionToImageOfQuasiCompact", "AlgebraicGeometry.Scheme.Hom.ker_toImage", "AlgebraicGeometry.ext_of_isSchemeTheoreticallyDominant_of_isSeparated'"]
tags = ["sketch"]
+++
Let $i:U\to T$ be a quasi-compact immersion. Its
scheme-theoretic image $\overline U\subseteq T$ is a closed subscheme,
$U\to\overline U$ is an open immersion, and $U$ is scheme-theoretically
dense in $\overline U$.

If $U\subseteq T$ is a scheme-theoretically dense open and $Y\to S$ is
separated, two $S$-maps $T\to Y$ agreeing on $U$ agree on $T$.
