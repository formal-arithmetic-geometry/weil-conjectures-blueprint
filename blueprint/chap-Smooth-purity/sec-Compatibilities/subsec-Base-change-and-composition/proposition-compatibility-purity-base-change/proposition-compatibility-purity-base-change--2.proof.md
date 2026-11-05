+++
kind = "proof"
of = "proposition-compatibility-purity-base-change--2"
order = 797005
uses = ["proposition-compatibility-purity-base-change--1", "proposition-sp-tower-geometric", "lemma-sp-tower-adjunction-foundation"]
+++
The blueprint argument carries the finite identity of
[proposition-compatibility-purity-base-change--1] to compatible towers and
applies $R\varprojlim$, using [proposition-sp-tower-geometric] and
[lemma-sp-tower-adjunction-foundation]. This passage of the chosen purity
maps is bypassed by the Lean route. Lean uses reduction modulo $\ell$ to
check that an integral exceptional base change map is an isomorphism;
it does not deduce the displayed equality of integral purity maps.
