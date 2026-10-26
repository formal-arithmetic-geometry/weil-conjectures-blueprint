+++
id = "det-pe-injective-acyclicity-reduction"
kind = "lemma"
title = "Reduction of the acyclicity to affine étale objects"
order = 972
uses = ["def-weil-pbc-site-comparison-morphism", "lem-weil-pbc-comparison-injective-acyclicity", "lem-weil-pbc-etale-restriction-injectives", "lem-weil-pbc-proetale-restriction-injectives", "det-pe-classical-sheaves-modules"]
+++
Let $X$ be a scheme and $\Lambda$ a discrete commutative ring.

1. For every $\Lambda_X$-module sheaf $G$ on $X_{\Proet}$ and every $q\geq0$, the
   sheaf $R^q\nu_{X,*}G$ on $X_{\Et}$ is the sheafification of the presheaf
   $$
   W\longmapsto H^q(W_{\Proet},G|_W)
   $$
   on affine étale $W\to X$. In particular, if $H^q(W_{\Proet},G|_W)=0$ for all
   affine étale $W\to X$, then $R^q\nu_{X,*}G=0$.
2. If $I$ is an injective $\Lambda$-module sheaf on $X_{\Et}$ and $W\to X$ is
   affine and étale, then $(\nu_X^*I)|_W\cong\nu_W^*(I|_W)$, the sheaf $I|_W$ is
   injective on $W_{\Et}$, and $H^q(W_{\Proet},(\nu_X^*I)|_W)=0$ for $q>0$.

Consequently $R^q\nu_{X,*}\nu_X^*I=0$ for $q>0$.
