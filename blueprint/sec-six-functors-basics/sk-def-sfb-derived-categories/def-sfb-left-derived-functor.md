+++
id = "def-sfb-left-derived-functor"
kind = "definition"
title = "Left derived functor via K-flat resolutions"
order = 1612
uses = ["def-sfb-preserves-kflat-quasi-iso"]
lean = ["CategoryTheory.Functor.leftDerivedFunctor"]
+++
Let $\mathcal C$ be a monoidal abelian category with the following properties: its
tensor product is additive in each variable; it has countable coproducts and exact
$\mathbf Z$-indexed colimits, which tensoring with a fixed object on either side
preserves; and it has functorial flat resolutions. Let $F\colon\mathcal C\to\mathcal D$
be an additive functor to an abelian category that preserves K-flat quasi-isomorphisms
[def-sfb-preserves-kflat-quasi-iso]. The *left derived functor*
$LF\colon D(\mathcal C)\to D(\mathcal D)$ is the total left derived functor of
$K(\mathcal C)\xrightarrow{F}K(\mathcal D)\xrightarrow{Q}D(\mathcal D)$ with respect to
the quasi-isomorphisms. It comes with a counit $LF\circ Q\Rightarrow Q\circ F$, which is
an isomorphism on K-flat complexes. So $LF(K)=F(P)$ for a K-flat resolution $P\to K$.
Conversely, a functor with a counit is the left derived functor if and only if its counit
is an isomorphism on all K-flat complexes.
