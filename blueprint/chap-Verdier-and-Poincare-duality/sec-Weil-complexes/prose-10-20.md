+++
id = "prose-10-20"
kind = "hidden"
title = "Weil complexes (2)"
order = 870
+++
A Weil structure is the datum needed to define a Frobenius operator on
cohomology. The basic example is a complex $K$ pulled back from a complex
$K_0$ on $T_0$. Since the projection $T\to T_0$ composed with
$\operatorname{Fr}_T$ is again the projection, the pullback of $K_0$ gives a
canonical isomorphism $\operatorname{Fr}_T^*K\simeq K$.

The triangles, truncations and spectral sequences we form in
$D^b_{\mathrm{ctf}}(T,\Lambda)$ are compatible with Weil structures. Since
$\operatorname{Fr}_T^*$ is exact on sheaves, it commutes with standard
truncations and with the triangle of a short exact sequence of sheaves.
It also commutes with the localization triangle $j_!j^*K\to K\to i_*i^*K$ for an
open immersion $j:U\to T$ obtained by base change from an open
$U_0\subset T_0$, with closed complement $i$. Indeed, for such $U$ we have
$\operatorname{Fr}_T^{-1}(U)=U$, and $\operatorname{Fr}_T$ restricts to
$\operatorname{Fr}_U$ and to the Frobenius of the complement. These constructions
therefore carry Weil structures to Weil structures, and the induced long exact
cohomology sequences are Frobenius-equivariant.

Let $(M,\phi_M)$ be a Weil complex on $X$ and let $f:X\to Y$ come from $f_0$
over $k_0$. The base change map for the cartesian square with horizontal
arrows $\operatorname{Fr}_X$, $\operatorname{Fr}_Y$ identifies
$\operatorname{Fr}_Y^*Rf_{!}M$ with $Rf_{!}\operatorname{Fr}_X^*M$, and the
composite

$$
\operatorname{Fr}_Y^*Rf_{!}M
\simeq Rf_{!}\operatorname{Fr}_X^*M
\xrightarrow{\ Rf_{!}(\phi_M)\ }Rf_{!}M
$$

is a Weil structure on $Rf_!M$. Likewise $f^*$, $Rf_*$, $f^!$,
$\otimes^{\mathbf L}$ and $\cHom$ carry Weil structures, via the corresponding
base change maps. These maps are isomorphisms for every $f$, because
$\operatorname{Fr}_X$ and $\operatorname{Fr}_Y$ are isomorphisms of schemes
and base change along an isomorphism is transport of structure.
