+++
id = "lem-pc-flf-properties"
kind = "lemma"
title = "The module f_*O_X of a finite locally free morphism"
order = 4280
lean = ["AlgebraicGeometry.locallyFree_pushforward_of_isFiniteLocallyFree"]
uses = ["def-pc-finite-locally-free", "def-pc-morphism-conventions", "lem-pc-flat-base-change-cohom", "def-pc-base-change"]
+++
Let $f:X\to S$ be a morphism finite locally free of degree $d$
[def-pc-finite-locally-free]. Then $f_*\mathcal{O}_X$ is a locally free
$\mathcal{O}_S$-module of rank $d$, and for every $s\in S$ the canonical
map
$(f_*\mathcal{O}_X)_s\otimes_{\mathcal{O}_{S,s}}\kappa(s)\to\Gamma(X_s,\mathcal{O}_{X_s})$
is an isomorphism.

## Proof

$f$ is finite, so $f_*\mathcal{O}_X$ is a finite $\mathcal{O}_S$-module; $f$
is of finite presentation and flat, hence $f_*\mathcal{O}_X$ is flat over
$S$. Flatness can be checked on stalks: for $s$ a point and
$x_1,\dots,x_m\in f^{-1}(s)$ the finitely many preimages,
$\mathcal{O}_{X,x_i}$ is flat over $\mathcal{O}_{S,s}$, and the finite
module $N=(f_*\mathcal{O}_X)_s=\mathrm{colim}_{V\ni s}\Gamma(f^{-1}(V),\mathcal{O}_X)$
has the property that
$N\otimes_{\mathcal{O}_{S,s}}\kappa(s)=\Gamma(X_s,\mathcal{O})$ (the base
change identity [lem-pc-flat-base-change-cohom]). Since $N$ is finitely
presented and flat over the local ring $\mathcal{O}_{S,s}$, Nakayama's
lemma makes it free, of rank
$\dim_{\kappa(s)}N\otimes\kappa(s)=\dim_{\kappa(s)}\Gamma(X_s,\mathcal{O})=d$,
the last equality being the definition [def-pc-finite-locally-free]. Hence
$f_*\mathcal{O}_X$ is locally free of rank $d$.

*Import note.* The source writes "$V\,$i$\,s$", a place where a backslash
was lost in the conversion; it is restored above as $V\ni s$. The source's
flatness paragraph is a chain of parenthetical false starts ("here we may
argue via the finite presentation ... the classical reference is: $f$ is
flat and fp, then $f_*\mathcal O_X$ is flat"); the argument above keeps the
route it settles on — finite presentation plus flatness over a local ring,
then Nakayama — and drops the abandoned attempts.
