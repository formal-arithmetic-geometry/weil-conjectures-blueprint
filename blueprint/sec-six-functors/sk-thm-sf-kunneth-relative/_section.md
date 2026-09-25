+++
id = "sk-thm-sf-kunneth-relative"
kind = "section"
title = "Relative product theorem"
order = 2305
uses = ["sk-prop-sf-cbc", "sk-prop-sf-comp-proper", "sk-rem-sf-pf-done", "sk-thm-sf-comp-composition"]
+++
*Theorem (sketch).*

Let $B$ be a separated finite-type $k$-scheme, let $f:X\to B$ and $g:Y\to B$ be
separated of finite type, let $p,q$ be the projections of $X\times_BY$, and put
$K\boxtimes L=p^*K\otimes^L_\Lambda q^*L$ for $K\in\Dctf(X,\Lambda)$,
$L\in\Dctf(Y,\Lambda)$. Then the canonical map

$$
R(f\times_Bg)_!\bigl(K\boxtimes L\bigr)\xrightarrow{\ \sim\ }
Rf_!K\otimes^L_\Lambda Rg_!L
$$

in the ambient category $D^+(B,\Lambda)$, is an isomorphism, natural in $K$ and
$L$, compatible with base change
$B'\to B$, finite reduction, scalar extension, and with the identifications
$Rf_!\cong Rf_*$ for proper $f$; for $B=\mathrm{Spec}\,k$ and closed
subschemes $Z\subseteq X$, $W\subseteq Y$ it gives the supported product
$\RG_Z(X,K)\otimes^L_\Lambda\RG_W(Y,L)\cong\RG_{Z\times W}(X\times_kY,K\boxtimes L)$.

## Proof

Four steps, each an instance of one ingredient.
*(1)* By the composition law, $R(f\times_Bg)_!=Rg_!\circ Rq_!$, so
$R(f\times_Bg)_!(K\boxtimes L)=Rg_!\bigl(Rq_!(q^*L\otimes^Lp^*K)\bigr)$.
*(2)* The projection formula for $q$ (proved in this section,
[sk-rem-sf-pf-done]) gives
$Rq_!(q^*L\otimes^Lp^*K)\cong L\otimes^L_\Lambda Rq_!(p^*K)$.
*(3)* Base change for the Cartesian square (prop:sf-cbc, and
[sk-thm-properbasechange] in the proper case) gives $Rq_!(p^*K)\cong Lg^*Rf_!K$.
*(4)* The projection formula for $g$ gives
$Rg_!\bigl(L\otimes^LLg^*Rf_!K\bigr)\cong Rg_!L\otimes^LRf_!K$. The supported
form follows by applying the result to the extensions by zero
$i_{Z*}i_Z^*K$, $i_{W*}i_W^*L$, using
$\RG_Z(X,K)=\RG_c(X,i_{Z*}i_Z^*K)$ and that the exterior product of extensions
by zero is the extension by zero of the exterior product. The coherence of the
isomorphism (symmetry, triple products, base change, compatibility with the
projection formula) is the mate identity of [sk-lem-sf-mate] applied to the
pasted squares.

Uses: `\Cref{prop:sf-cbc}`, `\Cref{prop:sf-comp-proper}`, `\Cref{rem:sf-pf-done}`, `\Cref{thm:sf-comp-composition}`, `def:pur-support-cohomology`, `def:pur-supported-exterior-product`
