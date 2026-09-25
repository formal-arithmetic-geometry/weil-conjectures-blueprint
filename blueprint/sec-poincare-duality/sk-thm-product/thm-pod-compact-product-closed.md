+++
id = "thm-pod-compact-product-closed"
kind = "theorem"
title = "Compact-support product on closed subschemes over a relative base"
order = 2611
uses = ["def-sf-datum", "def-sf-pf", "thm-sf-kunneth-relative"]
+++
In the setting of [def-sf-datum], let $B$ be a finite-type $k$-scheme,
$f:X\to B$, $g:Y\to B$ separated of finite type,
$h=f\times_Bg:X\times_BY\to B$ with projections $p,q$, and
$K\boxtimes L=p^*K\otimes^L_\Lambda q^*L$ for
$K\in D^b_{ctf}(X,\Lambda)$, $L\in D^b_{ctf}(Y,\Lambda)$. For closed
immersions $i:Z\hookrightarrow X$, $j:W\hookrightarrow Y$, with
$i\times_Bj:Z\times_BW\hookrightarrow X\times_BY$, there is a canonical
isomorphism

$$
Rf_!\bigl(i_*i^*K\bigr)\otimes^L_{\Lambda_B}Rg_!\bigl(j_*j^*L\bigr)\cong
Rh_!\bigl((i\times_Bj)_*(i\times_Bj)^*(K\boxtimes L)\bigr),
$$

natural in $K$ and $L$. For $B=\operatorname{Spec}k$ it reads

$$
R\Gamma_c(Z,i^*K)\otimes^L_\Lambda R\Gamma_c(W,j^*L)\cong
R\Gamma_c\bigl(Z\times_kW,(K\boxtimes L)|_{Z\times_kW}\bigr).
$$

## Proof

Step 1: the exterior product of extensions by zero along closed
immersions is the extension by zero of the exterior product. Write
$i'=i\times_B\mathrm{id}_Y$, $j'=\mathrm{id}_Z\times_Bj$, so that
$i\times_Bj=i'\circ j'$, and let $p_Z,q_W$ be the projections of
$Z\times_BW$. Proper base change (the (A2)-part of [def-sf-datum], with
$Ri_*=Ri_!$ for the proper map $i$) gives $p^*i_*\cong i'_*p_Z'^*$ for the
projection $p_Z':Z\times_BY\to Z$, and similarly for $j$. The projection
formula ([def-sf-pf], (A3)) for the closed immersion $i'$ then gives

$$
(i_*i^*K)\boxtimes(j_*j^*L)
\cong i'_*\bigl(p_Z'^*i^*K\otimes^L_\Lambda i'^*q^*j_*j^*L\bigr),
$$

and applying the same two steps to $j'$ inside $Z\times_BY$ yields
$(i\times_Bj)_*\bigl(p_Z^*i^*K\otimes^L_\Lambda q_W^*j^*L\bigr)
=(i\times_Bj)_*(i\times_Bj)^*(K\boxtimes L)$, since pullback commutes
with $\otimes^L$ and $p\circ(i\times_Bj)=i\circ p_Z$,
$q\circ(i\times_Bj)=j\circ q_W$.

Step 2: apply the relative product theorem [thm-sf-kunneth-relative] to
$i_*i^*K\in D^b_{ctf}(X,\Lambda)$ and $j_*j^*L\in D^b_{ctf}(Y,\Lambda)$
and substitute Step 1 on the left-hand side of that theorem.

Step 3: for $B=\operatorname{Spec}k$, $Rh_!$, $Rf_!$, $Rg_!$ are the
compactly supported cohomologies, and since $i$, $j$, $i\times_kj$ are
proper, the composition law (A4) of [def-sf-datum] gives
$Ra_{X!}i_*=Ra_{Z!}$, $Ra_{Y!}j_*=Ra_{W!}$ and
$Ra_{X\times Y!}(i\times j)_*=Ra_{Z\times W!}$.
