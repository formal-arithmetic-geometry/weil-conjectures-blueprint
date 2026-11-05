+++
id = "prose-16-01"
kind = "hidden"
title = "The Fourier transform"
order = 1217
+++
Theorem [theorem-purity-real-sheaves-curves] controls the Frobenius
eigenvalues of a real sheaf at the points of a curve. The bound we need
next, however, is of a different kind. Let $M$ be an irreducible lisse sheaf, pure
of weight $w$, on a dense open $j:U_0\hookrightarrow\mathbf A^1$. The
curve case of the Deligne–Laumon theorem comes down to showing that
$H^1_c(\mathbf A^1,j_*M)$ has weights at most $w+1$. This is a
cohomology group, not the stalk of a sheaf at a point, and Rankin's
argument does not reach it. Is there a sheaf on another curve whose stalk
at one point is this group, and whose weight we can compute from that of
$M$? Up to a shift, the Fourier transform of $(j_*M)[1]$ is such a sheaf.

For functions on $\mathbf F_q$ the discrete Fourier transform already
does what we want. Fix a nontrivial additive character $\psi$ and put
$\hat t(y)=\sum_xt(x)\psi(xy)$. Two properties matter. First, the value
$\hat t(0)$ is the sum of all values of $t$, so a sum over the line
becomes a single value. Second, Plancherel's formula
$\sum_y|\hat t(y)|^2=q\sum_x|t(x)|^2$ holds, by orthogonality of
characters.

To see Plancherel compute an absolute value, let $\chi$ be a
nontrivial character of $\mathbf F_q^\times$, extended by $\chi(0)=0$,
and let $g=\sum_x\chi(x)\psi(x)$ be its Gauss sum. Substituting
$x\mapsto x/y$ shows that $\hat\chi(y)=\overline\chi(y)g$ for $y\ne0$, so
the transform has the same absolute value $|g|$ at all $q-1$ nonzero points,
while $\hat\chi(0)=0$. Plancherel therefore reads $(q-1)|g|^2=q(q-1)$, and we
find $|g|=\sqrt q$. In the language of weights, this means that the transform
carries a function of weight $0$ to one of weight $1$. For the quadratic character of
$\mathbf F_3$, moreover, Example [example-gauss-sum-over-f-3] finds this Gauss
sum, up to sign, as a Frobenius eigenvalue on a cohomology group.

The proof in Section [chap-The-Deligne-Laumon-theorem-for-curves] follows the same two
steps for $M$: first we show that the transform is pure, and then
Plancherel finds its weight.

Grothendieck's function–sheaf dictionary
(Proposition [proposition-function-sheaf-dictionary]) turns the
transform into a functor. Let $\mathcal K_\psi=\mu^*\mathcal L_\psi$ be the pullback of the
Artin–Schreier sheaf (Lemma [lemma-artin-schreier-character-sheaf]) along the
multiplication $\mu(x,y)=xy$. Its trace function on $\mathbf F_q$-points is
$\psi(xy)$, and we put

$$
\operatorname{FT}_\psi K=Rp_{2!}(p_1^*K\otimes\mathcal K_\psi)[1].
$$

On trace functions it is the discrete transform up to sign: for
$y\in\mathbf F_q$,

$$
t_{\operatorname{FT}_\psi K}(y)=-\sum_{x\in\mathbf F_q}t_K(x)\,\psi(xy),
$$

because under the dictionary (Section [sec-The-function-sheaf-dictionary-2])
pullback, tensor product and $Rp_{2!}$ become composition, multiplication
and summation over the fibres, the three operations from which $\hat t$
is built, while the shift $[1]$ contributes the sign. Both properties of the
discrete transform carry over. The first becomes the statement that the
stalk at the origin of the dual line is $R\Gamma_c(\mathbf A^1,K)[1]$
(Proposition [proposition-base-change-fourier-inversion]), so for
$K=j_*M$ this complex contains the group we want. Plancherel becomes an
identity of trace functions (Corollary [corollary-plancherel]), and
it is what will compute the weight of the transform. In addition,
Fourier inversion,
$\operatorname{FT}_{\psi^{-1}}\operatorname{FT}_\psi K\simeq K(-1)$,
holds because $R\Gamma_c(\mathbf A^1,\mathcal L_\psi)=0$, the sheaf
version of $\sum_x\psi(x)=0$. The $\ell$-adic transform is due to Deligne, and
Laumon's proof [laumon87] of the Deligne–Laumon theorem is built on it.

To speak of the weight of the transform we need it to be a lisse sheaf on
a dense open. But the transform of a sheaf need not be a sheaf. For
example, the transform of the constant sheaf is a skyscraper at the
origin in degree one, $\operatorname{FT}_\psi(E)=\delta_0(-1)[-1]$. This
is the sheaf version of $\hat1=q\,\delta_0$, up to the sign coming from
the shift. What the transform does preserve, however, is the category of perverse
sheaves on the line (Proposition [proposition-fourier-transform-perverse-heart],
proved in Section [sec-Perverse-t-exactness] below). Since the transform is an exact equivalence of
perverse sheaves, it sends the simple object $(j_*M)[1]$ to a simple object,
which is either punctual or a middle extension. Moreover, only character sheaves
$\mathcal L_{\psi(ax)}$ are sent to skyscrapers. Hence, if no geometric constituent
of the irreducible sheaf $M$ is such a character, we have

$$
\operatorname{FT}_\psi((j_*M)[1])\simeq(j'_*M')[1]
$$

for an irreducible lisse $M'$ on a dense open $j'$ of the dual line
(Proposition [proposition-fourier-transform-middle-extension] below).
Comparing stalks at the origin then identifies $H^1_c(\mathbf A^1,j_*M)$ with
a stalk of $j'_*M'$, and this is the sheaf we asked for.

We use the six operations on the pro-étale site. At first the
coefficients are a finite extension $E/\mathbf Q_\ell$ that contains the
$p$th roots of unity, where $p$ is the characteristic of $k_0$, so that $E$ contains the values of the additive characters of $k_0$. Later the
coefficients are $\overline{\mathbf Q}_\ell$.
