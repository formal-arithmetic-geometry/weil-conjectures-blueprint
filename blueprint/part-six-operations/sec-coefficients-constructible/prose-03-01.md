+++
id = "prose-03-01"
kind = "hidden"
title = "Coefficients and constructible complexes"
order = 126
+++
Classically each coefficient ring comes with its own theory, and each
theory is built on the previous one:

| coefficients | classical constructible objects |
|---|---|
| finite ring $A$ | constructible étale sheaves of $A$-modules |
| $\Zl$, $\mathcal O_E$ | systems $(F_n)$ of constructible
$\mathcal O_E/\pi_E^n$-sheaves |
| | with $F_{n+1}\otimes\mathcal O_E/\pi_E^n\simeq F_n$ |
| $\Ql$, $E$ | the same systems up to isogeny, that is, with $\ell$ inverted |
| $\overline{\mathbf Q}_\ell$ | a colimit of the categories for all finite $E/\Ql$ |

Every operation and every comparison has to be defined, and checked to be
compatible with the others, once for each line. On the pro-étale site
of Section [sec-proetale-coefficients] one definition covers all of
them, both for the coefficient sheaves and for the constructible
complexes, and the lines of the table become comparison theorems.

The coefficient rings are defined on a point. A topological ring $V$
defines a condensed ring $\underline V$, with $\underline V(S)$ the
continuous maps $S\to V$ for a profinite set $S$. For every scheme $X$
the functor sending $S$ to the pro-étale $X$-scheme
$X\times S=X\times_{\mathbf Z}\operatorname{Spec}LC(S,\mathbf Z)$, where
$LC(S,\mathbf Z)$ is the ring of locally constant functions, defines a
morphism of topoi from $X_{\mathrm{pro}\acute{e}t}$ to condensed sets
(Section [sec-n-coefficients]), and pulling $\underline V$ back along it gives a
sheaf of rings $V_X$ on $X_{\mathrm{pro}\acute{e}t}$. Pullback along
a morphism $f:X\to Y$ carries $V_Y$ to $V_X$, and a map of condensed rings
induces change of coefficients, which therefore commutes with pullback,
because the map of rings is itself pulled back. In
Lemma [sk-prop-sfb-qlbar-colimit-x] we check that this recovers the
classical descriptions:
$\mathcal O_{E,X}\simeq\varprojlim_n(\mathcal O_E/\pi_E^n)_X$,
$E_X\simeq\mathcal O_{E,X}[1/\ell]$ and $\QbarX\simeq\varinjlim_EE_X$.
The condensed ring we use for $\overline{\mathbf Q}_\ell$ is the colimit of the
$\underline E$. It is $\underline V$ for $V=\overline{\mathbf Q}_\ell$ with the colimit
topology, and it is strictly smaller than the sheaf of continuous maps to
$\overline{\mathbf Q}_\ell$ with its $\ell$-adic (norm) topology: algebraic numbers of
unbounded degree can converge to $0$.
We exclude such maps on purpose, so that every constructible
$\overline{\mathbf Q}_\ell$-complex is defined over a finite extension $E$
(Lemma [sk-thm-sfb-qlbar-two-colimit]).

Constructibility is then a single local condition. A
$\Lambda_X$-module is constructible if, on the strata of a finite
stratification of $X$, it is pro-étale locally of the form
$\Lambda_X\otimes_{\Lambda(*)}P$ for a finitely presented module $P$ over
$\Lambda(*)$, the ring of sections over the point
(Definition [sk-def-sfb-constructible]). For a finite ring $A$ these are
the classical constructible sheaves, by the comparison theorem of
Section [sec-proetale-coefficients]. For $E$ and $\overline{\mathbf Q}_\ell$ they are the
sheaves that are lisse, that is locally free of finite rank, on the strata.
For $\mathcal O_E$ torsion is allowed, and $\mathcal O_{E,X}/\pi_E$ is
constructible. The six operations will act on the category $D^b_{\mathrm{ctf}}(X,\Lambda)$
of bounded complexes with constructible cohomology and finite Tor
amplitude. For every $\Lambda$ other than a finite ring the Tor condition
is automatic, so that $D^b_{\mathrm{ctf}}(X,\Lambda)=\Dbc(X,\Lambda)$
(Proposition [sk-prop-n-ctf-equals-bc]). For a finite ring it is not: the
$\mathbf Z/\ell^2$-module $\mathbf F_\ell$ is constructible but has
infinite Tor dimension, and changing coefficients from $\mathbf Z/\ell^2$
to $\mathbf F_\ell$ carries it to an unbounded complex. Moreover,
$D^b_{\mathrm{ctf}}$ is not stable under truncation. For $A=\mathbf Z/\ell^2$ the
complex $[A\xrightarrow{\ell}A]$ is perfect, while its cohomology sheaves
$\mathbf F_\ell$ are not, so arguments by dévissage along cohomology
sheaves are made in $\Dbc$.

The definition is local, but integral complexes are usually known
through their reductions. The main result on constructibility is the
criterion of Proposition [sk-prop-integral-criterion]: for Noetherian $X$, a
complex $K\in D(X_{\mathrm{pro}\acute{e}t},\mathcal O_E)$ is constructible exactly when it
is derived complete and its reduction $K\otimes^{\mathbf L}\mathcal O_E/\pi_E$
is constructible. In this way questions over $\mathcal O_E$ become
questions with finite coefficients, where the étale theory applies. The
difficult implication produces, from the reductions $K_n$ modulo $\pi_E^n$,
local models $\mathcal O_{E,X}\otimes_{\mathcal O_E}P^\bullet$ with
$P^\bullet$ a bounded complex of finite free $\mathcal O_E$-modules. Each
$K_n$ has such a model separately, and the work is to make the local
isomorphisms compatible in $n$. On a weakly contractible cover this is a
Mittag–Leffler argument, whose uniform rate comes from the fact that the
torsion in the cohomology of $P^\bullet$ is killed by a fixed power of
$\pi_E$ (Proposition [sk-prop-integral-local-structure]). This description
of the integral constructible category is due to Bhatt and
Scholze (BS).

With the categories in place we can state the main theorem of
Part “The six operations” (Theorem [sk-thm-existence]): for every
admissible $\Lambda$ and every morphism $f$ of separated schemes of finite
type over $k$, the functor $Rf_!$ has a right adjoint $f^!$, constructed
by Brown representability on the localizing subcategory generated by
$D^b_{\mathrm{ctf}}$, and $f^!$ preserves $D^b_{\mathrm{ctf}}$. The plan of its proof is given in
Section [sec-plan]. Everything after this section takes place in the
categories $D^b_{\mathrm{ctf}}(X,\Lambda)$ defined here, together with their
localizing subcategories.
