+++
id = "sk-prop-proper-base-change-unbounded"
kind = "proposition"
title = "Proper base change on the localizing categories"
order = 2495
uses = ["sk-def-localizing-closure", "sk-prop-sfb-cartesian-coefficients"]
tags = ["sketch"]
+++
Let $\Lambda$ be admissible. Consider a cartesian square

$$
\begin{array}{ccc}
X'&\xrightarrow{g'}&X\\
\downarrow p'&&\downarrow p\\
Y'&\xrightarrow{g}&Y
\end{array}
$$

with $p$ proper. The base change map $g^*Rp_*K\to Rp'_*g'^*K$ is an isomorphism for every
$K\in\Loc(\Dctf(X,\Lambda))$ ([sk-def-localizing-closure]).

Here the base change map of a commutative square as above is the map $g^*Rp_*\to Rp'_*g'^*$ of functors
$\D(X_{\mathrm{proét}},\Lambda)\to\D(Y'_{\mathrm{proét}},\Lambda)$ obtained by applying the unit of $p'^*\dashv Rp'_*$,
the isomorphism $p'^*g^*\simeq g'^*p^*$, and the counit of $p^*\dashv Rp_*$. By
[sk-prop-sfb-cartesian-coefficients], these inverse images are the exact inverse images of sheaves, so the
adjunctions are the usual ones between the unbounded derived categories.
