+++
kind  = "proof"
of    = "lem-sfb-modobj-cokernels"
+++
Since $\mathcal R\otimes-$ preserves cokernels and $\mathcal R\otimes0=0$, the morphism
$\mathcal R\otimes\pi$ is a cokernel of $\mathcal R\otimes f$. Moreover
$\pi\gamma_N(\mathcal R\otimes f)=\pi f\gamma_M=0$. So $\pi\gamma_N$ factors uniquely through
$\mathcal R\otimes\pi$, which gives $\gamma_Q$.

For the unit axiom, precompose with $\mathbf 1\otimes\pi$. This is an epimorphism, since it
agrees with $\pi$ up to the unitors. Then
$$
\gamma_Q(\eta\otimes Q)(\mathbf 1\otimes\pi)=\gamma_Q(\mathcal R\otimes\pi)(\eta\otimes N)
=\pi\gamma_N(\eta\otimes N)=\pi\lambda_N=\lambda_Q(\mathbf 1\otimes\pi).
$$
For associativity, precompose with $(\mathcal R\otimes\mathcal R)\otimes\pi$. Through the
associator it is identified with $\mathcal R\otimes(\mathcal R\otimes\pi)$, which is an
epimorphism because $\mathcal R\otimes-$ preserves epimorphisms. After this
precomposition, both sides become $\pi\gamma_N(\mu\otimes N)
=\pi\gamma_N(\mathcal R\otimes\gamma_N)\alpha$, by the module axioms for $N$.

Let $g\colon N\to L$ be a morphism of module objects with $gf=0$, and let
$h\colon Q\to L$ be its factorization in $\mathcal C$, so $h\pi=g$. Then
$$
h\gamma_Q(\mathcal R\otimes\pi)=h\pi\gamma_N=g\gamma_N=\gamma_L(\mathcal R\otimes g)
=\gamma_L(\mathcal R\otimes h)(\mathcal R\otimes\pi).
$$
Since $\mathcal R\otimes\pi$ is an epimorphism, $h$ is a morphism of module objects. It is
unique because $\pi$ is an epimorphism.
