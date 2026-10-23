+++
id = "sk-prop-proper-base-change-unbounded"
kind = "proposition"
title = "Proper base change on the localizing categories"
order = 2269
uses = ["sk-prop-proper-image-localizing", "sk-lem-sf-determination", "sk-prop-sfb-cartesian-coefficients"]
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

with $p$ proper. The base change map $g^*Rp_*K\to Rp'_*g'^*K$ in $\D(Y'_{\mathrm{proét}},\Lambda)$ is an
isomorphism for every $K\in\Loc(\Dctf(X,\Lambda))$.

Here the base change map is the natural transformation of functors
$\D(X_{\mathrm{proét}},\Lambda)\to\D(Y'_{\mathrm{proét}},\Lambda)$ obtained by applying the unit of $p'^*\dashv Rp'_*$,
the isomorphism $p'^*g^*\simeq g'^*p^*$, and the counit of $p^*\dashv Rp_*$; the inverse images are the
exact inverse images of sheaves ([sk-prop-sfb-cartesian-coefficients]).
