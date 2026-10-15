+++
id = "lem-cbc-completed-extension-zero-comparison"
kind = "lemma"
title = "Completed extension-by-zero base change"
order = 1938
uses = ["def-cbc-open-immersion-square", "def-weil-pbc-adic-coefficient-datum", "def-weil-pbc-completed-pullback", "def-weil-pbc-extension-by-zero", "lem-cbc-exact-functor-rlim", "lem-cbc-proetale-extension-zero", "lem-cbc-proetale-extension-zero-base-change", "lemma-weil-pbc-completed-pullback-reduction"]
+++
Let $(A,I)$ satisfy [def-weil-pbc-adic-coefficient-datum], let

$$
\begin{array}{ccc}
U'&\xrightarrow{g_U}&U\\
j'\downarrow&&\downarrow j\\
X'&\xrightarrow{g}&X
\end{array}
$$

be an open-immersion square,
and let $K\in D(U_{\Proet},A)$ be derived $I$-complete. Then the
canonical map

$$
Lg^*_{\mathrm{comp}}j_!K\xrightarrow{\ \sim\ }j'_!Lg_{U,\mathrm{comp}}^*K
$$

is an isomorphism, natural in $K$.
