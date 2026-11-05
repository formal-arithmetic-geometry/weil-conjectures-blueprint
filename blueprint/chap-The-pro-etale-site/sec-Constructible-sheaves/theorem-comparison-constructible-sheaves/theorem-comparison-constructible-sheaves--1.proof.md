+++
kind = "proof"
of = "theorem-comparison-constructible-sheaves--1"
order = 149005
uses = ["proposition-locally-constant-sheaves-finite-presentation", "proposition-comparison-morphism-inverse-image", "theorem-classical-sheaves-essential-image", "proposition-comparison-immersions", "theorem-comparison-direct-images", "corollary-bounded-below-classical-complexes"]
+++
Choose an affine neighborhood of each point and a finite stratification
on which $F$ has finitely presented constant local models. Quasi-compactness
gives a finite affine subcover. Quasi-separatedness allows these local
partitions to be refined to a finite constructible stratification of $X$,
with each stratum mapping into one of the chosen local strata. Pullback
preserves the finite local models.

For this global stratification, finite generation and finite presentation
agree over $\Lambda$. Proposition
[proposition-locally-constant-sheaves-finite-presentation] therefore gives
an étale antecedent on each stratum. Induct on the number of strata,
locally shrinking to an affine open on which the stratum through the
chosen point is closed. On its open complement that stratum disappears,
so induction applies. The open-closed exact sequence, comparison for
immersions [proposition-comparison-immersions] and direct images
[theorem-comparison-direct-images], and closure under extensions
[corollary-bounded-below-classical-complexes] give an étale antecedent on
the affine neighborhood. Full faithfulness of comparison makes étale
origin local for the Zariski topology, so these antecedents descend.

Finally, sections of an étale inverse image on an affine presentation
are the filtered colimit of its sections on the stages, by
[proposition-comparison-morphism-inverse-image]. Naturality transports
this isomorphism to $F$, giving exactly the displayed restriction map.
