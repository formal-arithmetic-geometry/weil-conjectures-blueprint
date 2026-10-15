+++
id = "sk-prop-av-rigidity"
kind = "proposition"
title = "The rigidity lemma"
lean = ["AlgebraicGeometry.exists_eq_snd_comp"]
order = 547
uses = ["sk-prop-av-image-open"]
tags = ["sketch"]
+++
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
