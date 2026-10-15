+++
kind = "proof"
of = "det-prop-sfb-module-pullback-exact-lifted"
+++
**Additivity.** The abelian group structure on Hom-sets of module objects is that of the
underlying Hom-sets (sums of module maps are module maps because $\otimes$ is additive), so the
forgetful functors are additive. For module maps $a,b$,
$U_{\mathcal S}G(a+b)=F(U_{\mathcal R}a+U_{\mathcal R}b)=U_{\mathcal S}(Ga+Gb)$, and $U_{\mathcal S}$ is
faithful ([lem-sfb-modobj-forget-faithful]), so $G(a+b)=Ga+Gb$.

**$U_{\mathcal S}$ reflects kernels.** Let $\varphi\colon M\to N$ and $\kappa\colon K\to M$ be morphisms
of $\mathcal S$-modules with $\varphi\kappa=0$ such that $U\kappa$ is a kernel of $U\varphi$ in
$\mathcal D$. If $\psi\colon P\to M$ is a module map with $\varphi\psi=0$, there is a unique $u$ in
$\mathcal D$ with $\kappa u=\psi$. Then
$\kappa\circ u\gamma_P=\psi\gamma_P=\gamma_M(\mathcal S\otimes\psi)=\gamma_M(\mathcal S\otimes\kappa)(\mathcal S\otimes u)=\kappa\circ\gamma_K(\mathcal S\otimes u)$,
and $\kappa$ is a monomorphism, so $u$ is a module map. Hence $\kappa$ is a kernel of $\varphi$ in
$\Mod_{\mathcal S}(\mathcal D)$.

**$U_{\mathcal S}$ reflects cokernels.** Dually, let $\pi\colon N\to Q$ with $\pi\varphi=0$ and $U\pi$ a
cokernel of $U\varphi$. For a module map $\psi\colon N\to P$ with $\psi\varphi=0$ write $\psi=u\pi$ in
$\mathcal D$. Then
$u\gamma_Q(\mathcal S\otimes\pi)=u\pi\gamma_N=\psi\gamma_N=\gamma_P(\mathcal S\otimes\psi)=\gamma_P(\mathcal S\otimes u)(\mathcal S\otimes\pi)$.
Since $\mathcal S\otimes-$ is right exact, it preserves epimorphisms, so $\mathcal S\otimes\pi$ is an
epimorphism and $u\gamma_Q=\gamma_P(\mathcal S\otimes u)$. Hence $\pi$ is a cokernel in
$\Mod_{\mathcal S}(\mathcal D)$.

**Exactness of $G$.** Let $\kappa$ be a kernel of $\varphi$ in $\Mod_{\mathcal R}(\mathcal C)$. By
[lem-sfb-modobj-kernels], kernels in $\Mod_{\mathcal R}(\mathcal C)$ are computed in $\mathcal C$, so
$U_{\mathcal R}\kappa$ is a kernel of $U_{\mathcal R}\varphi$ (any two kernels are isomorphic). As $F$ is
exact, $U_{\mathcal S}G\kappa=FU_{\mathcal R}\kappa$ is a kernel of $U_{\mathcal S}G\varphi$, and by the
reflection step $G\kappa$ is a kernel of $G\varphi$. The same argument with
[lem-sfb-modobj-cokernels] shows that $G$ preserves cokernels. An additive functor between abelian
categories preserving kernels and cokernels is exact, and it preserves finite limits and finite
colimits, as these are built from finite biproducts and kernels, resp. cokernels.
