+++
id = "lem-pur-kummer-coefficient-base-change"
kind = "lemma"
title = "Base change of the Kummer coefficients"
order = 2933
uses = ["def-coefficient-twists-detailed", "def-pur-conventions", "def-sbc-smooth-morphisms", "def-sc-curves", "def-weil-pbc-etale-sheaves", "def-weil-pbc-proetale-site", "def-weil-scheme-morphism-properties", "lem-pur-finite-kummer-level"]
+++
Fix the finite-field datum of [def-pur-conventions], let $k$ be
algebraically closed, let $N\geq1$, and let $A$ be a finite
$\mathbf Z/\ell^N\mathbf Z$-module which is free of finite rank (for
instance $A=A_{E,n}$ with $N=n\cdot v_\ell(\pi_E)$ under the
hypothesis $e(E/\Ql)\mid n$ of [lem-pur-finite-kummer-level]). For every
smooth separated curve $C$ over $k$ and every
integer $q\geq0$, the natural map

$$
H^q(C_{\Et},\mu_{\ell^N})\otimes_{\mathbf Z/\ell^N}A
\longrightarrow
H^q(C_{\Et},\mu_{\ell^N}\otimes_{\mathbf Z/\ell^N}A)
$$

is an isomorphism, compatibly with the Kummer boundary maps of the Kummer
sequence with $A$-coefficients.
