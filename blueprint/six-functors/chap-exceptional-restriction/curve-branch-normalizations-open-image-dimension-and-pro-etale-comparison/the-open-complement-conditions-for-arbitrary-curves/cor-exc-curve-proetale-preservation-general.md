+++
id = "cor-exc-curve-proetale-preservation-general"
kind = "theorem"
title = "The ambient pro-etale restriction for arbitrary curves"
order = 3345
tags = ["latex:corollary"]
uses = ["def-weil-finite-tor-amplitude", "def-weil-finite-torsion-constructibility", "def-weil-pbc-scheme-conventions", "def-weil-pbc-site-comparison-morphism", "lem-exc-comparison-tor-interval", "prop-exc-closed-site-comparison", "prop-weil-pbc-site-comparison-finite-level", "thm-exc-curve-closed-preservation-general"]
+++
For a finite-type scheme $T$ of dimension at most one
over a finite field or its algebraic closure, any closed
immersion $i:Z\hookrightarrow T$, and $A=A_{E,n}$
with $\ell$ invertible, the ambient pro-etale right
adjoint $Ri^!$ preserves
bounded
constructible complexes of finite Tor amplitude.
For the pullback under
site comparison
of an etale object with Tor amplitude $[a,b]$, the
result has Tor
amplitude $[a,b+2]$.

## Proof

Take an etale representative of the constructible finite
Tor object, as in
[def-weil-finite-torsion-constructibility].
Its etale Tor interval is the same as the given pro-etale
one by [lem-exc-comparison-tor-interval].
The actual ambient comparison
[prop-exc-closed-site-comparison] identifies its
pro-etale exceptional image with the pullback of its
etale exceptional image. The latter is bounded
constructible of the asserted Tor amplitude by
[thm-exc-curve-closed-preservation-general].
The exact comparison functor of
[prop-weil-pbc-site-comparison-finite-level] preserves
the finite lisse partition and hence constructibility.
The forward implication of
[lem-exc-comparison-tor-interval] gives the same Tor
bound against every pro-etale module sheaf.
This proves preservation for the ambient right adjoint.
