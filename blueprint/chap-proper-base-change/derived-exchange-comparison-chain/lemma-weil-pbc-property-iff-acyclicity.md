+++
id = "lemma-weil-pbc-property-iff-acyclicity"
kind = "lemma"
title = "Equivalence of PBC and IA"
order = 1541
uses = ["def-weil-pbc-injective-acyclicity-property", "def-weil-pbc-property", "lemma-weil-pbc-leray-acyclicity", "lemma-weil-pbc-prime-torsion-devissage", "lemma-weil-pbc-proper-underived-exchange"]
+++
For proper $f$, $\mathsf{PBC}(f)$ holds if and only if $\mathsf{IA}(f)$ holds.

## Proof

Assume $\mathsf{PBC}(f)$. For an injective $\mathbf F_\ell$-module sheaf
$I$ and a base change $g$, apply
the isomorphism to the complex concentrated in degree zero. The source has
no higher cohomology because $I$ is injective, so the target has none; this is
the required acyclicity. Conversely assume $\mathsf{IA}(f)$. Resolve any
torsion $F$ by injectives $I^\bullet$. The inverse image complex
$g'^{-1}I^\bullet$ computes $Rf'_*g'^{-1}F$ because each term is acyclic.
For an $\mathbf F_\ell$-module sheaf $E$, choose an injective resolution
$E\to I^\bullet$ in the $\mathbf F_\ell$-module category. IA makes every
$g'^{-1}I^r$ $f'_*$-acyclic, so Lemma
[lemma-weil-pbc-leray-acyclicity] identifies the target of the derived
exchange map with the cohomology of $f'_*g'^{-1}I^\bullet$. In each degree,
the underived proper exchange lemma gives an isomorphism

$$
g^{-1}f_*I^r\xrightarrow{\sim}f'_*g'^{-1}I^r,
$$

and the replacement-independence lemma makes these maps a morphism of the
chosen resolutions. Thus $\operatorname{Ex}_{\square,E}$ is an isomorphism.
For $F[n]$, the prime-factor induction lemma and the five-lemma transfer
propagate this isomorphism through the exact sequences
$0\to F[\ell]\to F[n]\xrightarrow{\ell}\ell F[n]\to0$; the induction
parameter is $\nu(n)=\sum_\ell v_\ell(n)$, with the prime-torsion case just
proved. Finally $F=\varinjlim_nF[n]$ by the filtered torsion-union lemma.
The filtered-colimit direct-image lemma applies after every quasi-compact
etale base change, so it identifies both cohomology sheaves and carries the
isomorphisms for the $F[n]$ to the specified map $\operatorname{Ex}_{\square,F}$.
This proves PBC for every torsion sheaf and closes the converse implication.
