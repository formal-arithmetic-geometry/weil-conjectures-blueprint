+++
kind = "proof"
of = "sk-prop-pe-replete"
+++
Evaluate the sequence on a weakly contractible $W$. Since every cover of
$W$ splits, the transition maps $F_{n+1}(W)\to F_n(W)$ are surjective. Given a section at stage
$m$, we choose lifts successively at stages $m+1,m+2,\ldots$ (by countable
choice), while the earlier stages are determined by the transition maps.
This gives a compatible section of $\varprojlim_nF_n(W)$. Since limits
are computed on sections, the projection is surjective on $W$.

An arbitrary $U$ is covered by affine weakly contractible objects, so
every section of $F_m$ over $U$ lifts to $\varprojlim_nF_n$ on each
member of such a cover. Hence the projection is an epimorphism of
sheaves; see
[bhatt-scholze15, §§3.1–3.2].
