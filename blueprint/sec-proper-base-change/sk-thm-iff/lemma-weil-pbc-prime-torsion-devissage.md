+++
id = "lemma-weil-pbc-prime-torsion-devissage"
kind = "lemma"
title = "Prime-torsion devissage"
order = 1090
lean = ["AlgebraicGeometry.Etale.isIso_baseChangeHomologyMap_of_isTorsionSheaf"]
uses = ["lemma-weil-pbc-five-lemma-transfer", "lemma-weil-pbc-torsion-filtered-union"]
+++
Let $\Lambda$ be a commutative ring and $\square$ a cartesian square in which
$f$ (equivalently, by base change, also $f'$) is quasi-compact and
quasi-separated, and let $\Ex^q_{\square,E}:g^{-1}R^qf_*E\to R^qf'_*g'^{-1}E$ be
the degree-$q$ exchange maps on sheaves $E$ of $\Lambda$-modules on $X_{\Et}$.
Suppose that $\Ex^q_{\square,E}$ is an isomorphism for every $q$ and every sheaf
$E$ killed by a prime. Then $\Ex^q_{\square,F}$ is an isomorphism for every $q$
and every torsion sheaf $F$ (every geometric stalk is a torsion abelian group).

For this, write $F[n]=\ker(n:F\to F)$. Then $F=\varinjlim_nF[n]$; for $m\mid n$
the inclusion $F[m]\subseteq F[n]$ is monic, and if $n=\prod_i\ell_i^{e_i}$,
repeated use of

$$
0\longrightarrow F[\ell_i]\longrightarrow F[n]
\xrightarrow{\ell_i}\ell_iF[n]\longrightarrow0
$$

reduces assertions about $F[n]$ to assertions about $\ell_i$-torsion.
