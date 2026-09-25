+++
id = "lem-sf-stage-independent-model-criterion"
kind = "lemma"
title = "Stage-independent local models from a uniform trivializing cover"
order = 2340
uses = ["def-weil-derived-cohomology-sheaves", "def-weil-finite-tor-amplitude", "def-weil-pbc-adic-coefficient-datum", "def-weil-pbc-bounded-constructible-tower", "def-weil-pbc-proetale-site", "lem-sf-bounded-free-model", "lem-sf-fullcd-detection-equivalence", "lem-sf-lift-free-tower", "lem-sf-minimal-free-model"]
+++
Let $T$ be a scheme on which $\ell$ is invertible, let
$M_\bullet$ be an adic tower on $T$ in the sense of
[def-weil-pbc-adic-coefficient-datum], with the normalization
isomorphisms $M_{n+1}\otimes^L_{A_{E,n+1}}A_{E,n}\simeq M_n$ of
[def-weil-pbc-bounded-constructible-tower], and let
$u:U\to T$ be a finite étale surjective morphism. Assume that for every
$n\geq1$ the restriction $M_n|_U$ is a bounded complex of
$A_{E,n}$-module sheaves whose
cohomology sheaves are
locally constant with finite $A_{E,n}$-module stalks and vanish outside
the interval $[a,b]$, and that $M_n|_U$ has
finite Tor amplitude in $[a,b]$.
Then $M_\bullet$ is uniformly bounded constructible in the sense of
[def-weil-pbc-bounded-constructible-tower]: there are an affine weakly
contractible object $W$ of the
small pro-étale site of $T$, with
a pro-étale covering $\lbrace W\to T\rbrace$, and a bounded complex
$L$ of finite locally constant $A_T|_W$-modules with $L^q=0$ for
$q\notin[a,b]$, such that

$$
M_n|_W\xrightarrow{\ \sim\ }
L\otimes^L_{A_T}(P_n)_T|_W
\qquad(n\geq1),
$$

the isomorphisms being compatible with the normalization maps.

## Proof

*Step 0: a covering member, and the two facts used about it.* The
pro-étale site has enough affine quasi-compact weakly contractible
objects: Stacks Project, Pro-étale Cohomology, Lemma 61.13.4,
[Tag 0990](https://stacks.math.columbia.edu/tag/0990). What is used
here is the sharper form of that statement, Stacks Project, Pro-étale
Cohomology, Lemma 61.13.5,
[Tag 0F4P](https://stacks.math.columbia.edu/tag/0F4P): for every object
$U$ of the small pro-étale site there is a covering $\lbrace W\to U\rbrace$
by a *single* weakly contractible object $W$, which may be chosen
affine when $U$ is quasi-compact, as it is here. We take such a $W$ over
$U$; the composite $W\to U\to T$ is a pro-étale covering of $T$ and
$W$ is affine and weakly contractible. Recall the
two consequences of weak contractibility used below, both of them the
argument of [lem-sf-fullcd-detection-equivalence]: (i) the
global-sections functor $\Gamma(W,-)$ is exact, because for a surjection
$\mathcal G\to\mathcal G'$ of sheaves and a section of $\mathcal G'$
over $W$ there is a covering family of $W$ on which the section lifts,
and weak contractibility supplies a member of that family admitting a
section $W\to W_i$ along which the lift pulls back; (ii) every locally
constant sheaf on $W_{\Proet}$ is constant, because a covering family
trivializing it contains a member with a section, and pulling back a
constant sheaf along a morphism that admits a section gives a constant
sheaf. In particular $\Gamma(W,\underline{N}_W)=N$ for every
$A_{E,n}$-module $N$: a locally constant function on $W$ with values
in $N$ is constant, being constant on a member of a covering that admits a
section.
*Step 1: the value complexes.* By (ii) the cohomology sheaves of
$M_n|_W$ are constant, with finite values, for every $n$; choose a
representative $K_n^\bullet$ of $M_n|_W$ concentrated in degrees
$[a,b]$, namely the truncation
$\sigma_{\geq a}\sigma_{\leq b}$, and put

$$
V_n=\Gamma(W,K_n^\bullet),
$$

a complex of $A_{E,n}$-modules concentrated in $[a,b]$ whose cohomology
modules are finite, $H^q(V_n)=\Gamma(W,H^q(K_n^\bullet))$, by exactness
(i). Let $(V_n)_W$ be the constant complex with value $V_n$ and let
$c_n:(V_n)_W\to K_n^\bullet$ be the unit of the adjunction between the
constant-sheaf functor and $\Gamma(W,-)$, which is adjoint to the identity
of $V_n$. The map $c_n$ is a quasi-isomorphism: on cohomology it is,
by exactness (i) and the identification $\Gamma(W,\underline{N}_W)=N$, the
map $H^q(K_n^\bullet)\to(H^q(V_n))_W$ of constant sheaves with the same
value, hence an isomorphism. So $M_n|_W\cong K_n^\bullet\cong(V_n)_W$.
*Step 2: the hypotheses pass to the value complexes.* For an
$A_{E,n}$-module $N$ the constant-sheaf functor is exact and monoidal,
so $(V_n\otimes^L_{A_{E,n}}N)_W\cong(V_n)_W\otimes^L_{A_{E,n}}\underline{N}_W \cong M_n|_W\otimes^L_{A_{E,n}}\underline{N}_W$; the right-hand side has
cohomology concentrated in $[a,b]$ by the assumed finite Tor amplitude of
$M_n|_W$, tested against the sheaf $\underline{N}_W$ placed in degree
zero, and a constant complex vanishes if and only if its value complex does.
Hence $V_n$ satisfies the hypothesis of
[lem-sf-bounded-free-model]: bounded, finite cohomology in $[a,b]$,
and $H^r(V_n\otimes^L_{A_{E,n}}N)=0$ for every $r\notin[a,b]$ and every
$A_{E,n}$-module $N$. By that lemma and by
[lem-sf-minimal-free-model] we may therefore choose, for every $n$,
a bounded complex $F_n$ of finite free $A_{E,n}$-modules with
$F_n^q=0$ for $q\notin[a,b]$, all of whose differentials have entries in
$\varpi_EA_{E,n}$, and isomorphisms $F_n\cong V_n$ in
$D(A_{E,n})$.
*Step 3: the ranks are independent of the stage.* The two lemmas give

$$
\operatorname{rank}_{A_{E,n}}F_n^q
=\dim_{\kappa_E}H^q\bigl(V_n\otimes^L_{A_{E,n}}\kappa_E\bigr)
=\dim_{\kappa_E}H^q\bigl(M_n|_W\otimes^L_{A_{E,n}}\kappa_E\bigr),
$$

the second equality by Step 2. Writing
$M_n|_W\cong M_{n+1}|_W\otimes^L_{A_{E,n+1}}A_{E,n}$ for the
normalization isomorphism of the statement and using associativity of the
derived tensor product,

$$
M_{n+1}|_W\otimes^L_{A_{E,n+1}}\kappa_E
\cong\bigl(M_{n+1}|_W\otimes^L_{A_{E,n+1}}A_{E,n}\bigr)
\otimes^L_{A_{E,n}}\kappa_E
\cong M_n|_W\otimes^L_{A_{E,n}}\kappa_E,
$$

so the displayed dimension is independent of $n$; write $r^q$ for it.
*Step 4: compatibility of the models.* From Step 1 and the
normalization isomorphisms,

$$
V_{n+1}\otimes^L_{A_{E,n+1}}A_{E,n}\cong V_n
\qquad(n\geq1):
$$

both sides are constant complexes, and after applying the exact functor
$(-)_W$ the isomorphism becomes
$(V_{n+1})_W\otimes^L_{A_{E,n+1}}A_{E,n}\cong(V_n)_W$, which is
$M_{n+1}|_W\otimes^L_{A_{E,n+1}}A_{E,n}\cong M_n|_W$ by Step 1; the
constant-complex functor is fully faithful, its right adjoint
$\Gamma(W,-)$ being exact with $\Gamma(W,\underline{N}_W)=N$, so the
isomorphism descends. Consequently
$F_{n+1}\otimes^L_{A_{E,n+1}}A_{E,n}\cong F_n$, and the hypotheses of
[lem-sf-lift-free-tower] are met, that lemma's rank hypothesis being
Step 3 and its minimality hypothesis being the minimality of the models
$F_n$ chosen in Step 2.
*Step 5: the stage-independent model.* By
[lem-sf-lift-free-tower] there is a bounded complex $F$ of finite
free $\mathcal O_E$-modules, concentrated in degrees $[a,b]$, with
$F\otimes^L_{\mathcal O_E}A_{E,n}\cong F_n$ for every $n$. Put

$$
L=F_W,
$$

the constant complex on $W$ with value $F$: its terms are finite
locally constant $A_T|_W$-modules, namely the constant sheaves with the
finite free values $F^q$, and $L^q=0$ for $q\notin[a,b]$. For every
$n$,

$$
L\otimes^L_{A_T}(P_n)_T|_W
=(F\otimes^L_{\mathcal O_E}A_{E,n})_W\cong(F_n)_W\cong(V_n)_W
\cong M_n|_W,
$$

using that the constant-sheaf functor is exact and monoidal, Step 5 for the
first isomorphism, Step 2 for the second and Step 1 for the last. These
isomorphisms intertwine the normalization maps because they are induced by
the transition maps of the tower and of the lifted complex $F$. Hence the
datum of [def-weil-pbc-bounded-constructible-tower] exists with the
stratification of $T$ by the single stratum $T$, the pro-étale
covering $\lbrace W\to T\rbrace$, the models $L_{\alpha j}=L$ and the
bounds $d_0=a$, $d_1=b$; the reductions of $L$ have finite lisse
cohomology because they are the $M_n|_W$.
