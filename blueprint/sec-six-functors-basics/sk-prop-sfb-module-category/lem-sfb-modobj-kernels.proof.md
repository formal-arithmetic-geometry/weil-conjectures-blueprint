+++
kind  = "proof"
of    = "lem-sfb-modobj-kernels"
+++
The tensor product is additive in each variable, so $\mathcal R\otimes0=0$. Hence
$$
f\gamma_M(\mathcal R\otimes\iota)=\gamma_N(\mathcal R\otimes f\iota)=\gamma_N(\mathcal R\otimes0)=0 .
$$
So $\gamma_M(\mathcal R\otimes\iota)$ factors uniquely through $\iota$, which gives
$\gamma_K$. The unit and associativity axioms for $\gamma_K$ hold after composition with the
monomorphism $\iota$, because they hold for $\gamma_M$. Hence they hold for $\gamma_K$.

Let $g\colon L\to M$ be a morphism of module objects with $fg=0$, and let
$h\colon L\to K$ be its factorization in $\mathcal C$, so $\iota h=g$. Then
$$
\iota h\gamma_L=g\gamma_L=\gamma_M(\mathcal R\otimes g)
=\gamma_M(\mathcal R\otimes\iota)(\mathcal R\otimes h)=\iota\gamma_K(\mathcal R\otimes h).
$$
Since $\iota$ is a monomorphism, $h$ is a morphism of module objects. It is unique because
$\iota$ is a monomorphism.
