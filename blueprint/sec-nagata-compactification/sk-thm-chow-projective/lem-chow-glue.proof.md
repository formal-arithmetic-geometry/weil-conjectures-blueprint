+++
kind  = "proof"
of    = "lem-chow-glue"
uses = ["def-nagata-affine-proj", "def-nagata-dense-compactification", "def-nagata-projective-space-base-change", "def-nagata-scheme-image-factor", "def-nagata-scheme-theoretic-image", "lem-chow-agree-on-dense-open", "lem-chow-tuple-immersion", "lemma-nagata-dense-flat-pullback", "lemma-nagata-immersion-open-in-scheme-image", "lemma-nagata-scheme-image-ideal-qc"]
+++
By [lem-chow-graph](3) we have $U\subseteq V_i$ for every $i$, and
$p_i|_U\colon U\to U_i\subseteq X$ is the inclusion. Since $U$ is
scheme-theoretically dense in $Z$ and $V_i\cap V_j\subseteq Z$ is open, $U$ is
scheme-theoretically dense in $V_i\cap V_j$. The two morphisms
$p_i|_{V_i\cap V_j}$ and $p_j|_{V_i\cap V_j}$ into $X$ agree on $U$, and
$X\to S$ is separated, so they are equal by
[lem-chow-agree-on-dense-open]. Hence the $p_i|_{V_i}$ glue to
$\pi\colon X'\to X$, and $\pi|_U=\mathrm{id}_U$.
