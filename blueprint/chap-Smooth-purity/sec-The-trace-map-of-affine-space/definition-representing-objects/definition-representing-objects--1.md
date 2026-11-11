+++
id = "definition-representing-objects--1"
kind = "definition"
title = "Representing objects (1)"
name_showing = false
order = 739001
aliases = ["bp-r222-1"]
lean = ["AlgebraicGeometry.Etale.FiniteRepresentingPair", "AlgebraicGeometry.ProEtale.FiniteRepresentingPair"]
uses = ["definition-ind-etale-pro-etale-weakly--3", "lemma-stability--2", "definition-small-pro-etale-site--1", "proposition-topos-functoriality--2", "definition-constructible-sheaves--5", "definition-compactification-refinement--1"]
+++
Let $f$ be smooth, and let us work in $D(Y,\mathbf Z/\ell^n\mathbf Z)$ and
$D(X,\mathbf Z/\ell^n\mathbf Z)$ on either the étale or the
pro-étale sites. Let $K$ be an object on $Y$. We say that a pair
$(H,\varepsilon)$, where $H$ is an object on $X$ and
$\varepsilon:Rf_!H\to K$ is a morphism, *represents*
$\operatorname{Hom}(Rf_!(-),K)$ if $b\mapsto\varepsilon\circ Rf_!(b)$ is a bijection
$\operatorname{Hom}(M,H)\to\operatorname{Hom}(Rf_!M,K)$ for all
$M\in D^b_{\mathrm{ctf}}(X,\mathbf Z/\ell^n\mathbf Z)$.
