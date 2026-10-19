+++
kind  = "proof"
of    = "lemma-nagata-scheme-theoretic-closure-minimal"
uses = ["def-nagata-scheme-image-factor", "def-nagata-scheme-theoretic-image", "lemma-nagata-scheme-image-ideal-qc", "lemma-nagata-scheme-image-of-closed-immersion"]
+++
If $\mathcal I_Z\subseteq\ker(g)$, then
[lemma-nagata-scheme-image-universal] gives the comparison
$c_{g,Z}\colon\operatorname{SIm}(g)\to Z$ with
$z\circ c_{g,Z}=g_{\mathrm{im}}$, so $h=c_{g,Z}\circ g^{\mathrm{im}}$
satisfies $z\circ h=g_{\mathrm{im}}\circ g^{\mathrm{im}}=g$. Conversely, if
$z\circ h=g$, every local section of $\mathcal I_Z$ maps to zero in
$z_*\mathcal O_Z$, hence in $g_*\mathcal O_T$; since $\mathcal I_Z$ is
quasi-coherent and $\ker(g)$ is the largest quasi-coherent ideal in the
kernel of $\mathcal O_Y\to g_*\mathcal O_T$, we get
$\mathcal I_Z\subseteq\ker(g)$. Uniqueness of the factorization holds
because the closed immersion $z$ is a monomorphism.
