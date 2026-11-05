+++
id = "lemma-covers-degree-prime-to-ell--1"
kind = "lemma"
title = "The Sylow cover and its normalization"
name_showing = false
order = 982001
aliases = ["bp-r299-1"]
lean = ["AlgebraicGeometry.Scheme.exists_sylow_galoisCover_trivializing_connected", "AlgebraicGeometry.exists_finite_smooth_cover_not_dvd_ramificationIdx", "AlgebraicGeometry.Etale.CurveLocalModel.nonempty_coverDatum"]
uses = ["definition-constructible-sheaves", "definition-lisse-sheaves"]
+++
The assertion for every prime-to-$\ell$ multiple is bypassed by Lean;
the proof uses one cover for both complexes on the same curve. The
construction takes place on the classical étale site.

1. Let $U$ be a connected scheme, $\ell$ a prime, $\Lambda$ a finite
   commutative ring, and $\mathcal F_1,\dots,\mathcal F_r$ finite locally
   constant sheaves of $\Lambda$-modules on $U_{\acute{e}t}$. There are a
   connected scheme $V$, a finite étale morphism $v:V\to U$, and an
   integer $d$ prime to $\ell$ such that every geometric fibre of $v$
   over a separably closed field has $d$ points. Moreover, there are a
   finite $\ell$-group $G$ and a connected finite étale Galois cover
   $g:Z\to V$ with group $G$ such that, for each $i$, the sheaf
   $g^*v^*\mathcal F_i$ is constant with value a finite $\Lambda$-module.

2. Let $X$ be a smooth curve over an algebraically closed field $k$,
   $y$ a $k$-point, $U$ an irreducible affine open neighbourhood of $y$,
   and $U'\subseteq U$ an open subscheme. Let $\ell,d\in\N$ satisfy
   $\ell\nmid d$, and let $v:V\to U'$ be finite étale with $V$
   connected and every geometric fibre over a separably closed field
   of cardinality $d$. There are a smooth curve $C$ over $k$, a finite
   morphism $p:C\to U$, a $k$-point $c$ over $y$, and an integer
   $e\geq1$ with $\ell\nmid e$ such that every uniformizer $u$ of
   $\mathcal O_{X,y}$ has image
   $$
   u=w\xi^e\quad\text{in }\mathcal O_{C,c},
   $$
   where $w$ is a unit and $\xi$ is a uniformizer. There is an open
   immersion $j:V\hookrightarrow C$ over $U$ whose image is
   $p^{-1}(U')$.

3. Let $M=(X,h,y)$ be a curve local model over $k$: the curve $X$ is
   smooth, separated and quasi-compact over the algebraically closed
   field $k$, the $k$-endomorphism $h$ fixes the $k$-point $y$, and
   $h^\#\mathfrak m_y\subseteq\mathfrak m_y^2$. Let $\ell$ be prime,
   $\Lambda$ a finite commutative ring, and $P_L,P_K$ bounded complexes
   of flat constructible $\Lambda$-sheaves on $X_{\acute{e}t}$.
   There are open neighbourhoods $U,W$ of $y$, a smooth separated
   curve $C$ over $k$, a finite morphism $p_U:C\to U$, and a $k$-point
   $c$ over $y$. Write $p:C\to X$ for the composite. There is an
   integer $e\geq1$ prime to $\ell$ satisfying the uniformizer relation
   in (2), and the restriction
   $$
   p^{-1}(W-\{y\})\longrightarrow W-\{y\}
   $$
   is étale. There are a finite $\ell$-group $G$ and a finite étale
   Galois cover $g:Z\to p^{-1}(W-\{y\})$ with group $G$ such that the
   pullbacks of $P_L$ and $P_K$ to $Z$ are isomorphic, as complexes,
   to constant complexes on bounded complexes of finite
   $\Lambda$-modules. These are the data of
   `AlgebraicGeometry.Etale.CurveLocalModel.CoverDatum`.
