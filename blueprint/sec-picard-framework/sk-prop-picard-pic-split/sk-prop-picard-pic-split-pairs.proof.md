+++
kind  = "proof"
of    = "det-picard-pic-split-pairs"
+++
(1) An automorphism of the invertible module $\cL$ is multiplication by a
unit $w\in\Gamma(C_T,\cO_{C_T})^\times$ (locally $\cL\cong\cO$, and
$\mathcal{E}nd(\cL)=\cO_{C_T}$). By hypothesis
$\Gamma(T,\cO_T)\to\Gamma(C_T,\cO_{C_T})$ is an isomorphism, so $w=f_T^*u$
for a unique unit $u$ of $T$. Then $\sigma_T^*(w)=\sigma_T^*f_T^*u=u$,
since $f\circ\sigma=\mathrm{id}$. Compatibility with $\alpha$ says
$\alpha\circ(\text{multiplication by }u)=\alpha$, i.e. $u=1$, hence
$w=1$. If $\varphi,\psi:(\cL,\alpha)\to(\cL',\alpha')$ are two
isomorphisms, $\psi^{-1}\varphi$ is an automorphism of $(\cL,\alpha)$,
hence the identity, so $\varphi=\psi$.

(2) The map is well defined, since isomorphic pairs have isomorphic
underlying modules, and it lands in $\ker\sigma_T^*$ because $\alpha$
trivializes $\sigma_T^*\cL$. *Surjective:* if $\sigma_T^*\cL\cong\cO_T$,
choose any such isomorphism $\alpha$. *Injective:* let
$\varphi:\cL\xrightarrow{\sim}\cL'$ be an isomorphism of the underlying
modules of $(\cL,\alpha)$ and $(\cL',\alpha')$. The composite
$\alpha'\circ\sigma_T^*\varphi\circ\alpha^{-1}$ is an automorphism of
$\cO_T$, i.e. multiplication by a unit $v$ of $T$. Then
$\varphi'=\varphi\circ(\text{multiplication by }f_T^*v^{-1})$ satisfies
$\alpha'\circ\sigma_T^*\varphi'=v^{-1}\cdot\alpha'\circ\sigma_T^*\varphi=\alpha$,
so $(\cL,\alpha)\cong(\cL',\alpha')$. Naturality: pullback along
$T'\to T$ commutes with $\sigma^*$, so pulled-back pairs are pairs and
the map commutes with pullback.

(3) By [thm-pc-pic-split], $\operatorname{Pic}(C_T)=f_T^*\operatorname{Pic}(T)\oplus\ker\sigma_T^*$
and $\operatorname{Pic}_{C/S}$ is the fppf sheafification of the presheaf
$K=\ker\sigma^*$, which is already an fppf sheaf; hence the canonical map
$K(T)\to\operatorname{Pic}_{C/S}(T)$ is a bijection, natural in $T$.
Composing with (2) gives the claim.
