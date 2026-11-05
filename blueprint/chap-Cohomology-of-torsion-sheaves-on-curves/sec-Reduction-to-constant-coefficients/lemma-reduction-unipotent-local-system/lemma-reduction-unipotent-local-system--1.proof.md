+++
kind = "proof"
of = "lemma-reduction-unipotent-local-system--1"
order = 1610003
uses = []
+++
Choose a geometric point of $U$ and let $H$ be the finite monodromy
group of $G$. An $\ell$-Sylow subgroup $P\subset H$ gives a connected
finite étale cover $v:V\to U$ of degree $d=[H:P]$, prime to $\ell$.
Every geometric fibre has $d$ points. The restricted representation
$M$ of $P$ gives $v^*G$ under an additive associated-sheaf functor
$T$ preserving finite limits and finite colimits; $T$ sends the trivial
one-dimensional representation to the constant sheaf $\mathbf F_\ell$.
These data are supplied by
`AlgebraicGeometry.Scheme.IsFiniteLocallyConstantSheaf.exists_sylow_cover_associated_sheaf`.

Every nonzero finite-dimensional $\mathbf F_\ell$-representation of
the $\ell$-group $P$ has a nonzero invariant vector: the number of fixed
vectors is congruent modulo $\ell$ to the number of all vectors, and
zero is already fixed. Applying this to successive quotient
representations constructs a $P$-stable flag in $M$ with trivial
one-dimensional quotients
(`Representation.invariants_ne_bot_and_exists_filtration_of_isPGroup`).

Regard the flag as monomorphisms in the category of representations.
Their cokernels are the quotient representations, hence the trivial
one-dimensional representation
(`Rep.exists_categorical_filtration_of_invariant_flag`). Applying $T$
preserves the zero object, monomorphisms and cokernels, and gives the
required filtration of $v^*G$. The zero representation gives the
filtration of length zero.
