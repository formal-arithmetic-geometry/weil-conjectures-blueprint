+++
id = "lem-weil-pbc-prime-factor-devissage"
kind = "lemma"
title = "Prime-factor devissage"
order = 1565
lean = ["CategoryTheory.Abelian.nsmulShortComplex", "CategoryTheory.Abelian.shortExact_nsmulShortComplex", "CategoryTheory.Abelian.nsmul_id_kernel_eq_zero", "CategoryTheory.Abelian.nsmul_id_image_eq_zero", "CategoryTheory.ObjectProperty.prop_of_nsmul_id_eq_zero"]
uses = ["def-weil-pbc-etale-sheaves"]
+++
Let $\mathcal C$ be an abelian category (for instance the etale sheaves of
[def-weil-pbc-etale-sheaves]), let $F$ be an object of $\mathcal C$, and let
$r\geq1$ be an integer. There is a natural short exact sequence

$$
 0\longrightarrow F[r]\longrightarrow F
 \xrightarrow{r} rF\longrightarrow0,
$$

with $F[r]=\ker(r\cdot\mathrm{id}_F)$ and $rF$ the image of $r\cdot\mathrm{id}_F$;
$F[r]$ is killed by $r$, and if $F$ is killed by $n$ and $r\mid n$, then $rF$ is
killed by $n/r$. Consequently, if a property $P$ of objects of $\mathcal C$ is
stable under extensions (whenever $0\to F_1\to F\to F_2\to0$ is exact and $P$
holds for $F_1$ and $F_2$, it holds for $F$) and holds for every object killed by
a prime, then $P$ holds for every object killed by a positive integer.
