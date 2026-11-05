+++
kind = "proof"
of = "lemma-scheme-frobenius-geometric-frobenius"
order = 955
+++
The maps $\Phi_X$ and $\operatorname{Fr}_X$ differ by the
absolute Frobenius, and pullback along the absolute Frobenius is
naturally the identity on étale sheaves. This gives $\kappa_m$, and we then compare the two pullback maps on one
compactification.
On coordinate rings the two maps are

$$
\Phi_X^\#(a\otimes b)=a^q\otimes b,
\qquad \operatorname{Fr}_X^\#(a\otimes b)=a\otimes b^{1/q}
$$

so that $\Phi_X=F_X\operatorname{Fr}_X$, where
$F_X$ is the absolute $q$-power Frobenius of $X$. The absolute Frobenius
commutes with every morphism of schemes over $\mathbf F_p$, so also
$\Phi_X^m=\operatorname{Fr}_X^mF_X^m$. On the classical constructible
category, pullback along absolute Frobenius is naturally isomorphic to the
identity, because for an étale object its relative Frobenius is an
isomorphism, functorial in that object. Transporting this natural
isomorphism to $D^b_{\mathrm{ctf}}(X,A)$ by the comparison with the pro-étale site,
we obtain $\theta:F_X^*\simeq\mathrm{id}$. It is compatible with pullback
along every morphism $h$, that is, $h^*\theta=\theta h^*$ under
$h^*F^*=F^*h^*$, since relative Frobenius of étale objects is
compatible with base change. Let $\theta^m:(F_X^m)^*\simeq\mathrm{id}$ be
its $m$-fold composite and put

$$
\kappa_m=\theta^m_{(\operatorname{Fr}_X^m)^*K}:
(\Phi_X^m)^*K=(F_X^m)^*(\operatorname{Fr}_X^m)^*K
\xrightarrow{\sim}(\operatorname{Fr}_X^m)^*K .
$$

Compatibility with iteration means that
$\kappa_{m+1}=\kappa_{m,\operatorname{Fr}_X^*K}\circ(\Phi_X^m)^*\kappa_1$,
and it follows from the compatibility of $\theta$ with pullback along
$\Phi_X^m$. Now $\psi_m=\phi_m\kappa_m$ follows by induction on $m$. If it
holds for $m$, then

$$
\begin{aligned}
\psi_{m+1}&=\psi_m\circ(\Phi_X^m)^*\psi
=\phi_m\circ\kappa_m\circ(\Phi_X^m)^*\phi\circ(\Phi_X^m)^*\kappa_1\\
&=\phi_m\circ(\operatorname{Fr}_X^m)^*\phi\circ\kappa_{m,\operatorname{Fr}_X^*K}\circ(\Phi_X^m)^*\kappa_1
=\phi_{m+1}\kappa_{m+1},
\end{aligned}
$$

where the third equality is the naturality of $\kappa_m$ in $K$.

For the pullback maps on compact cohomology, let $j:X\hookrightarrow\bar X$
be the base change of a compactification of $X_0$ over $k_0$, and use the
pullback maps $\operatorname{pb}_h$ of Section [sec-Weil-complexes]. The
endomorphisms $\Phi_{\bar X}$, $\operatorname{Fr}_{\bar X}$ and
$F_{\bar X}$ of the scheme $\bar X$ restrict to $\Phi_X$,
$\operatorname{Fr}_X$ and $F_X$. Each of them has inverse image $X$ of $X$,
so each commutes with $j_!$, and
$\Phi_{\bar X}^m=\operatorname{Fr}_{\bar X}^mF_{\bar X}^m$. Put
$L=j_!K$, so that $R\Gamma_c(X,K)=R\Gamma(\bar X,L)$.

First, the map $(\Phi_X^m)^*$ of
Definition [definition-frobenius-correspondences-their-operators] is
$\operatorname{pb}_{\Phi_{\bar X}^m,L}$. Indeed, $\Phi_X^m$ is finite, so
$R(\Phi_X^m)_!=R(\Phi_X^m)_*$, and the square $j\Phi_X^m=\Phi_{\bar X}^mj$
is cartesian, so $j_!R(\Phi_X^m)_*\simeq R(\Phi_{\bar X}^m)_*j_!$. Under
this isomorphism the identification
$R\Gamma_c(X,R(\Phi_X^m)_*-)=R\Gamma_c(X,-)$ used there is the composition
of direct images $R\Gamma(\bar X,R(\Phi_{\bar X}^m)_*-)=R\Gamma(\bar X,-)$,
and the unit for $\Phi_X^m$ corresponds to the unit for $\Phi_{\bar X}^m$.

Second, by transitivity,
$\operatorname{pb}_{\Phi_{\bar X}^m,L}
 =\operatorname{pb}_{F_{\bar X}^m,(\operatorname{Fr}_{\bar X}^m)^*L}\circ
 \operatorname{pb}_{\operatorname{Fr}_{\bar X}^m,L}$. The absolute Frobenius
$F_{\bar X}^m$ satisfies the hypothesis of [Stacks, [03SP](https://stacks.math.columbia.edu/tag/03SP)], since its
relative Frobenius over each étale object is an isomorphism, functorial
in that object. Since $A$ is finite, we may compute on the étale site
(Proposition [proposition-comparison-etale-derived-category]). There
the formal argument of [Stacks, [03SP](https://stacks.math.columbia.edu/tag/03SP)] identifies $(F_{\bar X}^m)_*$ and
$(F_{\bar X}^m)^{-1}$ with the identity functors of the topos, compatibly
with the unit, and this identification is $\theta^m$, since both come from
the relative Frobenius isomorphisms of étale objects. Hence for every
$N\in D^b_{\mathrm{ctf}}(\bar X,A)$ the pullback map
$\operatorname{pb}_{F_{\bar X}^m,N}$ followed by
$R\Gamma(\bar X,\theta^m_N)$ is the identity of $R\Gamma(\bar X,N)$. With $N=(\operatorname{Fr}_{\bar X}^m)^*L$
this gives

$$
R\Gamma_c(X,\kappa_m)\circ(\Phi_X^m)^*=\operatorname{pb}_{\operatorname{Fr}_X^m} .
$$

Finally, the naturality of $\operatorname{pb}_{\operatorname{Fr}_X}$ moves the maps
$R\Gamma_c(X,(\operatorname{Fr}_X^i)^*\phi)$ past the pullback maps, and
transitivity gives
$\operatorname{Frob}_{X,K}^m=R\Gamma_c(X,\phi_m)\circ\operatorname{pb}_{\operatorname{Fr}_X^m}$.
Hence

$$
T_{c_m}(\psi_m)=R\Gamma_c(X,\phi_m)\circ R\Gamma_c(X,\kappa_m)\circ(\Phi_X^m)^*
=R\Gamma_c(X,\phi_m)\circ\operatorname{pb}_{\operatorname{Fr}_X^m}
=\operatorname{Frob}_{X,K}^m .
$$

The same computation with an arbitrary morphism
$\chi:(\operatorname{Fr}_X^m)^*K\to K$ in place of $\phi_m$ gives
$T_{c_m}(\chi\kappa_m)=R\Gamma_c(X,\chi)\circ\operatorname{pb}_{\operatorname{Fr}_X^m}$.
