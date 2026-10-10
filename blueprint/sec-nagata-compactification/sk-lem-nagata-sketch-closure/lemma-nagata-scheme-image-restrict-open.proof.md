+++
kind  = "proof"
of    = "lemma-nagata-scheme-image-restrict-open"
+++
The inclusion $W\hookrightarrow Y$ is an open immersion, hence flat, and
$g_W$ is the base change of the quasi-compact morphism $g$ along it. By
[lemma-nagata-dense-flat-pullback], $\ker(g_W)$ is the ideal sheaf of the
closed subscheme $\operatorname{SIm}(g)\times_YW\hookrightarrow W$. By
[def-nagata-extended-ideal] this is the extended ideal
$\ker(g)\mathcal O_W$, and along an open immersion the extended ideal of a
quasi-coherent ideal is its restriction: on an affine open
$\operatorname{Spec}(A)\subseteq W$ the extension of $\ker(g)(\operatorname{Spec}A)$
along the identity of $A$ is itself. Hence $\ker(g_W)=\ker(g)|_W$. Closed
subschemes of $W$ with the same ideal sheaf coincide, compatibly with their
inclusions into $W$, which gives the displayed isomorphism.
