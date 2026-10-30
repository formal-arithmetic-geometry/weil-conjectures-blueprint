+++
id = "sk-p-dl-a1-correction"
kind = "lemma"
title = "Fourier transform of the boundary sequence"
order = 743
lean = ["AlgebraicGeometry.WeilSheaf.LisseOnDenseOpen.FourierCorrection", "AlgebraicGeometry.WeilSheaf.LisseOnDenseOpen.nonempty_fourierCorrection", "AlgebraicGeometry.WeilSheaf.LisseOnDenseOpen.FourierCorrection.isLisse", "AlgebraicGeometry.WeilSheaf.LisseOnDenseOpen.FourierCorrection.hasWeightsAtMost"]
uses = ["sk-l-dl-a1-endpoints", "sk-lem-as-properties", "sk-p-dl-a1-middle", "sk-p-real-semi", "sk-thm-inversion"]
tags = ["sketch"]
+++
Put $B=j_*M/j_!M$. There are sheaves $G$ and $B'$ on the dual line such
that $\operatorname{FT}_\psi(j_!M)=G$, $\operatorname{FT}_\psi(B)=B'[1]$,
and the sequence

$$
0\longrightarrow B'\longrightarrow G
\longrightarrow j'_*M'\longrightarrow0
$$

is exact. The sheaf $B'$ is lisse on the entire dual line and has weights at
most $w$.
