+++
id = "def-trf-strict-weil-complex"
kind = "definition"
title = "Strict Weil complex at finite coefficients"
order = 2165
uses = ["def-trf-coefficient-conventions", "def-trf-scheme-frobenius", "def-weil-derived-pullback-tensor-hom", "def-weil-finite-field-fiber", "def-weil-pbc-proetale-site", "def-weil-scheme-morphism-properties", "def-weil-weil-sheaf-complex"]
+++
Fix the global finite-field datum
and the coefficient
conventions of this trace-formula blueprint: $A=A_{E,n}$, $X_0$
separated finite type over $k_0$, $X=X_0\times_{k_0}k$, on the
small pro-etale site. A
*strict Weil complex at $A$* is a pair $(K,\varphi)$ with
$K\in D^b_{ctf}(X,A)$ and an isomorphism formed using the
derived pullback

$$
\varphi:Lg_\gamma^*K\xrightarrow{\ \sim\ }K,
$$

where $g_\gamma=g_X$ is the
geometric-Frobenius
automorphism of [def-trf-scheme-frobenius]; morphisms are morphisms
of $K$ commuting with $\varphi$. Write
$D^b_{ctf,\mathrm W}(X,A)$ for the resulting category, the finite
coefficient stage of the
Weil-complex category of
the trace-formula chapter, with its forgetful functor $\operatorname{For}$.

*Recorded in advance* from chapter *The trace formula* of the source.
