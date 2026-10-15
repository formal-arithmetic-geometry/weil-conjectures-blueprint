+++
id = "det-sf-open-closed-sequence-ring-sheaf"
kind = "lemma"
title = "The open–closed sequence for module sheaves over a sheaf of rings"
uses = ["lem-exc-proetale-closed-exact", "lem-exc-proetale-closed-fully-faithful", "lem-exc-proetale-open-unit", "lem-weil-extension-by-zero-exact", "lem-weil-extension-by-zero-adjunction", "lem-exc-closed-localization", "lem-exc-closed-cover-extension", "det-sf-open-closed-pullback-limits"]
+++
Let $X$ be quasi-compact and quasi-separated, $j:U\hookrightarrow X$ a
quasi-compact open immersion with closed complement $i:Z\hookrightarrow X$,
and $B$ a sheaf of rings on $X_{\mathrm{proét}}$, with coefficient rings $j^*B$
on $U$ and $i^*B$ on $Z$. Then:

1. $j^*$ and $j_!$ are exact, $j_!\dashv j^*$, and the unit
$N\to j^*j_!N$ is an isomorphism;
2. $i_*$ is exact, the counit $i^*i_*G\to G$ is an isomorphism (so $i_*$ is
fully faithful), and $j^*i_*=0$;
3. for every $B$-module sheaf $M$ the sequence
$0\to j_!j^*M\to M\to i_*i^*M\to0$, formed by the counit of $j_!\dashv j^*$
and the unit of $i^*\dashv i_*$, is exact;
4. for a morphism $g:X'\to X$ with $X'$ qcqs and base changes
$j':U'\to X'$, $i':Z'\to X'$, $g_U:U'\to U$, $g_Z:Z'\to Z$, there are
canonical isomorphisms $g^*j_!\simeq j'_!g_U^*$, $g^*i_*\simeq i'_*g_Z^*$, and
$g^*$ carries the sequence of (3) for $M$ to the sequence of (3) for $g^*M$.
