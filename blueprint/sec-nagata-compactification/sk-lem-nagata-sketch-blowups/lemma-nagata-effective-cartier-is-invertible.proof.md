+++
kind  = "proof"
of    = "lemma-nagata-effective-cartier-is-invertible"
+++
Suppose $\mathcal J$ is invertible and $\alpha\colon Z\xrightarrow{\sim}V(\mathcal J)$
is an isomorphism over $X$, so that $z$ is $\alpha$ followed by the
inclusion $V(\mathcal J)\hookrightarrow X$. The ideal sheaf cut out by a
closed immersion does not change when the immersion is precomposed with an
isomorphism, and the ideal sheaf of $V(\mathcal J)\hookrightarrow X$ is
$\mathcal J$. Hence $\ker(z)=\mathcal J$ is invertible.

Conversely, suppose $\ker(z)$ is invertible and put
$\mathcal J=\ker(z)$. The closed immersions $z\colon Z\to X$ and
$V(\mathcal J)\hookrightarrow X$ have the same ideal sheaf. Since a closed
subscheme is determined by its quasi-coherent ideal sheaf — a closed
immersion $z$ factors through a closed immersion $w$ exactly when the ideal
of $w$ is contained in the ideal of $z$, and the factorization is then
unique — $z$ factors uniquely through $V(\mathcal J)$ and vice versa, and
the two factorizations are mutually inverse isomorphisms over $X$. Thus
$z$ is an effective Cartier centre.
