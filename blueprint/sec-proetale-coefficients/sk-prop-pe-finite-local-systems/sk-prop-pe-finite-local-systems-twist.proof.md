+++
kind = "proof"
of = "det-pe-finite-local-systems-twist"
+++
By [det-pe-finite-local-systems-type], $X=\coprod_MX_M$ with $X_M$ open and
closed, and sheaves on $X$ (on either site) are families of sheaves on the
$X_M$; so we may assume $F$ is pro-étale locally isomorphic to $\underline M$ for
one finitely presented $M$.

Let $H=\mathcal Aut(\underline M)$ and $T=\mathcal Isom(\underline M,F)$. The
group $H$ acts on $T$ by precomposition, $(h,\varphi)\mapsto\varphi\circ h^{-1}$;
the action is free and transitive on sections wherever $T$ has a section, and $T$
has sections locally. So $T$ is an $H$-torsor. By
[det-pe-finite-local-systems-hom], $H=\nu_X^*H_0$ with
$H_0=\operatorname{Aut}_\Lambda(M)_{X,\Et}$, and by
[det-pe-torsor-comparison-glue] there is an étale $H_0$-torsor $T_0$ with
$\nu_X^*T_0\cong T$.

Evaluation $T\times\underline M\to F$, $(\varphi,m)\mapsto\varphi(m)$, is invariant
under $(\varphi h^{-1},hm)\sim(\varphi,m)$ and induces a map from the contracted
product $T\times^H\underline M$ to $F$. Where $T$ has a section $\varphi$ this map
is identified with $\varphi\colon\underline M\to F$, an isomorphism; so it is an
isomorphism of sheaves, and $\Lambda$-linear for the module structure coming from
$\underline M$ (on which $H$ acts linearly). Put
$F_0=T_0\times^{H_0}M_{X,\Et}$, an étale sheaf of $\Lambda$-modules which is
isomorphic to $M_{X,\Et}$ wherever $T_0$ has a section, in particular on an étale
covering. The contracted product is a quotient of a finite product by a group
action, i.e. built from finite limits and colimits, which $\nu_X^*$ preserves;
hence $\nu_X^*F_0\cong\nu_X^*T_0\times^{H}\underline M\cong T\times^H\underline M
\cong F$.

Therefore $F$ is classical ([det-pe-classical-sheaves-modules]) and trivialized
on the étale covering trivializing $T_0$. The functor $\nu_X^*$ carries étale
local systems of finite presentation to pro-étale ones (an étale covering is a
pro-étale covering and $\nu_X^*M_{X,\Et}=\underline M$); it is fully faithful on
module sheaves, and essentially surjective onto pro-étale local systems of finite
presentation by the above, with $F_0\cong\nu_{X,*}F$. For a finite ring $A$, a
finite $A$-module is finitely generated over the Noetherian ring $A$, hence
finitely presented.
