+++
id = "lemma-nagata-scheme-theoretic-closure-minimal"
kind = "lemma"
title = "Minimality of the scheme-theoretic closure"
order = 80
lean = ["AlgebraicGeometry.Scheme.Hom.ker_le_ker_iff_existsUnique_fac"]
uses = ["lemma-nagata-scheme-image-universal"]
+++
Let $g\colon T\to Y$ be a morphism of schemes and let
$z\colon Z\hookrightarrow Y$ be a closed immersion with ideal sheaf
$\mathcal I_Z$. Then $\mathcal I_Z\subseteq\ker(g)$, i.e.
$\operatorname{SIm}(g)\subseteq Z$, if and only if $g$ factors through $z$,
and the factorization $T\to Z$ is then unique. Thus $\operatorname{SIm}(g)$
is the smallest closed subscheme of $Y$ through which $g$ factors; in
particular the scheme-theoretic closure of a locally closed subscheme is the
smallest closed subscheme containing it.
