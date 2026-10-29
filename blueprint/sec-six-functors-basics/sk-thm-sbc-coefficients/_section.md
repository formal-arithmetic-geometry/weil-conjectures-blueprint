+++
id = "sk-thm-sbc-coefficients"
kind = "theorem"
title = "Smooth base change for all admissible coefficients"
order = 2863
uses = ["sk-lem-sbc-exchange-compatibility", "sk-def-sfb-constructible", "sk-prop-scalar-six"]
tags = ["sketch"]
+++
Consider a cartesian square with $g'\colon X'\to X$, $f'\colon X'\to Y'$, $f\colon X\to Y$ and
$g\colon Y'\to Y$, and its base change map ([sk-lem-sbc-exchange-compatibility]). Assume that all
schemes are of finite type over $k$ and that $g$ is smooth. For every admissible coefficient ring

$$
 \Lambda\in\{A,\Zl,\mathcal O_E,\Ql,E,\Qlb\}
$$

and every $K\in\Dctf(X,\Lambda)$ ([sk-def-sfb-constructible]), the canonical map is an isomorphism

$$
 g^*Rf_*K\xrightarrow{\sim}Rf'_*g'^*K.
$$

These isomorphisms respect pasting and all change-of-coefficients maps of [sk-prop-scalar-six].

For integral and rational coefficients we have $\Dctf=\Dbc$, so in those cases the theorem concerns
all bounded constructible complexes.
