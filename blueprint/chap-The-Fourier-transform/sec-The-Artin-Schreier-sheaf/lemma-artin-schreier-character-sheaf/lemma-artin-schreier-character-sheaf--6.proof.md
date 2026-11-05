+++
kind = "proof"
of = "lemma-artin-schreier-character-sheaf--6"
order = 1217012
uses = ["lemma-artin-schreier-character-sheaf--1", "proposition-topos-functoriality"]
+++
Pullback functoriality of the trace function reduces the calculation to
the $\psi$-eigensheaf at the point with coordinate $ax$.
Choose a root $u$ of $u^q-u=ax$ over that point. Iterating Frobenius gives

$$
u^{q^n}=u+\operatorname{Tr}_{\Fqn/k_0}(ax).
$$

Geometric Frobenius on roots is the inverse action, with translation
$d=-\operatorname{Tr}_{\Fqn/k_0}(ax)$; this is the lift constructed by
`AlgebraicGeometry.affineLine.exists_comp_geometricArtinSchreierMap_eq`.
Evaluation trivializes the eigensheaf on the cover, compatibly with its
Weil structure. Transport of this trivialization identifies local
Frobenius on the stalk with multiplication by $\psi(-d)$.
`AlgebraicGeometry.affineLine.trace_frobeniusEnd_stalkAt_artinSchreierImage`
then computes its trace on the one-dimensional stalk as
$\psi(\operatorname{Tr}_{\Fqn/k_0}(ax))$.
