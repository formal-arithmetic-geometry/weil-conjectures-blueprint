+++
id = "sk-prop-rootpurity"
kind = "section"
title = "Reciprocal roots have the weight-$i$ absolute value"
order = 3113
uses = ["sk-def-cohfamily", "sk-def-roots", "sk-input-weights"]
+++
*Proposition (sketch).*

In the situation of [sk-def-cohfamily], for every $0\le i\le2d$ every
reciprocal root $\alpha\in\Qlb$ of $P_{i,\ell}$ satisfies

$$
|\iota(\alpha)|=q^{i/2}.
$$

## Proof

The roots of $P_{i,\ell}(T)=\det(1-TF_{i,\ell})$ are the inverses of the
eigenvalues of $F_{i,\ell}$ on $V_{i,\ell}=H^{i}(X,\Ql)$, which are
$V_{i,\ell}=H^{i}(X,\Ql)$, which by [sk-input-weights] (4)–(5) is $\iota$-pure of
weight $i$: every eigenvalue $\beta$ satisfies
$|\iota(\beta)|=q^{i/2}$. Hence every reciprocal root
$\alpha=\beta^{-1}$ has $|\iota(\alpha)|=q^{i/2}$.

Uses: [sk-def-cohfamily], [sk-def-roots], [sk-input-weights]
