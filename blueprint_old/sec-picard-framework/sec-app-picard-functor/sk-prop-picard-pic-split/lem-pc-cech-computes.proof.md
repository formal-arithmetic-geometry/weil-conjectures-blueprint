+++
kind  = "proof"
of    = "lem-pc-cech-computes"
+++
Use the Cech-to-cohomology spectral sequence of
[lem-sc-cech-spectral] (whose proof – the double complex
$C^p(\mathcal U,I^q)$ of an injective resolution $I^\bullet$ of
$\mathcal{F}$ – is included there): it has
$E_2^{p,q}=\check H^p(\mathcal U,\underline H^q(\mathcal{F}))$ and converges to
$H^{p+q}(X,\mathcal{F})$. For $q>0$ and every multi-index $J$ the open $U_J$
is affine, so
$\underline H^q(\mathcal{F})(U_J)=H^q(U_J,\mathcal{F}|_{U_J})=0$ by
[pqf-lem-affine-vanishing]; hence $E_1^{p,q}=0$ for $q>0$, the
spectral sequence degenerates at $E_2$, and the filtration of
$H^n(X,\mathcal{F})$ has only the nonzero piece
$E_\infty^{n,0}\cong\operatorname{gr}^n H^n(X,\mathcal F)$: thus
$\check H^p(\mathcal U,\mathcal{F})=H^p(X,\mathcal{F})$ for all $p$. This
identification is $\Gamma(X,\mathcal O_X)$-linear: an element
$a\in\Gamma(X,\mathcal O_X)$ acts on both sides through the endomorphism
$a\cdot\colon\mathcal F\to\mathcal F$, and the spectral sequence is natural
in $\mathcal F$. (This is the
argument of Stacks Project, Cohomology of Schemes, Lemma 30.2.6, Tag
[01XD](https://stacks.math.columbia.edu/tag/01XD); its two
ingredients, Cech acyclicity of injective sheaves and the spectral
sequence of the double complex, are exactly the content of
[lem-sc-cech-spectral].)
