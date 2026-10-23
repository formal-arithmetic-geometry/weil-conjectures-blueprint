+++
id = "lem-weil-pbc-etale-pointed-map-rigidity"
kind = "lemma"
title = "Rigidity of maps from a local spectrum to an etale scheme"
uses = ["def-pc-scheme"]
lean = ["AlgebraicGeometry.etalePointedMapRigidity"]
order = 1737
+++
Let $B$ be a commutative local ring, $\Omega$ a field, and $\beta:B\to\Omega$ a local ring map. Let $f:X\to S$ be an etale morphism of schemes [def-pc-scheme]. If $u,v:\operatorname{Spec}B\to X$ satisfy $f\circ u=f\circ v$ and $u\circ\operatorname{Spec}\beta=v\circ\operatorname{Spec}\beta$, then $u=v$. Henselianity of $B$, algebraic closure of $\Omega$, and locality of $u$ and $v$ are not assumed.
