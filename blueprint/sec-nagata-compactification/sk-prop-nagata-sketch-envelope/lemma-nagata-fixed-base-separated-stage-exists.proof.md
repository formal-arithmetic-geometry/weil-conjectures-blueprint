+++
kind  = "proof"
of    = "lemma-nagata-fixed-base-separated-stage-exists"
+++
Since $X_{\alpha_1}$ is quasi-compact for one fixed index $\alpha_1$, its
image meets only finitely many affine opens $V_1,\dots,V_n$ of $S$ covering
it, and every $X_\alpha$ with $\alpha\ge\alpha_1$ maps into
$V_1\cup\dots\cup V_n$. Separatedness is local on the target, so it suffices
to treat each $V_k$ separately: it is enough that the preimage of $V_k$ in
$X_\alpha$ is a separated scheme, since $V_k$ is affine. That preimage in
$X$ is separated, because $X\to S$ is separated and $V_k$ is affine, and it
is the limit of the preimages of $V_k$ in the $X_\alpha$, a cofiltered system
of qcqs schemes with affine transition maps. So
[lemma-nagata-separated-stage-exists-absolute] applies to each of the
finitely many $k$, and a common lower bound of the resulting indices is the
required $\alpha_0$.
