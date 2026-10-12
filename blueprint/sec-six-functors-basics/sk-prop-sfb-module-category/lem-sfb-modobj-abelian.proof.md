+++
kind  = "proof"
of    = "lem-sfb-modobj-abelian"
+++
Since $\mathcal R\otimes-$ is additive, sums and negatives of morphisms of module objects
are again morphisms of module objects. So the morphism groups of $\mathcal C$ make
$\Mod_{\mathcal R}(\mathcal C)$ preadditive. The zero object of $\mathcal C$ with the zero
action is a zero object. The biproduct $M\oplus N$, with the action whose components are
$\gamma_M$ and $\gamma_N$, is a biproduct in $\Mod_{\mathcal R}(\mathcal C)$. Kernels and
cokernels exist and are computed in $\mathcal C$ by [lem-sfb-modobj-kernels] and
[lem-sfb-modobj-cokernels].

It remains to show that for every morphism $f$ the canonical map
$\operatorname{coim}f\to\operatorname{im}f$ is an isomorphism. The forgetful functor
preserves kernels and cokernels, so it sends this map to the canonical map
$\operatorname{coim}f\to\operatorname{im}f$ of $\mathcal C$, which is invertible because
$\mathcal C$ is abelian. A morphism $e$ of module objects with invertible underlying
morphism is an isomorphism, because $e^{-1}$ is again a morphism of module objects:
$$
\gamma_M(\mathcal R\otimes e^{-1})=e^{-1}e\gamma_M(\mathcal R\otimes e^{-1})
=e^{-1}\gamma_N(\mathcal R\otimes e)(\mathcal R\otimes e^{-1})=e^{-1}\gamma_N .
$$
A preadditive category with finite biproducts, kernels and cokernels in which every
coimage-image comparison is invertible is abelian.
