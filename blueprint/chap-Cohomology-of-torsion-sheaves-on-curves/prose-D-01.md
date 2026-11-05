+++
id = "prose-D-01"
kind = "hidden"
title = "Cohomology of torsion sheaves on curves"
order = 1571
+++
The last step of proper base change for $\mathbf P^1$ compares the
cohomology of a curve over two separably closed fields, one inside the
other. Smooth base change needs the same comparison for affine
curves, with coefficients prime to the characteristic. Both
rest on Theorem [theorem-cohomology-curves], whose assertions we
recall. Let $k$ be algebraically closed, let $C$ be a separated scheme
of finite type over $k$ with $\dim C\leq1$, and let $F$ be a classical
torsion abelian sheaf on $C_{\mathrm{pro}\acute{e}t}$. Then:

- $(C_{1})$ $H^q(C,F)=0$ for $q>2$;
- $(C_{2})$ if $C$ is affine, $H^q(C,F)=0$ for $q>1$;
- $(C_{3})$ if $\operatorname{char}k=p>0$ and $F$ is $p$-primary,
  $H^q(C,F)=0$ for $q>1$;
- $(C_{4})$ if $F$ is constructible with finite stalks and prime to
  $\operatorname{char}k$, all $H^q(C,F)$ are finite;
- $(C_{5})$ if $C$ is proper and $F$ is constructible with finite stalks,
  all $H^q(C,F)$ are finite;
- $(C_{6})$ if $k'/k$ is an extension of algebraically closed fields and $F$
  is prime to $\operatorname{char}k$, the pullback maps
  $H^q(C,F)\to H^q(C_{k'},F|)$ are isomorphisms;
- $(C_{7})$ if $C$ is proper, the maps in $(C_6)$ are isomorphisms for every
  torsion $F$;
- $(C_{8})$ for any open $U\subseteq C$, restriction
  $H^2(C,F)\to H^2(U,F|_U)$ is surjective.

Over $\mathbf C$ the vanishing and finiteness assertions are statements
about a Riemann surface, which has the homotopy type of a CW complex of
dimension two, or of one if it is not compact.

In algebraic geometry we compute the groups. Let $C$ be a smooth proper
connected curve of genus $g$ and let $n$ be invertible in $k$. Three
ingredients compute the cohomology of $\mu_n$: the Kummer
sequence $0\to\mu_n\to\mathbf G_m\xrightarrow{n}\mathbf G_m\to0$, the
vanishing of $H^q(C,\mathbf G_m)$ for $q\geq2$, which is a consequence of
Tsen's theorem, and the Jacobian of Appendix [chap-The-Picard-scheme-of-a-curve]. They give

$$
H^0(C,\mu_n)=\mu_n(k),\qquad H^1(C,\mu_n)=J(C)[n](k)\simeq(\mathbf Z/n)^{2g},
\qquad H^2(C,\mu_n)=\mathbf Z/n
$$

(Proposition [proposition-smooth-proper-curves-torsion-prime]).
These groups do not change under extension of algebraically closed
fields, because torsion points of an abelian variety do not. For $\mathbf P^1$, which has $g=0$, the computation fixes the normalization of
the class of $\mathcal O(1)$ that
Remark [remark-twists-projective-line] provides for the proof of
proper base change. Removing a nonempty finite set of $r$ points kills
$H^2$ and raises the rank of $H^1$ to $2g+r-1$
(Proposition [proposition-cohomology-smooth-affine-curve]).

Proper base change, however, is needed for all torsion coefficients,
including those divisible by the characteristic $p$, and there the
answer changes. On the affine line,
$H^1(\mathbf A^1_k,\mathbf F_p)=k[t]/\{h^p-h\}$ is infinite, and it grows
when $k$ is enlarged (Example [example-affine-line-characteristic-p]).
Indeed, the Artin–Schreier torsors $y^p-y=at$, for $a\in k$, have
pairwise distinct classes, and over a larger field $k'$ there are new ones
with $a\in k'\setminus k$. So for $p$-torsion coefficients, finiteness
and invariance under field extension hold only for proper curves. This is
why $(C_5)$ and $(C_7)$ of Theorem [theorem-cohomology-curves] assume
properness, and why
Lemma [lemma-extension-separably-closed-ground-field] is stated for
proper curves.

The Artin–Schreier sequence
$0\to\mathbf F_p\to\mathbf G_a\xrightarrow{\varphi-1}\mathbf G_a\to0$
reduces the cohomology of $\mathbf F_p$ to the coherent cohomology of
$\mathcal O_C$. On the affine line it presents $H^1$ as the cokernel of
$h\mapsto h^p-h$ on $k[t]$, as above. On every curve it gives
$H^q(C,\mathbf F_p)=0$ for $q\geq2$
(Theorem [theorem-cohomology-curves], $(C_3)$).

A general torsion sheaf is reduced to a constant one by two observations.
First, a sheaf supported on finitely many points has no cohomology in
positive degrees. Hence passing to the normalization of a curve, or
extending a sheaf by zero from a dense open subset, changes cohomology
only in degrees zero and one, and only by finite groups
(Lemmas [lemma-normalization-constant-sheaf] and [lemma-removing-finitely-many-points]).
Second, a finite $\mathbf F_\ell$-local system becomes a successive
extension of constant sheaves on a finite étale cover of degree $d$
prime to $\ell$. This cover is given by an $\ell$-Sylow subgroup of the
monodromy. Dividing the trace of the cover by $d$ shows that the local
system is a direct summand of the pushforward of its pullback
(Lemma [lemma-reduction-unipotent-local-system]). We follow the
proof of [Stacks, [03SC](https://stacks.math.columbia.edu/tag/03SC)].

Throughout this appendix, cohomology means cohomology on $C_{\mathrm{pro}\acute{e}t}$,
and the sheaves are classical in the sense of
Definition [definition-classical-pro-etale-sheaves]: by
Theorem [theorem-classical-sheaves-essential-image] such a sheaf is the inverse image
$\nu_C^*G$ of a sheaf $G$ on $C_{\acute{e}t}$ along the comparison morphism.
By Theorem [theorem-bounded-below-cohomology-comparison], its cohomology, together with
the restriction and pullback maps, agrees with étale cohomology, so
we carry out all calculations on $C_{\acute{e}t}$ and transport them back by
$\nu_C^*$.

Let $p\ge0$ be the characteristic of $k$. In this appendix $\ell$ is
an arbitrary prime, possibly equal to $p$. In characteristic zero the
hypotheses in $(C_4)$ and $(C_6)$ of Theorem [theorem-cohomology-curves] that
$F$ be prime to the characteristic hold automatically. We begin with direct images along finite morphisms,
which all the reductions below use.
