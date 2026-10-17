+++
id = "sk-thm-sbc-coefficients"
kind = "theorem"
title = "Smooth base change for all admissible coefficients"
order = 1577
uses = ["sk-def-bc", "sk-thm-sbc-derived", "sk-prop-scalar-six", "sk-thm-sf-ctf-stability", "sk-thm-pe-constructible-comparison", "sk-def-pe-derived-completion", "sk-prop-integral-criterion", "sk-lem-sbc-exchange-compatibility", "sk-lem-pe-derived-nakayama", "sk-lem-integral-models", "sk-cor-pe-bounded-continuity", "sk-thm-sfb-qlbar-two-colimit"]
tags = ["sketch"]
+++
Consider a cartesian square with $u:X'\to X$, $f':X'\to Y'$, $f:X\to Y$, $g:Y'\to Y$, and
the exchange map $\operatorname{Ex}_{g,f}(K):g^*Rf_*K\to Rf'_*u^*K$ of
[sk-lem-sbc-exchange-compatibility].
Assume the standing finite-type hypotheses
and that $g$ is smooth. For every admissible coefficient ring

$$
 \Lambda\in\{A,\Zl,\mathcal O_E,\Ql,E,\overline{\mathbf Q}_\ell\}
$$

and every $K\in\Dctf(X,\Lambda)$, the
canonical map is an isomorphism

$$
 g^*Rf_*K\xrightarrow{\sim}Rf'_*u^*K
       \quad\text{in }\Dctf(Y',\Lambda).
 \tag{1}
$$

These isomorphisms respect pasting and all coefficient comparisons in
Proposition [sk-prop-scalar-six].

For integral and rational coefficients $\Dctf=\Dbc$, so in those cases
the theorem concerns all bounded constructible complexes.

*Complement.* In the setting of the complement of [sk-thm-sbc-derived], with all schemes
Noetherian and $\ell$ invertible, the exchange isomorphism holds for the coefficient stages
of the six-functor formalism:

1. at a finite stage on the pro-étale site, by conjugating the étale statement
by the site comparison ([sbc-thm-finite-proetale-smooth-base-change]);
1. at $\mathcal O_E$, for derived-complete complexes of étale origin
([sbc-thm-adic-smooth-base-change]);
1. at $E$, for complexes with an admissible lattice, independently of the
lattice ([sbc-thm-e-coefficient-smooth-base-change]);
1. at $\Qlb$, as the colimit over finite subextensions
([sbc-thm-overline-mathbf-q-ell-coefficient-smooth-base-ch]).
