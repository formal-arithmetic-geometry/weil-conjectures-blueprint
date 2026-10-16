+++
id = "lem-sf-ext-sheaf-constructible"
kind = "lemma"
title = "Constructible internal Hom with a site-perfect first variable"
lean = ["AlgebraicGeometry.Etale.boundedConstructible_derivedHom_of_isDualizable", "AlgebraicGeometry.Etale.boundedConstructible_derivedHom_singleFunctor_of_isDualizable"]
order = 2541
uses = ["def-weil-site-perfect-complex", "lem-sf-hom-finite-projective", "thm-constructible-serre"]
+++
If $K$ is site-perfect and $M$ is bounded constructible on
$X_{\Et}$, then every cohomology sheaf of
$R\mathcal Hom_A(K,M)$ is constructible. In particular, for a finite
locally free sheaf $F$ and a constructible sheaf $G$,
$\mathcal Ext_A^r(F,G)=0$ for $r\ne0$, and
$\mathcal Hom_A(F,G)$ is constructible.
