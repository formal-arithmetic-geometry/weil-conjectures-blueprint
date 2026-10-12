+++
id = "thm-trf-trace-proper-compatibility"
kind = "theorem"
title = "Proper global trace comparison; Varshavsky 1.2.5"
order = 2670
uses = ["def-trf-borel-moore-pushforward", "def-trf-coefficient-pushforward", "def-trf-kernel-pushforward-maps", "def-trf-trace-class", "fix-prop-adjunctions", "lem-trf-fixed-map-proper", "lem-trf-trace-map-exchange", "lem-trf-trace-map-from-external-duality", "lem-trf-trace-source-exchange", "prop-trf-pairing-point-normalization", "thm-sf-comp-composition"]
+++
Let $(C,c,u)$ be an admissible correspondence on $(X,K)$, with
$K\in D^b_{ctf}(X,A)$, and let $(f,g):(C,c)\to(D,b)$ be a proper pushforward
diagram of [def-trf-coefficient-pushforward]: $f:X\to Y$ and $g:C\to D$ are
proper and $b_ig=fc_i$ for $i=1,2$. Assume the exceptional admissibility of
[def-trf-kernel-pushforward-maps]. Let
$h:F_c=\operatorname{Fix}(c)\to F_b=\operatorname{Fix}(b)$ be the induced
map, proper by [lem-trf-fixed-map-proper]. Then

$$
h_*\operatorname{Tr}_c(u)
=
\operatorname{Tr}_b\bigl([f,g]_!u\bigr)
\qquad\text{in }\operatorname{Hom}(A_{F_b},\omega_{F_b}),
$$

where $\operatorname{Tr}$ is the trace class of [def-trf-trace-class] and
$h_*$ is the Borel–Moore pushforward of [def-trf-borel-moore-pushforward].
No properness over $s$ of $X,Y,C,D$ and no Cartesian leg square is
required.
