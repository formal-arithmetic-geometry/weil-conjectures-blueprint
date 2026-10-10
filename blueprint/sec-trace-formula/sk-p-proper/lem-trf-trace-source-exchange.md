+++
id = "lem-trf-trace-source-exchange"
kind = "lemma"
title = "Exchange of the trace-class sources: the kernel of the coefficient pushforward"
order = 2330
uses = ["def-exchange-projection", "def-sf-kv-maps", "def-trf-coefficient-pushforward", "def-trf-kernel-pushforward-maps", "fix-prop-adjunctions", "fix-prop-coherence", "fix-prop-projection-formula", "lem-trf-correspondence-class", "lem-trf-exceptional-internal-hom-exchange", "thm-trf-kunneth-verdier", "thm-trf-verdier-duality"]
+++
Let $(f,g):(C,c)\to(D,b)$ be a proper pushforward diagram of
[def-trf-coefficient-pushforward] (no Cartesian leg square, no properness
over $s$), with the notation and admissibility of
[def-trf-kernel-pushforward-maps]. Then the kernel class of the coefficient
pushforward $[f,g]_!u$ is the transported kernel class of $u$:

$$
[\,[f,g]_!u\,]_P
=\rho_f\circ Rq_*[u]_P\circ\Xi\circ Rb_!\eta_g
\quad:\ Rb_!A_D\longrightarrow P_Y ,
$$

where $\eta_g:A_D\to Rg_*A_C$ is the unit.
