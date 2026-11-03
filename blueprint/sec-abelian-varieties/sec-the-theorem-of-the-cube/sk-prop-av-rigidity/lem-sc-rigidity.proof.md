+++
kind  = "proof"
of    = "lem-sc-rigidity"
uses = ["lem-sc-constant-locus-closed", "lem-av-rigidity-local"]
+++
*Classical references: Milne, Abelian Varieties, Ch. I (the
rigidity lemma); Mumford, Abelian Varieties, II.6 (both over an
algebraically closed field).* The geometric hypotheses on $X$ cannot be
weakened to "connected and reduced". For $k=\mathbf R$, $X=\Spec\mathbf C$
(proper, connected, reduced, not geometrically connected),
$Y=\mathbf A^1_{\mathbf R}$, $Z=\mathbf A^1_{\mathbf C}$ viewed over
$\mathbf R$ and $f$ the identity of $X\times_kY=\mathbf A^1_{\mathbf C}$,
the fibre over $y_0=0$ is one point but $f$ does not factor through
$\operatorname{pr}_2$. For $\operatorname{char}k=p>0$, with
$X=\alpha_p=\Spec k[x]/(x^p)$ (proper and geometrically connected but
not reduced), $Y=Z=\mathbf A^1_k$ and $f(x,y)=y+x$, the set
$f(X\times\{0\})=\{0\}$ is a single point, yet $f$ does not factor
through $\mathbf A^1_k\to\mathbf A^1_k$ (the morphism $f$ is not the
pullback of any morphism of the $y$-line). Reducedness alone is not
enough either, i.e. *geometric* reducedness is needed: for $k$
imperfect of characteristic $p$, $a\in k\smallsetminus k^p$,
$k'=k(a^{1/p})$, $X=\Spec k'$ (proper, geometrically connected and
reduced, but not geometrically reduced), $Y=\mathbf A^1_k$,
$Z=\mathbf A^1_{k'}$ viewed over $k$ and $f$ the identity of
$X\times_kY=\mathbf A^1_{k'}$, the fibre over $y_0=0$ is one point, but
$\operatorname{pr}_2:\mathbf A^1_{k'}\to\mathbf A^1_k$ is finite flat of
degree $p$, hence not a monomorphism, so $f=g\circ\operatorname{pr}_2$
is impossible; the argument below fails only in Step 1, as
$\Gamma(X,\mathcal O_X)=k'\ne k$.

*Notation.* For $y\in Y$ let $f_{\bar y}:X_{\overline{\kappa(y)}}\to
Z_{\overline{\kappa(y)}}$ be the base change of
$(f,\operatorname{pr}_2):X\times_kY\to Z\times_kY$ along a geometric point
$\bar y:\Spec\overline{\kappa(y)}\to Y$ over $y$, as in
[lem-sc-constant-locus-closed]. Note $X\ne\emptyset$ (connected spaces
are nonempty), and $\Gamma(X,\mathcal O_X)=k$ by Stacks Project,
Varieties, Lemma 33.9.3
([Tag 0BUG](https://stacks.math.columbia.edu/tag/0BUG)), since $X$ is
proper, geometrically connected and geometrically reduced over $k$.

*Step 1: local factorization* ([lem-av-rigidity-local]). Let $y\in Y$ be a point such that
$f(\operatorname{pr}_2^{-1}(y))$ is contained in an affine open
$V\subseteq Z$; this holds in particular when
$f(\operatorname{pr}_2^{-1}(y))$ is a single point. We show that there
are an affine open $U\ni y$ of $Y$ and a $k$-morphism $g_U:U\to Z$ with
$f|_{X\times_kU}=g_U\circ\operatorname{pr}_2$. The projection
$\operatorname{pr}_2:X\times_kY\to Y$ is proper, hence closed, so
$Y\smallsetminus\operatorname{pr}_2\bigl(f^{-1}(Z\smallsetminus V)\bigr)$
is open; it contains $y$ because $f(\operatorname{pr}_2^{-1}(y))\subseteq V$.
Choose an affine open $U\ni y$ inside it; then
$f(X\times_kU)\subseteq V$. By flat base change along the flat map
$k\to\mathcal O(U)$ ($X$ is quasi-compact and separated),

$$
\Gamma(X\times_kU,\mathcal O)=\Gamma(X,\mathcal O_X)\otimes_k\mathcal O(U)=\mathcal O(U),
$$

the identification being $\operatorname{pr}_2^\#$. Since $V$ is affine,
$f|_{X\times_kU}:X\times_kU\to V$ corresponds to a $k$-algebra map
$\mathcal O(V)\to\Gamma(X\times_kU,\mathcal O)=\mathcal O(U)$, i.e.
$f|_{X\times_kU}=g_U\circ\operatorname{pr}_2$ for the morphism
$g_U:U\to V\subseteq Z$ given by this ring map.

*Step 2: the factorization locus.* Put

$$
L:=\{y\in Y:\ \text{there are an open }U\ni y\text{ and }g_U:U\to Z
\text{ with }f|_{X\times_kU}=g_U\circ\operatorname{pr}_2\}.
$$

By definition $L$ is open, and $y_0\in L$ by Step 1, since
$f(\operatorname{pr}_2^{-1}(y_0))$ is a single point by hypothesis.

*Step 3: $L$ is closed.* Let $L'$ be the set of $y\in Y$ for which
$f_{\bar y}(X_{\overline{\kappa(y)}})$ is a single point; it is closed
by [lem-sc-constant-locus-closed] ($X$ is proper and nonempty, $Z$ is
separated). We claim $L=L'$. If $y\in L$, with $f=g_U\circ\operatorname{pr}_2$
over $U\ni y$, then $f_{\bar y}$ is the composite of the structure
morphism $X_{\overline{\kappa(y)}}\to\Spec\overline{\kappa(y)}$ with the
base change of $g_U$ along $\bar y$, so its image is a single point and
$y\in L'$. Conversely, if $y\in L'$, then $f(\operatorname{pr}_2^{-1}(y))$
is the image in $Z$ of the single point
$f_{\bar y}(X_{\overline{\kappa(y)}})$, because
$X_{\overline{\kappa(y)}}\to\operatorname{pr}_2^{-1}(y)
=X\times_k\Spec\kappa(y)$ is surjective; hence it is a single point,
and $y\in L$ by Step 1. So $L=L'$ is closed.

*Step 4: $L=Y$ and gluing.* By Steps 2 and 3 the subset $L\subseteq Y$
is open, closed and nonempty, while $Y$ is connected; hence $L=Y$, and
$Y$ is covered by opens $U$ with morphisms $g_U:U\to Z$ such that
$f|_{X\times_kU}=g_U\circ\operatorname{pr}_2$. The projection
$X\times_kY\to Y$ is faithfully flat ($X\ne\emptyset$) and
quasi-compact, hence an epimorphism in the category of schemes (fpqc
descent of morphisms), and the same holds over every open of $Y$;
therefore on overlaps $U\cap U'$ the morphisms $g_U$ and $g_{U'}$, both
satisfying $f=g\circ\operatorname{pr}_2$ there, agree. The $g_U$ thus
glue to $g:Y\to Z$ with $f=g\circ\operatorname{pr}_2$.
