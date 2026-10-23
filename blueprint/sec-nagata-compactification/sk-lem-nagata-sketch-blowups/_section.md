+++
id = "sk-lem-nagata-sketch-blowups"
kind = "lemma"
title = "Finite refinements of blow-ups"
order = 223
uses = ["sk-def-nagata-sketch-data", "sk-def-nagata-admissible"]
lean = ["AlgebraicGeometry.IsAdmissible.mul", "AlgebraicGeometry.Scheme.IdealSheafData.exists_blowup_mul_iso", "AlgebraicGeometry.IsAdmissible.exists_comp", "AlgebraicGeometry.IsAdmissible.exists_extend"]
tags = ["sketch"]
+++
Let $T$ be qcqs and $U\subseteq T$ an open, not necessarily quasi-compact.
If $\mathcal I_1,\mathcal I_2$ are centres of $U$-admissible blow-ups of $T$
([sk-def-nagata-admissible]), so is $\mathcal I_1\mathcal I_2$, and
$\operatorname{Bl}_{\mathcal I_1\mathcal I_2}(T)$ is, over $T$, the blow-up
of $\operatorname{Bl}_{\mathcal I_1}(T)$ along the pulled-back
$\mathcal I_2$; so two $U$-admissible blow-ups have a common $U$-admissible
blow-up. A composite $T''\to T'\to T$ of a $U$-admissible blow-up $T'\to T$
and a blow-up of $T'$ admissible for the preimage of $U$ is isomorphic over
$T$ to a $U$-admissible blow-up of $T$. A $U$-admissible blow-up on a
quasi-compact open $V\subseteq T$ containing $U$ extends to a
$U$-admissible blow-up of $T$ whose restriction to $V$ is the given one.
