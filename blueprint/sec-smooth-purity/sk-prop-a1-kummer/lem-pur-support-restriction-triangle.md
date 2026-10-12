+++
id = "lem-pur-support-restriction-triangle"
kind = "lemma"
title = "Restriction triangle inside a closed support"
order = 2276
uses = ["def-pur-flasque-support", "def-pur-support-cohomology", "def-weil-open-closed-recollement", "def-weil-pbc-derived-categories", "def-weil-pbc-etale-site", "def-weil-pbc-kinjective-resolutions", "def-weil-scheme-morphism-properties"]
+++
Let $T$ be a scheme, let $B,C\subseteq T$ be
closed subschemes, and
put $V=T\setminus C$, with open immersion $v:V\hookrightarrow T$.
Let $F$ be a bounded-below complex of module sheaves on the
small etale site.
Write $R\Gamma_B(T,F)$ for the derived functor of the
sections supported on $B$,
whose cohomology is the
cohomology with support.
There is a natural distinguished triangle in the
derived category of modules:

$$
R\Gamma_{B\cap C}(T,F)\longrightarrow R\Gamma_B(T,F)
\longrightarrow R\Gamma_{B\cap V}(V,v^*F)\longrightarrow
R\Gamma_{B\cap C}(T,F)[1].
$$

The third support is closed in $V$; its ambient scheme is $V$.
