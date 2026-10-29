+++
id = "prose-A5-00"
kind = "hidden"
title = "Opening of the specialization appendix"
order = 3640
+++
If a correspondence contracts a closed subscheme $Z$ towards itself,
then its local terms along $Z$ can be computed on $Z$ alone
(Theorem [sk-thm-tf-contracting-local-term]). For $Z$ a point this says
that the local term at an isolated fixed point is the trace on the
stalk (Corollary [sk-cor-tf-contracting-input]). This gives a second
computation, by specialization, of local terms that
Section “The Grothendieck–Lefschetz trace formula” computes directly on curves. The trace
formula there (Theorem [sk-thm-tf-uniform-formula]) does not depend on this
appendix.

The idea is to deform the correspondence to the normal cone of $Z$.
On the special fibre of the deformation the leg that contracts maps into
the zero section, and there the trace class only involves the
restriction to $Z$, by Verdier's theorem that specialization to the
normal cone, restricted to the zero section, is restriction to $Z$. It
remains to show that the trace class on the generic fibre specializes
to the trace class on the special fibre. Since the trace class is built
from $K\boxtimes\mathbb DK$, this comes down to the fact that nearby
cycles commute with external products and with Verdier duality, and we
prove both by a dimension argument of Illusie.

We use the six operations and the notation for correspondences and
trace classes of Section “Frobenius, trace classes and the Lefschetz–Verdier formula”, and classical results
on nearby cycles over a trait, which we recall where they are first
needed. Throughout this appendix, $k$ is algebraically closed, $\ell$ is
invertible in $k$, and $A$ is a finite commutative ring annihilated by
a power of $\ell$. Statements about
constructible complexes on $k$-schemes are made on the pro-étale site.
We construct nearby cycles on the classical étale site and transport
them by the comparison for constructible complexes (Theorem [sk-thm-pe-constructible-comparison] and
Corollary [sk-cor-pe-finite-tor-comparison]).

Specialization to the normal cone is defined by nearby cycles on the
deformation to the normal cone, so for Verdier's theorem
(Theorem [sk-thm-tf-sp-zero-section]; see
Var, §§1.3–1.4 and 3) we first recall the facts about
nearby cycles that we need.

This defines a functor
$R\Psi_{\mathcal Y}:D^b_c(\mathcal Y_{\eta,\mathrm{\acute et}},A)\to
D(\mathcal Y_{s,\mathrm{\acute et}},A)$. We suppress the inertia action, except
where invariants under the wild inertia group of a finite extension of
traits are taken below.

By the finiteness theorem for nearby cycles with torsion coefficients
(SGA4.5, *Théorèmes de finitude*, §3;
Ill, §4.1, pp. 44–45), $R\Psi_{\mathcal Y}$ takes
bounded constructible complexes of finite Tor dimension to bounded
constructible complexes of finite Tor dimension. We need the
preservation of finite Tor dimension for traces. We deduce that
$R\Psi_{\mathcal Y}$ preserves bounded constructible complexes in
general as follows.
The underlying torsion sheaves of $A$-linear nearby cycles are the
usual nearby cycles of torsion sheaves, and hence boundedness and
constructibility can be checked after forgetting the $A$-action.  Since
bounded constructible complexes are stable under extensions, truncation
reduces us to one finite $\ell$-primary constructible sheaf, and then to
the graded pieces of its filtration by powers of $\ell$. These are
constructible $\mathbf F_\ell$-sheaves, which have finite Tor dimension
over $\mathbf F_\ell$, so the theorem applies to them.

These base change maps commute with composition and with the specialization
map defined below. Their invertibility follows from two base change
theorems for torsion coefficients. Proper base change [Stacks, Tag 095T](https://stacks.math.columbia.edu/tag/095T)
says that restriction to a fibre commutes with proper direct image.
Smooth base change [Stacks, Tag 0F09](https://stacks.math.columbia.edu/tag/0F09) (for sheaves [Stacks, Tag 0EYU](https://stacks.math.columbia.edu/tag/0EYU)) says that
pullback along a smooth map commutes with direct image along a qcqs
morphism when the coefficients are torsion of order invertible on the
base. If $g$ is proper, the two direct images on the generic fibres
agree because direct image is compatible with composition, and
$\bar i^*$ commutes with the proper direct image by proper base change.
If $g$ is smooth, we apply smooth base change to $R\bar j_*$, which is
direct image along a qcqs morphism, and restrict to the special fibre.
This is allowed because the coefficients are annihilated by a power of $\ell$, which is
invertible on $S$. The same base change maps appear in
SGA7II, Exposé XIII, (2.1.7.1)–(2.1.7.3).

We also use two calculations for a finite $A$-module $M$. The first is
$R\Psi_S(M_{\eta})=M$. To see this, note that the integral closure
$\bar S$ of $S$ in the separable closure is strictly henselian, so the
stalk of $R\bar j_*M$ at its closed point is
$R\Gamma(\bar\eta,M)=M$. The second says that $H^r(\mathbf A^1_k,M)=0$ for
$r>0$ and $H^0(\mathbf A^1_k,M)=M$. This is the usual
calculation for the affine line with coefficients prime to the
characteristic, and to prove it we apply [Stacks, Tag 03RR](https://stacks.math.columbia.edu/tag/03RR) to the
compactification $\mathbf A^1\subset\mathbf P^1$, which has genus zero
and one point at infinity.  Over the algebraically closed field $k$, the
cyclic constant coefficients are isomorphic to the corresponding roots
of unity, and every finite $M$ is a finite direct sum of these.
By truncation the two calculations extend to a bounded complex
$M^\bullet$ of finite $A$-modules, viewed as a constant complex:

$$
R\Psi_S(M^\bullet_\eta)\simeq M^\bullet,
 \qquad R\Gamma(\mathbf A^1_k,M^\bullet_{\mathbf A^1_k})\simeq M^\bullet.
$$
