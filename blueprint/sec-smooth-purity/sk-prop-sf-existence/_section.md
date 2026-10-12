+++
id = "sk-prop-sf-existence"
kind = "proposition"
title = "Existence of the exceptional right adjoint"
order = 2139
uses = ["sk-prop-sf-comparison"]
lean = ["AlgebraicGeometry.Etale.rightDerivedUpperShriekAdjunction", "AlgebraicGeometry.ProEtale.rightDerivedUpperShriekAdjunction"]
tags = ["sketch"]
+++
(a) *On the ordinary derived categories of the small étale sites*: if
$f:X\to S$ is a morphism of schemes admitting a compactification and $A$ is a
Grothendieck abelian coefficient category, the functor
$Rf_!=Rr_*j_!:D(X_{\Et},A)\to D(S_{\Et},A)$ on the unbounded derived
categories has a right adjoint
$f^{\times}:D(S_{\Et},A)\to D(X_{\Et},A)$; no restriction to a constructible
subcategory is made. (b) *On the small pro-étale sites (conditional;
its hypothesis is false in general)*:
if $\operatorname{FullCD}(p,A;c)$ holds for the proper part $p$ of a
compactification of a separated finite-type $f$, then
$Rf_{!,n}:D(X_{\Proet},A)\to D(Y_{\Proet},A)$ preserves
coproducts and therefore has a right adjoint
$Rf_n^{\times}:D(Y_{\Proet},A)\to D(X_{\Proet},A)$, and the
adjunction is independent of the compactification. The hypothesis
$\operatorname{FullCD}(p,A;c)$ is *false* for a general proper $p$ —
already for an elliptic curve over $\overline{\mathbf F}_p$ with
$A=\mathbf F_r$, $r\ne p$ — and for that $p$ the conclusion fails as well:
$Rp_*$ does not preserve coproducts and has no right adjoint on
$D(E_{\Proet},A)$ or on $D^+(E_{\Proet},A)$
([sk-rem-sf-fullcd-scope]). So (b) is a conditional implication
whose hypothesis is not a theorem.
(c) *The constructible exceptional adjoint (unconditional)*: let
$f:X\to Y$ be a separated finite-type morphism of finite-type $k$-schemes,
$k=\overline{\mathbf F}_q$, and $A=A_{E,n}$. With $f^{\times}$ the étale
right adjoint of (a), the functor
$$
Rf^!:=\nu_X^*\,f^{\times}\,R\nu_{Y,*}:
D^+(Y_{\Proet},A)\longrightarrow D^+(X_{\Proet},A)
$$
satisfies $\operatorname{Hom}_Y(Rf_{!,n}K,L)\cong\operatorname{Hom}_X(K,Rf^!L)$,
naturally, for every bounded-below $K$ of étale origin and every
bounded-below $L$; its units and counits are compatible with refinements of
the compactification, and on $\Dctf(Y,A)=\nu_Y^*\Dctf(Y_{\Et},A)$ it is
$Rf^!(\nu_Y^*G)=\nu_X^*f^{\times}G$. This is the functor $Rf^!$ of
[sk-def-sf-operations] (vi); that it carries $\Dctf(Y,A)$ into
$\Dctf(X,A)$ is [sk-prop-sf-rf-shriek-preservation].
