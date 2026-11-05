+++
id = "prose-10-20"
kind = "hidden"
title = "Weil complexes (2)"
order = 877
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

For $Rf_!$ this needs a word, since $\operatorname{Fr}_X$ and
$\operatorname{Fr}_Y$ are not $k$-morphisms, while $Rf_!$ is built from
compactifications over $k$. We compute $Rf_!=R\bar f_*j_!$ with a
compactification $X\overset{j}{\hookrightarrow}\bar X\xrightarrow{\bar f}Y$
obtained by base change from a compactification of $f_0$ over $k_0$
(Theorem [theorem-nagata-s-compactification-theorem]). Then
$\operatorname{Fr}_{\bar X}$ is an automorphism of the scheme $\bar X$ with
$\operatorname{Fr}_{\bar X}^{-1}(X)=X$ and
$\bar f\operatorname{Fr}_{\bar X}=\operatorname{Fr}_Y\bar f$. For an
automorphism $h$ of a scheme, $h^*\simeq(h^{-1})_*$, so transport of
structure gives
$\operatorname{Fr}_Y^*R\bar f_*\simeq R\bar f_*\operatorname{Fr}_{\bar X}^*$
and $\operatorname{Fr}_{\bar X}^*j_!\simeq j_!\operatorname{Fr}_X^*$, and
their composite is the base change map for $Rf_!$. It does not depend on
the compactification. Indeed, two compactifications of $f_0$ are dominated
by a third, the closure of $X_0$ in their fibre product over $Y_0$, and the
refinement isomorphisms of $Rf_!$ come from proper maps over $k_0$, which
commute with the Frobenii. The map for $f^!$ is the mate of the map for
$Rf_!$, and it is an isomorphism because both functors
$\operatorname{Fr}^*$ are equivalences.

Pullback along $\operatorname{Fr}_T$ on compactly supported cohomology is
constructed in the same way. For a morphism of schemes $h:S'\to S$ and
$L\in D(S_{\mathrm{pro}\acute{e}t},\Lambda)$, the *pullback map*

$$
\operatorname{pb}_{h,L}:R\Gamma(S,L)\longrightarrow R\Gamma(S',h^*L)
$$

is $R\Gamma$ of the unit $L\to Rh_*h^*L$, followed by the identification
$R\Gamma(S,Rh_*-)=R\Gamma(S',-)$. We write $\operatorname{pb}_h$ when $L$
is clear. It is natural in $L$, and it is transitive: for $g:S'\to S$ and
$h:S''\to S'$ we have
$\operatorname{pb}_{gh,L}=\operatorname{pb}_{h,g^*L}\circ\operatorname{pb}_{g,L}$
under $(gh)^*\simeq h^*g^*$. Let $j:T\hookrightarrow\bar T$ be the base change of
a compactification of $T_0$ over $k_0$. Then $\operatorname{Fr}_{\bar T}$
is an automorphism of $\bar T$ with $\operatorname{Fr}_{\bar T}^{-1}(T)=T$,
and *pullback along $\operatorname{Fr}_T$* is the composite

$$
\operatorname{pb}_{\operatorname{Fr}_T}:
R\Gamma_c(T,K)=R\Gamma(\bar T,j_!K)
\xrightarrow{\ \operatorname{pb}_{\operatorname{Fr}_{\bar T}}\ }
R\Gamma(\bar T,\operatorname{Fr}_{\bar T}^*j_!K)
\simeq R\Gamma(\bar T,j_!\operatorname{Fr}_T^*K)
=R\Gamma_c(T,\operatorname{Fr}_T^*K).
$$

It does not depend on $\bar T$. Indeed, a refinement $\pi:\bar T'\to\bar T$
between two such compactifications comes from $k_0$, so
$\pi\operatorname{Fr}_{\bar T'}=\operatorname{Fr}_{\bar T}\pi$. Transitivity
of pullback maps for this composite, together with the base change
$\operatorname{Fr}_{\bar T}^*R\pi_*\simeq R\pi_*\operatorname{Fr}_{\bar T'}^*$
along the automorphisms $\operatorname{Fr}$ and with
$R\pi_*j'_!\simeq j_!$, shows that the refinement isomorphism
$R\Gamma(\bar T',j'_!K)\simeq R\Gamma(\bar T,R\pi_*j'_!K)
\simeq R\Gamma(\bar T,j_!K)$ carries one pullback map to the other. In the
same way, the pullback map along $\operatorname{Fr}_T^m$ is defined, and by
transitivity it is the $m$-fold composite
$\operatorname{pb}_{\operatorname{Fr}_T^m,K}=\operatorname{pb}_{\operatorname{Fr}_T,(\operatorname{Fr}_T^{m-1})^*K}\circ\cdots\circ\operatorname{pb}_{\operatorname{Fr}_T,K}$.
