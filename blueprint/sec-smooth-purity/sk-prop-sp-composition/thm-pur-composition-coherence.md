+++
id = "thm-pur-composition-coherence"
kind = "theorem"
title = "Composition coherence"
order = 2360
uses = ["cor-pur-vector-bundle-purity", "def-coefficient-twists-detailed", "def-pur-conventions", "def-sbc-smooth-morphisms", "def-weil-exceptional-inverse-image", "def-weil-pbc-proetale-site", "def-weil-scheme-morphism-properties", "lem-pur-diagonal-base-change", "sbc-thm-etale-local-normal-form", "thm-pur-cohomological-smoothness", "thm-pur-diagonal-dualizing-object", "thm-pur-dnc-invariance"]
+++
Work in the purity conventions of [def-pur-conventions], with the
global finite-field datum $(p,a,q,k_0,k)$
with $q=p^a$, the prime $\ell\neq p$, the finite extension
$E/\Ql$ with valuation ring $\mathcal O_E$ and uniformizer
$\pi_E$, the level $n\geq1$, and the finite coefficient ring
$A=A_{E,n}=\mathcal O_E/\pi_E^n$; let
$f:X\to Y$ and $g:Y\to Z$ be smooth separated
morphisms of relative dimensions $d$ and $e$. Under the canonical
identification

$$
L(gf)^*(-)(d+e)[2d+2e]
\cong Lf^*Lg^*(-)(d)[2d](e)[2e],
$$

the smooth purity map $\gamma_{gf,K}$ equals the composite

$$
\begin{array}{l}
L(gf)^*K(d+e)[2d+2e]
\xrightarrow{\ Lf^*(\gamma_{g,K})(d)[2d]\ }
Lf^*Rg^!K(d)[2d]
\xrightarrow{\ \gamma_{f,Rg^!K}\ }
Rf^!Rg^!K\\
\hphantom{L(gf)^*K(d+e)[2d+2e]}
\xrightarrow{\ c_{g,f}^{-1}\ }R(gf)^!K,
\end{array}
$$

where $c_{g,f}:R(gf)^!\cong Rf^!Rg^!$ is the composition isomorphism for
the exceptional inverse image.
