+++
kind  = "proof"
of    = "det-nagata-density-normalization-setup"
uses = ["lemma-nagata-immersion-open-in-scheme-image"]
+++
A Noetherian scheme has a Noetherian underlying space, so every open subset
of $\overline X$ is quasi-compact; in particular $\overline X$ is
quasi-separated (intersections of affine opens are quasi-compact), $j$ is
quasi-compact, and $V$ is quasi-compact. Closed subschemes of Noetherian
schemes are Noetherian, so the same holds for $Z$.

Since $j$ is a quasi-compact immersion into the quasi-separated scheme
$\overline X$, [lemma-nagata-immersion-open-in-scheme-image] shows that $j$
factors through its scheme-theoretic image $Z$ as an open immersion
$j_Z:X\to Z$ which is scheme-theoretically dense; it is quasi-compact
because $Z$ is Noetherian. This proves (1) and (2).

For (3), $j$ factors through the closed subscheme $Z$, so the underlying
set $j(X)$ lies in $Z$ and misses $V$. Hence $X\times_{\overline X}V$ is
empty. The base change of the closed immersion $i$ along $j=i\circ j_Z$ is
the closed immersion $X\times_{\overline X}Z\to X$; since $j$ factors through
$i$ and $i$ is a monomorphism, this base change is an isomorphism, i.e.
$X\times_{\overline X}Z=X$ with projection to $Z$ equal to $j_Z$.

For (4), $i$ is a closed immersion, hence proper, and $p$ is proper, so
$p\circ i$ is proper.
