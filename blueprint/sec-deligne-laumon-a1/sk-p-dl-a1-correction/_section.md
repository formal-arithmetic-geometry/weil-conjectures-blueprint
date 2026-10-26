+++
id = "sk-p-dl-a1-correction"
kind = "lemma"
title = "Fourier transform of the boundary sequence"
order = 4004
uses = ["sk-l-dl-a1-endpoints", "sk-lem-as-properties", "sk-p-dl-a1-middle", "sk-p-real-semi", "sk-thm-inversion"]
lean = ["AlgebraicGeometry.WeilSheaf.LisseOnDenseOpen.FourierCorrection", "AlgebraicGeometry.WeilSheaf.LisseOnDenseOpen.nonempty_fourierCorrection", "AlgebraicGeometry.WeilSheaf.LisseOnDenseOpen.FourierCorrection.isLisse", "AlgebraicGeometry.WeilSheaf.LisseOnDenseOpen.FourierCorrection.hasWeightsAtMost"]
tags = ["sketch"]
+++
Let $M$ be as in [sk-p-dl-a1-middle], pure of weight $w$, and let $M'$
be its Fourier partner. Put $B=j_*M/j_!M$. Then there are sheaves
$G,B'$ on the dual line such that

$$
 \operatorname{FT}_\psi(j_!M)=G,
 \qquad \operatorname{FT}_\psi(B)=B'[1],
 \qquad
 0\longrightarrow B'\longrightarrow G
        \longrightarrow j'_*M'\longrightarrow0.
$$

The sheaf $B'$ is lisse on the entire dual line and has weights at
most $w$.
