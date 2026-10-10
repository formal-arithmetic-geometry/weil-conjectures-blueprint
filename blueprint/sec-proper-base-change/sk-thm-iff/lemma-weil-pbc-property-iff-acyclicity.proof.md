+++
kind  = "proof"
of    = "lemma-weil-pbc-property-iff-acyclicity"
+++
Suppose $\mathrm{PBC}(f)$ holds. If $I$ is injective among $\mathbf
F_r$-module sheaves, then $Rf_*I=f_*I$ in that category; after arbitrary base
change, [def-weil-pbc-property] identifies $Rf'_*g'^{-1}I$ with the
degree-zero complex $g^{-1}f_*I$, so $R^qf'_*g'^{-1}I=0$ for $q>0$, which is
$\mathrm{IA}_r(f)$ by [def-weil-pbc-injective-acyclicity-property].

Conversely assume $\mathrm{IA}(f)$. For an $\mathbf F_r$-module sheaf $E$,
take an injective resolution $E\to I^\bullet$. Acyclicity and
[lemma-weil-pbc-leray-acyclicity] make $f'_*g'^{-1}I^\bullet$ compute
$Rf'_*g'^{-1}E$, while $g^{-1}f_*I^\bullet$ computes $g^{-1}Rf_*E$; the
underived proper exchange of [lemma-weil-pbc-proper-underived-exchange] is an
isomorphism in every degree, and by naturality these maps form an isomorphism
of complexes, which is the derived exchange morphism of
[def-weil-pbc-derived-exchange]. For a sheaf $F$ killed by $n$,
induction on the number of prime factors of $n$ using the exact sequence of
[lem-weil-pbc-prime-factor-devissage] and the five-lemma transfer of
[lemma-weil-pbc-five-lemma-transfer] gives the assertion for $F[n]$. Finally
every torsion sheaf is the filtered union of the $F[n]$ by
[lemma-weil-pbc-torsion-filtered-union], and
[lemma-weil-pbc-direct-image-filtered-colimit] passes the isomorphism to the
colimit, since proper maps are quasi-compact and quasi-separated. This proves
$\mathrm{PBC}(f)$ by [def-weil-pbc-property].
