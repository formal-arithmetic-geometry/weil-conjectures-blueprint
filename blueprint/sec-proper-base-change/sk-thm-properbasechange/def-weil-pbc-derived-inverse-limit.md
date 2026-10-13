+++
id = "def-weil-pbc-derived-inverse-limit"
kind = "definition"
title = "Sequential derived inverse limit"
order = 1308
uses = ["def-weil-derived-limit", "def-weil-pbc-adic-coefficient-datum", "def-weil-pbc-kinjective-resolutions"]
+++
Let $\operatorname{Tow}_{A}(T)$ be the tower category of
[def-weil-pbc-adic-coefficient-datum], with its evaluation functors
$\operatorname{ev}_n$, and let $M_\bullet\in
D(\operatorname{Tow}_{A}(T))$. The evaluations $\operatorname{ev}_nM_\bullet$,
together with the transition maps they carry, exhibit
$(\operatorname{ev}_nM_\bullet)_{n\geq1}$ as an inverse system in the single
triangulated category $D(T_{\Proet},A)$. Its *sequential derived inverse
limit*

$$
 \Rlim M_\bullet
$$

is its derived limit in the sense of the conventions chapter; it is defined
by the Roos triangle applied to $(\operatorname{ev}_nM_\bullet)$. The derived
product $R\!\prod_nM_n$ is the product in $D(T_{\Proet},A)$, computed
termwise (in the derived category of an abelian category with exact
countable products, countable products exist and are represented by
termwise products of any representatives, with
$H^p(\prod_iK_i)=\prod_iH^p(K_i)$).
