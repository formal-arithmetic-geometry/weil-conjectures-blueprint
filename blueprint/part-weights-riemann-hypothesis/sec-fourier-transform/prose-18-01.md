+++
id = "prose-18-01"
kind = "hidden"
title = "The Fourier transform on the affine line"
order = 712
+++
Rankin's argument bounds the eigenvalues of a real sheaf at the points
of a curve, but the group we must bound is a cohomology group,
$H^1_c(\mathbf A^1,j_*M)$ for an irreducible lisse sheaf $M$, pure of
weight $w$, on a dense open $j:U_0\hookrightarrow\mathbf A^1$. To bring the pointwise
theorem to bear we want a sheaf on another curve whose stalk at one
point is this group, and whose weight we can compute from that of $M$.
The Fourier transform provides both.

The classical model is the discrete Fourier transform on $\mathbf F_q$.
Fix a nontrivial additive character $\psi$ and put
$\hat t(y)=\sum_xt(x)\psi(xy)$. Its value at $y=0$ is the sum of $t$,
and Plancherel's formula
$\sum_y|\hat t(y)|^2=q\sum_x|t(x)|^2$ holds by orthogonality of
characters. Gauss sums show how these two facts together give an
absolute value. Let $\chi$ be a nontrivial character of
$\mathbf F_q^\times$, extended by $\chi(0)=0$. Substituting $x\mapsto x/y$ gives $\hat\chi(y)=\overline\chi(y)g$ for $y\ne0$, where
$g=\sum_x\chi(x)\psi(x)$, and $\hat\chi(0)=\sum_x\chi(x)=0$. Plancherel
then reads $(q-1)|g|^2=q(q-1)$, and so $|g|=\sqrt q$. Thus the transform
of a nontrivial multiplicative character is again of constant absolute
value on $\mathbf F_q^\times$, and the Plancherel formula forces that
value to be $\sqrt q$. In terms of weights, a sheaf of weight $0$ such as
a Kummer sheaf is carried to a sheaf of weight $1$, and
its sum over the line, the value at $0$, is controlled by the transform.

Grothendieck's dictionary (Section [sec-n-dictionary]) turns this into a
functor. With $\mathcal K_\psi$ the Artin–Schreier sheaf on
$\mathbf A^1\times\mathbf A^1$ with trace function $\psi(xy)$
(Lemma [sk-lem-as-properties]), the Fourier transform is

$$
\operatorname{FT}_\psi K=Rp_{2!}(p_1^*K\otimes\mathcal K_\psi)[1].
$$

By the trace formula it transforms trace functions as above, up to the
sign $-1$ coming from the shift (18.3), and its stalk at the
origin of the dual line is $R\Gamma_c(\mathbf A^1,K)[1]$
(Proposition [sk-thm-inversion]). Both classical facts survive:
Fourier inversion, $\operatorname{FT}_{\psi^{-1}}\operatorname{FT}_\psi K\simeq K(-1)$, comes from the vanishing of
$R\Gamma_c(\mathbf A^1,\mathcal L_\psi)$, the sheaf version of
$\sum_x\psi(x)=0$, and Plancherel (Corollary [sk-cor-plancherel]) is an
identity of trace functions which raises by one the growth rate of
the sums of squared traces; for a pure sheaf this growth rate is the
weight (Theorem [sk-thm-wrp-l2-dictionary]). The $\ell$-adic transform is due to Deligne, and Laumon's proof of
Deligne's theorem (Lau) is built on it. Example [sk-ex-ex-gauss-sum]
works out the Gauss sum over $\mathbf F_3$ in this language.

Beware that the transform of a sheaf need not be a sheaf. The transform
of the constant sheaf is a skyscraper at the origin in degree one,
$\operatorname{FT}_\psi(E)=\delta_0(-1)[-1]$, the sheaf version of
$\hat1=q\,\delta_0$ up to the sign coming from the shift. What the transform does preserve is the category of
perverse sheaves on the line. On a curve these have an elementary
description (Lemma [sk-lem-wft-curve-heart]): complexes in degrees $-1$
and $0$ with $\mathcal H^0$ punctual and $\mathcal H^{-1}$ without
punctual subsheaves, such as $(j_*M)[1]$ and skyscrapers. The
transform is an exact equivalence of this abelian category
(Proposition [sk-p-dl-a1-perverse]). The proof only needs the stalk
formula and the fact that on an affine curve $H^2_c$ is the
coinvariants of geometric monodromy, so that the degree-zero part of the
transform is supported at the finitely many $y$ for which
$\mathcal L_{\psi(-yx)}$ is a quotient of $M$. An exact equivalence
carries simple objects to simple objects, and the simple perverse
sheaves are the irreducible punctual sheaves and the middle extensions
$(j_*M)[1]$ of irreducible lisse sheaves
(Lemma [sk-lem-wft-curve-simples]). If no geometric constituent of $M$ is
a character $\mathcal L_{\psi(ax)}$, whose transform is a skyscraper,
it follows that

$$
\operatorname{FT}_\psi((j_*M)[1])\simeq(j'_*M')[1]
$$

for an irreducible lisse $M'$ on a dense open $j'$ of the dual line
(Proposition [sk-p-dl-a1-middle]). Comparing stalks at the origin
identifies $H^1_c(\mathbf A^1,j_*M)$ with a stalk of $j'_*M'$, which
is how Section [sec-deligne-laumon-a1] bounds it.

We use the six operations on the pro-étale site, first with
coefficients in a finite extension $E/\mathbf Q_\ell$ that contains
the $p$th roots of unity, $p$ being the characteristic of $k_0$, so
that it contains the values of the additive characters of $k_0$, and
then with coefficients in $\overline{\mathbf Q}_\ell$.
