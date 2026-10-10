+++
id = "sk-prop-sf-existence"
kind = "section"
title = "Existence of the exceptional right adjoint"
order = 1801
uses = ["sk-prop-sf-comparison"]
lean = ["AlgebraicGeometry.Etale.rightDerivedUpperShriekAdjunction", "AlgebraicGeometry.ProEtale.rightDerivedUpperShriekAdjunction"]
+++
*Proposition (sketch).*

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

## Proof

*(a)* Choose a compactification $f=rj$, $j$ an open immersion and $r$
proper. The functor $j_!$ is exact and a left adjoint (of $j^*$), so its
derived functor preserves coproducts; $Rr_*$ preserves coproducts, so the
exact functor $Rf_!=Rr_*j_!$ preserves coproducts. The derived category of a
Grothendieck abelian category is well generated, so Brown representability
(Stacks `0F5Y`) gives the right adjoint $f^{\times}$.

*(b)* Let $f=pj$ be the chosen compactification, with
$\operatorname{FullCD}(p,A;c)$. The uniform bound
$\mathcal H^r(R(p_V)_*\mathcal F)=0$ for $r>c$, for every sheaf $\mathcal F$
and every $V\in Y_{\Proet}$, says that $Rp_*$ has cohomological amplitude
$\le c$ on sheaves; hence it carries $D^{<m}$ into $D^{<m+c}$ for every $m$,
also on unbounded complexes. For a fixed degree $q$ and $m=q-c$, the triangle
$\tau^{<m}K\to K\to\tau^{\geq m}K$ then gives
$\mathcal H^q(Rp_*K)\cong\mathcal H^q(Rp_*\tau^{\geq m}K)$ for every $K$.
Truncation commutes with coproducts, and on bounded-below complexes $Rp_*$
commutes with coproducts because the cohomology of the quasi-compact
quasi-separated $\overline X\times_YV$ commutes with direct sums of sheaves.
Hence $\mathcal H^q(Rp_*\bigoplus_iK_i)\cong\bigoplus_i\mathcal H^q(Rp_*K_i)$
for every $q$, i.e. $Rp_*$ preserves all coproducts. As in (a), $j_!$
preserves coproducts, hence so does $Rf_{!,n}=Rp_*j_!$, and Brown
representability on the well-generated $D(X_{\Proet},A)$ gives the right
adjoint $Rf_n^{\times}$. Two compactifications give isomorphic functors
$Rf_{!,n}$ (through a common refinement), and right adjoints of isomorphic
functors are isomorphic compatibly with the units and counits, which is the
independence of the compactification.

*(c)* Write $K=\nu_X^*G$ with $G\in D^+(X_{\Et},A)$. The compact-support
comparison ([sk-prop-sf-comparison] applied to the proper part and the
extension by zero) gives $Rf_{!,n}K\cong\nu_Y^*Rf^{\Et}_!G$; then
$$
\operatorname{Hom}_Y(\nu_Y^*Rf^{\Et}_!G,L)
\cong\operatorname{Hom}_{Y_{\Et}}(Rf^{\Et}_!G,R\nu_{Y,*}L)
\cong\operatorname{Hom}_{X_{\Et}}(G,f^{\times}R\nu_{Y,*}L)
\cong\operatorname{Hom}_X(\nu_X^*G,\nu_X^*f^{\times}R\nu_{Y,*}L),
$$
the first by the adjunction $\nu_Y^*\dashv R\nu_{Y,*}$, the second by (a),
the third by the full faithfulness of $\nu_X^*$ on bounded-below complexes
([sk-prop-sf-comparison]; $f^{\times}$ preserves $D^+$ because $Rf^{\Et}_!$
has finite cohomological amplitude, so $f^{\times}R\nu_{Y,*}L$ is bounded
below). Compactification independence follows from that of $Rf^{\Et}_!$
by uniqueness of adjoints. Every object of $\Dctf(X,A)$ is of étale origin
([09AK](https://stacks.math.columbia.edu/tag/09AK)), so the adjunction holds on the small categories.
