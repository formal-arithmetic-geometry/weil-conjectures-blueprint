+++
id = "lem-weil-pbc-fibre-ring-primes-residue-fields"
kind = "lemma"
title = "Primes and residue fields of the fibre ring"
lean = ["PrimeSpectrum.fibre_primes_residue_fields"]
order = 1738
+++
Let $\varphi:A\to B$ be a homomorphism of commutative rings, $\mathfrak p\subset A$ a prime ideal with residue field $\kappa(\mathfrak p)=A_{\mathfrak p}/\mathfrak pA_{\mathfrak p}$, $C=B\otimes_A\kappa(\mathfrak p)$ the fibre ring and $j:B\to C$, $b\mapsto b\otimes1$. For a prime $\mathfrak q\subset B$ with $\varphi^{-1}(\mathfrak q)=\mathfrak p$ let $\kappa(\mathfrak q)=B_{\mathfrak q}/\mathfrak qB_{\mathfrak q}$ and let $\psi_{\mathfrak q}:C\to\kappa(\mathfrak q)$ be the ring map $b\otimes\lambda\mapsto\bar b\,\bar\lambda$, where $\bar b$ is the image of $b$ and $\bar\lambda$ the image of $\lambda$ under the map $\kappa(\mathfrak p)\to\kappa(\mathfrak q)$ induced by $\varphi$. Then (1) the map $\mathfrak Q\mapsto j^{-1}(\mathfrak Q)$ is a bijection from the set of prime ideals of $C$ onto the set of prime ideals $\mathfrak q\subset B$ with $\varphi^{-1}(\mathfrak q)=\mathfrak p$, with inverse $\mathfrak q\mapsto\ker\psi_{\mathfrak q}$, and it preserves and reflects inclusions; (2) for each such $\mathfrak q$, with $\mathfrak Q=\ker\psi_{\mathfrak q}$, the map $\psi_{\mathfrak q}$ induces an isomorphism of fields $\kappa(\mathfrak Q)=C_{\mathfrak Q}/\mathfrak QC_{\mathfrak Q}\xrightarrow{\sim}\kappa(\mathfrak q)$; in other words $\psi_{\mathfrak q}$ is the composite of $C\to\kappa(\mathfrak Q)$ with this isomorphism.
