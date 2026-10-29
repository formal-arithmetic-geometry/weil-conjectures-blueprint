+++
id = "det-def-sfb-change-of-scalars"
kind = "definition"
title = "Restriction, extension and coextension of scalars"
order = 1184
uses = ["det-prop-sfb-module-category", "det-def-sfb-ring-object", "det-def-sfb-module-objects"]
lean = ["CategoryTheory.Mod.comap", "CategoryTheory.Mod.extendScalars", "CategoryTheory.Mod.extendRestrictAdjunction", "CategoryTheory.Mod.preservesFiniteColimits_extendScalars", "CategoryTheory.Adjunction.rightAdjoint_preservesLimits", "CategoryTheory.Mod.coextendScalars", "CategoryTheory.Mod.restrictCoextendAdjunction", "CategoryTheory.Adjunction.leftAdjoint_preservesColimits", "CategoryTheory.Mod.comapEquivalenceOfIsIso", "CategoryTheory.Mod.extendScalarsIsoComapInv", "CategoryTheory.Mod.coextendScalarsIsoComapInv", "CategoryTheory.Mod.extendScalarsIsoCoextendScalars"]
+++
Let $\mathcal C$ be a monoidal category and let $\varphi\colon\mathcal R\to\mathcal S$ be a
morphism of monoid objects ([det-def-sfb-ring-object]). Module objects are as in
[det-def-sfb-module-objects].

1. **Restriction.** The functor
   $\operatorname{Res}_\varphi\colon\Mod_{\mathcal S}(\mathcal C)\to\Mod_{\mathcal R}(\mathcal C)$
   gives $N$ the action
   $\mathcal R\otimes N\xrightarrow{\varphi\otimes N}\mathcal S\otimes N\xrightarrow{\gamma_N}N$.
   It is the identity on underlying objects and morphisms, so it commutes with the forgetful
   functors.
2. **Extension.** Let $\mathcal C$ be braided with coequalizers, with $X\otimes-$ and
   $-\otimes X$ preserving colimits for every $X$, and let $\mathcal R$ be commutative. Define
   $$
   \operatorname{Ext}_\varphi(M)=\mathcal S\otimes_{\mathcal R}M:=\operatorname{coeq}\Bigl(
   \mathcal S\otimes\mathcal R\otimes M\rightrightarrows\mathcal S\otimes M\Bigr),
   $$
   the coequalizer of $\bigl(\mu_{\mathcal S}(\mathcal S\otimes\varphi)\bigr)\otimes M$ and
   $(\mathcal S\otimes\gamma_M)\alpha$, with $\mathcal S$ acting on the first factor. This
   is a functor $\Mod_{\mathcal R}(\mathcal C)\to\Mod_{\mathcal S}(\mathcal C)$, left
   adjoint to $\operatorname{Res}_\varphi$. Hence $\operatorname{Ext}_\varphi$ is right
   exact and $\operatorname{Res}_\varphi$ preserves limits.
3. **Coextension.** Let $\mathcal C$ be closed with equalizers, and write
   $\underline{\Hom}(X,-)$ for the right adjoint of $X\otimes-$. Define
   $$
   \operatorname{Coext}_\varphi(N)=\Hom_{\mathcal R}(\mathcal S,N):=\operatorname{eq}\Bigl(
   \underline{\Hom}(\mathcal S,N)\rightrightarrows\underline{\Hom}(\mathcal R\otimes\mathcal S,N)\Bigr).
   $$
   The first map precomposes with the action $\mu_{\mathcal S}(\varphi\otimes\mathcal S)$ of
   $\mathcal R$ on $\mathcal S$, and the second postcomposes with the action of $\mathcal R$
   on $N$. Here $\mathcal S$ acts by right multiplication on the source, $(s\cdot f)(t)=f(ts)$.
   This is a functor $\Mod_{\mathcal R}(\mathcal C)\to\Mod_{\mathcal S}(\mathcal C)$, right
   adjoint to $\operatorname{Res}_\varphi$. Hence $\operatorname{Res}_\varphi$ preserves
   colimits.
4. Under the hypotheses of 2 and 3,
   $\operatorname{Ext}_\varphi\dashv\operatorname{Res}_\varphi\dashv\operatorname{Coext}_\varphi$.
   If $\mathcal C$ is moreover abelian with $\otimes$ additive in each variable, then both
   module categories are abelian ([det-prop-sfb-module-category]) and
   $\operatorname{Res}_\varphi$ is exact.
5. **Invertible $\varphi$.** Under the hypotheses of 2 and 3, let $\varphi$ be an
   isomorphism. Then $\operatorname{Res}_\varphi$ is an equivalence with quasi-inverse
   $\operatorname{Res}_{\varphi^{-1}}$, and
   $$
   \operatorname{Ext}_\varphi\cong\operatorname{Res}_{\varphi^{-1}}\cong\operatorname{Coext}_\varphi .
   $$
