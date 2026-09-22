+++
id = "lem-amb-proper-coproducts"
kind = "lemma"
title = "Proper direct image preserves arbitrary coproducts"
order = 5605
lean = ["AlgebraicGeometry.Etale.IsProper.derivedPushforward_preservesCoproducts"]
uses = ["lem-exc-direct-image-coproducts"]
+++
Let $r:V\to T$ be a proper morphism of finite type between Noetherian
schemes. On the ordinary derived categories of étale $A$-module sheaves,
$Rr_*$ preserves arbitrary coproducts.

## Proof

Choose a common finite bound $e$ for the dimensions of the geometric fibres
of the finite-type morphism $r$. The geometric-fibre stalk formula and the
torsion cohomological-dimension bound for finite-type schemes give
$R^ar_*F=0$ for $a>2e$, for every sheaf $F$.

The functors $R^ar_*$ commute with filtered colimits: on each geometric
fibre this is the compatibility of cohomology with filtered colimits, and
conservativity of geometric stalks detects the comparison. They therefore
commute with direct sums, a direct sum being the filtered colimit of its
finite subsums.

The finite acyclic-resolution argument of [lem-exc-direct-image-coproducts]
applies on the unbounded ordinary category. Its hypercohomology spectral
sequence has only the columns $0,\dots,2e$. For each total degree it thus
uses a finite interval of cohomology sheaves of the input. Applying this
spectral sequence to the coproduct comparison proves the assertion,
including for unbounded complexes. It also extends the geometric-fibre
formula to unbounded complexes by the same finite-interval argument.

Unresolved dependencies: def:weil-pbc-derived-categories, def:weil-pbc-direct-image, def:weil-scheme-morphism-properties, cor:weil-pbc-geometric-fiber-finite, thm:sc-finite-type-torsion-cd, lem:weil-pbc-cohomology-filtered-colimit, lem:weil-pbc-geometric-stalk-conservative
