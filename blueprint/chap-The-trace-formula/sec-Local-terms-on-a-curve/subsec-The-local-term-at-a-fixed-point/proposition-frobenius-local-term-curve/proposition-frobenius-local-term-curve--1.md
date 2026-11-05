+++
id = "proposition-frobenius-local-term-curve--1"
kind = "proposition"
title = "The Frobenius local term with rational coefficients"
name_showing = false
order = 993001
aliases = ["bp-r303-1"]
lean = ["AlgebraicGeometry.ProEtale.CondensedRing.Correspondence.localTerm_traceClass_frobeniusGraph_eq_trace_of_smooth"]
uses = ["definition-constructible-sheaves", "definition-correspondence", "definition-frobenius-correspondences-their-operators", "definition-trace-class-local-terms", "definition-categorical-trace"]
+++
Let $k_0$ be a finite field with $q$ elements, let $k$ be an
algebraically closed extension of $k_0$, and let $\ell\ne\operatorname{char}k$
be a prime. Let $X_0\to\operatorname{Spec}k_0$ be locally of finite type,
and suppose that $X=X_0\times_{k_0}k$ is separated of finite type and
smooth of relative dimension one over $k$. Write $\Phi_X$ for the
base change of the $q$-power Frobenius of $X_0$.

Let $m\geq1$, let $K\in\Dctf(X,\Qbarl)$, and let
$\psi:(\Phi_X^m)^*K\to K$ be any morphism. Let
$x:s=\operatorname{Spec}k\to X$ satisfy $\Phi_X^m\circ x=x$,
and assume that $K_x=x^*K$ is dualizable. Put
$c_m=(\operatorname{id}_X,\Phi_X^m)$ and $F=\Fix(c_m)$, and let
$\tilde x:s\to F$ be the point induced by $x$. For every open and
closed immersion $b:B\hookrightarrow F$ with $B$ proper over $k$ and
image the single point $\tilde x$, one has

$$
\operatorname{LT}_B(\psi)
=\operatorname{tr}_{\Qbarl}(\psi_x\mid K_x),
$$

where $\psi_x$ is the composite
$K_x\simeq x^*(\Phi_X^m)^*K\xrightarrow{x^*\psi}K_x$.
Neither invertibility of $\psi$ nor local constancy of $K$ at $x$ is
assumed.
