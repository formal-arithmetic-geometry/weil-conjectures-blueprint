+++
kind  = "proof"
of    = "def-sfb-modobj-linearization-right-adjoint"
+++
Transposing along $P\dashv G$ turns the naturality, unit and associativity compatibilities
of $\pi$ ([def-sfb-projection-formula]) into the following properties of $\theta$:
- $\theta$ is natural in $L$ and $N$;
- with $\varepsilon^S\colon\mathbf 1\to S\mathbf 1$ the unit structure map of $S$,
  $G(\lambda_N)\circ\theta_{\mathbf 1,N}\circ(\varepsilon^S\otimes GN)=\lambda_{GN}$;
- with $\mu^S$ the lax structure maps of $S$,
  $G(\alpha_{L,L',N})\circ\theta_{L\otimes L',N}\circ(\mu^S_{L,L'}\otimes GN)
  =\theta_{L,L'\otimes N}\circ(SL\otimes\theta_{L',N})\circ\alpha_{SL,SL',GN}$.

These are the unit and associativity axioms of the lax structure of a lax monoidal
functor, with $\theta$ in place of the structure maps. The module axioms
for $GN$ and the linearity of $Gf$ then follow exactly as in the case of a lax monoidal
functor.
