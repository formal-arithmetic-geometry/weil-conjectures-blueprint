+++
kind  = "proof"
of    = "thm-sf-kunneth-relative"
+++
The operations are those of [def-sf-datum] and [def-sf-pf],
cohomology with supports has its separate meaning in
[def-pur-support-cohomology].
Step 1: by (A4), $R(f\times_Bg)_!=Rg_!\circ Rq_!$, so
$R(f\times_Bg)_!(K\boxtimes L)=Rg_!\bigl(Rq_!(q^*L\otimes^L_\Lambda p^*K)\bigr)$. Step 2: the projection formula (A3) for $q$, whose target is
$Y$, gives $Rq_!(q^*L\otimes^L p^*K)\cong L\otimes^L_\Lambda Rq_!(p^*K)$.
Step 3: base change (A2) for the Cartesian square with $p,q,f,g$ gives
$Rq_!(p^*K)\cong Lg^*Rf_!K$. Step 4: applying the projection formula to
$g$ with first variable $L$ and second variable $Rf_!K$ gives
$Rg_!\bigl(L\otimes^L_\Lambda Lg^*Rf_!K\bigr)\cong Rg_!L\otimes^L_\Lambda Rf_!K$, which is the displayed isomorphism. Step 5:
apply the same formula to the separated finite-type morphisms
$Z\to\operatorname{Spec}k$, $W\to\operatorname{Spec}k$ and the
pullbacks $i_Z^*K,i_W^*L$. Pullback preserves their finite-Tor
hypotheses, and the exterior product is the pullback of $K\boxtimes L$.
This proves the claimed compact-support formula on the closed subschemes.
