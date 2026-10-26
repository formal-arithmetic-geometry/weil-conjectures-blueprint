+++
id = "lem-wft-fourier-weil"
kind = "lemma"
title = "The Fourier transform of a Weil complex"
order = 3963
uses = ["sk-def-sf-weil-complexes", "def-fd-kernel", "def-fd-transform", "lem-fd-stalk-formula", "lem-fd-base-change", "prop-base-linear", "lem-fd-inversion", "lem-fd-first-formula", "prop-pur-weil-equivariance-compatibilities", "thm-pur-vector-bundle-thom", "lem-wft-as-unit-trivialization"]
+++
Let $S_0$ be a separated finite-type $k_0$-scheme, $V_0\to S_0$ a vector
bundle of rank $r$, and $V\to S$ its base change to $k$. For a Weil complex
$(K,\phi)$ on $V$ ([sk-def-sf-weil-complexes]), $\operatorname{FT}_\psi(K)$
carries a canonical Weil structure, functorial in $(K,\phi)$, and the
isomorphisms of [lem-fd-base-change] (for base changes defined over $k_0$),
[prop-base-linear], [lem-fd-stalk-formula] (at the geometric points over
$\mathbf F_{q^n}$-points, with the local Frobenius operators), [lem-fd-inversion]
and [lem-fd-first-formula] (for $S_0=\operatorname{Spec}k_0$) are
isomorphisms of Weil complexes, the Tate twists carrying their standard Weil
structures.
