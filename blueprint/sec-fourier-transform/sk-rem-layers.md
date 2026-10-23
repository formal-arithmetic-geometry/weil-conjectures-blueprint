+++
id = "sk-rem-layers"
kind = "remark"
title = "The three layers, and why the order matters"
order = 3964
tags = ["sketch"]
+++
*Layer 1 (this section).* The transform and everything that follows from
the six operations and the trace formula. The properties are the ones a
kernel transform always has — it is a triangulated functor on bounded
constructible complexes, its stalks are integrals against the kernel, it
commutes with base change and with the coefficient complexes of the base,
with Tate twists, and it is invertible ([sk-thm-inversion]) — together with
the computations that the definition makes accessible: the character sheaf
itself ([sk-lem-as-properties]), the integral of a linear character
([sk-lem-wft-character-integral]), the exchange of the constant sheaf and the
skyscraper ([sk-thm-inversion]), and the numerical identities that come from
the classical finite Fourier transform ([sk-cor-plancherel]). The only
weight-flavoured statements are read off from trace functions: the character
sheaf is pure of weight zero because its traces are roots of unity, and the
$L^2$ growth parameter $\nu$ of [sk-def-wrp-l2-definition] goes up by one
under the transform because of the factor $q^n$ in Plancherel.

*Layer 2 (weight theory).* The dictionary between $\nu$ and pure weights
([sk-thm-wrp-l2-dictionary]) turns the Plancherel shift into the shift of
weights by one under the transform; purity and reality of the kernel and of
the input give the realified kernel, and the origin fibre of the transform
is identified with $H^1_c$ with its eigenvalue bound. These statements are
in the Deligne–Laumon section on the affine line.

*Layer 3 (perverse and middle-extension theory).* The perverse amplitude of
the transform and the Fourier theory of middle extensions: the concentration
statement for a nonexceptional input, and the identification at the origin.

The weight estimate on the affine line then uses layers 2 and 3 together.
Keeping the layers apart makes the estimate readable: layer 1 is formal,
layer 2 is where the arithmetic enters, layer 3 is where the geometry of the
input enters.
