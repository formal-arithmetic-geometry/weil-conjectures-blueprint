+++
id = "lem-pc-rf-perfect-base-change"
kind = "lemma"
title = "Perfectness of $Rf_*\\mathcal{G}$ and base change"
lean = ["AlgebraicGeometry.Scheme.Modules.perfect_and_baseChange_cechModuleComplex_of_isProper"]
order = 734
uses = ["def-pc-base-change", "def-pc-derived-category", "def-pc-derived-direct-image", "def-pc-derived-pullback", "def-pc-morphism-conventions", "def-pc-perfect-complex", "cor-pc-projective-noetherian-rf-perfect-base-change", "lem-pc-cech-resolution", "lem-pc-coherent-hi", "lem-pc-noetherian-flat-complex-perfect", "lem-pc-projective-noetherian-rf-perfect", "lem-pc-rf-base-change-flat-module"]
+++
Let $S=\operatorname{Spec}(A)$ be an affine scheme, $f:X\to S$ a proper
morphism of finite presentation, $\mathcal{G}$ an $\mathcal{O}_X$-module of
finite presentation and flat over $S$, and $\mathcal U$ a finite cover of
$X$ by affine opens, so that $Rf_*\mathcal G$ is represented in $D(A)$ by
the Cech complex $\check C^\bullet(\mathcal U,\mathcal G)$
([lem-pc-cech-resolution]). Then:

1. Every $t\in S$ has an open neighbourhood $V$, an integer $d\ge0$ and a
   complex $P$ of finite free $\mathcal O_V$-modules concentrated in
   degrees $[0,d]$ such that for every morphism
   $g:T'\to V$, with $f':X'\to T'$ the base change of $f$ along
   $T'\to V\subseteq S$ and $\mathcal G'$ the pullback of $\mathcal G$ to
   $X'$, there are isomorphisms
   $\mathcal H^q(g^*P)\cong R^qf'_*\mathcal G'$ for all $q\ge0$. In
   particular $P$ computes $R^qf_*\mathcal G|_V$ (take $g=\mathrm{id}_V$).
2. For every morphism $g:T\to S$ from an affine scheme
   $T=\operatorname{Spec}(B)$, the canonical base-change map

   $$
   Lg^*(Rf_*\mathcal{G})\;\longrightarrow\;Rf_{T,*}\mathcal{G}_T
   $$

   of [lem-pc-rf-base-change-flat-module] is an isomorphism in $D(B)$.
3. If $A$ is Noetherian, then $Rf_*\mathcal G$ is a perfect object of
   $D(A)$, and for every $g:T=\operatorname{Spec}(B)\to S$ as in (2),
   $Rf_{T,*}\mathcal G_T$ is a perfect object of $D(B)$.
