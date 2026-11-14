+++
kind = "proof"
of = "dag-lem-pe-coefficient-comparison-derived-functor"
tags = ["sheaf-dag"]
+++
1. the constant-sheaf adjunction identifies the pullback constant ring with the
specified pro-etale constant ring, and its unit is the constant-section map defining
our inverse image. The module inverse-image comparison identifies the underlying
additive sheaf with the additive inverse image. Representable flatness gives left
exactness there, and the conservative module forgetful functor reflects finite
limits. The module pullback is a left adjoint, so preserves finite colimits and
zero morphisms; left exactness then gives additivity. The exact-functor localization
of Mathlib sends quasi-isomorphisms to isomorphisms and supplies the displayed
natural factorization through the standard derived localization. (uses `lem-weil-pbc-module-inverse-image-unit-comparison`)

Proof dependencies not drawn: `lem-weil-pbc-module-inverse-image-unit-comparison`.
