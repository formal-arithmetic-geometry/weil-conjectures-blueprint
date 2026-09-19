+++
id = "the-base-case-is-finite-torsion-coefficients"
kind = "section"
title = "The base case is finite torsion coefficients"
order = 132
+++
The coefficient ring of the $\ell$-adic formalism is denoted $\Lambda$, and the
case the detailed chapters are written for is the *finite torsion* one:
$\Lambda=\Lambda_n=\mathbb Z/\ell^n\mathbb Z$, so that $A$ is `ModuleCat`
$\Lambda$, the category of $\Lambda$-modules. This is the instantiation named in the
docstring of `WeilConjectures/ConstructibleSheaf/Defs.lean`, both for
the coefficient category and for the constructibility predicate, and it is the
level at which every statement in the following chapters is to be read. The
chapter on proper base change fixes a complete discrete valuation ring
$\Lambda$ with maximal ideal $\mathfrak m$ and writes
$\Lambda_n=\Lambda/\mathfrak m^n$; the finite levels $\Lambda_n$ are the finite
torsion rings above, and it is the finite-level statements that correspond to
the Lean code.

Where a chapter needs $\ell$ to be invertible, that is an assumption on the
schemes considered, not a change of coefficients.
