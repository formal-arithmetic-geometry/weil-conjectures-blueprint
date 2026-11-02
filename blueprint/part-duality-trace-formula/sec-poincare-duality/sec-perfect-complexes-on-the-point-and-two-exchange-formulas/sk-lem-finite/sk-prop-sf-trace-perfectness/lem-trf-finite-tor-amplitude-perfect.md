+++
id = "lem-trf-finite-tor-amplitude-perfect"
kind = "lemma"
title = "Finite Tor amplitude and perfectness over the finite coefficient ring"
lean = ["DerivedCategory.finiteTorAmplitude_iff_exists_free"]
order = 3180
uses = ["def-trf-categorical-trace", "def-trf-coefficient-conventions", "def-weil-finite-coefficient-point", "def-weil-finite-tor-amplitude"]
+++
Let $A$ be the finite coefficient ring of [def-trf-coefficient-conventions], an
arbitrary finite commutative $\ell$-primary ring (hence Artinian, a finite product of
local Artinian rings), and let $C$ be a bounded complex of $A$-modules
whose cohomology modules are finite, i.e. an object of the
finite-coefficient
category over a point. Then $C$ has
finite Tor amplitude if and
only if $C$ lies in $D^b_{\mathrm{fin}}(A)$ in the sense of
[def-trf-categorical-trace], i.e. if and only if $C$ is
quasi-isomorphic to a bounded complex of finitely generated projective
$A$-modules. If $A$ is local (for instance $A=A_{E,n}$), these modules can be taken free.
