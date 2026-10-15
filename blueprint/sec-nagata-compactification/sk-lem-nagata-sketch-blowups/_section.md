+++
id = "sk-lem-nagata-sketch-blowups"
kind = "lemma"
title = "Finite refinements of blow-ups"
order = 10
uses = ["sk-def-nagata-sketch-data", "sk-def-nagata-admissible"]
lean = ["AlgebraicGeometry.Scheme.IdealSheafData.isProper_blowupMap", "AlgebraicGeometry.strictTransform", "AlgebraicGeometry.IsAdmissible.exists_extend", "AlgebraicGeometry.IsAdmissible.isSchemeTheoreticallyDominant_preimage_ι"]
tags = ["sketch"]
+++
Let $T$ be qcqs and $U\subseteq T$ a quasi-compact open. Finitely many
$U$-admissible blow-ups of $T$ ([sk-def-nagata-admissible]) admit a common
$U$-admissible blow-up. A composite of two $U$-admissible blow-ups is again
such a blow-up. A $U$-admissible blow-up on a quasi-compact open
$V\subseteq T$ containing $U$ extends to a $U$-admissible blow-up of $T$.
