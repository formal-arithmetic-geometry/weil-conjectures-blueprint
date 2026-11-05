+++
id = "proposition-base-change-fourier-inversion--1"
kind = "proposition"
title = "Base change and stalks (1)"
name_showing = false
order = 1229002
aliases = ["bp-r379-1"]
lean = []
uses = ["proposition-topos-functoriality", "lemma-artin-schreier-character-sheaf"]
+++
This general base-change statement for vector bundles is bypassed by Lean;
the mainline uses compact-support base change directly to obtain the
rational-point formula in [proposition-base-change-fourier-inversion--3].

The proper base change isomorphism for $p_2$ induces an
isomorphism $g_{V^\vee}^*\operatorname{FT}_\psi(K)\simeq
  \operatorname{FT}_\psi(g_V^*K)$.
