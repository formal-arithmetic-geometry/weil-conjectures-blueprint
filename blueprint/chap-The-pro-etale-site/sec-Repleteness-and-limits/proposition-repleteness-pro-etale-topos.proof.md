+++
kind = "proof"
of = "proposition-repleteness-pro-etale-topos"
order = 86
uses = ["definition-ind-etale-pro-etale-weakly", "definition-w-local-w-strictly-local", "lemma-w-contractible-affines-projective", "theorem-enough-affine-weakly-contractible-objects", "definition-weak-contractibility"]
+++
Evaluate the sequence on a weakly contractible $W$. Since every
epimorphism of sheaves is surjective on sections over $W$, the transition
maps $F_{n+1}(W)\to F_n(W)$ are surjective. Given a section at stage $m$,
we choose lifts successively at stages $m+1,m+2,\ldots$ (by countable
choice), while the earlier stages are determined by the transition maps.
This gives a compatible section of $\varprojlim_nF_n(W)$. Since limits
are computed on sections, the projection is surjective on $W$.

An arbitrary $U$ is covered by affine weakly contractible objects, so
every section of $F_m$ over $U$ lifts to $\varprojlim_nF_n$ on each
member of such a cover. Hence the projection is an epimorphism of
sheaves; see
[bhatt-scholze15, §§3.1–3.2].
