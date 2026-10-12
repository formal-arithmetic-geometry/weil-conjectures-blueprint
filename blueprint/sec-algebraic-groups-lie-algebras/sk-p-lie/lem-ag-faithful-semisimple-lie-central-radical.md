+++
id = "lem-ag-faithful-semisimple-lie-central-radical"
kind = "lemma"
title = "A faithful semisimple Lie representation forces a central radical"
order = 2812
uses = ["def-wf-lie-radical-centre", "lem-ag-central-radical-quotient", "lem-wf-solvable-common-eigenvector", "lem-wf-sum-of-solvable-ideals"]
+++
Let $L$ be a finite-dimensional Lie algebra over
$\overline{\mathbf Q}_\ell$, and let $\rho:L\to\operatorname{End}(V)$ be
a Lie representation on a finite-dimensional vector space $V$, i.e. a
linear map with $\rho([x,y])=\rho(x)\rho(y)-\rho(y)\rho(x)$. Assume that
$\rho$ is faithful ($\ker\rho=0$) and semisimple: $V=\bigoplus_iM_i$ is a
direct sum of nonzero $\rho(L)$-stable subspaces $M_i$, each having no
$\rho(L)$-stable subspaces other than $0$ and $M_i$. Then, in the notation
of [def-wf-lie-radical-centre], $L$ has central radical and

$$
\operatorname{rad}L=Z(L),\qquad L=Z(L)+[L,L],
$$

where the plus sign denotes a sum of subspaces.
