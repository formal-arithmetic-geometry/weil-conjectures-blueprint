+++
id = "proposition-fourier-inversion--2"
kind = "proposition"
title = "Fourier inversion (2)"
name_showing = false
order = 1231002
aliases = ["bp-r380-2"]
lean = []
uses = ["definition-tate-twists", "lemma-artin-schreier-character-sheaf"]
+++
This same-character inversion formula is bypassed by the Lean proof of
the main theorem: the mainline contains no corresponding natural
isomorphism, and uses inverse-character inversion and the resulting
equivalence instead.

For the vector bundle $V\to S$ of rank $r$, under $V^{\vee\vee}=V$,

$$
\operatorname{FT}_{\psi}\operatorname{FT}_\psi(K)
\simeq [-1]_V^*K(-r).
$$
