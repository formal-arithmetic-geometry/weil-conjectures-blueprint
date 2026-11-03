+++
id = "prose-03-02"
kind = "hidden"
title = "Derived functors"
order = 216
+++
Four of the six operations, $f^*$, $Rf_*$, $\otimes^{\mathbf L}$ and
internal Hom, exist for every condensed ring $\Lambda$ on the whole unbounded
derived categories by the usual resolutions. The remaining two need more work: $Rf_!$ is built
from proper direct image and extension by zero
(Section [sec-Direct-image-with-compact-support]), and its right adjoint comes from Brown
representability.

Sheaves of $\Lambda_X$-modules can be viewed as module objects over the
ring object $\Lambda_X$ in $\Sh(X_{\mathrm{pro}\acute{e}t},\operatorname{Ab})$, with the tensor product
over $\Lambda_X$ given by the coequalizer of the two actions
$M\otimes\Lambda_X\otimes N\rightrightarrows M\otimes N$. The category of
$\Lambda_X$-modules is Grothendieck abelian. Hence complexes have K-injective
resolutions, which define $Rf_*$ and $\cHom$ [Stacks, [07A5](https://stacks.math.columbia.edu/tag/07A5), [08J7](https://stacks.math.columbia.edu/tag/08J7)]. They also
have K-flat resolutions, which define $\otimes^{\mathbf L}$, and
$K\otimes^{\mathbf L}-$ is left adjoint to $\cHom(K,-)$ [Stacks, [06YL](https://stacks.math.columbia.edu/tag/06YL)].

The pullback of a $\Lambda_Y$-module $M$ along $f:X\to Y$ is
$f^*M=\Lambda_X\otimes_{f^{-1}\Lambda_Y}f^{-1}M$. Since
$f^{-1}\Lambda_Y\simeq\Lambda_X$ (Lemma [lemma-inverse-image-coefficient-sheaves]), this is just $f^{-1}M$. Therefore $f^*:\operatorname{Mod}(Y_{\mathrm{pro}\acute{e}t},\Lambda)\to
\operatorname{Mod}(X_{\mathrm{pro}\acute{e}t},\Lambda)$ is exact, and on derived
categories it is left adjoint to $Rf_*:D(X_{\mathrm{pro}\acute{e}t},\Lambda)\to
D(Y_{\mathrm{pro}\acute{e}t},\Lambda)$. For an open immersion $j:U\to X$, extension by
zero $j_!:\operatorname{Mod}(U_{\mathrm{pro}\acute{e}t},\Lambda)\to\operatorname{Mod}(X_{\mathrm{pro}\acute{e}t},\Lambda)$ is
exact and left adjoint to $j^*$.

For a locally closed immersion
$a:S\hookrightarrow X$, we factor $a=i\circ j$ with $j:S\hookrightarrow\overline S$ the open
immersion into the closure and $i:\overline S\hookrightarrow X$ the closed
immersion, and we put
$a_!=i_*j_!:\operatorname{Mod}(S_{\mathrm{pro}\acute{e}t},\Lambda)\to\operatorname{Mod}(X_{\mathrm{pro}\acute{e}t},\Lambda)$.
Since $j_!$ and $i_*$ are exact, so is $a_!$, and therefore it induces
$a_!:D(S_{\mathrm{pro}\acute{e}t},\Lambda)\to D(X_{\mathrm{pro}\acute{e}t},\Lambda)$ without deriving.
