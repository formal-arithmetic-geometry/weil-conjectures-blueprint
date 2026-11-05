+++
id = "proposition-additivity-trace-classes"
kind = "proposition"
title = "Additivity of trace classes"
order = 942
lean = ["AlgebraicGeometry.ProEtale.CondensedRing.Correspondence.traceClass_eq_add_of_distTriang", "AlgebraicGeometry.ProEtale.CondensedRing.Correspondence.traceClass_ofGraph_eq_add"]
uses = ["definition-correspondence", "definition-trace-class-local-terms", "lemma-lift-correspondence-invariant-decomposition", "lemma-closed-piece-pushforward"]
+++
Let $c:C\to X\times X$ be a correspondence.

1. Let $\mathcal K$ be a finitely filtered complex on $X$ with
   underlying complex $K$ and graded pieces $K_a$ in $D^b_{\mathrm{ctf}}(X,A)$, and let
   $\tilde u:c_2^*\mathcal K\to c_1^!\mathcal K$ be a cohomological
   correspondence in the filtered derived category, with underlying
   correspondence $u$ on $K$ and graded pieces $u_a$ on $K_a$. Then
   $$
   \operatorname{Tr}_c(u)=\sum_a\operatorname{Tr}_c(u_a)
   \quad\text{in }H^0(\Fix(c),\omega_{\Fix(c)}).
   $$
2. Let $i:Z\to X$ be a closed immersion with open complement $U$ such
   that $c_1^{-1}(Z)\subset c_2^{-1}(Z)$, let $K\in D^b_{\mathrm{ctf}}(X,A)$, and let
   $u$ be a cohomological correspondence on $(X,K)$. Then
   $$
   \operatorname{Tr}_c(u)=\operatorname{Tr}_c(u_U)+\operatorname{Tr}_c(u_Z),
   $$
   where $u_U$ and $u_Z$ are the graded pieces of the lift of
   Lemma [lemma-lift-correspondence-invariant-decomposition], and $u_Z$
   is the pushforward along $i$ and $C_Z\to C$ of the correspondence
   $u_{|Z}$ on $(Z,i^*K)$ for $c_Z:C_Z=(c_1^{-1}(Z))_{\mathrm{red}}\to
Z\times Z$ (Lemma [lemma-closed-piece-pushforward]).
