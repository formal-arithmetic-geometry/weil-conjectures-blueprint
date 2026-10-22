+++
id = "det-thm-picard-coherence"
kind = "theorem"
title = "Coherence of the higher direct images"
order = 722
uses = ["lem-pc-universal-finite-free-complex"]
lean = ["AlgebraicGeometry.Scheme.Modules.isQuasicoherent_higherDirectImage", "AlgebraicGeometry.Scheme.Modules.isFinitePresentation_higherDirectImage", "AlgebraicGeometry.Scheme.Modules.exists_isZero_higherDirectImage_restrict", "AlgebraicGeometry.Scheme.Modules.exists_isZero_higherDirectImage", "AlgebraicGeometry.exists_isIso_canonicalModuleBaseChange_of_isFlatOver", "AlgebraicGeometry.noetherian_perfect_directImage"]
+++
Let $f:X\to T$ be a proper morphism of finite presentation and $\cF$ an
$\cO_X$-module of finite presentation, flat over $T$ (the standing
assumptions of this subsubsection). Then:

- **(a)** For every $g:T'\to T$, with $f':X'\to T'$ and $\cF'$ the base
changes of $f$ and $\cF$, the base change map
$Lg^*Rf_*\cF\to Rf'_*\cF'$ is an isomorphism in the derived category of
$\cO_{T'}$-modules. Moreover $Rf_*\cF$ is locally computed by finite free
complexes ([lem-pc-universal-finite-free-complex]): every
point of $T$ has an open neighbourhood $U$ and an integer $d_U\ge0$ with a
complex $P$ of finite free $\cO_U$-modules concentrated in degrees
$[0,d_U]$ such that for every $g:T'\to U$, with
$f':X'\to T'$ and $\cF'$ the base changes of $f$ and $\cF$, one has
$H^q(g^*P)\cong R^qf'_*\cF'$ for all $q$. In particular
$R^qf_*\cF|_U=0$ for all $q>d_U$.
- **(b)** If $T$ is locally Noetherian, $R^qf_*\cF$ is a coherent
$\cO_T$-module for all $q$; for this, flatness of $\cF$ over $T$ is not
needed. If $T$ is locally Noetherian and $\cF$ is flat over $T$, then
$Rf_*\cF$ is perfect: locally on $T$ it is represented by a bounded complex
of finite locally free modules.
- **(c)** If $T$ is quasi-compact, $R^qf_*\cF=0$ for all $q\gg0$.
