+++
id = "definition-trace-map-affine-line"
kind = "definition"
title = "Trace map of the affine line"
order = 722
uses = ["lemma-cohomology-projective-line-trace", "proposition-ell-adic-cycle-class-diagonal"]
+++
The *trace map of the affine line* is the composite

$$
\operatorname{Tr}_p:Rp_!\Lambda_{\mathbf A^1_Y}(1)[2]
\simeq Rq_*j_!\Lambda_{\mathbf A^1_Y}(1)[2]
\longrightarrow Rq_*\Lambda_{\mathbf P^1_Y}(1)[2]
\xrightarrow{\ \operatorname{Tr}_q\ }\Lambda_Y,
\tag{9.1}
$$

where the first arrow is induced by the counit $j_!j^*\to\mathrm{id}$ and
$\operatorname{Tr}_q$ is the trace map of the projective line: for finite
$\Lambda$ it is the map (6.3) of
Lemma [lemma-cohomology-projective-line-trace] for the projection $q$, and
otherwise it is the trace of
Proposition [proposition-ell-adic-cycle-class-diagonal].
