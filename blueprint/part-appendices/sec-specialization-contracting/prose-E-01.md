+++
id = "prose-E-01"
kind = "hidden"
title = "Specialization and contracting correspondences"
order = 939
+++
The trace formula needs the local term at an isolated fixed point to be
the trace on the stalk. Section [sec-trace-formula] proves this
directly for Frobenius on a smooth curve
(Proposition [sk-p-frob]) and reduces the general case
to it by an induction on affine coordinates; its trace formula
(Theorem [sk-thm-tf-uniform-formula]) does not depend on this appendix. Here
we give a second computation, which works in any dimension and for a
whole class of correspondences at once. The model is the topological
Lefschetz formula: if a map $\varphi$ of a manifold contracts a
neighbourhood of a fixed point $y$ into itself, then the local index at
$y$ is $1$, and, with coefficients in a sheaf, it is the trace of
$\varphi$ on the stalk at $y$. Frobenius contracts in the strongest
possible sense, because its differential is zero.

The algebraic notion of contraction is measured by powers of ideals. Let
$c=(c_1,c_2):C\to X\times X$ be a correspondence, $Z\subset X$ a closed
subscheme with ideal $I$, and put $I_i=c_i^{-1}(I)\mathcal O_C$. We say,
as in (Var), that $c$ contracts towards $Z$ if
$I_2\subset I_1$ and $I_2^n\subset I_1^{n+1}$ for some $n\geq1$. For the
Frobenius correspondence $c=(\mathrm{id},\Phi_X^m)$ and $Z$ a point
$y\in X_0(\mathbf F_{q^m})$, choose coordinates $x_i$ of an affine
neighbourhood of $y$ defined over $\mathbf F_q$; then $y$ has coordinates
$a_i\in\mathbf F_{q^m}$, and we have $(\Phi_X^m)^*(x_i-a_i)=x_i^{q^m}-a_i=(x_i-a_i)^{q^m}$, so
$I_2\subset I_1^{q^m}$, and $n=1$ works. The
main theorem (Theorem [sk-thm-tf-contracting-local-term]) says that the
trace class of a contracting correspondence near a component of its
fixed locus that meets $Z$ can be computed on $Z$ alone, from the
correspondence restricted to $Z$. For $Z$ a point, the local term at an
isolated fixed point is the trace on the stalk
(Corollary [sk-cor-tf-contracting-input]); here $X$ may be singular. The theorem
and its proof are due to Varshavsky (Var). They generalize
the theorem, conjectured by Deligne, that the local terms of a
correspondence composed with a sufficiently high power of Frobenius are
the naive ones; Pink proved it in 1992 assuming resolution of
singularities, and Fujiwara proved it in general.

The proof deforms the correspondence to the normal cone of $Z$. Over the
trait $\operatorname{Spec}k[t]_{(t)}$, the deformation to the normal cone
$\mathcal D_ZX$ has generic fibre $X$ and special fibre the normal cone
$N_ZX$, and the contraction hypothesis says that on the special fibre the
second leg maps everything into the zero section
(Lemma [sk-lem-tf-contracting-cone-geometry]). Up to nilpotents the fixed
locus does not move in the family
(Lemma [sk-lem-tf-contracting-fixed-geometry]). Hence the trace class on the
special fibre is the specialization of the trace class of $c$
(Proposition [sk-prop-tf-trace-specialization]), and the specialization map
is an isomorphism. On the special fibre the contribution of the part of $K$
away from $Z$ vanishes, because the second leg lands in the zero section. That the
specialization of $K$ restricted to the zero section is $K|_Z$ is
Verdier's theorem (Theorem [sk-thm-tf-sp-zero-section]). To specialize a
trace class at all, we need nearby cycles to commute with external
products and with Verdier duality, since a trace class is built from
$K\boxtimes\mathbb DK$; we prove both by a dimension argument of
Illusie (Ill) (Propositions [sk-prop-tf-nearby-external-kunneth]
and [sk-prop-tf-nearby-duality-foundation]). This machinery, which the main
text never needs, is why the result is an appendix.

We use the six operations and the notation for correspondences and
trace classes of Section [sec-lefschetz-verdier], and classical
results on nearby cycles over a trait, which we recall where they are
first needed. Throughout this appendix, $k$ is algebraically closed,
$\ell$ is invertible in $k$, and $A$ is a finite commutative ring
annihilated by a power of $\ell$. Statements about constructible
complexes on $k$-schemes are made on the pro-étale site. We construct
nearby cycles on the classical étale site and transport them by the
comparison for constructible complexes
(Theorem [sk-thm-pe-constructible-comparison] and
Corollary [sk-cor-pe-finite-tor-comparison]).
