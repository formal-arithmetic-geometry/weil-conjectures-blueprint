+++
id = "def-galois-category"
kind = "definition"
title = "Galois category"
order = 1376
lean = ["CategoryTheory.PreGaloisCategory", "CategoryTheory.PreGaloisCategory.FiberFunctor", "CategoryTheory.GaloisCategory", "CategoryTheory.PreGaloisCategory.IsConnected", "CategoryTheory.PreGaloisCategory.autEmbedding"]
uses = ["def-galois-fibre-functor"]
+++
A category $\mathcal C$ is a *pre-Galois category* if

1. $\mathcal C$ has a final object and fibre products (hence all finite
limits);
1. $\mathcal C$ has finite coproducts and quotients $X/G$ of objects by
finite groups $G$ acting on them (colimits of the diagram $G\to\mathcal
C$ with one object);
1. every monomorphism $X\to Y$ is the inclusion of a direct summand:
there is $Z\to Y$ such that $Y=X\amalg Z$ via the two maps.

A functor $F:\mathcal C\to(\text{finite sets})$ on a pre-Galois category
is a *fibre functor* if

4. $F$ preserves the final object and fibre products;
4. $F$ preserves finite coproducts, epimorphisms and quotients by finite
groups;
4. $F$ reflects isomorphisms (if $F(f)$ is bijective then $f$ is an
isomorphism).

A *Galois category* is a pre-Galois category admitting a fibre functor,
and we write $(\mathcal C,F)$ for a Galois category with a chosen fibre
functor. An object $X$ is *connected* if it is not initial and every
monomorphism $Y\to X$ with $Y$ not initial is an isomorphism.

For a functor $F$ with all $F(X)$ finite, $\operatorname{Aut}(F)$ is
identified, by evaluation $\gamma\mapsto(\gamma_X)_X$, with the subgroup
of $\prod_X\operatorname{Aut}(F(X))$ formed by the tuples induced by the
natural automorphisms of $F$, and carries the topology induced from the
product of the discrete topologies.
