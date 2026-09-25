+++
id = "lem-sf-lift-free-tower"
kind = "lemma"
title = "Lifting a compatible tower of minimal models"
order = 2323
uses = ["lem-sf-minimal-free-model"]
+++
For $n\geq1$ let $F_n$ be a bounded complex of finite free
$A_{E,n}$-modules, all of them concentrated in the same degrees $[a,b]$,
with isomorphisms $F_{n+1}\otimes^L_{A_{E,n+1}}A_{E,n}\cong F_n$ in
$D(A_{E,n})$, and assume that each $F_n$ is minimal in the sense of
[lem-sf-minimal-free-model], that is,
$\operatorname{rank}_{A_{E,n}}F_n^q =\dim_{\kappa_E}H^q(F_n\otimes^L_{A_{E,n}}\kappa_E)$ for every $q$. Then
the ranks $\operatorname{rank}_{A_{E,n}}F_n^q$ are independent of $n$,
the identifications $F_n^q\cong A_{E,n}^{r^q}$ can be chosen so that the
given isomorphisms are the reduction maps, and there is a bounded complex
$F$ of finite free $\mathcal O_E$-modules with
$F^q\cong\mathcal O_E^{r^q}$ for $q\in[a,b]$, $F^q=0$ otherwise, and
$F\otimes^L_{\mathcal O_E}A_{E,n}\cong F_n$ for every $n$.

## Proof

*Auxiliary fact.* Let $F$, $G$ be minimal bounded complexes of
finite free $A_{E,n}$-modules, concentrated in $[a,b]$, with
$\operatorname{rank}F^q=\operatorname{rank}G^q$ for every $q$, and
suppose $F\cong G$ in $D(A_{E,n})$. Then $F\cong G$ as complexes.
Indeed, both are bounded complexes of free modules, hence K-projective, so
the isomorphism in the derived category is realised by a quasi-isomorphism
$f:F\to G$; reducing modulo $\varpi_E$, the differentials vanish by
minimality and $f\otimes\kappa_E$ is a quasi-isomorphism between
complexes with zero differentials, that is, an isomorphism of complexes, so
every matrix $f^q\otimes\kappa_E$ is invertible; by Nakayama's lemma every
$f^q$ is invertible over $A_{E,n}$, and $f$ is an isomorphism of
complexes.
*Ranks.* The reduction $F_{n+1}\otimes_{A_{E,n+1}}A_{E,n}$ is a
complex of finite free $A_{E,n}$-modules with the ranks of $F_{n+1}$,
its differentials are the reductions of matrices with entries in
$(\varpi_E)$ and therefore also have entries in $(\varpi_E)$, so it is
minimal. It is isomorphic in $D(A_{E,n})$ to $F_n$ by hypothesis, and
both have the same ranks by minimality and the hypothesis
$\operatorname{rank}F_n^q =\dim_{\kappa_E}H^q(F_n\otimes^L\kappa_E)$, the right-hand side being
unchanged by reduction in the derived category. The auxiliary fact
therefore applies: the given isomorphisms may be replaced by isomorphisms of
complexes, and the ranks $r^q$ are independent of $n$.
*Compatible bases.* Choose a basis of $F_1^q$. Given a basis of
$F_n^q$, the reduction map $F_{n+1}^q\to F_{n+1}^q\otimes_{A_{E,n+1}} A_{E,n}\cong F_n^q$ is surjective onto a free $A_{E,n}$-module of rank
$r^q$, so a basis of $F_n^q$ lifts to $r^q$ elements of $F_{n+1}^q$
generating it by Nakayama's lemma, that is, to a basis; this gives
identifications $F_n^q\cong A_{E,n}^{r^q}$, recursively for all $n$, for
which the transition maps are the reductions.
*The lift.* With these identifications the entries of the
differentials $d_n^q:A_{E,n}^{r^q}\to A_{E,n}^{r^{q+1}}$ satisfy
$d_{n+1}^q\equiv d_n^q\bmod\varpi_E^n$, so they define an element
$d^q\in M_{r^q\times r^{q+1}}(\varprojlim_nA_{E,n}) =M_{r^q\times r^{q+1}}(\mathcal O_E)$. Put $F^q=\mathcal O_E^{r^q}$ for
$q\in[a,b]$, $F^q=0$ otherwise, and let $d^q$ be the differentials:
this is a bounded complex $F$ of finite free $\mathcal O_E$-modules
concentrated in $[a,b]$. A bounded complex of free modules is K-flat, so
$F\otimes^L_{\mathcal O_E}A_{E,n}=F\otimes_{\mathcal O_E}A_{E,n}$, and
reducing the matrices $d^q$ modulo $\varpi_E^n$ gives exactly
$d_n^q$; hence $F\otimes^L_{\mathcal O_E}A_{E,n}\cong F_n$.
