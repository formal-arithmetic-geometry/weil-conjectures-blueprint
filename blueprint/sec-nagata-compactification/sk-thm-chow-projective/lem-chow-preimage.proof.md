+++
kind  = "proof"
of    = "lem-chow-preimage"
uses = ["def-nagata-affine-proj", "def-nagata-dense-compactification", "def-nagata-projective-space-base-change", "def-nagata-scheme-image-factor", "def-nagata-scheme-theoretic-image", "lem-chow-agree-on-dense-open", "lem-chow-tuple-immersion", "lemma-nagata-dense-flat-pullback", "lemma-nagata-immersion-open-in-scheme-image", "lemma-nagata-projective-space-base-change-proper", "lemma-nagata-proper-to-separated-target", "lemma-nagata-scheme-image-ideal-qc"]
+++
The inclusion $V_i\subseteq\pi^{-1}(U_i)$ holds because $\pi|_{V_i}=p_i|_{V_i}$
takes values in $U_i$. The morphism $p_i|_{V_i}\colon V_i\to U_i$ is proper,
being the base change of the proper morphism $p_i$ along the open immersion
$U_i\to Z_i$. The open subscheme $\pi^{-1}(U_i)\subseteq Z$ is separated over
$S$, hence $\pi^{-1}(U_i)\to U_i$ is separated. Applying 01W6
to the commutative triangle formed by $V_i\to\pi^{-1}(U_i)$ and the two
morphisms to $U_i$, we conclude that $V_i\to\pi^{-1}(U_i)$ is universally
closed; in particular $V_i$ is closed in $\pi^{-1}(U_i)$. On the other hand
$U\subseteq V_i$ and $U$ is dense in the open subscheme
$\pi^{-1}(U_i)\subseteq Z$, so $V_i$ is dense in $\pi^{-1}(U_i)$. Being closed
and dense, $V_i=\pi^{-1}(U_i)$.
