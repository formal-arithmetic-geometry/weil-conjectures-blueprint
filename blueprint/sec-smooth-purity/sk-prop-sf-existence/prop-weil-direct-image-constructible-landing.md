+++
id = "prop-weil-direct-image-constructible-landing"
kind = "theorem"
title = "Derived direct image on the constructible categories"
order = 1858
tags = ["latex:proposition"]
uses = ["def-weil-algebraically-closed-coefficients", "def-weil-derived-complete-integral-detailed", "def-weil-derived-direct-image", "def-weil-finite-field-fiber", "def-weil-finite-torsion-constructibility", "def-weil-pbc-proetale-site", "def-weil-rationalization-karoubi", "def-weil-scheme-morphism-properties", "prop-weil-pbc-direct-image-limits", "prop-weil-proper-direct-image-boundedness", "prop-weil-proper-direct-image-constructibility"]
+++
Fix the global finite-field datum
$(p,a,q,k_0,k)$, choose a prime $\ell\neq p$, write
$\Ql=\mathbf Q_\ell$, and choose an algebraic closure $\Qlb$ of
$\Ql$. Let $E/\Ql$ be finite with valuation ring $\mathcal O_E$ and
a uniformizer $\varpi_E$, put
$A_{E,n}=\mathcal O_E/\varpi_E^n$, and let $S$ be a scheme on which
$\ell$ is invertible. Let $X,Y$ be
finite-type $S$-schemes and
let $f:X\to Y$ be a
proper $S$-morphism. At
each coefficient level $\Lambda\in\{A_{E,n},\mathcal O_E,E,\Qlb\}$, on
the small pro-etale sites, where
the $E$-coefficient category is the
rationalized
category and the $\Qlb$-coefficient category is the
common-stage
algebraically closed category,

$$
Rf_*:D^b_c(X,\Lambda)\longrightarrow D^b_c(Y,\Lambda)
$$

is a well-defined exact triangulated functor.

## Proof

At the finite level $\Lambda=A_{E,n}$, the boundedness and
constructibility of the proper direct image are
[prop-weil-proper-direct-image-boundedness] and
[prop-weil-proper-direct-image-constructibility], which give
$Rf_*K\in D^b_c(Y,A_{E,n})$ for every
$K\in D^b_c(X,A_{E,n})$; exactness is that of the ambient $Rf_*$ of
[def-weil-derived-direct-image]. For $\Lambda=\mathcal O_E$,
the direct image is the derived inverse limit of the finite-level
images of [def-weil-derived-direct-image]; the reductions $K_n$
share the cohomological interval of $K$ by
[def-weil-derived-complete-integral-detailed], the finite-level interval
expansion of [prop-weil-proper-direct-image-boundedness] is
uniform in $n$, and
[prop-weil-pbc-direct-image-limits] of the ambient-foundations chapter identifies the
derived limit with the finite-level outputs, so
$Rf_*K\in D^b_c(Y,\mathcal O_E)$. For $\Lambda=E$ and
$\Lambda=\Qlb$, the functor is the rationalized
and, respectively, the common-stage extension of the integral one,
exact and triangulated by
[def-weil-rationalization-karoubi] and
[def-weil-algebraically-closed-coefficients].
