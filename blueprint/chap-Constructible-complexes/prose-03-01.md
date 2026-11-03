+++
id = "prose-03-01"
kind = "hidden"
title = "Constructible complexes"
order = 214
+++
A lisse $E$-sheaf is the analogue of a local system: pro-étale locally it is
isomorphic to $E_X^r$ for some $r$ (Definition [definition-lisse-sheaves] below).
A lattice in a lisse $E$-sheaf $L$ is a locally free $\mathcal O_E$-subsheaf
$L_0$ with $L_0[1/\ell]=L$. The first point of this section is that a lattice need
not exist. Glue $0$ and $\infty$ on $\mathbf P^1$ to obtain a nodal curve $X$. The infinite
chain $Y$ of projective lines, with $\infty$ on each line glued to $0$ on the next,
maps to $X$ by an étale covering. The group $\mathbf Z$ acts on $Y$ by
translation, simply transitively on the fibres, so $Y\to X$ is an étale
$\mathbf Z$-torsor. Letting
the generator of $\mathbf Z$ act on $E$ by multiplication by $\ell$, we obtain a
lisse $E$-sheaf of rank one. It has no lattice, because $\ell$ is not a unit of
$\mathcal O_E$, so that multiplication by $\ell$ does not carry any lattice onto
itself. The sheaf comes from the character
$n\mapsto\ell^n$ of $\mathbf Z$. Since this character does not extend continuously to
$\widehat{\mathbf Z}$, the sheaf has no classical counterpart as a system $(F_n)$
(see the discussion before Lemma [lemma-lattices-after-finite-stratification];
the example is in [bhatt-scholze15]).

This matters because every geometric input to the
next sections (proper base change, the cohomology of curves, Deligne's generic
base change) is a theorem about torsion sheaves. A rational sheaf has no
reduction modulo $\ell$: since $E_X$ is $\ell$-divisible, we have
$E_X\otimes^{\mathbf L}\mathcal O_E/\pi_E=0$. To use the torsion theory we must
therefore find integral objects inside rational ones, and then pass to their
torsion reductions. The example shows that this cannot be done globally.

Classically each coefficient ring comes with its own theory:

| coefficients | classical constructible objects |
|---|---|
| finite ring $A$ | constructible étale sheaves of $A$-modules |
| $\mathbf Z_\ell$, $\mathcal O_E$ | systems $(F_n)$ of constructible   $\mathcal O_E/\pi_E^n$-sheaves |
|  | with $F_{n+1}\otimes\mathcal O_E/\pi_E^n\simeq F_n$ |
| $\mathbf Q_\ell$, $E$ | the same systems up to isogeny, that is, with $\ell$ inverted |
| $\overline{\mathbf Q}_\ell$ | a colimit of the categories for all finite $E/\mathbf Q_\ell$ |

On the pro-étale site one local condition covers all of them. A
$\Lambda_X$-module is constructible if, on the strata of a finite stratification
of $X$, it is pro-étale locally of the form $\Lambda_X\otimes_{\Lambda(*)}P$ for
a finitely presented module $P$ over $\Lambda(*)$, the ring of sections over the
point
(Definition [definition-constructible-sheaves]). For finite $A$ these are the
classical constructible sheaves. For $E$ and $\overline{\mathbf Q}_\ell$ they are lisse on the strata.
For $\mathcal O_E$ torsion is allowed.

The six operations will act on $D^b_{\mathrm{ctf}}(X,\Lambda)$, bounded complexes with
constructible cohomology and finite Tor amplitude. For $\Lambda$ not a finite
ring, $D^b_{\mathrm{ctf}}(X,\Lambda)=\Dbc(X,\Lambda)$
(Proposition [proposition-ctf-equals-bc]). For a finite ring the Tor condition
matters: over $\mathbf Z/\ell^2$ the constructible sheaf $\mathbf F_\ell$ has
infinite Tor dimension (Section [sec-Constructibility] below).

Over $\mathcal O_E$ the passage to torsion is a criterion. For Noetherian $X$, a
complex is constructible exactly when it is derived complete and its reduction
modulo $\pi_E$ is constructible
(Proposition [proposition-integral-constructibility-criterion]). The criterion
is not formal, because the local models of the reductions modulo $\pi_E^n$ must be
made compatible in $n$
(Proposition [proposition-local-structure-integral-constructible-complexes],
Section [sec-Integral-constructible-complexes]). This description is due to Bhatt and
Scholze [bhatt-scholze15].

Over $E$ and $\overline{\mathbf Q}_\ell$, as the nodal curve shows, lattices exist only after
stratifying, and this is enough. After descending from $\overline{\mathbf Q}_\ell$ to a finite
extension $E$ of $\mathbf Q_\ell$ and refining a stratification, a lisse sheaf has a
lattice on each stratum
(Lemma [lemma-lattices-after-finite-stratification]), and the reductions
of the lattice modulo $\pi_E^n$ are classical torsion sheaves
(Lemma [lemma-integral-models]).

On a connected normal scheme no stratification is needed: there a lattice exists
globally, and lisse $E$-sheaves are continuous representations of
$\pi_1(X,\bar x)$
(Proposition [proposition-lattices-representations-normal-scheme], proved in
Part III).

Dévissage along strata also gives the continuity of $\Hom$ out of a constructible
complex (Lemma [lemma-continuity-ext-out-constructible-complex]), used with
descent to a finite $E$ in Section [chap-Construction-of-f]. Throughout this section
schemes are again separated and of finite type over $k$, as in our conventions.
