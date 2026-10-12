+++
kind = "proof"
of = "lem-weil-pbc-finite-product-integral-closure"
+++
For an integral tuple, apply IsIntegral.map_of_comp_eq to each pair of evaluation ring homomorphisms to obtain coordinatewise integrality. (`integralClosure, IsIntegral, IsIntegrallyClosedIn` ([Mathlib source](https://github.com/leanprover-community/mathlib4/blob/master/Mathlib/RingTheory/IntegralClosure/Algebra/Basic.lean))).

Conversely choose component monic annihilating polynomials, take the finite supremum of their natural degrees, multiply each by the required power of X, and assemble the coefficients with Polynomial.piEquiv. The resulting polynomial is monic and annihilates the tuple coordinatewise; the construction also handles the empty product. (`integralClosure, IsIntegral, IsIntegrallyClosedIn` ([Mathlib source](https://github.com/leanprover-community/mathlib4/blob/master/Mathlib/RingTheory/IntegralClosure/Algebra/Basic.lean))).

Use the coordinatewise criterion to prove the integral-closure subring equality by extensionality. Under injectivity, use isIntegrallyClosedIn_iff, single-coordinate tuples, and coordinatewise preimages to prove the equivalence of integral closedness. (`integralClosure, IsIntegral, IsIntegrallyClosedIn` ([Mathlib source](https://github.com/leanprover-community/mathlib4/blob/master/Mathlib/RingTheory/IntegralClosure/Algebra/Basic.lean))).
