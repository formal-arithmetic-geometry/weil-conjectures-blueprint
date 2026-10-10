+++
kind  = "proof"
of    = "lemma-nagata-scheme-image-transport-strict-transform"
+++
Restriction of scheme-theoretic image to $U\times_SY$ identifies the image
there with the image of $h|_U$ by
[lemma-nagata-scheme-image-restrict-open]. Work on an affine chart of
$X'\times_SY$ on which the pulled-back center has principal equation $a$.
Write its coordinate ring as $C$ and refine the source by affine opens
$\operatorname{Spec}(B_j)$. The image ideal on this chart is
$K=\bigcap_j\ker(C\to B_j)$, so $C/K\to\prod_jB_j$ is injective; the image
of $a$ is a unit in every $B_j$ because $h$ factors through $U$. Applying
[lemma-nagata-scheme-image-affine-saturation] to the product ring
identifies the kernel on this chart with the $a$-saturation of the pulled
back image ideal. By
[prop-nagata-strict-transform-closed-fiber-product] and
[lemma-nagata-strict-transform-closure-characterization], that
quotient is precisely the strict-transform chart. The identifications are
unchanged after localization, so they agree on overlaps and glue to the
claimed global equality.
