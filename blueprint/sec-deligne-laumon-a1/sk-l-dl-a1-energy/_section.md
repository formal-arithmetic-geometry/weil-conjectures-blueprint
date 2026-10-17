+++
id = "sk-l-dl-a1-energy"
kind = "lemma"
title = "Weight detection by trace energy"
order = 3100
uses = ["sk-d-dl-a1-setup", "sk-l-dl-a1-endpoints", "sk-p-linear-spectra", "sk-prop-logdet", "sk-thm-trace-transport", "sk-thm-tf-uniform-formula"]
lean = ["AlgebraicGeometry.WeilSheaf.traceEnergy", "AlgebraicGeometry.WeilSheaf.le_sub_one_of_traceEnergy_le"]
tags = ["sketch"]
+++
Let $N\ne0$ be pure of weight $v$ and lisse on a smooth geometrically
connected affine curve $V_0$. Put

$$
S_n(V_0,N)=\sum_{x\in V_0(\mathbf F_{q^n})}
|\iota\Tr(\DLAFr_x\mid N_{\bar x})|^2,
$$

where $\DLAFr_x$ means Frobenius relative to $\mathbf F_{q^n}$.
If $S_n(V_0,N)\le Cq^{nB}$ for every $n\ge1$, with a constant $C>0$
independent of $n$, then $v\le B-1$.
