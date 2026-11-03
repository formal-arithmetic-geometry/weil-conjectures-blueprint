+++
id = "prose-12-03"
kind = "hidden"
title = "Frobenius and Weil complexes (2)"
order = 532
+++
A Weil structure is what remains on $T$ of the fact that a complex comes
from $T_0$, and it is the datum needed to define a Frobenius operator on
cohomology. The basic example is a complex $K$ pulled back from a complex
$K_0$ on $T_0$. Since the projection $T\to T_0$ composed with
$\operatorname{Fr}_T$ is again the projection, the pullback of $K_0$ gives a
canonical isomorphism $\operatorname{Fr}_T^*K\simeq K$.

Triangles, truncations and spectral sequences are formed in
$D^b_{\mathrm{ctf}}(T,\Lambda)$, and the Weil structures are carried along. Since
$\operatorname{Fr}_T^*$ is exact on sheaves, it commutes with standard
truncations, with the triangle of a short exact sequence of sheaves and
with the localization triangle $j_!j^*K\to K\to i_*i^*K$ for an
open immersion $j:U\to T$ obtained by base change from an open
$U_0\subset T_0$, with closed complement $i$. For such $U$ we have
$\operatorname{Fr}_T^{-1}(U)=U$, and $\operatorname{Fr}_T$ restricts to
$\operatorname{Fr}_U$ and to the Frobenius of the complement. Hence these constructions
carry Weil structures to Weil structures, and the induced long exact
cohomology sequences are Frobenius-equivariant.

If $(M,\phi_M)$ is a Weil complex on $X$ and $f:X\to Y$ comes from $f_0$
over $k_0$, the base change map for the cartesian square with horizontal
arrows $\operatorname{Fr}_X$, $\operatorname{Fr}_Y$ identifies
$\operatorname{Fr}_Y^*Rf_{!}M$ with $Rf_{!}\operatorname{Fr}_X^*M$, and the
composite

$$
\operatorname{Fr}_Y^*Rf_{!}M
\simeq Rf_{!}\operatorname{Fr}_X^*M
\xrightarrow{\ Rf_{!}(\phi_M)\ }Rf_{!}M
$$

is a Weil structure on $Rf_!M$. The same holds for $f^*$, $Rf_*$, $f^!$,
$\otimes^{\mathbf L}$ and $\cHom$, with the corresponding base change maps.
These are isomorphisms for every $f$, because $\operatorname{Fr}_X$ and
$\operatorname{Fr}_Y$ are isomorphisms of schemes, and base change along an
isomorphism is transport of structure.

For a Weil complex $(K,\phi_K)$ on $T$, the induced geometric
Frobenius operator on compactly supported cohomology is the
endomorphism

$$
\begin{gathered}
\operatorname{Frob}_{T,K}:R\Gamma_c(T_{\mathrm{pro}\acute{e}t},K)
\xrightarrow{\ \text{pullback along }\operatorname{Fr}_T\ }
R\Gamma_c(T_{\mathrm{pro}\acute{e}t},\operatorname{Fr}_T^*K)\\
\xrightarrow{\ R\Gamma_c(T_{\mathrm{pro}\acute{e}t},\phi_K)\ }
R\Gamma_c(T_{\mathrm{pro}\acute{e}t},K).
\end{gathered}
$$

When $T$ and $K$ are clear, we write $F$ for $\operatorname{Frob}_{T,K}$ and
for the endomorphisms it induces on the groups $H^i_c(T,K)$. We keep three
letters for three roles: $\operatorname{Fr}_T$ (and $\Phi_T$) for maps of
schemes, $\phi_K$ (and $\psi$ for a correspondence that need not be
invertible) for structures on complexes, and $F$ or $\operatorname{Frob}$
for the operators they induce on cohomology and on stalks.

For $r\in\mathbf Z$, write
$\Lambda(r)=\Gamma((\operatorname{Spec}k)_{\mathrm{pro}\acute{e}t}, \Lambda_{\operatorname{Spec}k}(r))$ for the Tate coefficient
module with its induced Frobenius operator. Since arithmetic Frobenius
acts on $\mu_{\ell^n}(k)$ by $\zeta\mapsto\zeta^q$, geometric Frobenius
acts on $\Lambda(1)$ by $q^{-1}$, and hence on $\Lambda(-d)$ by $q^d$.
For $X_0$ smooth of pure dimension $d$, the trace map of
Definition [sk-def-sp-trace] is, after removing the twist and by
Proposition [sk-prop-prop-sp-frobenius-purity] below, a Frobenius-equivariant map

$$
H_c^{2d}(X_{\mathrm{pro}\acute{e}t},\Lambda_X)\longrightarrow\Lambda(-d)
$$

For $X=\mathbf P^1_k$ this says that geometric Frobenius acts on
$H^2(\mathbf P^1_k,\Lambda)=\Lambda(-1)$ by $q$, as checked after
Proposition [sk-prop-geo-p1-adjunction].
