+++
id = "corollary-sums-squared-traces-j-shriek--1"
kind = "corollary"
title = "Comparing squared traces with the direct image"
name_showing = false
order = 1211001
aliases = ["bp-r374-1"]
lean = ["AlgebraicGeometry.WeilSheaf.LisseOnDenseOpen.traceEnergy_le_traceEnergy_directImage", "AlgebraicGeometry.WeilSheaf.LisseOnDenseOpen.exists_traceEnergy_directImage_le_add"]
uses = ["definition-weil-structure", "definition-lisse-sheaves", "definition-weights", "definition-middle-extension", "definition-growth-squared-traces"]
+++
The comparison through $j_!$ is bypassed by the Lean route, which
compares the squared traces on $U_0$ directly with those of $j_*$ on
the affine line.

Let $j:U_0\hookrightarrow\mathbf A^1_{\mathbf F_q}$ be a dense open,
and let $\mathcal G$ be a lisse Weil $\Qbarl$-sheaf on $U_0$, where
$\ell\ne\operatorname{char}\mathbf F_q$. Fix an embedding
$\iota:\Qbarl\hookrightarrow\mathbf C$. With the notation of
Definition [definition-growth-squared-traces], for every $n\ge1$ we have

$$
S_n(\mathcal G)\le S_n(j_*\mathcal G).
$$

If $\mathcal G$ is punctually of weights $\le w$, there is a real
constant $C$ such that, for every $n\ge1$,

$$
S_n(j_*\mathcal G)\le S_n(\mathcal G)+Cq^{nw}.
$$
