+++
id = "prose-09-01"
kind = "hidden"
title = "Smooth base change"
order = 390
+++
Proper base change (Theorem [sk-thm-properbasechange]) says that ordinary
direct image commutes with an arbitrary change of base when the morphism
pushed forward is proper. Without properness this fails. Let
$j:U=\mathbf A^1\setminus\{0\}\hookrightarrow\mathbf A^1$ over an
algebraically closed field, and let $n$ be invertible in it. The stalk of
$R^1j_*(\mathbf Z/n)$ at $0$ is $H^1$ of the punctured strictly henselian
disc, which is $\mathbf Z/n(-1)\neq0$, while the fibre of $j$ over $0$ is
empty. So base change along the closed immersion of $0$ fails. If instead
we put the hypothesis on the change of base, the statement holds for every
quasi-compact quasi-separated $f$: when $g:Y'\to Y$ is smooth and $F$ is a
torsion sheaf whose torsion orders are invertible on $Y$, the base change
map $g^*R^qf_*F\to R^qf'_*g'^*F$ is an isomorphism
(Theorem [sk-thm-smooth-base-change]). The theorem is due to Artin
(SGA 4, Exposé XVI (SGA4)).

In topology the corresponding statement is close to obvious. If $g$ is a
local homeomorphism, base change along $g$ is restriction to open
subsets. If $g$ is the projection $Y\times\mathbf R^m\to Y$, then the
stalk of $R^qf'_*$ at $(y,t)$ is the colimit of the cohomology groups of
$f^{-1}(V)\times B$ over small neighbourhoods $V\times B$ of $(y,t)$, and
the contractible ball $B$ does not change them. A smooth morphism of
schemes is, Zariski locally on the source, étale over some
$\mathbf A^d_Y$, but the
affine line has no small contractible neighbourhoods, and the content of
the theorem is that, for coefficients prime to the characteristic, it
behaves as if it had. The essential case is a change of the algebraically
closed ground field. For an extension $\Omega/L$ of algebraically closed
fields, a smooth affine curve $C$ over $L$ and $n$ invertible in $L$,
pullback $H^1(C,\mathbf Z/n)\to H^1(C_\Omega,\mathbf Z/n)$ is an
isomorphism (Theorem [sk-thm-curve-package]): a cyclic cover of $C_\Omega$
of degree $n$ does not depend on the extra transcendental parameters of
$\Omega$. The proof below reduces smooth base change to a relative form of
this statement, over a normal base in place of $L$.

The hypothesis on the torsion orders cannot be dropped, and
the counterexample is again a change of ground field, from $k$ to the
separably closed field $k(t)^{\mathrm{sep}}$ (cohomology does not change
when we pass further to the algebraic closure of $K$). Let $k$ be algebraically closed of
characteristic $p>0$, and let $f:\mathbf A^1_k\to\operatorname{Spec}k$
and $g:\mathbf A^1_k\to\operatorname{Spec}k$ be the structure maps, with
coordinates $x$ on the source of $f$ and $t$ on the source of $g$. By the
Artin–Schreier sequence, $H^1(\mathbf A^1_K,\mathbf F_p)$ is the cokernel
of $h\mapsto h^p-h$ on $K[x]$, for every field $K\supset k$. At the
geometric generic point of the $t$-line, the stalk of
$g^*R^1f_*\mathbf F_p$ is $H^1(\mathbf A^1_k,\mathbf F_p)$, the stalk of
$R^1f'_*\mathbf F_p$ is $H^1(\mathbf A^1_K,\mathbf F_p)$ with
$K=k(t)^{\mathrm{sep}}$, and the base change map is pullback. The class of
$tx$ is not in its image. Indeed, suppose $tx=a+h^p-h$ with $a\in k[x]$ and
$h\in K[x]$, and let $b_e$ be the coefficient of $x^{p^e}$ in $h$. Comparing
the coefficients of $x$ and of $x^{p^{e+1}}$ gives $b_0\in -t+k$ and
$b_{e+1}\in b_e^p+k$, so that $b_e\in -t^{p^e}+k$ is nonzero for every
$e\geq0$, which is absurd for a polynomial. So smooth base change fails for
$p$-torsion coefficients.

We use the theorem in the Künneth formula for ordinary direct images
(Proposition [sk-lem-sf-kunneth-star]), from which the trace
formula builds its trace classes. The Künneth formula reduces to base
change along a product projection $Y\times T\to Y$
(Lemma [sk-lem-tf-independent-base-change]). This projection is not smooth
when $T$ is singular, and smooth base change enters instead through base
change under extension of the ground field [Stacks, Tag 0F1C](https://stacks.math.columbia.edu/tag/0F1C): after passing to
perfect closures, a larger field is a filtered union of smooth algebras
over the smaller one.

We prove the theorem for torsion sheaves by induction on the cohomological
degree, following the second proof of [Stacks, Tag 0EYU](https://stacks.math.columbia.edu/tag/0EYU). In degree zero
the base change map can be computed on sections
(Lemma [sk-prop-deg0]). By étale coordinates a smooth $g$ is
locally a composite of smooth morphisms of relative dimension one, so we
may assume that $g$ is a smooth affine curve. Suppose that base change
holds below degree $q$. Then the base change map in degree $q$ is
injective (Lemma [sk-prop-injectivity]), and this is why a failure in
degree $q$ survives the reductions that follow. A failure persists when
we shrink the source of the direct image, down to the spectrum of a field
(Lemma [sk-lem-failure-field]), and under integral changes of the
source and of the base (Lemma [sk-lem-sbc-integral-tests]). In the end it
becomes a failure of the special case above, with constant coefficients on
a smooth affine curve over a normal base whose fraction field is
algebraically closed (Lemma [sk-lem-universal-datum]). There the
cohomology of curves gives the vanishing in degrees $q\geq2$, and in
degree one a torsor over the generic fibre extends to a finite étale
cover of the curve by the extension theorem for Galois covers of order
invertible on the base
(Proposition [sk-thm-vanishing]). The theorem for bounded below
complexes (Theorem [sk-thm-sbc-derived]) and on $D^b_{\mathrm{ctf}}(-,\Lambda)$ for every
admissible $\Lambda$ (Theorem [sk-thm-sbc-coefficients]) then follow by a spectral
sequence and by Proposition [sk-prop-reduction-to-finite].
