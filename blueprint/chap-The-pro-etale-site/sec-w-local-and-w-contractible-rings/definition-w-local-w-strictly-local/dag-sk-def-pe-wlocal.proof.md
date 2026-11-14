+++
kind = "proof"
of = "dag-sk-def-pe-wlocal"
tags = ["sheaf-dag"]
+++
1. The affine setup uses `def-weil-affine-spectrum`: for a commutative ring R, Spec(R) is represented by its prime-spectrum space. The stated quasi-compact and quasi-separated background is supplied by `lem-weil-pbc-affine-scheme-qcqs`, and `lem-weil-pbc-qcqs-scheme-spectral` places its underlying space in the spectral-space framework of `def-weil-spectral-space`. These are the ambient facts for the definitions below.
2. The Lean class `WLocalSpace X` extends `SpectralSpace X` and adds `eq_of_specializes`, which says that any two closed specializations of one point are equal, together with `isClosed_closedPoints`, which says that the set of closed points is closed. Thus, with the existence of closed specializations supplied by the inherited spectral-space structure, these fields encode exactly the w-local condition.
3. For a ring R, `IsWLocalRing R` is defined by the single field `wLocalSpace_primeSepectrum : WLocalSpace (PrimeSpectrum R)`. By `def-weil-affine-spectrum`, this is precisely the assertion that Spec(R) is w-local; the Lean binder is even general enough to allow a commutative semiring.
4. The class `IsWStrictlyLocalRing R` extends `IsWLocalRing R` and adds, for every maximal ideal m, the field `isStrictlyHenselianLocalRing_localization` asserting `IsStrictlyHenselianLocalRing (Localization.AtPrime m)`. Here `Localization.AtPrime m` is the localization at the prime ideal m from `def-weil-pbc-localization-at-prime`. Consequently the class packages w-locality together with strict henselianity at every maximal localization.
5. Finally, `IsWContractibleRing R` extends `IsWStrictlyLocalRing R` and adds the field `extremallyDisconnected_connectedComponents : ExtremallyDisconnected (ConnectedComponents (PrimeSpectrum R))`. This is exactly the extra extremal-disconnectedness condition in the definition of w-contractibility, so the four Lean declarations together encode the stated hierarchy.
