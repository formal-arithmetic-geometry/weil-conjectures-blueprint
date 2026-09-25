+++
id = "sbc-lem-stability-and-locality"
kind = "lemma"
title = "Stability and locality of local acyclicity"
order = 1456
uses = ["def-sbc-smooth-morphisms", "sbc-def-local-acyclicity", "sbc-def-milnor-tube", "sbc-def-strict-localization", "sbc-def-universal-local-acyclicity"]
+++
The following hold.

1. The universal versions of local acyclicity are stable under
arbitrary base change, by [sbc-def-universal-local-acyclicity].
1. Local acyclicity is local for the etale topology on source and
target: if $\{U_i\to X\}$ is an etale covering, $f$ is locally
acyclic relative to $K$ if and only if each $f_i:U_i\to S$ is
locally acyclic relative to $K|_{U_i}$ (the
strict localizations and
Milnor tubes are etale-local
constructs).
1. A composition of universally locally acyclic morphisms is
universally locally acyclic: for $g:X\to Y$ and $h:Y\to Z$, the
specialization map for $h\circ g$ at $\bar x$ is the composite of
the specialization map for $g$ at $\bar x$ with that for $h$ at
the image of $\bar x$, after the base change by the geometric
point of $Z_{(h(g(\bar x)))}$ (Leray factorization of the two
Milnor tubes).
1. An etale morphism is
universally locally acyclic, by [sbc-def-milnor-tube]: every
Milnor tube of an etale morphism is a geometric point.

## Proof

(1) is [sbc-def-universal-local-acyclicity] (1) and (3) read as
definitions: the base change of a base change is a base change, and the
locally acyclic property of the new base change is the property of the
original one. (2): by [sbc-def-strict-localization] the strict
localizations of $X$ at the geometric points of the $U_i$ are the
strict localizations of the $U_i$, and by [sbc-def-milnor-tube]
the Milnor tube of $f$ at $\bar x\in X$ is the Milnor tube of $f_i$ at
a lift; hence the condition of [sbc-def-local-acyclicity] (1) is
etale-local. (3): for
$\bar x\xrightarrow{}\bar y\xrightarrow{}\bar z$ and a geometric point
$\bar t\to Z_{(\bar z)}$, the Milnor tube of $h\circ g$ at $\bar x$ is
the fibre product of the Milnor tube of $g$ at $\bar x$ over
$Y_{(\bar y)}$ with the Milnor tube of $h$ at $\bar y$; the Leray
spectral sequence for the projection of this fibre product shows that
the specialization map for $h\circ g$ is the composite of the two
specialization maps, so isomorphisms for $g$ and $h$ give one for
$h\circ g$, and universality is preserved. (4): for etale $f$ the
schemes $X_{(\bar x)}\to S_{(\bar s)}$ in
[sbc-def-strict-localization] are isomorphisms, so the Milnor tube
$F_{\bar x,\bar t}=\bar t$ of [sbc-def-milnor-tube] is a geometric
point and the specialization map of the constant sheaf is an
isomorphism by [sbc-def-local-acyclicity] (1).
