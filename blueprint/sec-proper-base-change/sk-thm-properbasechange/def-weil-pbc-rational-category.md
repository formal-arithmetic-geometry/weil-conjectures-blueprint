+++
id = "def-weil-pbc-rational-category"
kind = "definition"
title = "Rational category from an integral category"
order = 1365
uses = ["def-weil-karoubi-envelope", "def-weil-pbc-bounded-constructible-complete", "def-weil-rationalization-karoubi", "sk-def-sfb-bounded-constructible", "sk-thm-sfb-rationalization-comparison"]
+++
Let $E/\Ql$ be finite, let $\mathcal O_E$ be its ring of integers, and let
$\varpi$ be a uniformizer. The rational category $\Dbc(T,E)\subseteq D(T_{\Proet},E)$ is
the condensed one: the bounded complexes of $E_T$-modules with constructible cohomology
sheaves ([sk-def-sfb-bounded-constructible]), as in [def-weil-rationalization-karoubi]. For
$T$ of finite type over $k$, extension of scalars $E_T\otimes_{\mathcal O_{E,T}}-$
identifies it with the *rationalization* (raw scalar localization) of the integral
category [def-weil-pbc-bounded-constructible-complete]
([sk-thm-sfb-rationalization-comparison]), and we write
$$
 \Dbc(T,E)=
 \Dbc(T,\mathcal O_E)[1/\varpi].
$$
This rationalization has the same objects as $\Dbc(T,\mathcal O_E)$, and morphisms
$$
 \Hom(K,L)[1/\varpi]
 =\Hom_{\Dbc(T,\mathcal O_E)}(K,L)\otimes_{\mathcal O_E}E.
$$

No Karoubi envelope is taken in this identification. The category is idempotent
complete, and consequently the canonical functor into its Karoubi envelope is
an exact equivalence.
