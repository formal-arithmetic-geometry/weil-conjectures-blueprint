+++
id = "prose-13-01"
kind = "hidden"
title = "Trace formula: statement, strategy and Frobenius"
order = 3750
+++
Let $X_0$ be a separated scheme of finite type over $\mathbf F_q$,
let $X=X_0\times_{\mathbf F_q}\overline{\mathbf F}_q$, and let
$\ell$ be a prime with $\ell\nmid q$. Weil's axiom (b) asks that
$\ell$-adic cohomology count rational points: for every $m\geq1$,

$$
\#X_0(\mathbf F_{q^m})
 =\sum_i(-1)^i\operatorname{Tr}\bigl(\operatorname{Frob}_{X,\Lambda_X}^m
   \mid H_c^i(X_{\mathrm{pro\acute et}},\Lambda_X)\bigr),
 \qquad\Lambda\in\{\Ql,E,\overline{\mathbf Q}_\ell\},
$$

where $\operatorname{Frob}_{X,\Lambda_X}$ is the geometric Frobenius
operator of the constant Weil complex (Section “Frobenius and Weil complexes”). From this
formula we deduce
rationality of the zeta function, and together with duality its
functional equation
(Corollaries [sk-cor-tf-point-counting] and [sk-cor-tf-functional-equation]).
For the weights we need more. The proof of purity fibres $X_0$ in
curves, so the coefficients on the base are direct images, which are
not constant. Moreover, Rankin's argument (Section “Purity of real sheaves on curves”)
and the Fourier transform (Section “The Fourier transform on the affine line”) apply the
trace formula to tensor powers of lisse sheaves and to Fourier
transforms. We therefore prove it for every Weil complex $K\in\Dctf(X,\Lambda)$, where
$\Lambda\in\{A,\Zl,\mathcal O_E,\Ql,E,\overline{\mathbf Q}_\ell\}$ and $A$ is a finite
commutative $\ell$-primary ring: for every $m\geq1$, in $\Lambda$,

$$
\operatorname{tr}_\Lambda\bigl(\operatorname{Frob}_{X,K}^m\mid
   R\Gamma_c(X_{\mathrm{pro\acute et}},K)\bigr)
 =\sum_{y\in X_0(\mathbf F_{q^m})}
   \operatorname{tr}_\Lambda\bigl(\operatorname{Frob}_{y,m}\mid
   K_{\bar y}\bigr).
$$

Here $\operatorname{tr}_\Lambda$ is the trace of an endomorphism of a
perfect $\Lambda$-complex (Definition [sk-d-trace]).
The geometric point $\bar y:s\to X$ associated with $y$ is
fixed by the $m$-th power of Frobenius, and
$\operatorname{Frob}_{y,m}$ is the endomorphism of the stalk
$K_{\bar y}$ induced by the $m$-th iterate of the Weil structure.
This is Theorem [sk-thm-tf-uniform-formula], and for $K=\Lambda_X$ it is
the point count above. Over a field, the left-hand side is the
alternating sum of the traces on the groups $H^i_c$.

Following (SGA5, III), we deduce the formula from the
Lefschetz–Verdier formula. A cohomological correspondence $u$ on
$(X,K)$ has a trace class supported on its fixed locus. For a
correspondence with proper source on a proper scheme $X$, the trace
of the induced endomorphism of $R\Gamma(X,K)$ is the integral of
that class, which is a sum of local terms at the fixed points. To
apply this to Frobenius, we must solve two problems.
First, the right-hand side of the trace formula is a sum of traces on stalks of $K$,
whereas a local term is computed from the sheaf
$\cHom_A(c_2^*K,c_1^!K)$ near the fixed point, and the stalk of this
sheaf at the fixed point is not determined by the stalk of $K$ there
(Remark [sk-rem-tf-locality-warning]). Second, $X$ is in general not
proper. After extension by zero to a compactification, the boundary
fixed points have zero stalk, and one has to show that their local terms
vanish. Both problems are solved by a single local statement about the graph
of Frobenius: on a smooth curve, the local term at a rational point is
the trace on the stalk, and in particular it vanishes when the stalk
is zero.

Granting the local statement on curves, we prove the formula for finite
coefficients by fibring $X$ in curves. Both sides are additive along
stratifications and compatible with direct image with compact support,
so an induction on affine coordinates reduces the formula to
$\mathbf A^1$, where the curve statement applies on $\mathbf P^1$,
as in (SGA5, XV, §3) and (TFBP). Both sides are
also compatible with reduction modulo powers of $\pi_E$, with
inverting $\ell$ and with finite extensions of $E$, and this gives
the formula for integral and rational coefficients. In the theory of
weights it is used in the form of an Euler product for the
$L$-function, which we derive at the end of this section. A second
computation of the local terms, for contracting correspondences, is
given in Appendix “Specialization and contracting correspondences”.

The conventions of Section “Frobenius, trace classes and the Lefschetz–Verdier formula” remain in force.

Two Frobenius maps act on $X=X_0\times_{k_0}k$: the $k$-linear scheme
Frobenius $\Phi_X$ and the semilinear geometric Frobenius $\operatorname{Fr}_X$
that defines Weil structures. We prove the trace formula for $\Phi_X$, whose graph is a
correspondence over $k$, and Lemma [sk-lem-tf-frobenius-convention]
translates it to $\operatorname{Fr}_X$.

Since a finitely generated algebra over a perfect
field is finite over its subring of $q$-th powers, $\Phi_X$ and all
its iterates are finite. Hence the second leg $\Phi_X^m$ of the graph $c_m$
below is proper, and the operator $T_{c_m}$ on cohomology with compact
support is defined even when $X$ is not proper.
