+++
kind  = "proof"
of    = "lemma-nagata-scheme-image-partial-section"
uses = ["def-nagata-extended-ideal", "lem-weil-pbc-closed-immersion-from-composite", "lemma-nagata-dense-flat-pullback", "lemma-nagata-open-immersion-qc-over-separated-target", "lemma-nagata-scheme-image-of-closed-immersion"]
+++
By [lemma-nagata-scheme-image-restrict-open], restriction to
$U\times_SY$ commutes with taking the scheme-theoretic image. On this
open target the original map is a section of
$U\times_SY\to U$. That projection is separated, so its section is a
closed immersion. By
[lemma-nagata-scheme-image-of-closed-immersion], its
scheme-theoretic image is canonically its source, compatibly with the
projection to $U$.
