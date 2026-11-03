+++
id = "prose-03-06"
kind = "hidden"
title = "Derived functors of module sheaves"
order = 138
+++
For every condensed ring $\Lambda$ and $f:X\to Y$, the operations
$f^*:D(Y_{\mathrm{pro}\acute{e}t},\Lambda)\to D(X_{\mathrm{pro}\acute{e}t},\Lambda)$,
$Rf_*:D(X_{\mathrm{pro}\acute{e}t},\Lambda)\to D(Y_{\mathrm{pro}\acute{e}t},\Lambda)$, and
$\otimes^{\mathbf L}$ and internal Hom on $D(X_{\mathrm{pro}\acute{e}t},\Lambda)$, are derived
functors defined on the whole unbounded derived categories. The
remaining two operations need more work: $Rf_!$ is built from
proper direct image and extension by zero
(Section [sec-brown-construction]), and its right adjoint is obtained from
Brown representability.

Sheaves of $\Lambda_X$-modules can be viewed as module objects over the
ring object $\Lambda_X$ in $\Sh(X_{\mathrm{pro}\acute{e}t},\operatorname{Ab})$, with the tensor product
over $\Lambda_X$ given by the coequalizer of the two actions
$M\otimes\Lambda_X\otimes N\rightrightarrows M\otimes N$. The category of
$\Lambda_X$-modules is Grothendieck abelian, so complexes have K-injective
resolutions, which define $Rf_*$ and $\cHom$ [Stacks, Tag 07A5](https://stacks.math.columbia.edu/tag/07A5), [Stacks, Tag 08J7](https://stacks.math.columbia.edu/tag/08J7), and K-flat resolutions, which define $\otimes^{\mathbf L}$ with
$K\otimes^{\mathbf L}-$ left adjoint to $\cHom(K,-)$ [Stacks, Tag 06YL](https://stacks.math.columbia.edu/tag/06YL).

The pullback of a $\Lambda_Y$-module $M$ along $f:X\to Y$ is
$f^*M=\Lambda_X\otimes_{f^{-1}\Lambda_Y}f^{-1}M$. Since
$f^{-1}\Lambda_Y\simeq\Lambda_X$, this is just $f^{-1}M$. Therefore $f^*:\operatorname{Mod}(Y_{\mathrm{pro}\acute{e}t},\Lambda)\to \operatorname{Mod}(X_{\mathrm{pro}\acute{e}t},\Lambda)$ is exact and need not be derived, and on derived
categories it is left adjoint to $Rf_*:D(X_{\mathrm{pro}\acute{e}t},\Lambda)\to D(Y_{\mathrm{pro}\acute{e}t},\Lambda)$. For an open immersion $j:U\to X$, extension by
zero $j_!:\operatorname{Mod}(U_{\mathrm{pro}\acute{e}t},\Lambda)\to \operatorname{Mod}(X_{\mathrm{pro}\acute{e}t},\Lambda)$ is
exact and left adjoint to $j^*$.

Passing from $\mathcal O_E$ to $E$ means inverting $\ell$, and on derived
categories this is a Verdier localization.
