+++
id = "prose-05-01"
kind = "hidden"
title = "Constructible sheaves and reduction to finite coefficients"
order = 229
+++
With finite coefficients the finiteness theorems are classical. For a
finite commutative $\ell$-primary ring, including $\mathcal O_E/\pi_E^n$,
proper direct image preserves $D^b_{\mathrm{ctf}}$, by the étale theory together with
a bound on Tor amplitude (Proposition [sk-prop-ctf-finite-proper]). The
construction of $Rf_!$ and $f^!$ in Section [sec-six-functors-basics] needs
the same facts for $\mathcal O_E$, $E$ and $\overline{\mathbf Q}_\ell$, for which $D^b_{\mathrm{ctf}}=\Dbc$;
we write $\Dbc$ when discussing cohomology sheaves, truncations and
lattices. The main result of this section is the following
(Proposition [sk-thm-sfb-proper-base-change]): for $p:X\to Y$ proper and
$\Lambda$ admissible, $Rp_*$ maps $D^b_{\mathrm{ctf}}(X,\Lambda)$ into
$D^b_{\mathrm{ctf}}(Y,\Lambda)$, and on these categories proper base change and the
projection formula hold. Over an algebraically closed field this says, for
instance, that the groups $H^i(X,\overline{\mathbf Q}_\ell)$ of a proper scheme $X$ are
finite-dimensional and vanish outside a bounded range of degrees.

The classical model is the description of a lisse $\Ql$-sheaf on a
connected normal scheme $X$ as a continuous representation
$\rho:\pi_1(X,\bar x)\to\GL_r(\Ql)$. Since $\pi_1(X,\bar x)$ is compact,
its image stabilizes a lattice $\Zl^r$, and so $\rho$ is defined over
$\Zl$; its reductions modulo $\ell^n$ are representations on finite
groups, that is, finite locally constant sheaves, where the torsion theory
applies. The arguments of this section are versions of this passage from
$E$ to $\mathcal O_E$ and then to $\mathcal O_E/\pi_E^n$. It is needed
because a rational coefficient sheaf has no reduction modulo $\pi_E$: the
sheaf $E_X$ is $\ell$-divisible, so that
$E_X\otimes^{\mathbf L}\mathcal O_E/\pi_E=0$, and to control a complex
over $E$ by torsion data we must first find integral objects inside it.

This can be done locally. An object of $\Dbc(X,\overline{\mathbf Q}_\ell)$ is defined over a
finite extension $E$ of $\Ql$
(Lemma [sk-thm-sfb-qlbar-two-colimit]). An object of $\Dbc(X,E)$
is built by finitely many cones from extensions by zero $a_!L$ of lisse
sheaves on locally closed strata
(Corollary [sk-cor-coefficient-heart-ii]); on $\mathbf A^1$, for
example, the localization sequence
$0\to j_!\Lambda_{\mathbf G_m}\to\Lambda_{\mathbf A^1}\to i_*\Lambda\to0$
exhibits the constant sheaf in this way (Example [sk-rem-running]).
After refining the stratum, a lisse sheaf $L$ contains a lattice $L_0$,
with $L=L_0[1/\ell]$ (Lemma [sk-lem-stratified-lattice]), and the
reductions of $a_!L_0$ modulo $\pi_E^n$ are classical torsion sheaves
(Lemma [sk-lem-integral-models]). The proof of the main result follows
these steps backwards. For $\mathcal O_E$, the complex $Rp_*K$ is derived
complete and its reduction modulo $\pi_E$ is $Rp_*$ of the reduction of
$K$, so the integral constructibility criterion
(Proposition [sk-prop-integral-criterion]) and derived Nakayama
(Lemma [sk-lem-pe-derived-nakayama]) reduce everything to torsion
coefficients. For $E$ and $\overline{\mathbf Q}_\ell$ it then suffices to treat the
generators $(a_!L_0)[1/\ell]$, because on bounded below complexes $Rp_*$
commutes with inverting $\ell$ and with extension of scalars to finite
extensions and to $\overline{\mathbf Q}_\ell$, both being filtered colimits
(Corollary [sk-cor-pe-bounded-continuity]).

The lattice cannot in general be chosen on all of $X$. On the
nodal curve obtained from $\mathbf P^1$ by gluing $0$ and $\infty$, the
infinite chain of projective lines is an étale $\mathbf Z$-torsor, and
letting the generator of $\mathbf Z$ act on $E$ by multiplication by $\ell$
we obtain a lisse $E$-sheaf of rank one with no lattice (see the
discussion before Lemma [sk-lem-stratified-lattice]). It comes from
the character $n\mapsto\ell^n$ of $\mathbf Z$, which does not extend
continuously to $\widehat{\mathbf Z}$, so it has no classical counterpart
as a system $(F_n)$; this example is discussed in [bhatt-scholze15]. On a
connected normal scheme the lattice
exists globally, and lisse $E$-sheaves are then the continuous
representations of the profinite group $\pi_1(X,\bar x)$
(Proposition [sk-p-real-integral]). We use this
description for the weights of lisse sheaves on curves in
Section [sec-rank-one-curves].

The same dévissage gives the two further facts that the compactness
argument of Section [sec-six-functors-basics] needs for field coefficients:
$\Hom$ out of a constructible complex commutes with filtered colimits of
uniformly bounded below complexes
(Lemma [sk-lem-constructible-ext-continuity]), and every object and
morphism of $\Dbc(X,\overline{\mathbf Q}_\ell)$ descends to a finite $E$
(Lemma [sk-thm-sfb-qlbar-two-colimit]). To make the dévissage
possible at all, we first show that constructible $E$- and $\overline{\mathbf Q}_\ell$-sheaves
form an abelian category (Lemma [sk-lem-coefficient-heart]). This is
not formal: a morphism of lisse sheaves is locally a matrix of continuous
functions to $E$, and its kernel becomes locally constant only after we
choose lattices and pass to a connected pro-étale cover on which the
lattices are constant.
