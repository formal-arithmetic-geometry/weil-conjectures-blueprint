+++
kind  = "proof"
of    = "lem-pc-flat-complex-derived-pullback"
+++
By [def-pc-derived-pullback], $Lg^*$ is the left derived functor of
the termwise pullback $g^*$, and $g^*E\leftarrow Lg^*E$ is its canonical
comparison map. A left derived functor is computed on any class of
complexes which is stable under the relevant constructions and on which
$g^*$ preserves acyclicity. Bounded above complexes of flat
$\mathcal O_S$-modules form such a class: every bounded above complex admits
a quasi-isomorphism from one of them, and if $P$ is a bounded above
acyclic complex of flat modules then $g^*P$ is acyclic. Indeed, inverse
image $g^{-1}$ is exact and preserves flatness, a bounded above acyclic
complex of flat modules has flat cycle modules (descending induction in
the short exact sequences $0\to Z^n\to P^n\to Z^{n+1}\to0$), and
$\mathcal O_T\otimes_{g^{-1}\mathcal O_S}-$ is exact on short exact sequences
of flat modules (Cohomology of Sheaves, Lemma 20.26.9, Tag
[06YD](https://stacks.math.columbia.edu/tag/06YD), for the
K-flatness of such complexes). Hence $Lg^*E\to g^*E$ is an isomorphism in
$D(\mathcal O_T)$ for $E$ bounded above with flat terms, which is the
claim.
