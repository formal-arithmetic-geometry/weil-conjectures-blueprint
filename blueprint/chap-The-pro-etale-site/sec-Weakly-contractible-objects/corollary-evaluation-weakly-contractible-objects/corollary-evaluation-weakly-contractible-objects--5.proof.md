+++
kind = "proof"
of = "corollary-evaluation-weakly-contractible-objects--5"
order = 79011
uses = ["definition-weak-contractibility", "proposition-pro-etale-coverings"]
+++
The functor from $\mathcal R$-module sheaves to abelian sheaves preserves
epimorphisms. Such maps are locally surjective on underlying sheaves
of sets, so weak contractibility makes their maps on $W$-sections
surjective. Since kernels are sectionwise and evaluation is additive,
evaluation is exact and preserves finite colimits.

For a coproduct of module sheaves, the comparison from the presheaf
colimit to the sheaf colimit is locally surjective. Express the
coproduct as a filtered colimit of finite subsums. Local
representatives of a section over $W$, together with a finite covering
refinement from [proposition-pro-etale-coverings], give a common finite
support. Projection onto this support fixes the section locally, hence
globally by separatedness. The finite-sum comparison is an isomorphism,
so this proves surjectivity of the coproduct comparison. A kernel
element also comes from a finite subsum; applying its split retraction
and the finite comparison proves injectivity. The argument includes
the empty sum. Coproducts and coequalizers now give all colimits in the
common module universe.

To allow independent diagram universes, use that the category of
module sheaves is Grothendieck abelian and has a generator. On an
equivalent category with morphisms in the common universe, the special
adjoint functor theorem makes evaluation a left adjoint. It preserves
existing colimits of every size, and this property transports back to
the original evaluation functor.
