+++
kind = "proof"
of = "sk-prop-pe-replete"
+++
Evaluate the sequence on a weakly contractible $W$ [sk-def-pe-weak-contractible]; the
transitions $F_{n+1}(W)\to F_n(W)$ are then surjective. Given a section at stage $m$,
choose lifts successively at stages $m+1,m+2,\ldots$ (by countable choice); the earlier
stages are determined by the transition maps. This gives a compatible section of
$\varprojlim_nF_n(W)$, and since limits are computed sectionwise, the projection is
surjective on $W$ ([det-pe-replete-on-contractible]).

An arbitrary $U$ is covered by affine weakly contractible objects
[sk-thm-pe-weakly-contractible-basis], and the construction on each member of the cover
gives compatible lifts at all stages. Hence the projection is an epimorphism of sheaves
([det-pe-replete-epimorphism]); see Bhatt–Scholze, §§3.1–3.2.
