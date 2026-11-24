+++
id = "prose-17-01"
kind = "hidden"
title = "The Deligne–Laumon theorem for curves"
order = 1273
+++
Let $F$ be a [pure](@definition-weights) [lisse](@definition-lisse-sheaves) [Weil sheaf](@definition-weil-structure) of weight $w$ on a smooth curve $C$.
Why should $H^1_c(C,F)$ have [weights at most](@definition-weights) $w+1$? For the constant
sheaf on a smooth projective curve this is Weil's theorem, proved with
the Jacobian, and for an arbitrary $F$ there is no such object to work
with. Yet the [Deligne–Laumon theorem](@theorem-weights-rf-shriek) comes down to exactly this bound. The theorem
says that $H^r_c(C,F)$ has [weights at most](@definition-weights) $w+r$
(Theorem [theorem-weight-bound-curve]), and only $r=1$ requires work.
Indeed, on an affine curve $H^0_c$ vanishes, while by
Lemma [lemma-extreme-degrees-affine-curve] $H^2_c$ is a twist of
the coinvariants of geometric monodromy, [pure](@definition-weights) of weight $w+2$. For
$r=1$ the bound can be strict: on $\mathbf G_m$ the group $H^1_c$ comes from the boundary
and has weight $0$ (see the example of Chapter [chap-Weights]).

For a Gauss sum the answer takes two steps. The transform
$\hat\chi(y)=\overline\chi(y)g$ has the same absolute value for all
$y\ne0$, and Plancherel finds the common value $\sqrt q$. On an open of
the affine line, Chapter [chap-The-Fourier-transform] makes the same two steps
available for sheaves. More precisely, let $M$ be irreducible on a dense open
$j:U_0\hookrightarrow\mathbf A^1$, with no geometric constituent of the
form [$\mathcal L_{\psi(ax)}$](@lemma-artin-schreier-character-sheaf), and let $M'$ be the [lisse](@definition-lisse-sheaves) sheaf with
$\operatorname{FT}_\psi((j_*M)[1])\simeq(j'_*M')[1]$
(Proposition [proposition-fourier-transform-middle-extension]). Then

$$
H^1_c(\mathbf A^1,j_*M)\simeq(j'_*M')_{0'}
$$

(Corollary [corollary-h-1-c-stalk-fourier]). Since a stalk of a [middle
extension](@definition-middle-extension) has [weights at most](@definition-weights) the weight of the [lisse](@definition-lisse-sheaves) sheaf
(Proposition [proposition-weights-j-boundary-points]), it
suffices to show that $M'$ is [pure](@definition-weights) of weight $w+1$. Here the second step
is the easy one, because once $M'$ is [pure](@definition-weights), the [sums of squared traces](@definition-growth-squared-traces) of
Chapter [chap-Pure-sheaves-on-curves] give its weight $w+1$
(Theorem [theorem-weight-fourier-transform]).

The first step, [purity](@definition-weights) of $M'$, is the deep one. The only purity theorem
we have is Theorem [theorem-purity-real-sheaves-curves], for [real](@definition-real-sheaves)
sheaves. But the transform of a [real](@definition-real-sheaves) sheaf is not [real](@definition-real-sheaves), since $\psi$
takes nonreal values. For example, over $\mathbf F_3$ let $M$ be the
Kummer sheaf of the quadratic character $\chi$ on $\mathbf G_m$, which
is [real](@definition-real-sheaves). By the computation of Chapter [chap-The-Fourier-transform] and the
signs in (16.3), the trace of $M'$ at
$y\in\mathbf F_3^\times$ is $-\chi(y)g$. Here
$g=\sum_x\chi(x)\psi(x)=\omega-\omega^2=1+2\omega$ is a square root of
$-3$, which is not real. In this case, admittedly, a twist by [$\mathcal B_{1/g}$](@proposition-weights-under-usual-operations)
makes $M'$ [real](@definition-real-sheaves), but in general no twist is known to do this.

The plan is to realize $M'$, up to a twist, as a quotient of a [real](@definition-real-sheaves)
sheaf on the dual line, to which that theorem applies. To build it we
add a conjugate. First we twist $M$ to weight zero,
$M^0=M\otimes\href{@proposition-weights-under-usual-operations}{\mathcal B_b}$. Then we transform $j_!M^0$ with the kernel
$\mathcal K_\psi$ and $j_!(M^0)^\vee$ with the kernel
$\mathcal K_{\psi^{-1}}$. At each point the traces of the two transforms
are complex conjugate, so their sum is a [real](@definition-real-sheaves) sheaf $H$ on the dual
line. Since the twist $M'\otimes\href{@proposition-weights-under-usual-operations}{\mathcal B_b}$ is a quotient of $H$
(Proposition [proposition-purity-lisse-part-fourier-transform]),
[purity of real sheaves](@theorem-purity-real-sheaves-curves) then makes $M'$ [pure](@definition-weights). We use $j_!$ rather than
$j_*$ because its transform is a sheaf, and by
Lemma [lemma-fourier-transform-boundary-sequence] this transform
differs from the transform of $j_*M$ by a [lisse](@definition-lisse-sheaves) sheaf of [weights at most](@definition-weights)
$w$.

Passing from one irreducible $M$ to every [pure](@definition-weights) sheaf needs care, because
$j_*$ is not exact in general. For example, the extension
$0\to\href{@definition-tate-twists}{\overline{\mathbf Q}_\ell(1)}\to F\to\overline{\mathbf Q}_\ell\to0$ on $\mathbf G_m$ given by the Kummer class
of the coordinate is [lisse](@definition-lisse-sheaves), but $j_*F\to j_*\overline{\mathbf Q}_\ell$ is not surjective at
$0$, since the monodromy of $F$ around $0$ is a nontrivial unipotent
matrix. For sheaves of one weight $w$, however, exactness holds by a weight gap
(Proposition [proposition-exactness-fixed-pure-weight]): by local
duality at the boundary points
(Lemma [lemma-local-duality-point-c-u]), the connecting map
$j_*F_2\to R^1j_*F_1$ goes from [weights at most](@definition-weights) $w$ to weights at least
$w+2$, and so it vanishes.
