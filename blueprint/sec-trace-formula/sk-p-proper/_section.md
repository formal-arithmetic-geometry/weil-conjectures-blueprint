+++
id = "sk-p-proper"
kind = "proposition"
title = "Proper pushforward compatibility"
order = 2673
uses = ["sk-d-corr", "sk-d-integral", "sk-d-proper-pushforward", "sk-d-trace-class", "sk-def-sf-kv-maps", "sk-p-pairing", "sk-thm-sf-comp-composition", "sk-thm-sf-kunneth-verdier", "sk-thm-sf-package"]
lean = ["AlgebraicGeometry.ProEtale.GeometricOperations.borelMoorePushforward_traceClass"]
tags = ["sketch"]
+++
Let $s$ be the spectrum of a field, $X$ quasi-compact and compactifiable over
$s$, $K\in D^b_{ctf}(X,A)$, let $(C,c,u)$ be an endocorrespondence on $(X,K)$ and
let $(f,g):(C,c)\to(D,b)$ be a
proper pushforward diagram, with
$f:X\to Y$ and $g:C\to D$ proper, $Y$ quasi-compact and compactifiable over $s$,
and $b_i g=fc_i$ for $i=1,2$.
Put $F_c=\Fix(c)$, $F_b=\Fix(b)$, and let $h:F_c\to F_b$ be the induced map;
assume $h$ is proper.
Then the trace classes satisfy

$$
\boxed{h_*\Tr_c(u)=\Tr_b([f,g]_!u)}
\quad\text{in }\operatorname{Hom}(A_{F_b},\omega_{F_b}),
$$

where $h_*$ is Borel–Moore pushforward and $\Tr_b$ is taken for $Rf_*K\in D^b_{ctf}(Y,A)$.
No properness over $s$ of $X,Y,C,D$ and no Cartesian leg square are required.
