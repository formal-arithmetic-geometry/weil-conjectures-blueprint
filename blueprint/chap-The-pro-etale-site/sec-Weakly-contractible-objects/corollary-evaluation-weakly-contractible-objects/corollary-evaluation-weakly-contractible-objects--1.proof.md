+++
kind = "proof"
of = "corollary-evaluation-weakly-contractible-objects--1"
order = 79009
uses = ["definition-weak-contractibility", "proposition-pro-etale-coverings"]
+++
Kernels are computed on sections. An epimorphism of abelian sheaves is
locally surjective; after forgetting to sheaves of sets it is still an
epimorphism. Weak contractibility therefore makes it surjective on
$W$-sections. Evaluation is additive and preserves kernels and
epimorphisms, so it is exact.

For coproducts, write the presheaf sum as the filtered colimit of its
finite subsums and sheafify. Every section over $W$ has local
representatives with finite support. A finite covering refinement,
as in [proposition-pro-etale-coverings], bounds these supports by a
single finite set. Projection onto that finite subsum fixes the section
locally, hence globally by separatedness. This gives surjectivity of
the coproduct comparison. For injectivity, a kernel element comes from
a finite subsum; the split inclusion and the invertible finite-sum
comparison force it to vanish. This includes the empty sum. Exactness
gives preservation of coequalizers, and coproducts and coequalizers give
all small colimits.
