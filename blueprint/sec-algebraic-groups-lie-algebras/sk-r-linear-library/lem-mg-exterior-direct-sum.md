+++
id = "lem-mg-exterior-direct-sum"
kind = "lemma"
title = "Exterior power of a direct sum"
lean = ["Representation.exteriorPowerProdEquiv", "Representation.exteriorPowerDirectSumEquiv"]
order = 3743
uses = ["d-monodromy"]
+++
Let $V_1,\ldots,V_s$ be Weil representations of a degree datum
([d-monodromy]), or more generally finite-dimensional representations of
any group $W$. For every $N$, there is a canonical $W$-equivariant
decomposition

$$
\bigwedge\nolimits^{N}\!\left(\bigoplus_{i=1}^{s}V_i\right)
\simeq
\bigoplus_{\substack{n_1+\cdots+n_s=N\\ n_i\ge0}}
\bigotimes_{i=1}^{s}\bigwedge\nolimits^{n_i}V_i,
$$

where terms with $n_i>\dim V_i$ are zero.
