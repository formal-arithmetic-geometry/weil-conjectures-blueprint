+++
id = "def-sfb-modobj-internal-hom"
kind = "definition"
title = "Internal hom of module objects"
order = 1107
uses = ["def-sfb-modobj-symmetric-tensor", "lem-sfb-modobj-abelian"]
lean = ["CategoryTheory.Mod.monoidalClosed"]
+++
Let $\mathcal C$ be a closed symmetric monoidal Grothendieck abelian category whose tensor
product is additive in each variable. Write $\underline{\Hom}(X,-)$ for the right adjoint
of $X\otimes-$ and $\mathrm{ev}\colon X\otimes\underline{\Hom}(X,Y)\to Y$ for the counit.
Let $\mathcal R$ be a commutative monoid object. For $\mathcal R$-module objects $M$ and
$N$, let $\Hom_{\mathcal R}(M,N)$ be the equalizer of the two maps
$$
\underline{\Hom}(M,N)\rightrightarrows\underline{\Hom}(\mathcal R\otimes M,N)
$$
adjoint to the two composites
$$
\mathcal R\otimes M\otimes\underline{\Hom}(M,N)\xrightarrow{\mathcal R\otimes\mathrm{ev}}
\mathcal R\otimes N\xrightarrow{\gamma_N}N,
\qquad
\mathcal R\otimes M\otimes\underline{\Hom}(M,N)\xrightarrow{\gamma_M\otimes1}
M\otimes\underline{\Hom}(M,N)\xrightarrow{\mathrm{ev}}N .
$$
Let $\mathcal R$ act on $\Hom_{\mathcal R}(M,N)$ through its action on $N$. Then
$\Hom_{\mathcal R}(M,-)$ is right adjoint to $M\otimes_{\mathcal R}-$, so the symmetric
monoidal category $(\Mod_{\mathcal R}(\mathcal C),\otimes_{\mathcal R})$ of
[def-sfb-modobj-symmetric-tensor] is closed. Here $\Mod_{\mathcal R}(\mathcal C)$ is
abelian by [lem-sfb-modobj-abelian].
