+++
kind = "proof"
of = "dag-det-pe-wlocal-strict-contractible"
tags = ["sheaf-dag"]
+++
1. Use the w-local convention [dag-def-weil-pbc-w-local] on the spectral space `PrimeSpectrum R`. In Lean this is packaged by the class `IsWLocalRing R`, whose field is a `WLocalSpace (PrimeSpectrum R)`; thus the closed points are closed and each prime specializes to a unique closed point, equivalently each prime is contained in exactly one maximal ideal.
2. The class `IsWStrictlyLocalRing R` extends `IsWLocalRing R` and adds, for every maximal ideal `m : Ideal R`, the field `isStrictlyHenselianLocalRing_localization m` asserting `IsStrictlyHenselianLocalRing (Localization.AtPrime m)`. Since `Localization.AtPrime m` is the local ring at `m`, this is precisely the strict-henselian clause in the definition of w-strictly local.
3. Finally, `IsWContractibleRing R` extends `IsWStrictlyLocalRing R` with the field `extremallyDisconnected_connectedComponents : ExtremallyDisconnected (ConnectedComponents (PrimeSpectrum R))`. Hence the quotient space of connected components is extremally disconnected, while the preceding fields supply w-strict locality. In the w-local space, `WLocalSpace.closedPointsHomeomorph` identifies the closed-point space with `ConnectedComponents (PrimeSpectrum R)`, giving the stated equivalent formulation in terms of the extremally disconnected compact Hausdorff space of closed points.
