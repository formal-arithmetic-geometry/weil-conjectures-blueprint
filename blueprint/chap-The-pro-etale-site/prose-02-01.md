+++
id = "prose-02-01"
kind = "hidden"
title = "The pro-étale site"
order = 24
+++
As we saw, the étale topology forgets that $\mathbf Z_\ell$ is profinite. The
pro-étale site of Bhatt and Scholze [bhatt-scholze15] repairs this.

We want three properties. For a tower of surjections we want
$R\Gamma(X,\varprojlim_nF_n)\simeq R\varprojlim_nR\Gamma(X,F_n)$. The site
should remember the topology of $\mathbf Z_\ell$. And sheaves from the étale site
should keep their étale cohomology, so that SGA 4 still applies. The objects of $X_{\mathrm{pro}\acute{e}t}$ are the weakly étale $X$-schemes, and
the coverings are fpqc coverings
(Definition [definition-small-pro-etale-site]). Over a separably closed
field its topos is, up to a set-theoretic cutoff, that of condensed sets
(Proposition [proposition-pro-etale-site-separably-closed], proved in
Section [subsec-Condensed-rings] below). There the
sections of $\mathbf Z_\ell$ over a profinite set $S$ are all continuous maps $S\to\mathbf Z_\ell$.

|  | on $X_{\acute{e}t}$ | on $X_{\mathrm{pro}\acute{e}t}$ |
|---|---|---|
| objects | étale $X$-schemes | weakly étale $X$-schemes |
| local objects | strictly henselian local rings | w-contractible rings |
| topos of a geometric point | sets | condensed sets |
| the sheaf $\mathbf Z_\ell$ on a point | $\mathbf Z_\ell$ with discrete topology | continuous maps to $\mathbf Z_\ell$ |

The limit formula fails on $X_{\acute{e}t}$ because a surjection of sheaves is
surjective on sections only after refining the cover, and a tower needs
infinitely many refinements at once. On $X_{\mathrm{pro}\acute{e}t}$ there are enough objects
on which no refinement is needed: the spectra of w-contractible rings, roughly
families of strictly henselian local rings parametrized by an extremally
disconnected profinite set. Every cover of such a spectrum splits. Hence every
surjection of sheaves is surjective on its sections there, and limits of
sheaves can be computed there as limits of sets and modules. Building these
objects takes two theorems from outside algebraic geometry: Gleason's theorem
on extremally disconnected spaces and Olivier's theorem on weakly étale
maps. Once we have them, the limit formula follows in a few lines
(Proposition [proposition-continuous-cohomology-pro-etale-cohomology]).
Over $\mathbf F_q$ it gives back $H^1=\mathbf Z_\ell$
(Example [example-first-cohomology-finite-field]).

The comparison with SGA 4 holds for classical sheaves, those whose sections on a
limit of affine étale schemes are the colimit of the sections at finite stages.
Pullback from $X_{\acute{e}t}$ has four properties:

- it identifies étale sheaves with classical sheaves
  (Theorem [theorem-classical-sheaves-essential-image]);
- it preserves the cohomology of bounded below complexes
  (Theorem [theorem-bounded-below-cohomology-comparison]);
- it commutes with direct images along quasi-compact quasi-separated
  morphisms (Theorem [theorem-comparison-direct-images]);
- it identifies constructible complexes with finite coefficients
  (Theorem [theorem-comparison-constructible-sheaves]).

For unbounded complexes the comparison also uses finite cohomological
dimension
(Proposition [proposition-unbounded-comparison-finite-coefficients]). The
sheaf $\mathbf Z_\ell$ is not classical
(Example [example-coefficient-sheaf-outside-classical-part]), as the
computation of $H^1(\operatorname{Spec}\mathbf F_q,\mathbf Z_\ell)$ in
Section [sec-Weil-cohomology] demands. The comparison applies to the
$\mathbf Z/\ell^n$, and we reach $\mathbf Z_\ell$ from them by derived completion
(Section [sec-Extension-by-zero-and-completion]).

Throughout this section, schemes are arbitrary unless a result states a
finiteness hypothesis, because objects of $X_{\mathrm{pro}\acute{e}t}$ are in general neither
Noetherian nor of finite type, even when $X$ is a variety. The standing
assumption that schemes are of finite type over $k$ resumes in
Section [chap-Constructible-complexes].
