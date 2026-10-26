+++
id = "det-base-field-cd-finite-field"
kind = "proposition"
title = "A finite field has cohomological dimension at most one"
order = 2106
uses = ["det-base-field-cd-galois-group", "det-base-field-cd-cochains", "det-base-field-cd-inflation", "lem-exc-field-discrete-modules", "def-sc-etale-torsion-cd", "det-cd-etale-comparison", "lem-sf-separably-closed-torsion-cd"]
+++
Let $K$ be a finite field. Then $H^s(\widehat{\mathbf Z},M)=0$ for every $s\geq2$
and every torsion discrete $\widehat{\mathbf Z}$-module $M$. Consequently
$\operatorname{cd}_{\rm tor}(K)\leq1$ in the sense of [def-sc-etale-torsion-cd],
and $\operatorname{cd}_\ell(K)\leq1$. If $K$ is algebraically closed, then
$\operatorname{cd}_\ell(K)=0$.
