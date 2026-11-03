+++
id = "lem-weil-pbc-cech-criterion"
kind = "lemma"
title = "Injectives and the Cech acyclicity criterion"
order = 1018
lean = ["CategoryTheory.Presheaf.exact_cechFreeAug", "CategoryTheory.Presheaf.exact_cechFreeD", "CategoryTheory.Sheaf.exactAt_cechComplex_of_injective"]
uses = ["def-weil-pbc-cover-cech", "def-weil-pbc-etale-cohomology"]
+++
Let $(\mathcal C,J)$ be a site with finite fibre products, and for an object
$U$ write $\mathbb Z[U]$ for the free abelian sheaf on $U$, so that
$H^q(U,F)=\operatorname{Ext}^q(\mathbb Z[U],F)$ for an abelian sheaf $F$.

1. If $f\colon V\to U$ generates a covering sieve, the augmented Cech complex
   $$
   \cdots\to\mathbb Z[V\times_UV\times_UV]\to\mathbb Z[V\times_UV]\to
   \mathbb Z[V]\to\mathbb Z[U]\to0
   $$
   of free abelian sheaves, with alternating-face differentials, is exact.
   Consequently, for an injective abelian sheaf $I$ the Cech complex
   [def-weil-pbc-cover-cech] of $I$ along $f$ has no positive cohomology.
2. *(Cartan's criterion.)* Let $F$ be an abelian sheaf and $P$ a class of
   objects of $\mathcal C$. Suppose that for every $P$-object $U$ and every
   covering sieve $R$ of $U$ there is $f\colon V\to U$ such that: $f$ generates
   a covering sieve; every term $V\times_U\cdots\times_UV$ of its Cech nerve is
   a $P$-object; every positive-degree Cech cocycle of $F$ along $f$ is a
   coboundary; and every class in $H^{q}(U,F)$, $q>0$, whose restrictions to
   all members of $R$ vanish, also vanishes after restriction along $f$. Then
   $H^q(U,F)=0$ for every $P$-object $U$ and every $q>0$.
