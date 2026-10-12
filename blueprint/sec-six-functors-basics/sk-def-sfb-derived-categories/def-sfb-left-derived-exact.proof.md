+++
kind  = "proof"
of    = "def-sfb-left-derived-exact"
uses = ["def-sfb-preserves-kflat-quasi-iso"]
+++
By [def-sfb-preserves-kflat-quasi-iso], $F$ preserves K-flat quasi-isomorphisms, so $LF$
is defined. Since $F$ is exact, $D(F)$ is defined and $Q\circ F\cong D(F)\circ Q$. Its
inverse is a counit for $D(F)$ that is an isomorphism on all complexes, in particular on
the K-flat ones. By the characterization in [def-sfb-left-derived-functor], $D(F)$ is a
left derived functor of $F$. Left derived functors are unique up to unique isomorphism,
which gives $LF\cong D(F)$.
