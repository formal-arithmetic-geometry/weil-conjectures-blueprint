+++
id = "lem-sc-ga-gm-homomorphism"
kind = "lemma"
title = "There is no nontrivial homomorphism $\\mathbf G_a\\to\\mathbf G_m$"
order = 2046
uses = ["def-sc-gm-ga", "lem-sc-laurent-units"]
+++
Let $k$ be a field and let $\psi:\mathbf G_a\to\mathbf G_m$ be a
morphism of $k$-group schemes in the sense of [def-sc-gm-ga].
Then $\psi$ is the constant morphism with value the unit of
$\mathbf G_m$; equivalently, the dual map
$k[t,t^{-1}]\to k[y]$ sends $t$ to $1$.

## Proof

By [def-sc-gm-ga] the map $\psi$ is dual to a $k$-algebra map
$k[t,t^{-1}]\to k[y]$, $t\mapsto\phi(y)$. Since $t$ is a unit,
$\phi$ is a unit of $k[y]$, hence a nonzero constant by
[lem-sc-laurent-units](a); because $\psi$ carries the unit
section to the unit section, $\phi(0)=1$, so $\phi\in k^\times$.
Multiplicativity of $\psi$ gives the identity
$\phi(y+y')=\phi(y)\phi(y')$ in $k[y,y']$. Suppose
$\phi=\sum_{i}a_iy^i$ has degree $d\geq1$. Substituting
$y\mapsto2y$ gives $\phi(2y)=\phi(y)^2$; the right hand side has
degree $2d$ because $k[y]$ is a domain and $a_d^2\neq0$, while
the left hand side has degree $d$ if $2\neq0$ in $k$ and degree
$0$ if $2=0$. In both cases $d=0$, a contradiction.
