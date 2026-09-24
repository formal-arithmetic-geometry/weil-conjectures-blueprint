+++
id = "thm-trf-trace-additivity-categorical"
kind = "theorem"
title = "Additivity of the categorical traces of the global operators"
order = 3919
uses = ["def-trf-categorical-trace", "lem-trf-global-operator-perfect", "lem-trf-global-operator-triangulated", "prop-trf-trace-formal-laws"]
+++
In the situation of [lem-trf-global-operator-triangulated], assume
in addition that the ordinary leg $c_2$ is
proper, so that the
global operators are endomorphisms of perfect complexes
by [lem-trf-global-operator-perfect], in the sense of
[def-trf-categorical-trace]. Then

$$
\operatorname{tr}_A\bigl(T_c(u)\mid R\Gamma_c(X,K)\bigr)
=
\operatorname{tr}_A\bigl(T_c(u')\mid R\Gamma_c(X,K')\bigr)
+
\operatorname{tr}_A\bigl(T_c(u'')\mid R\Gamma_c(X,K'')\bigr)
$$

in $A$.

## Proof

By [lem-trf-global-operator-triangulated] the three operators form
an endomorphism of a distinguished triangle of perfect complexes, and
triangle additivity of the categorical trace is
[prop-trf-trace-formal-laws](2). Applying that law to the
displayed morphism of triangles gives the assertion.
