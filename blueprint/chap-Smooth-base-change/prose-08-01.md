+++
id = "prose-08-01"
kind = "hidden"
title = "Smooth base change"
order = 651
+++
To construct the trace classes in the trace formula we need the Künneth
formula for ordinary direct images,
$Rf_{1*}M_1\boxtimes Rf_{2*}M_2\simeq R(f_1\times f_2)_*(M_1\boxtimes M_2)$
(Proposition [proposition-ordinary-external-kunneth],
Section [sec-The-Kunneth-formula]). For $Rf_!$ this formula follows from
proper base change and the projection formula. For $Rf_*$ this argument does not
work, because $Rf_*$ does not commute with base change in general. For example,
let $j:U=\mathbf A^1\setminus\{0\}\hookrightarrow\mathbf A^1$ over an
algebraically closed field, and let $n$ be invertible in it. The stalk of
$R^1j_*(\mathbf Z/n)$ at $0$ is $H^1$ of the punctured strictly henselian
disc, which is $\mathbf Z/n(-1)\neq0$. The fibre of $j$ over $0$ is empty,
so base change along the closed immersion of $0$ fails.

The Künneth formula only needs base change along a product projection
$Y\times T\to Y$ (Lemma [lemma-base-change-along-product-projection]).
The question is whether base change along such a map holds for every $f$.

In topology it does, at least when $T$ is a manifold. If $g$ is a local
homeomorphism, base change along $g$ is restriction to open subsets. If $g$
is the projection $Y\times\mathbf R^m\to Y$, then the stalk of $R^qf'_*$ at
$(y,t)$ is the colimit of the cohomology groups of $f^{-1}(V)\times B$ over
small neighbourhoods $V\times B$ of $(y,t)$, and the contractible ball $B$
does not change them. For schemes the analogue is less clear. A smooth
morphism of schemes is, Zariski locally on the source, étale over some
$\mathbf A^d_Y$, but the affine line has no small contractible
neighbourhoods. The theorem of this section, due to Artin (SGA 4,
Exposé XVI [sga4]), says that for coefficients prime to the
characteristic the affine line behaves as if it had them. Precisely, let
$g:Y'\to Y$ be smooth, let $f$ be quasi-compact and quasi-separated, and
let $F$ be a torsion sheaf whose torsion orders are invertible on $Y$.
Then the base change map $g^*R^qf_*F\to R^qf'_*g'^*F$ is an isomorphism
(Theorem [theorem-smooth-base-change-classical-torsion]). On
$D^b_{\mathrm{ctf}}(-,\Lambda)$ the same holds for every admissible $\Lambda$
(Theorem [theorem-smooth-base-change-all-admissible]).

A product projection $Y\times T\to Y$ is not smooth when $T$ is singular.
What the Künneth formula uses is a consequence of smooth base change,
namely base change under extension of the ground field [Stacks, [0F1C](https://stacks.math.columbia.edu/tag/0F1C)].

The essential case is a change of the algebraically closed ground field,
and there the key input is a fact about curves. Let $\Omega/L$ be an
extension of algebraically closed fields, $C$ a smooth affine curve over
$L$, and $n$ invertible in $L$. Then pullback
$H^1(C,\mathbf Z/n)\to H^1(C_\Omega,\mathbf Z/n)$ is an isomorphism
(Theorem [theorem-cohomology-curves]). In other words, a cyclic cover
of $C_\Omega$ of degree $n$ does not depend on the extra transcendental
parameters of $\Omega$.

For $p$-torsion coefficients this invariance fails, and so does smooth base
change. Let $k$ be
algebraically closed of characteristic $p>0$, and let
$f:\mathbf A^1_k\to\operatorname{Spec}k$ and
$g:\mathbf A^1_k\to\operatorname{Spec}k$ be the structure maps, with
coordinates $x$ on the source of $f$ and $t$ on the source of $g$. By the
Artin–Schreier sequence, $H^1(\mathbf A^1_K,\mathbf F_p)$ is the cokernel
of $h\mapsto h^p-h$ on $K[x]$, for every field $K\supset k$. At the
geometric generic point of the $t$-line, the stalk of
$g^*R^1f_*\mathbf F_p$ is $H^1(\mathbf A^1_k,\mathbf F_p)$, the stalk of
$R^1f'_*\mathbf F_p$ is $H^1(\mathbf A^1_K,\mathbf F_p)$ with
$K=k(t)^{\mathrm{sep}}$, and the base change map is pullback. We
claim that
the class of $tx$ is not in its image. Suppose $tx=a+h^p-h$ with
$a\in k[x]$ and $h\in K[x]$, and let $b_e$ be the coefficient of $x^{p^e}$
in $h$. Comparing the coefficients of $x$ gives $b_0\in -t+k$, and comparing
those of $x^{p^{e+1}}$ gives $b_{e+1}\in b_e^p+k$. By induction
$b_e\in -t^{p^e}+k$, so $b_e\neq0$ for every $e\geq0$. This is absurd for a
polynomial. In geometric terms, the Artin–Schreier cover $y^p-y=tx$
depends on the parameter $t$. Hence the hypothesis on the torsion orders
cannot be dropped.
