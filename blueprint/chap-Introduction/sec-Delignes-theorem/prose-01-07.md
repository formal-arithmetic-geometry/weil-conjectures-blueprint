+++
id = "prose-01-07"
kind = "hidden"
title = "Deligne's theorem"
order = 15
+++
Part III proves purity. Fix an embedding
$\iota:\overline{\mathbf Q}_\ell\to\mathbf C$, and write $q_x$ for the number of elements of the
residue field of a closed point $x$ of $X_0$. A Weil sheaf with coefficients
in $\overline{\mathbf Q}_\ell$ is *pure of weight $w$* if every eigenvalue $\alpha$ of
Frobenius on every stalk satisfies $|\iota(\alpha)|=q_x^{w/2}$, and *mixed*
if it has a finite filtration whose quotients are pure. A complex has
*weights at most $w$* if each cohomology sheaf $\mathcal H^i$ is mixed with
weights at most $w+i$ (Definition [definition-weights]). The shift by $i$ is chosen so that both the constant sheaf, pure of weight
$0$, and its cohomology complex $R\Gamma(X,\overline{\mathbf Q}_\ell)$, whose $H^i$ should have
weight $i$, have weights at most $0$.

*Deligne's theorem* (Theorem [theorem-weights-rf-shriek]) says that
if $K$ has weights at most $w$, so does $Rf_!K$. It gives only an upper
bound. For the constant sheaf on a smooth proper $X_0$, duality supplies
the lower one. With $f$ the map to a point, the theorem says that the eigenvalues
on $H^i$ satisfy $|\iota(\alpha)|\le q^{i/2}$. Since Poincaré duality pairs
$\alpha$ on $H^i$ with $q^d/\alpha$ on $H^{2d-i}$, the same bound in degree
$2d-i$ gives $|\iota(\alpha)|\ge q^{i/2}$. The two bounds together are purity.
Theorem [theorem-weil-conjectures-smooth-proper-schemes] deduces the
Weil conjectures from it.

The theorem is stated for all sheaves, not only the constant one, because
the proof is an induction on dimension. Away from a closed subset, a variety
is fibred in curves over a variety of smaller dimension. The direct
image of the constant sheaf along such a fibration is no
longer constant, so the induction needs the theorem for all sheaves. The main case is that of curves, and Laumon's
proof [laumon87] of it has two ideas.

The first is a positivity argument, due to Rankin in the theory of
modular forms. Let $\mathcal G$ be a *lisse* sheaf on an affine curve
$U_0$, that is, a locally constant one. Such a sheaf is the same as a
representation of the fundamental group, and its *monodromy* is the
image of that representation. Call $\mathcal G$ *real* if the
characteristic polynomials of Frobenius on its stalks have real
coefficients (Definition [definition-real-sheaves]). Its $L$-function is
the product, over closed points $x$, of the *Euler factors*
$\det(1-\operatorname{Frob}_x T^{\deg x}\mid\mathcal G_{\bar x})^{-1}$. On an
affine curve $H^0_c=0$ and $H^i_c=0$ for $i>2$. So the trace formula shows
that the $L$-function equals $\det(1-TF\mid H^1_c)/\det(1-TF\mid H^2_c)$. Two
facts make this useful.

- Consider an even tensor power $\mathcal G^{\otimes 2m}$. The logarithm of
  an Euler factor has coefficients
  $\operatorname{Tr}(\operatorname{Frob}_x^n\mid\mathcal G_{\bar x})^{2m}/n$, and
  these are nonnegative because the traces are real. Each Euler factor
  therefore has nonnegative coefficients bounded by those of the whole
  product. In particular it converges wherever the product does
  (Lemma [lemma-positivity-convergence]).
- The product has poles only where $\det(1-TF\mid H^2_c)$ vanishes, and
  $H^2_c$ is easy to compute. It is the largest quotient of a stalk on which
  the monodromy acts trivially, twisted by $(-1)$.

The second fact bounds the eigenvalues on $H^2_c$ of $\mathcal G^{\otimes2m}$,
and the first turns this into a bound at every point
(Proposition [proposition-bound-largest-determinant-weight]). Let
$\beta$ be the largest *determinant weight* of the irreducible
constituents of $\mathcal G$. The determinant weight of a constituent of
rank $r$ is the weight of its determinant divided by $r$
(Definition [definition-determinant-weight]). By the second fact, the
eigenvalues on $H^2_c$ of $\mathcal G^{\otimes2m}$ have absolute value at most
$q^{m\beta+1}$, where the $+1$ comes from the twist $(-1)$. So the product
converges for $|T|<q^{-m\beta-1}$. By the first fact, the Euler factor at
$x$ converges there too. This factor has a pole where
$T^{\deg x}=\alpha^{-2m}$, for each eigenvalue $\alpha$ of
$\operatorname{Frob}_x$ on $\mathcal G_{\bar x}$. We conclude that
$|\iota(\alpha)|^{2m}\le q_x^{m\beta+1}$ for every $m$. Taking $2m$-th roots and
letting $m\to\infty$ gives $|\iota(\alpha)|^2\le q_x^\beta$.

This argument needs the determinants to have weights, that is, lisse
sheaves of rank one to be pure. A rank-one sheaf is a character of the
fundamental group. It is pure as soon as its restriction to the geometric
fundamental group has finite image, and we show that this image is finite.
If it were not, the logarithm of a power of the character would give a
nonzero class in $H^1$ of the curve fixed by Frobenius. This class cannot
come from the removed points, since Frobenius acts on those classes by
powers of $q$. So it comes from the compactification, and it gives a
nonzero vector in the Tate module of its Jacobian fixed by Frobenius. Such a
vector is a compatible system of rational $\ell$-power torsion points of
unbounded order. That is impossible, because the Jacobian has only finitely
many rational points (Section [sec-Sheaves-of-rank-one]). With more work one shows that each
irreducible constituent of a real sheaf is pure
(Theorem [theorem-purity-real-sheaves-curves]).

This bounds eigenvalues at the points of a curve, but we must bound
eigenvalues on its cohomology. The second idea, the Fourier transform,
turns one into the other. Its model is the discrete Fourier transform
$\hat t(y)=\sum_{x\in\mathbf F_q}t(x)\psi(xy)$ of a function $t$ on
$\mathbf F_q$, where $\psi$ is a nontrivial additive character. Two
properties matter. The value $\hat t(0)$ is the sum of all values of $t$, so
a sum over the line becomes a single value. And Plancherel's formula
$\sum_y|\hat t(y)|^2=q\sum_x|t(x)|^2$ holds.

Let $\chi$ be a
nontrivial multiplicative character, extended by $\chi(0)=0$, and let
$g=\sum_x\chi(x)\psi(x)$ be its Gauss sum. Substituting $x\mapsto x/y$ shows
that $\hat\chi(y)=\overline\chi(y)g$ for $y\neq0$. So the transform has the
same absolute value $|g|$ at all $q-1$ nonzero points, and $\hat\chi(0)=0$.
Plancherel now reads $(q-1)|g|^2=q(q-1)$, and we find $|g|=\sqrt q$. In other
words, a function of absolute value $1$ is carried to one of absolute value
$\sqrt q$, that is, weight $0$ to weight $1$.

Grothendieck's dictionary turns this transform into an operation on sheaves
on the affine line. Read the formula for $\hat t$ from the inside out: pull
$t$ back to the plane along $p_1(x,y)=x$, multiply by the function
$\psi(xy)$, and sum over the fibres of $p_2(x,y)=y$. Each step is a line of
the table in Section [sec-The-function-sheaf-dictionary]. So if $\mathcal K_\psi$ is a
sheaf on the plane with trace function $\psi(xy)$ and we put

$$
\operatorname{FT}_\psi K=Rp_{2!}(p_1^*K\otimes\mathcal K_\psi)[1],
$$

then for $y\in\mathbf F_q$ the table gives

$$
t_{\operatorname{FT}_\psi K}(y)
=-\,t_{Rp_{2!}(p_1^*K\otimes\mathcal K_\psi)}(y)
=-\sum_{x\in\mathbf F_q}t_{p_1^*K}(x,y)\,t_{\mathcal K_\psi}(x,y)
=-\sum_{x\in\mathbf F_q}t_K(x)\,\psi(xy)
=-\,\hat t_K(y).
$$

The sign comes from the shift $[1]$, which changes the sign of every trace.

Let $M$ be an irreducible lisse sheaf, pure of weight $w$, on a
dense open $j:U_0\to\mathbf A^1$, and let $j_*M$ be its direct image to
$\mathbf A^1$. Its compactly supported cohomology lives in degrees $1$ and
$2$. As above, $H^2_c$ is easy, and the group we must bound is
$H^1_c(\mathbf A^1,j_*M)$. Just as $\hat t(0)$ is the sum of $t$, the stalk
at $0$ of the Fourier transform of $j_*M$ is the compactly supported
cohomology of $j_*M$.

The sheaves $\mathcal L_{\psi(ax)}$ with trace function $x\mapsto\psi(ax)$
are exceptions, as the characters $\psi(ax)$ are for the discrete
transform: their transform is concentrated at one point. Suppose that no
constituent of $M$ over $\overline{\mathbf F}_q$ is of this form. Then the
transform is again of the form $j'_*M'$ for a lisse sheaf $M'$ on a dense
open of the dual line
(Proposition [proposition-fourier-transform-middle-extension]). The hypothesis excludes in particular constant constituents (the case $a=0$), so the monodromy
of $M$ has no coinvariants and $H^2_c(\mathbf A^1,j_*M)=0$. The stalk of
$j'_*M'$ at $0$ is therefore exactly $H^1_c(\mathbf A^1,j_*M)$.

To show that $M'$ is pure we use the first idea. Twist $M$ to weight $0$
and add its dual, whose eigenvalues are the complex conjugates. The result
is a real sheaf, and its transform maps onto a twist of $M'$
(Proposition [proposition-purity-lisse-part-fourier-transform]). The
weight of $M'$ is then found from the sheaf version of Plancherel's
formula, which compares the sums of $|t_M(x)|^2$ and $|t_{M'}(y)|^2$ over
$\mathbf F_{q^m}$ as $m$ grows. It is $w+1$
(Theorem [theorem-weight-fourier-transform]). By
Proposition [proposition-weights-j-boundary-points], the stalk of $j'_*M'$
at $0$ has weights at most $w+1$, and this is the bound we want.

Every curve, after removing finitely many points, maps to the affine line by
a finite map. Pushing forward along this map reduces the general curve to
the line (Theorem [theorem-weight-bound-curve]). The fibration argument
above then reduces the general case to curves, provided the direct images
that occur along the way are mixed. This is proved separately in
Theorem [theorem-real-constructible-sheaves-are-mixed]. For genus-one
curves over $\mathbf F_3$, purity gives $1\le N_1\le7$
(Example [example-running-example-purity]).
