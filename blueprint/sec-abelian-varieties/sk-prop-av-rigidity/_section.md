+++
id = "sk-prop-av-rigidity"
kind = "section"
title = "The rigidity lemma"
lean = ["AlgebraicGeometry.exists_eq_snd_comp"]
order = 489
uses = ["sk-prop-av-const-locus", "sk-prop-av-image-open"]
+++
*Proposition (sketch).*

Let $X,Y,Z$ be $k$-schemes with $X$ proper, geometrically connected
and geometrically reduced over $k$, $Y$ connected, $Z$ separated over
$k$, and let $f:X\times_kY\to Z$ be a morphism of $k$-schemes such
that, for some point $y_0\in Y$, the image under $f$ of the fibre
$\mathrm{pr}_2^{-1}(y_0)=X\times_k\Spec\kappa(y_0)$ is a single point.
Then $f$ factors through the projection:
$f=g\circ\mathrm{pr}_2$ for some $g:Y\to Z$. (Both geometric
hypotheses are needed. For $k=\mathbf R$, $X=\Spec\mathbf C$,
$Y=\mathbf A^1_{\mathbf R}$, $Z=\mathbf A^1_{\mathbf C}$ and $f=\mathrm{id}$ of
$X\times_kY=\mathbf A^1_{\mathbf C}$, $X$ is connected, reduced and even
geometrically reduced, but not geometrically connected, and $f$ does
not factor. For $k$ imperfect of characteristic $p$,
$a\in k\smallsetminus k^p$, $k'=k(a^{1/p})$, $X=\Spec k'$,
$Y=\mathbf A^1_k$, $Z=\mathbf A^1_{k'}$ and $f=\mathrm{id}$ of
$X\times_kY=\mathbf A^1_{k'}$, $X$ is geometrically connected and
reduced, but not geometrically reduced; here
$\mathrm{pr}_2:\mathbf A^1_{k'}\to\mathbf A^1_k$ is finite flat of degree
$p$, hence not a monomorphism, so $f=g\circ\mathrm{pr}_2$ is impossible;
the proof below fails only in Step 1, as $\Gamma(X,\mathcal O_X)=k'\ne k$.)

## Proof

Notation $f_{\bar y}$ as in [sk-prop-av-const-locus]; note
$X\ne\emptyset$, being connected, and $\Gamma(X,\mathcal O_X)=k$
(`0BUG`), since $X$ is proper, geometrically connected and
geometrically reduced.
*Step 1 (local factorization).* If $f(\mathrm{pr}_2^{-1}(y))$ lies in an
affine open $V\subseteq Z$ (e.g. it is a single point), then, as
$\mathrm{pr}_2$ is closed,
$Y\smallsetminus\mathrm{pr}_2(f^{-1}(Z\smallsetminus V))$ is an open
neighbourhood of $y$, containing an affine open $U\ni y$ with
$f(X\times_kU)\subseteq V$. By flat base change
$\Gamma(X\times_kU,\mathcal O)=\Gamma(X,\mathcal O_X)\otimes_k\mathcal O(U)=\mathcal O(U)$, so
$f|_{X\times_kU}$, given by $\mathcal O(V)\to\mathcal O(U)$, equals
$g_U\circ\mathrm{pr}_2$ for some $g_U:U\to V$.
*Step 2.* Let $L$ be the set of $y$ near which $f$ factors through
$\mathrm{pr}_2$. It is open by definition and contains $y_0$ by Step 1.
*Step 3.* $L$ equals the locus
$\{y: f_{\bar y}(X_{\overline{\kappa(y)}})\ \text{is a point}\}$, which is
closed by [sk-prop-av-const-locus]: a local factorization through
$\mathrm{pr}_2$ makes $f_{\bar y}$ factor through
$\Spec\overline{\kappa(y)}$; conversely, if $f_{\bar y}$ has one-point
image then so does $f$ on $\mathrm{pr}_2^{-1}(y)$, which is the image of
$X_{\overline{\kappa(y)}}$, and Step 1 applies.
*Step 4.* $L$ is nonempty, open and closed in the connected $Y$,
hence $L=Y$. As $\mathrm{pr}_2$ is faithfully flat and quasi-compact,
hence an epimorphism of schemes, the local $g_U$ agree on overlaps and
glue to $g:Y\to Z$ with $f=g\circ\mathrm{pr}_2$.
