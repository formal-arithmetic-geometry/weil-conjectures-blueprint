+++
id = "prose-02-01"
kind = "hidden"
title = "The pro-étale site"
order = 24
+++
On the étale site the constant sheaf $\mathbf Z_\ell$ forgets that $\mathbf Z_\ell$ is
profinite. The pro-étale site $X_{\mathrm{pro}\acute{e}t}$ of Bhatt and Scholze [bhatt-scholze15]
repairs this. Its objects are the weakly étale $X$-schemes, and its
coverings are fpqc coverings
(Definition [definition-small-pro-etale-site]).

We need three properties of this site.

- (a) *Limits.* For a tower $\cdots\to F_2\to F_1$ of surjections of
  sheaves, cohomology commutes with the limit:
  $R\Gamma(X,\varprojlim_nF_n)\simeq R\varprojlim_nR\Gamma(X,F_n)$.
- (b) *Topology.* The sheaf $\mathbf Z_\ell$ remembers the topology of $\mathbf Z_\ell$.
- (c) *Comparison.* Sheaves coming from the étale site keep their
  étale cohomology, so that the results of SGA 4 still apply to them.

Property (b) can be seen on a point. Over a separably closed field the topos
of $X_{\mathrm{pro}\acute{e}t}$ is, up to a set-theoretic cutoff, that of condensed sets
(Proposition [proposition-pro-etale-site-separably-closed], proved in
Subsection [subsec-Condensed-rings] below), and there the sections of $\mathbf Z_\ell$ over a
profinite set $S$ are all continuous maps $S\to\mathbf Z_\ell$, not only the locally
constant ones.

|  | on $X_{\acute{e}t}$ | on $X_{\mathrm{pro}\acute{e}t}$ |
|---|---|---|
| objects | étale $X$-schemes | weakly étale $X$-schemes |
| local objects | strictly henselian local rings | w-contractible rings |
| topos of a geometric point | sets | condensed sets |
| the sheaf $\mathbf Z_\ell$ on a point | $\mathbf Z_\ell$ with discrete topology | continuous maps to $\mathbf Z_\ell$ |

Property (a) fails on $X_{\acute{e}t}$, for the following reason. A surjection of
sheaves is surjective on sections only after refining the cover. A countable
product of surjections needs one refinement for each factor, and these
infinitely many refinements need not have a common refinement among étale
covers. So a countable product of surjections need not be surjective,
$R^1\varprojlim_nF_n$ need not vanish, and $\varprojlim_nF_n$ differs from
$R\varprojlim_nF_n$. For $F_n=\mathbf Z/\ell^n$ on $\operatorname{Spec}\mathbf F_q$
this is the lost $H^1$. On $X_{\mathrm{pro}\acute{e}t}$ there are enough objects
on which no refinement is needed: the spectra of w-contractible rings, roughly
families of strictly henselian local rings parametrized by an extremally
disconnected profinite set. Every cover of such a spectrum splits, so every
surjection of sheaves is surjective on its sections there, and limits of
sheaves can be computed there as limits of sets and modules. However, building these
objects takes two theorems from outside algebraic geometry: Gleason's theorem
on extremally disconnected spaces and Olivier's theorem on weakly étale
maps. Once we have them, property (a) follows in a few lines
(Proposition [proposition-continuous-cohomology-pro-etale-cohomology]).
In particular, over $\mathbf F_q$ it gives back $H^1=\mathbf Z_\ell$
(Example [example-first-cohomology-finite-field]).

For property (c) we compare the two sites through the pullback functor
$\nu_X^*$ from sheaves on $X_{\acute{e}t}$ to sheaves on $X_{\mathrm{pro}\acute{e}t}$. Its image
consists of the sheaves that we call *classical*: a sheaf on
$X_{\mathrm{pro}\acute{e}t}$ is classical if its sections over a limit
$U=\varprojlim_iU_i$ of affine étale $X$-schemes are the colimit of its
sections over the $U_i$ (Definition [definition-classical-pro-etale-sheaves]).
In other words, a classical sheaf is determined by its values on étale
$X$-schemes, as an étale sheaf is. The comparison has four parts.

- $\nu_X^*$ is an equivalence from étale sheaves onto classical sheaves
  (Theorem [theorem-classical-sheaves-essential-image]).
- It preserves the cohomology of bounded below complexes
  (Theorem [theorem-bounded-below-cohomology-comparison]).
- It commutes with direct images along quasi-compact quasi-separated
  morphisms (Theorem [theorem-comparison-direct-images]).
- For a finite coefficient ring, a constructible sheaf on $X_{\mathrm{pro}\acute{e}t}$
  is classical, and $\nu_X^*$ is an equivalence from
  $D^b_c(X_{\acute{e}t},\Lambda)$ onto $\Dbc(X,\Lambda)$
  (Theorem [theorem-comparison-constructible-sheaves]). So with finite
  coefficients the two sites have the same constructible complexes.

Later, $f^!$ is built by Brown representability on the unbounded derived
category, so we also need the comparison for unbounded complexes. With finite
coefficients it holds as well, because affine schemes étale over a scheme
of finite type over $k$ have uniformly bounded cohomological dimension. Each
cohomology group of an unbounded complex therefore depends only on a bounded
below truncation, where the comparison is already known
(Proposition [proposition-unbounded-comparison-finite-coefficients]). The
sheaf $\mathbf Z_\ell$, however, is not classical
(Example [example-coefficient-sheaf-outside-classical-part]). This is
what the computation of $H^1(\operatorname{Spec}\mathbf F_q,\mathbf Z_\ell)$ in
Section [sec-Weil-cohomology] needs: $H^1$ comes out as $\mathbf Z_\ell$ only when
sections see the topology of $\mathbf Z_\ell$. So the comparison applies to the
$\mathbf Z/\ell^n$ but not to $\mathbf Z_\ell$ itself, and we reach $\mathbf Z_\ell$ from them by derived completion
(Section [sec-Extension-by-zero-and-completion]).

Throughout this chapter, schemes are arbitrary unless a result states a
finiteness hypothesis, because objects of $X_{\mathrm{pro}\acute{e}t}$ are in general neither
Noetherian nor of finite type, even when $X$ is a variety. The standing
assumption that schemes are of finite type over $k$ resumes in
Chapter [chap-Constructible-complexes].
