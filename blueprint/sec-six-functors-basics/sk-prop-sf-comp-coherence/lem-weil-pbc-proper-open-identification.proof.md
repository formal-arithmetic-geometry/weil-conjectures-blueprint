+++
kind  = "proof"
of    = "lem-weil-pbc-proper-open-identification"
+++
By [lem-weil-pbc-proper-open-section] the morphism $s$ is an
open immersion with $ps=\operatorname{id}_X$ and closed image in
$V$, and $b s=j_1$; hence $j_{1!}=b_!s_!$, and the restriction
$b^{-1}b_!$ being the identity for the open immersion $b$, the
restriction of the extension by zero of
[def-weil-pbc-extension-by-zero] gives
$b^{-1}j_{1!}K=s_!K$. Applying
[lem-weil-pbc-derived-open-restriction] to the morphism
$u:T_1\to T_2$, the open immersion $j_2:X\hookrightarrow T_2$ and
the object $j_{1!}K$ of the derived category, the fibre product
there being $V=T_1\times_{T_2}X$ with maps $b$ and $p$,
identifies $j_2^{-1}Ru_*j_{1!}K$ with $Rp_*b^{-1}j_{1!}K$, the
derived direct image being that of
[def-weil-pbc-direct-image]. Substituting the previous
identification gives $j_2^{-1}Ru_*j_{1!}K\cong Rp_*s_!K$, and
[lem-weil-pbc-clopen-section-direct-image] gives
$Rp_*s_!K\cong K$; the composite of these identifications is the
specified isomorphism $\theta_{u,K}$ named in
[def-weil-pbc-proper-open-comparison].
