+++
id = "lem-sf-minimal-free-model"
kind = "lemma"
title = "Minimal free models and their ranks"
order = 2338
+++
Let $A=A_{E,n}$, with maximal ideal $(\varpi_E)$ and residue field
$\kappa_E=A/(\varpi_E)$, and let $G$ be a bounded complex of finite free
$A$-modules with $G^q=0$ for $q\notin[a,b]$. Then $G$ is isomorphic,
as a complex of $A$-modules, to a direct sum $F\oplus T$ in which
$T$ is a direct sum of complexes $A\xrightarrow{\ 1\ }A$ concentrated in
two adjacent degrees and every differential of $F$ has all of its entries
in $\varpi_EA$. For every such $F$ one has $F\cong G$ in $D(A)$,
$F^q=0$ for $q\notin[a,b]$, and

$$
\operatorname{rank}_AF^q
=\dim_{\kappa_E}H^q\bigl(G\otimes^L_A\kappa_E\bigr)
\qquad(q\in\mathbf Z).
$$

## Proof

*The splitting.* Suppose that the differential $d^q:G^q\to G^{q+1}$
has a unit among the entries of its matrix. Over the local ring $A$ the
matrix of $d^q$ can be brought into the block form
$\left(\begin{smallmatrix}1&0\\0&M'\end{smallmatrix}\right)$ by elementary
row and column operations with unit pivots, that is, by a change of bases of
the free modules $G^q$ and $G^{q+1}$. With respect to such bases the
complex $G$ is the direct sum of the two-term complex
$A\xrightarrow{1}A$ in degrees $q,q+1$ and of the complex $G'$ obtained
from $G$ by deleting one basis element in each of the degrees $q$ and
$q+1$, all other differentials being unchanged; the new differentials
still have their entries in $A$, and the new top and bottom degrees are
still $[a,b]$. The total rank $\sum_q\operatorname{rank}_AG^q$ drops, so
iterating terminates, and the remaining complex $F$ has no unit entry in
any differential, that is, all entries lie in the maximal ideal
$(\varpi_E)$. This is the displayed decomposition.
*The ranks.* The summands $A\xrightarrow{1}A$ are acyclic complexes
of free modules, so $F\cong G$ in $D(A)$, and $F^q=0$ for
$q\notin[a,b]$ because the splitting adds and removes terms only inside
that interval. As all entries of the differentials of $F$ lie in
$(\varpi_E)$, the differentials of the complex
$F\otimes_A\kappa_E$ vanish and
$H^q(F\otimes_A\kappa_E)=F^q\otimes_A\kappa_E$, of
$\kappa_E$-dimension $\operatorname{rank}_AF^q$. The complex $F$
consists of free modules, hence is K-flat, so
$F\otimes^L_A\kappa_E=F\otimes_A\kappa_E$, and $F\cong G$ in $D(A)$
gives $F\otimes^L_A\kappa_E\cong G\otimes^L_A\kappa_E$. Comparing
$\kappa_E$-dimensions yields the displayed rank formula.
