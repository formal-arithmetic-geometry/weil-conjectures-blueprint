+++
id = "sk-lem-sbc-exchange-compatibility"
kind = "lemma"
title = "Naturality, pasting and comparison"
order = 2028
uses = ["sk-def-exchange", "sk-thm-pe-direct-image-comparison"]
tags = ["sketch"]
+++
Consider a cartesian square

$$
\begin{array}{ccc}
X' & \xrightarrow{\ u\ } & X\\
{\scriptstyle f'}\downarrow & & \downarrow{\scriptstyle f}\\
Y' & \xrightarrow{\ g\ } & Y,
\end{array}
\tag{1}
$$

let $\Lambda$ be one of the coefficient rings of these notes, and recall that every inverse
image is the exact inverse image for the pulled-back coefficient ring. For
$K\in D(X_{\mathrm{pro\acute et}},\Lambda)$ the *exchange map* is the morphism in
$D(Y'_{\mathrm{pro\acute et}},\Lambda)$

$$
\operatorname{Ex}_{g,f}(K):g^*Rf_*K\longrightarrow Rf'_*u^*K
\tag{2}
$$

defined as the adjoint transpose, for $f'^*\dashv Rf'_*$, of the composite
$f'^*g^*Rf_*K\simeq u^*f^*Rf_*K\xrightarrow{u^*\epsilon_f}u^*K$, where $\epsilon_f$ is the
counit of $f^*\dashv Rf_*$; it is the pro-étale form of the exchange map of
[sk-def-exchange].

The maps (2) form a natural transformation
$g^*Rf_*\to Rf'_*u^*$ of functors
$D(X_{\mathrm{pro\acute et}},\Lambda)\to D(Y'_{\mathrm{pro\acute et}},\Lambda)$. It respects
composition of cartesian squares and is the identity for an identity
square. For a discrete ring $\Lambda$ and $K\in D^+(X_{\mathrm{\acute et}},\Lambda)$,
with $f$ and $f'$ qcqs, the comparison isomorphisms of
[sk-thm-pe-direct-image-comparison] identify the exchange map of
$\nu_X^*K$ with the inverse image on $Y'_{\mathrm{pro\acute et}}$ of the étale
exchange map of $K$. For a coefficient map $\Lambda\to\Lambda'$ of
Proposition [sk-prop-scalar-six] and $K\in\Dctf(X,\Lambda)$, the scalar
comparisons of that proposition identify the scalar extension of
(2) with the exchange map for $K_{\Lambda'}$ in
$\Dctf(Y',\Lambda')$.
