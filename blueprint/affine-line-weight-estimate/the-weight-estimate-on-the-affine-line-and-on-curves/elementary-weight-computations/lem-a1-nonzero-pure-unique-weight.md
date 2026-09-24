+++
id = "lem-a1-nonzero-pure-unique-weight"
kind = "lemma"
title = "A nonzero pure Frobenius module has a unique weight"
order = 4265
uses = ["def-weil-frobenius-module-weights"]
+++
If a nonzero finite Frobenius module $(V,F)$ is pure of weights $u$
and $v$ in the sense of [def-weil-frobenius-module-weights], then
$u=v$.

## Proof

Choose an eigenvalue $\alpha$ of $F$ on $V$. Both purity conditions
give $q^{u/2}=|\iota(\alpha)|=q^{v/2}$ in the fixed embedding
$\iota:\overline{\mathbf Q}_\ell\hookrightarrow\mathbf C$ of
[def-weil-frobenius-module-weights]; since $q>1$, the real
exponential function is injective and $u=v$.
