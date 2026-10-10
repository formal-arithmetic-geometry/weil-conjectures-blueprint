+++
id = "lem-galois-axioms"
kind = "lemma"
title = "Consequences of the axioms"
order = 970
uses = ["def-galois-category"]
+++
Let $(\mathcal C,F)$ be a Galois category. Then:

1. $F$ is faithful;
1. $X\to Y$ is a monomorphism if and only if $F(X)\to F(Y)$ is
injective, and an epimorphism if and only if $F(X)\to F(Y)$ is
surjective;
1. an object is initial if and only if its image under $F$ is empty,
and final if and only if its image is a singleton;
1. every morphism between connected objects is an epimorphism;
1. if $X$ is connected and $a,b:X\to Y$ agree on one element of
$F(X)$, then $a=b$;
1. for connected $X$ and $s\in F(X)$ the map
$\operatorname{Aut}(X)\to F(X)$, $g\mapsto F(g)(s)$, is injective, so
$\#\operatorname{Aut}(X)\le\#F(X)$; $X$ is *Galois* if equality
holds, equivalently if $\operatorname{Aut}(X)$ acts transitively on
$F(X)$;
1. if $X=\coprod_iX_i$ and $Y=\coprod_jY_j$ with connected $X_i$,
$Y_j$, then every morphism $X\to Y$ is given by a map of index sets
$\alpha$ with components $X_i\to Y_{\alpha(i)}$.
