+++
id = "det-pe-hypercover-complex"
kind = "lemma"
title = "Cohomology via a weakly contractible hypercover"
uses = ["det-pe-hypercover-existence", "det-pe-wc-sections-exact", "det-pe-wc-sections-derived"]
+++
Let $W_\bullet\to U$ be a hypercovering with every $W_r$ weakly contractible
([det-pe-hypercover-existence]), and let $K^\bullet$ be a complex of $\mathcal R$-modules
with $K^b=0$ for $b<a$. Let $C^{r,b}=K^b(W_r)$ with horizontal differential
$\delta=\sum_{i=0}^{r+1}(-1)^id_i^*\colon C^{r,b}\to C^{r+1,b}$ and vertical differential
$(-1)^rd_K\colon C^{r,b}\to C^{r,b+1}$, and let $\operatorname{Tot}(C)^q=
\bigoplus_{r+b=q}C^{r,b}=\bigoplus_{0\leq r\leq q-a}K^{q-r}(W_r)$. Then there is an
isomorphism $R\Gamma(U,K^\bullet)\simeq\operatorname{Tot}(C)$ in the derived category of
abelian groups, natural in $K^\bullet$.
