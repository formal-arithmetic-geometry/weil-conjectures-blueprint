+++
kind  = "proof"
of    = "lemma-nagata-scheme-image-universal"
uses = ["def-nagata-scheme-image-factor", "def-nagata-scheme-theoretic-closure", "def-nagata-scheme-theoretic-image", "lemma-nagata-scheme-image-ideal-qc", "lemma-nagata-scheme-image-of-closed-immersion"]
+++
The factorization equality is `Scheme.Hom.toImage_imageι`.
Let $\mathcal I_Z$ be the ideal of $Z$. From
$z\circ h=g$ every local section of $\mathcal I_Z$ maps to zero under $g$,
so $\mathcal I_Z\subseteq\operatorname{ker}(g)$. The induced quotient map
therefore gives a closed immersion
$c_{g,Z}\colon\operatorname{SIm}(g)\to Z$; its composite with $z$ is the
image inclusion by construction. If $c'$ is another compatible map, then
composing both $c'$ and $c_{g,Z}$ with the closed immersion $z$ gives the
same image inclusion

$$
z\circ c'=g_{\mathrm{im}}=z\circ c_{g,Z}.
$$

A closed immersion is a monomorphism, so cancellation of $z$ gives
$c'=c_{g,Z}$.
