+++
id = "lem-galois-axioms"
kind = "lemma"
title = "Consequences of the axioms"
order = 1484
lean = ["CategoryTheory.PreGaloisCategory.FiberFunctor", "CategoryTheory.PreGaloisCategory.initial_iff_fiber_empty", "CategoryTheory.PreGaloisCategory.surjective_on_fiber_of_epi", "CategoryTheory.PreGaloisCategory.epi_of_nonempty_of_isConnected", "CategoryTheory.PreGaloisCategory.evaluation_injective_of_isConnected", "CategoryTheory.PreGaloisCategory.evaluation_aut_injective_of_isConnected", "CategoryTheory.PreGaloisCategory.card_aut_le_card_fiber_of_connected", "CategoryTheory.PreGaloisCategory.IsGalois", "CategoryTheory.PreGaloisCategory.isGalois_iff_pretransitive", "CategoryTheory.PreGaloisCategory.has_decomp_connected_components"]
uses = ["def-galois-category"]
+++
Let $(\mathcal C,F)$ be a Galois category. Then:

1. $F$ is faithful;
1. $X\to Y$ is a monomorphism if and only if $F(X)\to F(Y)$ is
injective, and an epimorphism if and only if $F(X)\to F(Y)$ is
surjective;
1. an object is initial if and only if its image under $F$ is empty,
and final if and only if its image is a singleton;
1. every morphism from an object with nonempty fibre to a connected
object is an epimorphism; in particular every morphism between
connected objects is an epimorphism;
1. if $X$ is connected and $a,b:X\to Y$ agree on one element of
$F(X)$, then $a=b$;
1. for connected $X$ and $s\in F(X)$ the map
$\operatorname{Aut}(X)\to F(X)$, $g\mapsto F(g)(s)$, is injective, so
$\#\operatorname{Aut}(X)\le\#F(X)$; $X$ is *Galois* if it is connected
and equality holds, equivalently if $\operatorname{Aut}(X)$ acts
transitively on $F(X)$;
1. if $X=\coprod_iX_i$ and $Y=\coprod_jY_j$ with connected $X_i$,
$Y_j$, then every morphism $X\to Y$ is given by a map of index sets
$\alpha$ with components $X_i\to Y_{\alpha(i)}$;
1. every object of $\mathcal C$ is a finite coproduct of connected
objects.
