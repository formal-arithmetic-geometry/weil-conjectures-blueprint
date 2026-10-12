+++
id = "lem-weil-pbc-proper-open-identification"
kind = "lemma"
title = "The specified comparison isomorphism"
order = 1823
uses = ["def-weil-pbc-derived-categories", "def-weil-pbc-direct-image", "def-weil-pbc-extension-by-zero", "def-weil-pbc-proper-open-comparison", "def-weil-pbc-scheme-conventions", "lem-weil-pbc-clopen-section-direct-image", "lem-weil-pbc-derived-open-restriction", "lem-weil-pbc-proper-open-section"]
+++
Let $u:T_1\to T_2$ be proper, let $j_i:X\hookrightarrow T_i$ be
open immersions with $u j_1=j_2$, let $\Lambda$ be a finite ring and
let $K\in D^+(X_{\Et},\Lambda)$, as in
[def-weil-pbc-proper-open-comparison], with $V=T_1\times_{T_2}X$,
projections $b:V\to T_1$, $p:V\to X$ and section $s:X\to V$.
Then restriction of
extension by zero along the
clopen section identifies $b^{-1}j_{1!}K$ with $s_!K$, and
restriction of the
derived direct image identifies
$j_2^{-1}Ru_*j_{1!}K$ with $Rp_*b^{-1}j_{1!}K$; consequently the
composite

$$
\theta_{u,K}:j_2^{-1}Ru_*j_{1!}K\xrightarrow{\sim}K
$$

is a specified isomorphism, namely the one used in
[def-weil-pbc-proper-open-comparison].
