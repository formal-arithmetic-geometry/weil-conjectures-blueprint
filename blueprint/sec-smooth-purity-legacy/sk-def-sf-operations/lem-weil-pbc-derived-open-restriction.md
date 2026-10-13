+++
id = "lem-weil-pbc-derived-open-restriction"
kind = "lemma"
title = "Derived direct image restricted to an open"
order = 1834
uses = ["def-weil-pbc-cartesian-square", "def-weil-pbc-derived-categories", "def-weil-pbc-direct-image", "def-weil-pbc-extension-by-zero", "def-weil-pbc-inverse-image", "def-weil-pbc-scheme-conventions", "prop-weil-pbc-inverse-image-exact", "prop-weil-pbc-kinjective-resolutions-exist"]
+++
Let $f:T\to S$ be a scheme morphism and
$a:U\hookrightarrow S$ an
open immersion. Put $V=T\times_SU$, with projections
$b:V\hookrightarrow T$ and $f_U:V\to U$.
For a finite ring $\Lambda$ and
$L\in\hyperref[def-weil-pbc-derived-categories]{D^+(T_{\Et},\Lambda)}$,
restriction gives a natural isomorphism

$$
a^{-1}Rf_*L \xrightarrow{\sim} Rf_{U,*}b^{-1}L,
$$

using the
derived direct image and
inverse image functors.
