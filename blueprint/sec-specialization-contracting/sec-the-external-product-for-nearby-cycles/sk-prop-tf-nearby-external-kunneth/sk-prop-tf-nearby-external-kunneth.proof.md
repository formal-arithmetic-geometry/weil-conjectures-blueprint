+++
kind = "proof"
of = "sk-prop-tf-nearby-external-kunneth"
uses = ["sk-lem-sf-kunneth-star"]
+++
When $X$ and $Y$ are projective, $\Cone(\Pi_{L,M})$ has zero
global sections by the ordinary Künneth formula on the geometric generic fibres,
together with the compatibility of $\Pi$ with proper direct images in
the two factors. Using (E.2) and induction on dimension, we
then show that it has finite support, and a complex with finite support
and zero global sections vanishes.

*Proper direct images.* Let $f:X\to X_1$ and $g:Y\to Y_1$ be
proper. If we identify direct images of products by the ordinary
Künneth formula, and direct images of nearby cycles by the
base change isomorphism for proper maps, then $R(f_s\times g_s)_*\Pi_{L,M}$ becomes

$$
\Pi_{Rf_{\eta*}L,Rg_{\eta*}M}.
$$

To verify this equality, we write the two product maps in terms of the
tensor maps of $R\bar j_*$, commute proper direct image past these maps
on the generic fibres, and take the adjoints of the ordinary Künneth
arrows. Both adjoints are equal to
$f_\eta^*Rf_{\eta*}L\boxtimes g_\eta^*Rg_{\eta*}M\to L\boxtimes M$, the tensor product of the two
counits. Therefore, by the triangle identities of the adjunctions and
their compatibility with composition, the maps themselves agree.

*Reduction to projective flat families.*
We argue by induction on
$n=\dim(X_{\bar\eta}\times_{\bar\eta}Y_{\bar\eta})$, simultaneously for
all such traits. The assertion is local on $X_s\times_kY_s$. On
affine neighbourhoods of the two factors, we take projective closures
over $S$ and extend the coefficients by zero on their generic fibres.
By the base change isomorphism for nearby cycles along open immersions,
the restriction of the new map is the original map. Thus we may assume
that $X$ and $Y$ are projective. Using the base change isomorphism for the closed immersions
of the closures of their generic fibres, and invariance under nilpotent
thickenings, we may also assume that they are reduced and that their
generic fibres are dense, and then they are flat over the trait. These
reductions do not increase $n$.

*Global sections.* By the base change isomorphism for the proper structure maps,
the compatibility with proper direct images, and the ordinary Künneth
formula on the geometric generic fibres, we see that the cone $Q$ of
the map (E.4) satisfies

$$
R\Gamma(X_s\times_kY_s,Q)=0.
\tag{E.5}
$$

Under these identifications, the map of global complexes is the
Künneth isomorphism

$$
R\Gamma(X_{\bar\eta},L)\otimes_A^{\mathbf L}
R\Gamma(Y_{\bar\eta},M)
\xrightarrow{\sim}
R\Gamma(X_{\bar\eta}\times Y_{\bar\eta},L\boxtimes M).
$$

*Finite support.* It remains to show that $Q$ has finite
support. When $n=0$, the special fibres are zero-dimensional by
flatness, and there is nothing to prove.

For $n>0$, we work on small neighbourhoods with quasi-finite
coordinate maps

$$
b:X\longrightarrow\mathbf A^q_S,\qquad
c:Y\longrightarrow\mathbf A^r_S,\qquad q+r\leq n.
$$

To construct $b$ near a closed point $x$ of $X_s$, put
$q=\dim_xX_s$. By flatness, $q\leq\dim X_{\bar\eta}$. Choose a system
of parameters $f_1,\ldots,f_q$ of the local ring
$\mathcal O_{X_s,x}$ of the special fibre, defined on an affine
neighbourhood, and lift them to functions on the corresponding affine
open of $X$. The resulting map $b:X\to\mathbf A^q_S$ is quasi-finite at
$x$, because its fibre through $x$ is the fibre of
$b_s=(f_1,\ldots,f_q)$, in which $x$ is isolated. We shrink $X$ to the
open locus where $b$ is quasi-finite, and construct $c$ in the same way,
so that $q+r\leq n$. Since $b_\eta$ and $c_\eta$ are quasi-finite, the
generic fibres of these neighbourhoods have dimensions at most $q$ and
$r$. If $q+r<n$, the induction hypothesis therefore applies, and hence
we may assume that $q+r=n$. Suppose first that $q>0$, and compose $b$ with one of the
coordinate projections $\mathbf A^q_S\to\mathbf A^1_S$. We use the
trait $S'$ as above, and set

$$
X'=X\times_{\mathbf A^1_S}S',\qquad Y'=Y\times_S S',\qquad
L'=L|_{X'_{\eta'}},\quad M'=M|_{Y'_{\eta'}}.
$$

The map $X'\to\mathbf A^q_S\times_{\mathbf A^1_S}S'=\mathbf A^{q-1}_{S'}$
is a base change of $b$, hence quasi-finite, and therefore the generic
dimensions satisfy

$$
\dim X'_{\bar\eta'}\leq q-1,\qquad
\dim Y'_{\bar\eta'}\leq r.
$$

Therefore the product $X'_{\bar\eta'}\times Y'_{\bar\eta'}$ has
dimension at most $n-1$, and by induction $\Pi_{L',M'}$ is an
isomorphism.
By the slicing calculation, the invariance under change of trait in the
second factor, and the same slicing calculation on $X\times_SY$, the
restrictions to this slice are

$$
\begin{aligned}
R\Psi_{X/S}L|_{s'}&\simeq(R\Psi_{X'/S'}L')^P,\\
R\Psi_{Y/S}M|_{s'}&\simeq R\Psi_{Y'/S'}M',\\
R\Psi_{(X\times Y)/S}(L\boxtimes M)|_{s'}
&\simeq
(R\Psi_{(X'\times Y')/S'}(L'\boxtimes M'))^P.
\end{aligned}
$$

In the middle line, $P$ acts trivially, because the action on this
complex of nearby cycles is the restriction of an action of $I$, and
$P$ is the kernel of $I'\to I$. We apply $(-)^P$ to $\Pi_{L',M'}$ and
use (E.3). By the compatibility with
composition in (E.2), the result is the
restriction of (E.4), which is therefore an
isomorphism.

Thus the restriction of $Q$ over $s'$ is zero, that is, the support of
$Q$ has no point over the generic point of this coordinate line in the
special fibre. The image of the support in that line is
constructible and does not contain the generic point, so it is a
finite set of closed points. We repeat this argument for each of the
$q$ coordinates of $b$ and, interchanging the factors, for each of the
$r$ coordinates of $c$. It follows that the support is contained in
the inverse image under $b_s\times c_s$ of a finite product of finite
sets. This inverse image is finite because $b_s\times c_s$ is
quasi-finite. Covering $X_s\times Y_s$ by finitely many such
neighbourhoods, we conclude that the support of $Q$ is finite.

A bounded constructible complex supported on a finite set of closed
points over a separably closed field is the direct image of its
stalk complexes on that finite closed reduced subscheme. Its
global sections are the finite direct sum of these stalks, and hence
they detect vanishing. Therefore (E.5) implies
that $Q=0$, which completes the induction.
