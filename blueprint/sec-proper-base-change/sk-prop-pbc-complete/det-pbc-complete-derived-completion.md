+++
id = "det-pbc-complete-derived-completion"
kind = "lemma"
title = "Towers of $\\mathcal O_E$-modules and the derived completion"
order = 2019
uses = ["det-def-sfb-pulled-back-coefficients", "det-def-sfb-module-pushforward-pullback", "def-weil-derived-direct-image", "def-pe-derived-complete", "det-pe-derived-nakayama-resolution", "def-weil-derived-limit"]
+++
Fix a finite extension $E/\Ql$ with uniformizer $\pi_E$, and for a scheme $T$
write $\mathcal O_{E,T}=p_T^*\underline{\mathcal O_E}$ and
$(\mathcal O_E/\pi_E^n)_T$ for the pulled-back coefficient rings
([det-def-sfb-pulled-back-coefficients]), and
$D(T)=D(T_{\mathrm{proét}},\mathcal O_E)$ for the derived category of
$\mathcal O_{E,T}$-modules.

*Notation.*

1. *Towers.* $\operatorname{Tow}(T)$ is the abelian category of towers
   $M_\bullet=(M_n,t_n\colon M_{n+1}\to M_n)_{n\geq1}$ of
   $\mathcal O_{E,T}$-module sheaves on $T_{\mathrm{proét}}$, with levelwise
   morphisms. Write
   $\operatorname{ev}_n\colon\operatorname{Tow}(T)\to\Mod_{\mathcal O_{E,T}}$ for
   evaluation at level $n$, $c\colon\Mod_{\mathcal O_{E,T}}\to\operatorname{Tow}(T)$
   for the constant tower with identity transitions, and
   $\varprojlim\colon\operatorname{Tow}(T)\to\Mod_{\mathcal O_{E,T}}$ for the
   limit, right adjoint to $c$. The *derived limit*
   $R\varprojlim\colon D(\operatorname{Tow}(T))\to D(T)$ is the right derived
   functor of $\varprojlim$; on a tower of complexes it is the Milnor cone
   $\operatorname{Cone}(\prod_nM_n\xrightarrow{1-T}\prod_nM_n)[-1]$, a derived
   limit of $(\operatorname{ev}_nM_\bullet)_n$ in the sense of
   [def-weil-derived-limit].
2. *Levelwise functors.* For a morphism of schemes $u\colon T'\to T$, the module
   pullback and pushforward of [det-def-sfb-module-pushforward-pullback], applied
   levelwise, give $u^*_{\operatorname{Tow}}\colon\operatorname{Tow}(T)\to
   \operatorname{Tow}(T')$ and $u_*^{\operatorname{Tow}}\colon
   \operatorname{Tow}(T')\to\operatorname{Tow}(T)$, with
   $u^*_{\operatorname{Tow}}\dashv u_*^{\operatorname{Tow}}$. Write
   $Ru_*^{\operatorname{Tow}}$ for the right derived functor of
   $u_*^{\operatorname{Tow}}$; $u^*_{\operatorname{Tow}}$ is exact and needs no
   deriving.
3. *Reduction tower.* For a complex $M$ of $\mathcal O_{E,T}$-modules let

   $$
   \operatorname{red}(M)_n=\operatorname{Cone}\bigl(M\xrightarrow{\pi_E^n}M\bigr)
   =M\otimes_{\mathcal O_{E,T}}[\mathcal O_{E,T}\xrightarrow{\pi_E^n}\mathcal O_{E,T}],
   $$

   with transitions induced by the map of resolutions
   $[\mathcal O_{E,T}\xrightarrow{\pi_E^{n+1}}\mathcal O_{E,T}]\to
   [\mathcal O_{E,T}\xrightarrow{\pi_E^n}\mathcal O_{E,T}]$ equal to $\pi_E$ in
   degree $-1$ and the identity in degree $0$, which lifts
   $(\mathcal O_E/\pi_E^{n+1})_T\to(\mathcal O_E/\pi_E^n)_T$. By
   [det-pe-derived-nakayama-resolution],
   $\operatorname{red}(M)_n\simeq M_n=M\otimes^{\mathbf L}_{\mathcal O_{E,T}}
   (\mathcal O_E/\pi_E^n)_T$. The construction is functorial on complexes,
   commutes with cones and preserves quasi-isomorphisms, so it defines an exact
   functor $\operatorname{red}\colon D(T)\to D(\operatorname{Tow}(T))$, the
   *reduction tower*.
4. *Completion map.* The inclusions of $M$ in degree $0$ of the cones give a
   morphism of towers $c(M)\to\operatorname{red}(M)$; applying $R\varprojlim$ and
   using $R\varprojlim c(M)\simeq M$ gives the *completion map*

   $$
   \kappa_M\colon M\longrightarrow\widehat M:=R\varprojlim\operatorname{red}(M),
   $$

   natural in $M$. It is the canonical map of [def-pe-derived-complete], so $M$
   is derived complete if and only if $\kappa_M$ is an isomorphism.
   $\widehat M$ is the *derived completion* of $M$.

*Assertions.* Let $u\colon T'\to T$ be a morphism of schemes.

1. $\operatorname{Tow}(T)$ is a Grothendieck abelian category. Each
   $\operatorname{ev}_n$ is exact and has an exact left adjoint, so it carries
   K-injective complexes of towers to K-injective complexes of modules.
2. A morphism $a$ of $D(\operatorname{Tow}(T))$ is an isomorphism if and only if
   $\operatorname{ev}_n(a)$ is an isomorphism in $D(T)$ for every $n$.
3. $\operatorname{ev}_n\circ u^*_{\operatorname{Tow}}=u^*\circ\operatorname{ev}_n$ and
   $\operatorname{ev}_n\circ Ru^{\operatorname{Tow}}_*\simeq Ru_*\circ\operatorname{ev}_n$,
   compatibly with the units and counits of $u^*\dashv Ru_*$
   ([def-weil-derived-direct-image]) and
   $u^*_{\operatorname{Tow}}\dashv Ru^{\operatorname{Tow}}_*$.
4. There is a canonical isomorphism
   $Ru_*\circ R\varprojlim\simeq R\varprojlim\circ Ru_*^{\operatorname{Tow}}$ of
   functors $D(\operatorname{Tow}(T'))\to D(T)$.
5. $R\varprojlim$ is exact. For an exact equivalence
   $F\colon\Mod_{\mathcal O_{E,T}}\to\Mod_{\mathcal O_{E,T'}}$, applied levelwise
   as $F^{\operatorname{Tow}}$, one has $F\circ R\varprojlim\simeq
   R\varprojlim\circ F^{\operatorname{Tow}}$; and
   $R\varprojlim(M_\bullet)\otimes_{\mathcal O_{E,T}}P\simeq
   R\varprojlim(M_\bullet\otimes_{\mathcal O_{E,T}}P)$ for every bounded complex
   $P$ of finite free $\mathcal O_{E,T}$-modules.
6. For every $M\in D(T)$ the derived completion $\widehat M$ is derived
   complete, and $\kappa_M$ induces an isomorphism
   $\operatorname{red}(\kappa_M)\colon\operatorname{red}(M)\xrightarrow{\sim}
   \operatorname{red}(\widehat M)$ in $D(\operatorname{Tow}(T))$; in particular
   $M_m\simeq\widehat M_m$ for every $m\geq1$.
