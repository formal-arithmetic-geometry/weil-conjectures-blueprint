+++
kind  = "proof"
of    = "prop-nagata-dense-refinement"
+++
Write $C=(X\xrightarrow{j}\overline X\xrightarrow{p}S)$. Since $p$ is
proper, it is quasi-separated, and $j;p=f$ is quasi-compact; by
[lemma-nagata-open-immersion-qc-over-separated-target], the open immersion
$j$ is quasi-compact. Hence [lemma-nagata-immersion-open-in-scheme-image]
applies to $j$: the induced map
$j^{\mathrm{im}}\colon X\to\operatorname{SIm}(j)$ is a quasi-compact open
immersion and is scheme-theoretically dense. The new ambient scheme
$\operatorname{SIm}(j)$ is closed in $\overline X$, so it remains proper
over $S$. Finally,

$$
j^{\mathrm{im}};j_{\mathrm{im}};p
=j;p=f
$$

by the factorization of [def-nagata-scheme-image-factor]; hence the refined
factorization has the same composite as $C$.
