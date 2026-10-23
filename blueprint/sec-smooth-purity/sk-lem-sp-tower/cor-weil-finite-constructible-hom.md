+++
id = "cor-weil-finite-constructible-hom"
kind = "theorem"
title = "Internal Hom for arbitrary finite-stage constructible complexes"
lean = ["AlgebraicGeometry.Etale.constructibleFiniteTor_derivedHom_of_isSeparated"]
order = 2992
tags = ["latex:corollary"]
uses = ["def-weil-derived-pullback-tensor-hom", "lem-sf-tensor-ctf", "lem-weil-finite-duality-site-comparison", "lem-weil-verdier-preservation-strata", "thm-fix-general-biduality"]
+++
Let $\dim X\leq d$, and let $K,L\in D^b_{ctf}(X,A_{E,n})$,
on the etale or pro-etale site over $\overline{\mathbf F}_q$.
Then $R\mathcal Hom_A(K,L)$ is bounded constructible of finite
Tor amplitude. If the Tor intervals of $K,L$ are respectively
$[a,b]$, $[c,e]$, one valid interval for this internal Hom is
$[c-b-2d,e-a+2d]$.
