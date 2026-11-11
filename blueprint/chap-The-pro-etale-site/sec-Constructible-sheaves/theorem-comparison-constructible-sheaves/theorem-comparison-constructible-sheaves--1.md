+++
id = "theorem-comparison-constructible-sheaves--1"
kind = "theorem"
title = "Classical constructible sheaves"
order = 149002
aliases = ["bp-r043-1"]
lean = ["AlgebraicGeometry.ProEtale.constructibleComparison_classical"]
uses = ["definition-ind-etale-pro-etale-weakly--3", "lemma-stability--1", "definition-small-pro-etale-site--1", "definition-classical-pro-etale-sheaves--1"]
+++
Let $X$ be quasi-compact and quasi-separated, and let $\Lambda$ be a
discrete commutative Noetherian ring. Every constructible pro-étale
$\Lambda_X$-module sheaf $F$ is classical: for every pro-étale affine
presentation $U=\varprojlim_i U_i$ with affine étale stages, the
restriction maps induce an isomorphism of $\Lambda$-modules

$$
\varinjlim_i F(U_i)\xrightarrow{\ \sim\ }F(U).
$$

Here constructibility is the condition of Section [sec-Constructible-sheaves]: locally on $X$,
there is a finite partition into constructible locally closed strata on each of which $F$
is locally constant of finite type.
