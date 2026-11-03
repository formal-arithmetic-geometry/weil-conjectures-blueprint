+++
id = "prose-E-01"
kind = "hidden"
title = "Specialization and contracting correspondences"
order = 1611
+++
The trace formula needs the local term at an isolated fixed point to be
the trace on the stalk. This is not a formal fact. A local term is
computed from $\cHom(c_2^*K,c_1^!K)$ near the fixed point, and the stalk
does not determine this complex (Remark [remark-locality-warning]).
Section [chap-The-trace-formula] proves the equality by a computation
for Frobenius on a smooth curve
(Proposition [proposition-frobenius-local-term-curve]) and reduces
everything else to that case. In particular, its trace formula
(Theorem [theorem-grothendieck-lefschetz-trace-formula]) does not
depend on this appendix.

The computation leaves open why Frobenius behaves so well. Topology
suggests that the reason is contraction. If a map $\varphi$ of a manifold
contracts a neighbourhood of a fixed point $y$ into itself, then the local
index at $y$ is $1$. With coefficients in a sheaf, the local index is the
trace of $\varphi$ on the stalk at $y$. Frobenius contracts in the
strongest possible sense, because its differential is zero. In this
appendix we make this explanation into a theorem, in any dimension and
for a whole class of correspondences at once.

In algebraic geometry we measure contraction by powers of ideals. Let
$c=(c_1,c_2):C\to X\times X$ be a correspondence, $Z\subset X$ a closed
subscheme with ideal $I$, and put $I_i=c_i^{-1}(I)\mathcal O_C$. We say,
as in [varshavsky05], that $c$ contracts towards $Z$ if
$I_2\subset I_1$ and $I_2^n\subset I_1^{n+1}$ for some $n\geq1$.
Frobenius is the model case. Take $c=(\mathrm{id},\Phi_X^m)$ and $Z$ a
point $y\in X_0(\mathbf F_{q^m})$, and choose coordinates $x_i$ of an
affine neighbourhood of $y$ defined over $\mathbf F_q$. Then $y$ has
coordinates $a_i\in\mathbf F_{q^m}$, and
$(\Phi_X^m)^*(x_i-a_i)=x_i^{q^m}-a_i=(x_i-a_i)^{q^m}$. Hence
$I_2\subset I_1^{q^m}$, and $n=1$ works.

The main theorem,
Theorem [theorem-contracting-correspondences-local-terms], says that
near a component of its fixed locus that meets $Z$, the trace class of a
contracting correspondence can be computed on $Z$ alone, from the
correspondence restricted to $Z$. For $Z$ a point,
Corollary [corollary-contracting-local-terms-point] says that the local
term at an isolated fixed point is the trace on the stalk, even when $X$
is singular. The theorem and its proof are due to
Varshavsky [varshavsky05]. They generalize Fujiwara's theorem, conjectured by Deligne, that
the local terms of a correspondence composed with a sufficiently high
power of Frobenius are the naive ones.

The proof makes the contraction literal by deforming $X$ to the normal
cone of $Z$. Over the trait $\operatorname{Spec}k[t]_{(t)}$, the
deformation to the normal cone $\mathcal D_ZX$ has generic fibre $X$ and
special fibre the normal cone $N_ZX$. On the special fibre, the
contraction hypothesis says that the second leg maps everything into the
zero section (Lemma [lemma-normal-cones-contracting-ideals]). There
the part of $K$ away from $Z$ contributes nothing. What remains is the
specialization of $K$ restricted to the zero section, and by Verdier's
theorem (Theorem [theorem-verdier-s-theorem-specialization-zero])
this is $K|_Z$.

It remains to transport the answer back to $X$. We identify the trace
class on the special fibre with the specialization of the trace class of
$c$ (Proposition [proposition-specialization-trace-class]). The
specialization map is an isomorphism, because the fixed locus does not
move in the family up to nilpotents
(Lemma [lemma-fixed-point-scheme-deformation]). Before any of this,
we must be able to specialize a trace class at all. A trace class is
built from $K\boxtimes\mathbb DK$, so we need nearby cycles to commute
with external products and with Verdier duality.
Propositions [proposition-external-kunneth-formula-nearby-cycles]
and [proposition-nearby-cycles-commute-verdier-duality] prove both,
by a dimension argument of Illusie [illusie94].

We use the six operations and the notation for correspondences and
trace classes of Section [chap-The-Lefschetz-Verdier-formula], and classical
results on nearby cycles over a trait, which we recall where they are
first needed. Throughout this appendix, $k$ is algebraically closed,
$\ell$ is invertible in $k$, and $A$ is a finite commutative ring
annihilated by a power of $\ell$. The only exception is the base of
nearby cycles in
Sections [sec-Kunneth-formula-for-nearby-cycles]–[sec-Specialization-of-the-trace-class], which
may be any excellent strictly henselian trait, with residue field only
separably closed. Statements about constructible
complexes on $k$-schemes are made on the pro-étale site. We construct
nearby cycles on the classical étale site and transport them by the
comparison for constructible complexes
(Theorem [theorem-comparison-constructible-sheaves] and
Corollary [corollary-finite-tor-amplitude-under-comparison]).
