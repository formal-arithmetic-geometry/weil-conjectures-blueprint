+++
kind  = "proof"
of    = "lemma-weil-pbc-curve-filtered-cohomology"
+++
For $q=0$, choose a finite etale cover on which a section is represented.
The section and its finitely many equalizer equations on pairwise fibre
products occur at one index, proving surjectivity; if two representatives
become equal in the colimit, the finite cover and equality witnesses occur
at one later index, proving injectivity.

For $q>0$, represent a class on a split etale hypercover whose
$(q+1)$-skeleton has finitely many quasi-compact components. A cocycle uses
finitely many sections and face-map equations, so all occur at one index
$\lambda$. This proves surjectivity. If the class from $F_\lambda$ dies in
the colimit, choose a finite refinement and a degree-$(q-1)$ cochain whose
coboundary is the cocycle. The refinement maps, cochain sections, and
coboundary equations occur at one $\mu\geq\lambda$, so the class already
dies in $H^q(X,F_\mu)$. This is the filtered-colimit theorem for etale
cohomology of quasi-compact quasi-separated schemes,
[lem-weil-pbc-cohomology-filtered-colimit].
