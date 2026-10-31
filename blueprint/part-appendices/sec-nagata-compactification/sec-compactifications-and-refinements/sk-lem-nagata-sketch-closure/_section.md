+++
id = "sk-lem-nagata-sketch-closure"
kind = "lemma"
title = "Schematic closure and uniqueness"
order = 813
lean = ["AlgebraicGeometry.Scheme.Hom.image", "AlgebraicGeometry.IsImmersion.instIsOpenImmersionToImageOfQuasiCompact", "AlgebraicGeometry.Scheme.Hom.ker_toImage", "AlgebraicGeometry.ext_of_isSchemeTheoreticallyDominant_of_isSeparated'"]
uses = ["sk-def-nagata-sketch-data"]
tags = ["sketch"]
+++
Let $i:U\to T$ be a quasi-compact immersion, with $T$ quasi-separated.
Its scheme-theoretic image $\overline U\subseteq T$ is a closed
subscheme, $U\to\overline U$ is an open immersion, and $U$ is
scheme-theoretically dense in $\overline U$.
If $U\subseteq T$ is a scheme-theoretically dense open and $Y\to S$
is separated, then two $S$-maps $T\to Y$ that agree on $U$ agree on $T$.
