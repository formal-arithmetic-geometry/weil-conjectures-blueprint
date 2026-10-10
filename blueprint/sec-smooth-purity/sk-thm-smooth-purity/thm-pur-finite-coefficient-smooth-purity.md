+++
id = "thm-pur-finite-coefficient-smooth-purity"
kind = "theorem"
title = "Finite-coefficient smooth purity"
order = 2014
uses = ["cor-sf-ambient-adjoint-discharge", "def-coefficient-twists-detailed", "def-compact-support-direct-image-detailed", "def-pur-conventions", "def-pur-smooth-purity-map", "def-sbc-smooth-morphisms", "def-weil-ambient-exceptional-adjoint", "def-weil-derived-pullback-tensor-hom", "def-weil-exceptional-inverse-image", "def-weil-finite-tor-amplitude", "def-weil-finite-torsion-constructibility", "def-weil-pbc-proetale-site", "def-weil-scheme-morphism-properties", "thm-pur-cohomological-smoothness", "thm-pur-diagonal-dualizing-object"]
+++
Fix the purity conventions with its
explicit ingredients: the global finite-field datum $(p,a,q,k_0,k)$,
the prime $\ell\neq p$, the finite extension $E/\Ql$ with valuation
ring $\mathcal O_E$ and uniformizer $\varpi_E$, the integer
$n\geq1$, and the finite coefficient ring
$A=A_{E,n}=\mathcal O_E/\varpi_E^n$; on the
small pro-etale site of a
$k$-scheme $T$, let $D^b_{ctf}(T,\Lambda)$ be the bounded
[def-weil-finite-torsion-constructibility] constructible
finite-Tor category for
$\Lambda=A$, with the
derived pullback,
tensor, and internal Hom, the
compact-support direct
image $Rf_!$, and the
exceptional inverse image
$Rf^!$ of the operations (on this coefficient class the ambient
exceptional right adjoint datum of [def-weil-ambient-exceptional-adjoint]
is supplied by [cor-sf-ambient-adjoint-discharge]), and let
$K(m)=K\otimes^L_{\Lambda_T}\Lambda(m)$
be the coefficient twist of degree
$m\in\mathbf Z$. Let $f:X\to Y$ be a
smooth – i.e. locally of finite
presentation, flat, with regular geometric fibers (equivalently a
formally smooth morphism of finite type) – separated morphism of
relative dimension $d\in\mathbf Z_{\geq0}$ of
separated finite-type
$k$-schemes, and let $K\in D^b_{ctf}(Y,\Lambda)$. The
smooth purity map

$$
\gamma_{f,K}:Lf^*K(d)[2d]\longrightarrow Rf^!K
$$

of [def-pur-smooth-purity-map] is an isomorphism.
