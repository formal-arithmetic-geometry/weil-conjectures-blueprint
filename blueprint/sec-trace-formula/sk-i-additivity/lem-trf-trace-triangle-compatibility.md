+++
id = "lem-trf-trace-triangle-compatibility"
kind = "lemma"
title = "Triangle compatibility of the trace class"
order = 2353
uses = ["d-curve-pieces", "def-trf-correspondence", "def-trf-dualizing-complex", "def-trf-supported-pairing", "def-trf-trace-class", "def-trf-trace-class-source", "def-weil-derived-pullback-tensor-hom", "lem-trf-global-operator-triangulated", "lem-trf-local-term-locality", "lem-trf-trace-class-diagonal-pairing", "prop-trf-trace-formal-laws", "thm-trf-dualizing-complex-composition", "thm-trf-kunneth-verdier"]
+++
Let $c=(c_1,c_2):C\to X\times X$ be an admissible correspondence with
coefficient $K\in D^b_{ctf}(X,A)$ and $u:c_2^*K\to c_1^!K$
([def-trf-correspondence]), with fixed scheme $F$, and let
$i:Z\hookrightarrow X$ be a closed subscheme with open complement
$j:U\hookrightarrow X$ which is *$c$-invariant*: $c_2(c_1^{-1}(Z))\subset Z$
set-theoretically, so that $c_1^{-1}(Z)\subset c_2^{-1}(Z)$ and
$c_2^{-1}(U)\subset c_1^{-1}(U)$. Then $u$ induces coefficient morphisms
$u^U$ on $K'=j_!j^*K$ and $u^Z$ on $K''=Ri_*i^*K$: $u^U=[j]_!(u|_U)$ is
the extension by zero of the restriction of $u$ to the open correspondence
$c|_U$ on $c^{-1}(U\times U)=c_2^{-1}(U)$, and $u^Z=[i]_!(u|_Z)$ is the
pushforward of the restriction of $u$ to the closed correspondence
$c|_Z:c_1^{-1}(Z)_{\mathrm{red}}\to Z\times Z$ (in the Frobenius case
these are the pieces $u^U,u^Z$ of [d-curve-pieces]). The triple
$(u^U,u,u^Z)$ is a morphism of the open–closed triangles
$K'\to K\to K''\to K'[1]$ of the functors $Lc_2^*$ and $Rc_1^!$, and the
Verdier trace classes of [def-trf-trace-class] satisfy

$$
\operatorname{Tr}_c(u)=\operatorname{Tr}_c(u^U)+\operatorname{Tr}_c(u^Z)
$$

in $\operatorname{Hom}_{D(F,A)}(A_F,\omega_{F,A})$.
This is the additivity of the Verdier trace class along a $c$-invariant
open–closed decomposition. It
is *not* asserted for an arbitrary morphism $(u',u,u'')$ of distinguished
triangles in $D^b_{ctf}(X,A)$: for the identity correspondence of a point
that assertion is the additivity of the categorical trace on arbitrary
endomorphisms of distinguished triangles of perfect complexes, which fails
([prop-trf-trace-formal-laws], item (2)).
