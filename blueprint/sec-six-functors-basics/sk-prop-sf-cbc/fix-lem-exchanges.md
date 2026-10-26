+++
id = "fix-lem-exchanges"
kind = "lemma"
title = "Exchange functoriality: naturality, identities, and pasting"
order = 2726
uses = ["def-cbc-exchange-map", "def-exchange-projection", "def-fix-six-functor-datum", "def-weil-derived-direct-image", "def-weil-derived-pullback-tensor-hom", "def-weil-pbc-cartesian-square", "def-weil-scheme-morphism-properties", "lem-weil-pbc-exchange-identity-pasting", "prop-compactification-coherence-detailed", "sbc-def-base-change-map", "sbc-lem-identity-and-base-change-composition", "sbc-thm-bounded-below-derived-smooth-base-change", "sk-thm-sbc-coefficients", "thm-cbc-finite-torsion", "sk-def-sfb-shriek-base-change-morphism", "sk-thm-sfb-shriek-base-change", "thm-cbc-complete-proetale", "thm-sf-comp-composition"]
+++
In the six-functor datum of
[def-fix-six-functor-datum], let

$$
\begin{array}{ccc}
X'&\xrightarrow{g'}&X\\
f'\downarrow&&\downarrow f\\
Y'&\xrightarrow{g}&Y
\end{array}
$$

be a cartesian square of
finite-type $k$-schemes
whose four arrows are
separated and of finite
type, and let $K\in D^b_c(X,\Lambda)$, with $K'=Lg'^*K$. The
exchange transformations

$$
\operatorname{Ex}_*(K):Lg^*Rf_*K\longrightarrow Rf'_*K',
\qquad
\operatorname{Ex}_!(K):Lg^*Rf_!K\longrightarrow Rf'_!K',
$$

of [def-exchange-projection] satisfy:

1. both are natural in $K$, in the morphisms of the square, and
in the coefficient ring; $\operatorname{Ex}_!$ agrees with the
compact-support exchange map of [def-cbc-exchange-map] at every
finite level and with the compact-support base change morphism of
[sk-def-sfb-shriek-base-change-morphism] on the condensed categories
$\Dbc(-,\Lambda)$ for $\Lambda=\mathcal O_E,E,\Qlb$, where it is an
isomorphism ([thm-cbc-complete-proetale], [sk-thm-sfb-shriek-base-change]);
1. both are the identity for an identity square, and for
vertically or horizontally pasted cartesian squares the exchange
transformation of the outer rectangle is the composite of the
exchange transformations of the two inner squares after inserting
the canonical associativity isomorphisms; $\operatorname{Ex}_*$
obeys the identity and pasting equations of
[lem-weil-pbc-exchange-identity-pasting] and of
[sbc-lem-identity-and-base-change-composition],
$\operatorname{Ex}_!$ those of [thm-cbc-finite-torsion];
1. for smooth $g$,
$\operatorname{Ex}_*$ is the smooth-base-change exchange morphism of
[sbc-thm-bounded-below-derived-smooth-base-change], and it is an
isomorphism at every coefficient ring ([sk-thm-sbc-coefficients]);
1. $\operatorname{Ex}_!$ is independent of the chosen
compactification and compatible with the refinement comparison
isomorphisms of [prop-compactification-coherence-detailed] and with the
composition law of [thm-sf-comp-composition].
