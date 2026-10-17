+++
id = "lem-mg-exterior-direct-sum"
kind = "lemma"
title = "Exterior power of a direct sum"
lean = ["Representation.exteriorPowerProdEquiv", "Representation.exteriorPowerDirectSumEquiv"]
order = 2891
uses = ["def-wf-weil-group"]
+++
Let $V_1,\ldots,V_s$ be finite-dimensional Weil
representations. For every $N$, there is a canonical Weil-equivariant
decomposition

$$
\bigwedge\nolimits^{N}\!\left(\bigoplus_{i=1}^{s}V_i\right)
\simeq
\bigoplus_{\substack{n_1+\cdots+n_s=N\\ n_i\ge0}}
\bigotimes_{i=1}^{s}\bigwedge\nolimits^{n_i}V_i,
$$

where terms with $n_i>\dim V_i$ are zero.
