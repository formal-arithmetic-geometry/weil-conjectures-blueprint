+++
id = "thm-wf-internal-hom-weight"
kind = "theorem"
title = "Internal-Hom weight theorem"
order = 3145
uses = ["def-wf-internal-hom", "def-wf-tensor-product", "def-wf-wtle", "lem-tw-multiplicativity"]
+++
Let $K,L\in\mathrm{WeilD}(X_0,E)$. Assume that $K$ is
*dualizable*, meaning that the canonical evaluation map

$$
K^\vee\otimes^L_E L\stackrel{\sim}{\to}R\operatorname{Hom}_E(K,L)
$$

is an isomorphism, and assume $\mathrm{WtLe}(K^\vee,-u)$. Then

$$
\mathrm{WtLe}(L,v)\quad\Longrightarrow\quad
\mathrm{WtLe}(R\operatorname{Hom}_E(K,L),v-u),
$$

and the same holds for the integral weight predicates.

## Proof

For dualizable $K$, the evaluation identification
$K^\vee\otimes^L_E L\cong R\operatorname{Hom}_E(K,L)$ is
Frobenius-equivariant: the tensor Frobenius of
[def-wf-tensor-product] is
$\varphi_{K^\vee}\otimes\varphi_L$ and the conjugation formula of
[def-wf-internal-hom] is compatible with the evaluation. Hence the
weights of $R\operatorname{Hom}_E(K,L)$ are sums $w_{K^\vee}+w_L$ of
weights of $K^\vee$ and of $L$, bounded by
$-u+v$ using $\mathrm{WtLe}(K^\vee,-u)$,
$\mathrm{WtLe}(L,v)$ and the multiplicativity of weights
([lem-tw-multiplicativity]); the integral version follows from the
integral predicates.
