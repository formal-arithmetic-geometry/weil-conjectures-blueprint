+++
id = "prop-weil-pbc-direct-image-limits"
kind = "theorem"
title = "Direct image, derived limits, and completeness"
order = 1324
uses = ["def-weil-pbc-adic-coefficient-datum", "def-weil-pbc-derived-inverse-limit", "def-weil-pbc-projection-formula-map", "lemma-weil-pbc-perfect-projection-formula", "prop-weil-pbc-roos-triangle"]
tags = ["latex:proposition"]
+++
Levelwise direct image on tower categories has a total right derived functor

$$
 Rf_*^{\operatorname{Tow}}:
 D(\operatorname{Tow}_{A}(X))
 \longrightarrow D(\operatorname{Tow}_{A}(Y)),
$$

with $\operatorname{ev}_nRf_*^{\operatorname{Tow}}M_\bullet\simeq Rf_*M_n$.
For every $M_\bullet$ the canonical map

$$
 Rf_*\Rlim M_\bullet
 \xrightarrow{\sim}
 \Rlim\bigl(Rf_*^{\operatorname{Tow}}M_\bullet\bigr)
$$

is an isomorphism. Under the two canonical Roos triangles associated with the
derived inverse-limit [def-weil-pbc-derived-inverse-limit] construction, it
is induced by the canonical isomorphisms

$$
 Rf_*R\!\prod_nM_n\xrightarrow{\sim}
 R\!\prod_nRf_*M_n
$$

and their commutation with $(1-s)$. If $K\in D(X_{\Proet},A)$ is derived
$I$-complete, then $Rf_*K$ is derived $I$-complete. For every $n\geq1$, the
projection-formula morphism

$$
 (Rf_*K)\otimes_A^LP_n\longrightarrow Rf_*(K\otimes_A^LP_n)
$$

is a functorial isomorphism

$$
 (Rf_*K)\otimes_A^LP_n
 \xrightarrow{\sim}Rf_*(K\otimes_A^LP_n)=Rf_*K_n,
$$

and these isomorphisms commute with $P_{n+1}\to P_n$. Under them, the
completion map for $Rf_*K$ is the composite

$$
 Rf_*K\xrightarrow{\sim}Rf_*\Rlim K_\bullet
 \xrightarrow{\sim}\Rlim Rf_*^{\operatorname{Tow}}K_\bullet.
$$
