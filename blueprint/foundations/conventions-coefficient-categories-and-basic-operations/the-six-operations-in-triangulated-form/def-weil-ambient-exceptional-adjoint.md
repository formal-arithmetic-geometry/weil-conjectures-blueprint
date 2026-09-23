+++
id = "def-weil-ambient-exceptional-adjoint"
kind = "definition"
title = "Ambient exceptional right adjoint datum"
order = 1396
uses = ["def-compact-support-direct-image-detailed", "def-weil-compactifications-refinements", "def-weil-exceptional-adjoint-admissibility", "def-weil-full-cohomological-dimension", "def-weil-scheme-morphism-properties", "def-weil-small-proetale-site-detailed"]
+++
Fix a prime $\ell$, a finite extension $E/\Ql$, an integer $n\in\mathbf
Z_{\geq1}$, and put $A=A_{E,n}$. Let $S$ be a scheme on which $\ell$ is
invertible, let $X,Y$ be finite-type
[def-weil-scheme-morphism-properties] $S$-schemes, and let $f:X\to Y$ be a
separated finite-type $S$-morphism, with a compactification
[def-weil-compactifications-refinements] $X\xrightarrow{j}\overline
X\xrightarrow{p}Y$. Say that $f$ carries the *ambient exceptional right
adjoint datum at $A$* if clause (1) of
[def-weil-exceptional-adjoint-admissibility] holds: the full
cohomological-dimension condition [def-weil-full-cohomological-dimension]
$\operatorname{FullCD}(p,A;c_{\mathrm{cd}})$ holds for some
$c_{\mathrm{cd}}\in\mathbf Z_{\geq0}$, the compact-support direct image
[def-compact-support-direct-image-detailed] $Rf_{!,n}$ has a right adjoint
$Rf_n^{\times}$ on the *ordinary* derived categories of the small pro-etale
sites [def-weil-small-proetale-site-detailed],

$$
 \operatorname{Hom}_Y\bigl(Rf_{!,n}K,L\bigr)\cong
 \operatorname{Hom}_X\bigl(K,Rf_n^{\times}L\bigr),
$$

and for every refinement of the compactification the units, counits and
comparison maps agree. This datum asserts the *existence* of the ambient
right adjoint and nothing about its values; it says nothing about
constructibility or finite Tor amplitude.
