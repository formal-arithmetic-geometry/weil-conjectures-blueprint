+++
id = "lem-kun-095R"
kind = "lemma"
title = "Pushforward of constructible sheaves along finite morphisms"
order = 6117
lean = ["AlgebraicGeometry.Etale.isConstructible_pushforward_of_finite"]
+++
Let $k$ be a field, $X$ and $Y$ schemes of finite type over $k$,
$f:X\to Y$ a finite and finitely presented morphism, and $\Lambda$ a finite
ring annihilated by an integer invertible on $k$. If $F$ is a constructible
$\Lambda$-module sheaf on $X_{\Et}$, then $f_*F$ is constructible on
$Y_{\Et}$, and $R^qf_*F=0$ for every $q>0$.

## Proof

The constructibility of $f_*F$, including that of all higher direct
images, is the finite-morphism constructibility theorem of the
smooth-base-change chapter (stated there for the coefficient ring of that
chapter's conventions, under exactly the hypotheses on $X$, $Y$ and $\Lambda$
displayed above); the vanishing of the higher direct images is the exactness
of finite pushforward.

Unresolved dependencies: def:weil-pbc-scheme-conventions, def:weil-pbc-constructible-complexes, def:weil-pbc-direct-image, sbc-def-coefficient-conventions, fin4-thm-finite-morphisms-constructible, lem:weil-pbc-finite-direct-image-exact
