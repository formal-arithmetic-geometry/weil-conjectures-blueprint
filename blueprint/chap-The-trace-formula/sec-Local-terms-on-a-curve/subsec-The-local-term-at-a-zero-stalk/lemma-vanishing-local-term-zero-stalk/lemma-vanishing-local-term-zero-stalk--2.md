+++
id = "lemma-vanishing-local-term-zero-stalk--2"
kind = "lemma"
title = "Vanishing of the Frobenius local term"
name_showing = false
order = 989002
aliases = ["bp-r302-2"]
lean = ["AlgebraicGeometry.ProEtale.CondensedRing.Correspondence.localTerm_traceClass_frobeniusGraph_eq_zero_of_smooth"]
uses = ["definition-constructible-sheaves", "definition-correspondence", "definition-frobenius-correspondences-their-operators", "definition-trace-class-local-terms"]
+++
Let $k$ be an algebraically closed extension of a finite field $k_0$,
let $\ell\neq\operatorname{char}(k)$ be prime, and let
$X=X_0\times_{k_0}k$ be a separated smooth curve, with $X_0$ of finite
type over $k_0$. Let $m\geq1$, let $K\in\Dctf(X,\Qbarl)$, and let
$\psi:(\Phi_X^m)^*K\to K$ be any morphism. Suppose that $y\in X(k)$ is
fixed by $\Phi_X^m$ and $K_{\bar y}=0$.

Let $F$ be the fixed locus of the graph correspondence
$c=(\operatorname{id}_X,\Phi_X^m)$ with coefficient $\psi$, and let
$B\hookrightarrow F$ be a quasi-compact open and closed subscheme,
proper over $k$, whose underlying set is the single fixed point
determined by $y$. Then

$$
\operatorname{LT}_B(\psi)=0\qquad\text{in }\Qbarl.
$$

In particular, the local term $\operatorname{LT}_y(\psi)$ vanishes.
The morphism $\psi$ need not be an isomorphism.
