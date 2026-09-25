+++
id = "cor-pod-supports-kunneth"
kind = "theorem"
title = "Künneth for cohomology with supports, by duality"
order = 2612
tags = ["latex:corollary"]
uses = ["cor-sf-duality-pullback", "def-pur-support-cohomology", "def-sf-datum", "def-sf-pf", "def-trf-dualizing-complex", "lem-sf-tensor-hom", "prop-pod-biduality-at-the-point", "prop-trf-compact-support-perfectness", "thm-pod-compact-product-closed", "thm-trf-kunneth-verdier"]
+++
In the setting of [thm-pod-compact-product-closed] with $B=\operatorname{Spec}k$,
$k$ algebraically closed and finite coefficients $\Lambda=A=A_{E,n}$ as in
[def-trf-dualizing-complex], write
$R\Gamma_Z(X,K)=R\Gamma(Z,i^!K)$ for cohomology with support in $Z$
([def-pur-support-cohomology]). Then there is a canonical isomorphism

$$
R\Gamma_Z(X,K)\otimes^L_AR\Gamma_W(Y,L)\cong
R\Gamma_{Z\times_kW}(X\times_kY,K\boxtimes L).
$$

## Proof

Write $C^\vee=R\operatorname{Hom}_A(C,A)$ at the point and
$\mathbb D$ for the Verdier dual of [def-sf-pf].

Step 1 (supports as duals of compact supports). For a closed immersion
$i:Z\hookrightarrow X$, biduality [def-sf-datum] and duality against
pullback [cor-sf-duality-pullback] give
$i^!K\cong i^!\mathbb D_X\mathbb D_XK\cong\mathbb D_Zi^*\mathbb D_XK$.
The tensor–Hom exchange [lem-sf-tensor-hom] for $a_Z$ with $M=i^*\mathbb D_XK$
and $N=A$,
$Ra_{Z*}R\mathcal Hom_Z(M,a_Z^!A)\simeq R\operatorname{Hom}_A(Ra_{Z!}M,A)$,
then gives

$$
R\Gamma_Z(X,K)=R\Gamma(Z,\mathbb D_Zi^*\mathbb D_XK)\cong
R\Gamma_c(Z,i^*\mathbb D_XK)^\vee ,
$$

and likewise for $W\subseteq Y$ and for $Z\times W\subseteq X\times Y$.

Step 2 (the dual of an exterior product). By
[cor-sf-duality-pullback] and the tensor–Hom adjunction,
$\mathbb D(K\boxtimes L)=R\mathcal Hom(q^*L,R\mathcal Hom(p^*K,\omega_{X\times Y}))
\cong R\mathcal Hom(q^*L,p^!\mathbb D_XK)$, and the Künneth–Verdier
isomorphism [thm-trf-kunneth-verdier] with $M=\mathbb D_XK$, $N=L$
identifies the latter with $\mathbb D_XK\boxtimes\mathbb D_YL$.

Step 3 (dualize the compact product). By
[thm-pod-compact-product-closed] applied to $\mathbb D_XK,\mathbb D_YL$ and
Step 2,

$$
R\Gamma_c(Z,i^*\mathbb D_XK)\otimes^L_AR\Gamma_c(W,j^*\mathbb D_YL)\cong
R\Gamma_c\bigl(Z\times W,(i\times j)^*\mathbb D(K\boxtimes L)\bigr).
$$

Both factors on the left are perfect by
[prop-trf-compact-support-perfectness], so by
[prop-pod-biduality-at-the-point]
$(P\otimes^L_AQ)^\vee\cong R\operatorname{Hom}_A(P,Q^\vee)\cong P^\vee\otimes^L_AQ^\vee$.
Applying $(-)^\vee$ to the display and Step 1 to each term gives the claim.

This deduction uses Verdier duality; the smooth-purity chapter needs the
same statement earlier and proves it directly
([lem-pur-kunneth-supported]).
