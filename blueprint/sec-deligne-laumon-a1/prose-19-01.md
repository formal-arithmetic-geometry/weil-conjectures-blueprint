+++
id = "prose-19-01"
kind = "hidden"
title = "Deligne's theorem for curves"
order = 740
+++
The reduction of Section [sec-wdef-route] leaves one bound to prove: for a
pure lisse Weil sheaf $F$ of weight $w$ on a smooth curve, the group
$H_c^r(C,F)$ has weights at most $w+r$ (Theorem [sk-thm-wft-curve-middle-upper]).
On an affine curve $H^0_c$ vanishes and $H^2_c$ is a twist of the
coinvariants of geometric monodromy, pure of weight $w+2$
(Lemma [sk-l-dl-a1-endpoints]). So the content of the theorem is
that $H^1_c(C,F)$ has weights at most $w+1$. For the constant sheaf on
a smooth projective curve this is Weil's theorem, and the example of
Section [sec-weights-deligne-theorem] shows that the bound can be strict: on
$\mathbf G_m$ the group $H^1_c$ has weight $0$, because it comes from
the boundary.

On an open of the affine line we prove the bound with the Fourier
transform, following the model of Gauss sums from
Section [sec-fourier-transform]. Let $M$ be irreducible on a dense
open $j:U_0\hookrightarrow\mathbf A^1$, with no geometric constituent of
the form $\mathcal L_{\psi(ax)}$, and let $M'$ be the lisse sheaf with
$\operatorname{FT}_\psi((j_*M)[1])\simeq(j'_*M')[1]$
(Proposition [sk-p-dl-a1-middle]). The stalk of the transform at
the origin of the dual line gives

$$
H^1_c(\mathbf A^1,j_*M)\simeq(j'_*M')_{0'}
$$

(Corollary [sk-c-dl-a1-hc1]), and by
Proposition [sk-p-real-semi] a stalk of a middle extension has
weights at most the weight of the lisse sheaf. It remains to show that
$M'$ is pure of weight $w+1$. This splits into two problems of a
different nature: that $M'$ is pure of some weight $v$, and that $v=w+1$.

Purity is the deep half, and the difficulty is that $M'$ need not be
real, so Theorem [sk-p-real-purity] does not apply to it directly.
Even for a real $M$ the transform is not real, since $\psi$ takes
nonreal values. Over $\mathbf F_3$, let $M$ be the Kummer sheaf of the
quadratic character $\chi$ on $\mathbf G_m$, which is real. By the
computation of Section [sec-fourier-transform] and the signs in
(18.3), the trace of $M'$ at $y\in\mathbf F_3^\times$ is
$-\chi(y)g$ with
$g=\sum_x\chi(x)\psi(x)=\omega-\omega^2=i\sqrt3$, which is not real.
Here a twist by $\mathcal B_{1/g}$ makes $M'$ real, but in general no
twist is known to do this. The remedy is to pair the transform with the
$\psi^{-1}$-transform of the dual. We twist $M$ to weight zero,
$M^0=M\otimes\mathcal B_b$, and transform $j_!M^0$ with the kernel
$\mathcal K_\psi$ and $j_!(M^0)^\vee$ with the kernel
$\mathcal K_{\psi^{-1}}$ at the same time. The traces of the two
summands at each point are complex conjugate, so the sum of the two
transforms is a real sheaf $H$ on the dual line, and $M'\otimes\mathcal B_b$ is a quotient of it. Purity of real sheaves then makes $M'$ pure of
some weight (Proposition [sk-p-dl-a1-some-weight]). Here we use
$j_!$ rather than $j_*$ because its transform is a sheaf; it differs from
the transform of $j_*M$ by a lisse sheaf of weights at most $w$
(Lemma [sk-p-dl-a1-correction]).

The value of the weight is then a matter of counting. For a pure sheaf
the weight is the growth rate $\nu$ of the sums of squared traces
(Theorem [sk-thm-wrp-l2-dictionary] and
Corollary [sk-cor-wrp-l2-real-blocks]), and the Plancherel formula
multiplies these sums by $q^n$ over $\mathbf F_{q^n}$. Hence

$$
v=\nu(j'_*M')=\nu\bigl(\operatorname{FT}_\psi((j_*M)[1])\bigr)=\nu(j_*M)+1=w+1
$$

(Theorem [sk-p-dl-a1-fourier-weight]). This is the argument by which
$|g|=\sqrt q$ for a Gauss sum, applied to a sheaf whose transform we
only know to be pure.

The rest is reduction. To pass from irreducible sheaves to an arbitrary
pure sheaf through a composition series, we need $j_*$ to be exact on
sequences of pure sheaves of the same weight
(Proposition [sk-p-dl-a1-exact]). This is again a weight argument:
the connecting map $j_*F_2\to R^1j_*F_1$ goes from weights at most $w$
to weights at least $w+2$, by local duality at the boundary points
(Lemma [sk-i-dl-a1-local]), and therefore vanishes. Note that
exactness fails without the weight condition: the extension
$0\to \overline{\mathbf Q}_\ell(1)\to F\to \overline{\mathbf Q}_\ell\to0$ on $\mathbf G_m$ given by the Kummer
class of the coordinate is lisse, but $j_*F\to j_*\overline{\mathbf Q}_\ell$ is not
surjective at $0$, since the monodromy of $F$ around $0$ is a nontrivial
unipotent matrix. Together these steps give the bound on the affine
line for sheaves unramified at infinity (Theorem [sk-thm-dl-a1-upper]).
An arbitrary affine curve is reduced to the line by a finite
generically étale map (Lemma [sk-lem-wft-finite-map]), whose direct image
preserves compactly supported cohomology and, on a dense open, purity,
and a point where the sheaf is lisse is moved to infinity
(Lemma [sk-lem-wft-infinity-reduction]). On a curve that is not affine, the
sheaf is the middle extension of its restriction to a dense affine open.
