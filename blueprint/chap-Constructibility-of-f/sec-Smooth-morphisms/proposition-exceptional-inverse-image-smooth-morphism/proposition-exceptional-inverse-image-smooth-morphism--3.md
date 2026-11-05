+++
id = "proposition-exceptional-inverse-image-smooth-morphism--3"
kind = "proposition"
title = "Dualizing complex on a chart"
order = 561004
aliases = ["bp-r169-3"]
lean = []
uses = ["lemma-affine-space-etale-localization", "proposition-exceptional-inverse-image-smooth-morphism--1"]
+++
The named Tate-twist identification on a chart is bypassed by the Lean route
at this stage, which uses the shifted rank-one local system of
[proposition-exceptional-inverse-image-smooth-morphism--1].

The chart formula retained in part (1) of the human statement is
$$
\omega_f|_U\simeq A_U(d)[2d].
$$
The formalized smooth-duality argument does not choose this identification;
it descends the rank-one shape and the canonical tensor map instead.
