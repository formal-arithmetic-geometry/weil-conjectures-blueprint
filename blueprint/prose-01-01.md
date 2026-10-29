+++
id = "prose-01-01"
kind = "hidden"
title = "Introduction: conjectures, strategy, coefficients, conventions"
order = 2
+++
The Weil conjectures, formulated by Weil in 1949 (Wei), are
statements about the number of solutions of polynomial equations over
finite fields. The simplest case already shows what is at stake. Let
$X_0$ be a smooth projective geometrically connected curve of genus
$g$ over $\mathbf F_q$, and
let $N_m$ be the number of its points over $\mathbf F_{q^m}$. Then
$N_m$ is close to $1+q^m$, the number of points of the projective
line, and the precise form of this statement is the bound

$$
|N_m-(1+q^m)|\le 2g\,q^{m/2}.
$$

Hasse proved it for elliptic curves and Weil for all curves. Written in
terms of the zeta function, it says that the zeros of a certain
function of a complex variable $s$ lie on the line $\operatorname{Re}s=\tfrac12$,
which is why it is called the Riemann hypothesis for $X_0$. Weil
conjectured that the same structure exists in every dimension.

Let $X_0$ be a separated scheme of finite type over $\mathbf F_q$. Its
zeta function is

$$
Z(X_0,T)=\exp\Bigl(\sum_{m\ge 1}\#X_0(\mathbf F_{q^m})\frac{T^m}{m}\Bigr)
\in 1+T\mathbf Z[[T]].
$$

Weil conjectured the following.

1. *Rationality.* $Z(X_0,T)$ is a rational function of $T$.
2. *Functional equation.* If $X_0$ is smooth and proper of pure
   dimension $d$, then $Z(X_0,1/(q^dT))=\pm q^{d\chi/2}T^{\chi}Z(X_0,T)$
   for an integer $\chi$, the self-intersection number of the diagonal.
3. *Riemann hypothesis.* If $X_0$ is smooth and proper of pure
   dimension $d$, then

   $$
   Z(X_0,T)=\frac{P_1(T)P_3(T)\cdots P_{2d-1}(T)}
   {P_0(T)P_2(T)\cdots P_{2d}(T)},
   $$

   where $P_i\in\mathbf Z[T]$ has constant term $1$ and its reciprocal
   roots are algebraic integers all of whose complex conjugates have
   absolute value $q^{i/2}$.
4. *Betti numbers.* The degree $b_i$ of $P_i$ is an invariant of
   $X_0$ that behaves like a Betti number; for instance $b_i=b_{2d-i}$,
   and if $X_0$ is the reduction, at a prime of good reduction, of a
   smooth projective variety over a number field, $b_i$ is the $i$th
   Betti number of the associated complex manifold.

For a curve, (3) says that $Z(X_0,T)=P_1(T)/((1-T)(1-qT))$ with $P_1$ of
degree $2g$ and reciprocal roots of absolute value $q^{1/2}$, and taking
logarithms gives the bound on $N_m$ above.

We follow one example through the notes: the elliptic curve

$$
C_0\colon\ y^2=x^3-x\qquad\text{over }\mathbf F_3 .
$$

Counting points gives $N_1=4$, $N_2=16$ and $N_3=28$. The Weil conjectures
predict $Z(C_0,T)=P_1(T)/((1-T)(1-3T))$ with
$P_1(T)=1-(1+3-N_1)T+3T^2=1+3T^2$, which has reciprocal roots $\pm i\sqrt3$ of absolute value
$3^{1/2}$, and then $N_m=1+3^m-\bigl((i\sqrt3)^m+(-i\sqrt3)^m\bigr)$. For
$m=2,3$ this gives $16$ and $28$, as it should. We return to it after
duality, after the trace formula and at the end
(Examples “The running example: duality”, “The running example: the trace formula” and
“The running example: purity”).

Weil also explained why the conjectures should be true. Suppose that
there is a cohomology theory for varieties over
$\overline{\mathbf F}_q$, assigning to $X=X_0\times_{\mathbf F_q}\overline{\mathbf F}_q$
finite-dimensional vector spaces $H^i_c(X)$ over a field of
characteristic zero, on which the Frobenius $F$ of $X_0$ acts. These are
cohomology groups with compact supports, and they agree with the
ordinary cohomology groups $H^i(X)$ when $X_0$ is proper. The theory
should satisfy the following.

- (a) *Finiteness.* $H^i_c(X)=0$ unless $0\le i\le 2\dim X$.
- (b) *Trace formula.* The points of $X_0$ over
  $\mathbf F_{q^m}$ are the fixed points of $F^m$, and they are counted
  by a Lefschetz formula,

  $$
  \#X_0(\mathbf F_{q^m})=\sum_i(-1)^i\operatorname{Tr}\bigl(F^m\mid H^i_c(X)\bigr).
  $$

- (c) *Poincaré duality.* For smooth proper $X_0$ of pure dimension
  $d$, cup product gives a perfect pairing between $H^i$ and $H^{2d-i}$,
  and $\langle Fx,Fy\rangle=q^d\langle x,y\rangle$.
- (d) *Purity.* For smooth proper $X_0$, the eigenvalues of $F$ on
  $H^i(X)$ are algebraic integers of absolute value $q^{i/2}$.

Then (a) and (b) imply rationality: taking logarithms of both sides of
the trace formula, we see that $Z(X_0,T)$ is the alternating product of
the polynomials $\det(1-TF\mid H^i_c(X))$. Duality (c) says that the eigenvalues in degree
$2d-i$ are the $q^d/\alpha$ for the eigenvalues $\alpha$ in degree $i$,
and the functional equation follows. Purity (d) implies the Riemann
hypothesis, and more: since the factors in different degrees
have roots of different absolute values, they cannot cancel in the
alternating product, so they are determined by $Z(X_0,T)$ alone. In
particular they have integer coefficients and do not depend on the
cohomology theory, which is the statement about Betti numbers.

Grothendieck constructed such a theory: $\ell$-adic cohomology, for a
prime $\ell$ not dividing $q$. He and his collaborators proved (a), (b) and (c) in
SGA 4 and SGA 5 (SGA4, SGA5), and this proves rationality and the
functional equation (Section “Determinants, closed points and the Euler product”). Purity (d) is the hard
part. It was proved by Deligne (De1), and later in a
more general form (De2). We follow the proof of Deligne's
theorem on weights by the Fourier transform, due to Laumon (Lau). Its main idea is to
prove an upper bound for the absolute values of the Frobenius
eigenvalues (the *weights*) on the cohomology with compact supports
of the fibres of every morphism $f$, with coefficients in every
$\ell$-adic sheaf and not only in the constant sheaf. Duality then turns
the upper bound into purity. Working with sheaves allows an induction:
a variety is fibred in curves, and the essential case is a curve,
where the bound comes from a positivity argument and the Fourier
transform.

We prove two parts of the statement (4) on Betti numbers: that
$b_i=b_{2d-i}$, and that $b_i=\dim H^i(X,\Ql)$ for every $\ell$ not
dividing $q$, so that this dimension does not depend on $\ell$ (Theorem [sk-thm-weil-final]). The comparison
of $b_i$ with the Betti numbers of a lift to characteristic zero needs
the comparison theorem between étale and singular cohomology, which
we do not prove.

Poincaré duality is the axiom that shapes the construction of the
six operations. Let $X$ be smooth of pure dimension $d$ over an
algebraically closed field $k$, let $a:X\to\operatorname{Spec}k$ be its
structure map, and let $\Lambda$ be a coefficient ring such as
$\mathbf Z/\ell^n$. We want perfect pairings

$$
H_c^i(X,\Lambda)\times H^{2d-i}(X,\Lambda(d))\longrightarrow\Lambda
$$

between cohomology with compact supports and cohomology with
coefficients in the Tate twist $\Lambda(d)$
(Definition [sk-def-sp-tate-twist]); for $\Lambda=\mathbf Z/\ell^n$ this
is the sheaf $\mu_{\ell^n}^{\otimes d}$.
For a manifold one proves duality by working locally and gluing, and in
algebraic geometry the device that makes this possible is a right
adjoint $a^!$ of the direct image with compact supports $Ra_!$, the
functor whose cohomology groups are the $H^i_c$. This right adjoint is
called the *exceptional inverse image*. Once
$a^!$ exists, duality says two things: that $\cHom(-,a^!\Lambda)$ is a
perfect duality on constructible complexes (Verdier duality), and that
$a^!\Lambda\simeq\Lambda_X(d)[2d]$, where $\Lambda_X$ is the constant
sheaf (smooth purity). The pairing is
evaluation followed by the counit $Ra_!a^!\Lambda\to\Lambda$, and the
twist $(d)$, the shift $[2d]$ and the trace all come from the
isomorphism of smooth purity. The same right adjoint, for a general morphism $f$, is
what makes the trace formula local: the local term at a fixed point is
computed from $f^!$.

So the main theorem of Part “The six operations” is that $f^!$ exists and has the
expected finiteness (Theorem [sk-thm-existence]). Existence is a general
fact about triangulated categories: Brown representability produces a
right adjoint of any triangulated functor out of a compactly generated
triangulated category that preserves direct sums, and the problem
is to put $Rf_!$ in a setting where this applies. Finiteness, that
$f^!$ carries constructible complexes to constructible complexes, is a
geometric statement; it reduces to an explicit computation for the
projective line and to Deligne's theorem that direct images along open
immersions preserve constructibility.

The trace formula and duality are easiest to prove with torsion
coefficients $\mathbf Z/\ell^n$, where the classical theory of
SGA 4 (SGA4) applies, but the eigenvalues of Frobenius live in
characteristic zero. One therefore needs the six operations for
$\Zl$, $\Ql$ and $\overline{\mathbf Q}_\ell$ as well, compatibly with reduction modulo
$\ell^n$. Classically an $\ell$-adic sheaf is a compatible system
$(F_n)$ of sheaves of $\mathbf Z/\ell^n$-modules; this works well for
sheaves, but on the level of derived categories one has to construct the
$\ell$-adic theory by hand, as Ekedahl did (Eke).

We avoid this by working on the pro-étale site of Bhatt and
Scholze (BS). There $\Zl$ is a sheaf of rings, an $\ell$-adic sheaf
is a sheaf of modules over it, and the derived category is the ordinary
one. All coefficient rings are obtained in one way, by pulling back a
*condensed ring* (a sheaf of rings on the category of profinite
sets; a topological ring $R$ such as $\Zl$ gives one,
$S\mapsto C(S,R)$) to every scheme (Section “The coefficient rings”), so a
single construction of $f^!$ applies to all of them at once. The
classical descriptions by completion, by inverting $\ell$ and by
colimits become comparison theorems (Section “Change of coefficients”), and the
geometric arguments are needed only with torsion coefficients, where
they are classical.

Throughout, $\Lambda$ is one of the *admissible* coefficient rings

$$
A,\quad\Zl,\quad\mathcal O_E,\quad\Ql,\quad E,\quad\overline{\mathbf Q}_\ell,
$$

where $A$ is a finite commutative ring killed by a power of $\ell$ and
$E$ is a finite extension of $\Ql$ with ring of integers $\mathcal O_E$.
We allow $E=\Ql$, so that $\Zl$ and $\Ql$ are among the rings
$\mathcal O_E$ and $E$.
The operations act on the category $\Dctf(X,\Lambda)$ of bounded
constructible complexes of finite Tor amplitude
(Section “Constructible complexes”). For integral and rational coefficients this is
just the category $\Dbc(X,\Lambda)$ of bounded constructible complexes;
for a finite ring such as $\mathbf Z/\ell^2$ the Tor condition is needed
so that changing coefficients preserves boundedness.

The main theorem of these notes is the Weil conjectures for smooth
proper varieties over $\mathbf F_q$ (Theorem [sk-thm-weil-final]
and Remark [sk-rem-wweil-disconnected]),
with the statement on Betti numbers in the form explained above. Neither
the proof of (a)–(c) nor the proof of purity can be carried out with
the cohomology groups of a single variety. The trace formula is proved by
cutting $X_0$ into pieces and comparing their cohomology; duality is
proved by induction on dimension; and the proof of purity pushes sheaves
forward along families of curves. All of this happens in the derived
category of $\ell$-adic sheaves, with the *six operations* $f^*$,
$Rf_*$, $Rf_!$, $f^!$, $\otimes^{\mathbf L}$ and $\cHom$ and the base
change theorems relating them. The notes have three parts.

- Part “The six operations” (Sections “The pro-étale site and its comparison theorems”–“Smooth base change”)
  constructs the six operations for all coefficient rings
  (Theorem [sk-thm-existence]). It ends with smooth base change, which
  completes the formalism but is not used in the proof of the Weil conjectures.
- Part “Duality and the trace formula” (Sections “Smooth purity”–“The Grothendieck–Lefschetz trace formula”)
  proves (a), (b) and (c): smooth purity $f^!\simeq f^*(d)[2d]$,
  Verdier and Poincaré duality, and the trace formula with its Frobenius compatibilities,
  and it ends with rationality and the functional equation.
- Part “Weights and the Riemann hypothesis” (Sections “Weights: definitions and the main theorem”–“Cohomology of smooth proper schemes and the Weil conjectures”)
  proves purity (d) and the Weil conjectures, following (WBP).
  Section “Weights: definitions and the main theorem” explains how the argument is organized.

The appendices prove results from algebraic geometry that we use.

We assume a first course in algebraic geometry: schemes, quasi-coherent
sheaves and their cohomology, and étale morphisms. Some familiarity
with étale cohomology with torsion coefficients, at the level of the
statements in SGA 4$\tfrac12$ (SGA4.5), helps, but the results we use are
stated where they are needed. Derived categories are used throughout;
the reader should know what a triangulated category and a derived
functor are.

On a first reading one can take the foundations on trust and follow the
main line:

- the statements of Section “Coefficients, constructible complexes and the main theorem” and of the main
  theorem of Part “The six operations”, Theorem [sk-thm-existence];
- the base change map and the statement of proper base change
  (Theorem [sk-thm-properbasechange]);
- Section “The exceptional inverse image preserves constructibility” on why $f^!$ preserves
  constructibility with torsion coefficients;
- smooth purity with finite coefficients (Section “Finite coefficients: the plan”),
  which is where the twist $(d)$, the shift $[2d]$ and the trace come
  from;
- Section “Verdier and Poincaré duality” on duality;
- Frobenius and Weil complexes (Section “Frobenius and Weil complexes”); in
  Section “The Grothendieck–Lefschetz trace formula”, the local
  calculation at a fixed point of Frobenius on a curve;
- Sections “Weights: definitions and the main theorem”–“Cohomology of smooth proper schemes and the Weil conjectures”, beginning with
  the explanation in Section “The weight bound and why it holds”.

The passages between coefficient rings (most of which are applications of
Proposition [sk-prop-reduction-to-finite]), the coherence of the various
comparison maps, smooth base change (Section “Smooth base change”),
and the pro-étale foundations of Section “The pro-étale site and its comparison theorems”
can be read when needed.

We fix a prime $\ell$ and a field $k$ that is finite or algebraically
closed, of characteristic different from $\ell$. Unless said otherwise,
schemes are separated and of finite type over $k$, and morphisms are
$k$-morphisms. The hypothesis on $k$ is used to bound the
$\ell$-cohomological dimension of $k$
(Lemma [sk-lem-base-field-cd]). The constructions of
Sections “The coefficient rings” and “Derived functors of module sheaves” make sense for arbitrary
schemes.

All coefficient rings are regarded as condensed rings, and in every case
the coefficient sheaf $\Lambda_X$ on $X$ is the pullback of $\Lambda$
along the map from $X$ to a point (Section “The coefficient rings”). For a
finite ring $A$ this pullback is the classical constant sheaf.

Derived categories are the classical ones: $D(X_{\mathrm{pro\acute et}},\Lambda)$ is
the derived category of the abelian category of sheaves of
$\Lambda_X$-modules. All functors are derived, and we write $f^*$,
$Rf_*$, $Rf_!$ and $f^!$. Unless another category is named,
$f^*:D(Y_{\mathrm{pro\acute et}},\Lambda)\to D(X_{\mathrm{pro\acute et}},\Lambda)$ and
$Rf_*:D(X_{\mathrm{pro\acute et}},\Lambda)\to D(Y_{\mathrm{pro\acute et}},\Lambda)$; the
categories on which $Rf_!$ and $f^!$ act are fixed where these functors
are defined. Sizes are taken with respect to a fixed universe, large enough to
contain the w-contractible covers of Theorem [sk-thm-pe-wc-cover].

Part “The six operations” constructs the six operations and proves
Theorem [sk-thm-existence], the existence and finiteness of $f^!$ described
in the introduction. The base field is finite or algebraically closed, and
Frobenius plays no role. A reader who is willing to take the six
operations on trust can start with Part “Duality and the trace formula”.
