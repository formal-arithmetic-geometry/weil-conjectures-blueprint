+++
kind  = "proof"
of    = "lem-coef-finite-free-extension"
+++
The module $\mathcal O_L$ is finite and torsion free over the
DVR $\mathcal O_E$, hence finite free; reducing a free basis
modulo $\varpi_E^n$ proves the assertion about $B/A$.
The ordinary direct-image projection comparison is an isomorphism
for a finite free coefficient module by additivity; this is the
finite-free starting case of [lem-coef-finite-direct-image].
Apply it to the closed-support triangle exactly as in
[lem-coef-finite-closed-shriek]. This proves the closed
exceptional comparison with the same counit-defined map.
The local closed-embedding computation of
[lem-coef-finite-dualizing] then proves the comparison for
$\omega_X$. The Tate twists of [def-coefficient-twists-detailed]
commute with coefficient extension: they are the tensor extensions
of the same prime-to-characteristic root-of-unity sheaves, and
the affine-space trace uses their coefficient-linear counit.

For internal Hom one can either repeat the strata argument of
[thm-coef-finite-hom], or use finite freeness directly.
The tensor–Hom adjunction in
[def-weil-derived-pullback-tensor-hom] identifies the
underlying $A$-object of the target with
$R\mathcal Hom_A(K,M\otimes_A B)$.
For a finite free coefficient module, additivity identifies this
with $R\mathcal Hom_A(K,M)\otimes_A B$. The canonical
identification is independent of the temporary choice of a
free basis, since it is the map adjoint to evaluation. Combining
this with the dualizing comparison gives the Verdier comparison
by precisely the construction of [cor-coef-finite-verdier].

For two field extensions, or a quotient followed by extension,
transpose both proposed composite comparisons under the same
adjunction. Both are tensor reassociation followed by the same
evaluation or counit. This proves their equality, as well as
evaluation and double-dual compatibility. The constructions use
only pullback, tensor, evaluation, and natural adjunction maps,
so they are unchanged by transporting along a scheme
isomorphism. Finally the positive multiples $en$ are cofinal
among the positive integers, and
$(\varpi_E^n)\mathcal O_L=(\varpi_L^{en})$. These are exactly
the finite levels needed when reconstructing after scalar extension;
one does not identify equal numerical indices for the two different
uniformizers.
