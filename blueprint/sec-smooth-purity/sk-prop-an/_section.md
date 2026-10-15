+++
id = "sk-prop-an"
kind = "proposition"
title = "Vector-bundle purity"
order = 1816
uses = ["sk-def-purity-conv", "sk-lem-sf-mate", "sk-prop-a1", "sk-prop-a1-inv", "sk-prop-a1-kummer", "sk-prop-cd", "sk-prop-h2", "sk-prop-sf-cbc", "sk-prop-sf-open-closed-triangle", "sk-thm-properbasechange", "sk-lem-sp-p1", "sk-lem-sp-finite-existence"]
lean = ["AlgebraicGeometry.Etale.nonempty_iso_rightDerivedUpperShriek_affineSpaceZero"]
tags = ["sketch"]
+++
*Integration on affine space.* Let $j:\mathbf A^1_S\hookrightarrow\mathbf P^1_S$ be the
complement of the section at infinity and $p=q\circ j$. Composing
[sk-lem-sp-p1] with $j_!\dashv j^*$ gives $Rp_!\dashv p^*(-)(1)[2]$; at the
constant sheaf its counit is the *trace map of the affine line*
$\operatorname{Tr}_p:Rp_!(\mathbf Z/\ell^n\mathbf Z)_{\mathbf A^1_S}(1)[2]\to(\mathbf Z/\ell^n\mathbf Z)_S$,
an isomorphism. For $p_j:\mathbf A^j_S\to S$ and $r_j:\mathbf A^j_S\to\mathbf A^{j-1}_S$
forgetting the last coordinate, $\operatorname{Tr}_{p_j}$ is defined inductively
as $\operatorname{Tr}_{p_{j-1}}\circ Rp_{j-1!}(\operatorname{Tr}_{r_j})$, using
$Rp_{j!}=Rp_{j-1!}Rr_{j!}$ and the projection formula. For $j=d$ this is the
*integration isomorphism* (the identity when $d=0$)

$$
\operatorname{Tr}_{p_d}:Rp_{d!}(\mathbf Z/\ell^n\mathbf Z)_{\mathbf A^d_S}(d)[2d]\xrightarrow{\ \sim\ }(\mathbf Z/\ell^n\mathbf Z)_S,
$$

the counit of $Rp_{d!}\dashv p_d^*(-)(d)[2d]$ at the constant sheaf; unit and
counit commute with base change. On a vector bundle this gives an integration
map after choosing a local frame; to get a global map one must show that it
does not depend on the frame.

**Proposition.** Let $\pi:V\to S$ be a vector bundle of rank $d$. For
$K\in\Dctf(S_{\mathrm{proét}},\mathbf Z/\ell^n\mathbf Z)$, integration induces an isomorphism
in $\Dctf(V_{\mathrm{proét}},\mathbf Z/\ell^n\mathbf Z)$

$$
\pi^*K(d)[2d]\xrightarrow{\ \sim\ }\pi^!K.
$$
