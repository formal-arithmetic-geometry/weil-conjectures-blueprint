+++
id = "det-pe-unbounded-classical-truncation"
kind = "lemma"
title = "Fixed-degree truncation for pro-étale sections"
order = 2112
uses = ["sk-prop-pe-left-complete", "sk-prop-pe-milnor", "sk-def-pe-classical-definition"]
+++
Let $X$ be a scheme, $A$ a finite ring, $W$ an object of $X_{\Proet}$ and $e\geq0$
an integer such that $H^q(W,H)=0$ for all $q>e$ and every classical $A$-module
sheaf $H$ on $X_{\Proet}$.

1. If $L\in D(X_{\Proet},A)$ has classical cohomology sheaves and $H^q(L)=0$ for
   $q>b$, then $H^mR\Gamma(W,L)=0$ for $m>b+e+1$.
2. If $K\in D(X_{\Proet},A)$ has classical cohomology sheaves and $m,N$ are
   integers with $N<m-e-1$, then
   $H^mR\Gamma(W,K)\to H^mR\Gamma(W,\tau_{\geq N}K)$ is an isomorphism.
