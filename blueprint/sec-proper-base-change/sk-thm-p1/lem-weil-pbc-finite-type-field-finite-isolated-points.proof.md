+++
kind = "proof"
of = "lem-weil-pbc-finite-type-field-finite-isolated-points"
+++
The field $k$ is Noetherian because its only ideals are $0$ and $k$. Applying `Algebra.FiniteType.isNoetherianRing` ([Mathlib source](https://github.com/leanprover-community/mathlib4/blob/master/Mathlib/RingTheory/FiniteType.lean)) to the finite type map $k\to A$ shows that $A$ is Noetherian.

By `minimalPrimes.finite_of_isNoetherianRing` ([Mathlib source](https://github.com/leanprover-community/mathlib4/blob/master/Mathlib/RingTheory/Ideal/MinimalPrime/Noetherian.lean)), the Noetherian ring $A$ has a finite set of minimal prime ideals.

Let $\mathfrak q$ be a prime whose singleton is open. By the basic-open basis `PrimeSpectrum.isTopologicalBasis_basic_opens; PrimeSpectrum.localization_away_isOpenEmbedding; PrimeSpectrum.localization_away_comap_range` ([Mathlib source](https://github.com/leanprover-community/mathlib4/blob/master/Mathlib/RingTheory/Spectrum/Prime/Topology.lean)), there is $f\in A$ with $\mathfrak q\in D(f)\subseteq\{\mathfrak q\}$, so $D(f)=\{\mathfrak q\}$. If $\mathfrak p\subseteq\mathfrak q$ is any prime, then $f\notin\mathfrak q$ implies $f\notin\mathfrak p$, hence $\mathfrak p\in D(f)=\{\mathfrak q\}$ and $\mathfrak p=\mathfrak q$. Thus every isolated prime is minimal.

The set of isolated primes, including the isolated closed primes counted in the source, is therefore a subset of the finite set of minimal primes from step 2, and is finite. (`minimalPrimes.finite_of_isNoetherianRing` ([Mathlib source](https://github.com/leanprover-community/mathlib4/blob/master/Mathlib/RingTheory/Ideal/MinimalPrime/Noetherian.lean))).
