+++
id = "lem-cbc-proetale-extension-zero-base-change"
kind = "lemma"
title = "Pro-etale extension-by-zero base change"
order = 1930
uses = ["def-cbc-open-immersion-square", "def-weil-pbc-inverse-image", "lem-cbc-proetale-extension-zero"]
+++
Let

$$
\begin{array}{ccc}
U'&\xrightarrow{g_U}&U\\
j'\downarrow&&\downarrow j\\
X'&\xrightarrow{g}&X
\end{array}
$$

be an open-immersion square
and let $\Lambda$ be a finite commutative ring. For every complex
$K$ of $\Lambda$-module sheaves on $U_{\Proet}$ the canonical map

$$
g^{-1}j_!K\xrightarrow{\ \sim\ }j'_!g_U^{-1}K
$$

is an isomorphism, natural in $K$; here all functors are the
pro-etale ones of [lem-cbc-proetale-extension-zero].
