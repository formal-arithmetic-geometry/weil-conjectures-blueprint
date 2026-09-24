+++
id = "thm-trf-trace-proper-compatibility"
kind = "theorem"
title = "Proper global trace comparison; Varshavsky 1.2.5"
order = 3907
uses = ["def-trf-coefficient-pushforward", "def-trf-integration", "def-trf-trace-class", "lem-trf-trace-map-exchange", "lem-trf-trace-source-exchange"]
+++
Let $X$ be proper over $s$, let $K\in D^b_{ctf}(X,A)$, and let
$(C,c,u)$ be a correspondence whose ordinary leg $c_2$ is proper.
In the notation of [def-trf-coefficient-pushforward], the induced
proper map $h:\operatorname{Fix}(c)\to\operatorname{Fix}(b)$ satisfies

$$
h_*\operatorname{Tr}_c(u)
=
\operatorname{Tr}_b\bigl([f,g]_!u\bigr).
$$

## Proof

By [def-trf-trace-class], $\operatorname{Tr}_c(u)$ is the composite
of the mate $\widetilde u$ with the trace map $\mathfrak t_{c,K}$,
restricted to the fixed scheme. Applying the pushforwards, the mate
part is [lem-trf-trace-source-exchange], and the trace-map part is
[lem-trf-trace-map-exchange]; the restriction to the fixed schemes
is compatible with $h$ because $h$ is the base change of $g$ along
the diagonal, and the pushforward along the proper $h$ of the
dualizing data is the integration of [def-trf-integration]. Hence
the equality.
