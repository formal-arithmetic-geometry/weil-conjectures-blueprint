+++
id = "lemma-weil-pbc-cancellation"
kind = "lemma"
title = "Cancellation along a proper surjection"
order = 1563
uses = ["lemma-weil-pbc-proper-underived-exchange", "lemma-weil-pbc-property-iff-acyclicity"]
+++
Let $f:X\to Y$ be proper and surjective and $h:Y\to Z$ proper. If $f$ and
$hf$ satisfy $\mathsf{IA}$, then $h$ satisfies $\mathsf{IA}$.

## Proof

Fix a base change $a:Z'\to Z$ and an injective $\mathbf F_\ell$-module sheaf
$I$ on $Y$. Choose a
monomorphism $f^{-1}I\hookrightarrow J$ with $J$ injective on $X$. Applying
$f_*$ gives $\iota:I\to f_*J$. If a germ $a\in I_{\bar y}$ maps to zero,
choose a geometric $\bar x\to X$ above $\bar y$ (surjectivity). The canonical
stalk identification $(f^{-1}I)_{\bar x}\cong I_{\bar y}$ sends $a$ to the
germ of $a$ at $\bar x$; the monomorphism into $J$ makes that germ zero. The
definition of the direct-image stalk then says that $a$ vanishes on an etale
neighbourhood of $\bar y$, so $a=0$. Thus $\iota$ is monic. Injectivity of $I$ supplies a retraction
$r:f_*J\to I$ with $r\circ\iota=\mathrm{id}_I$, making $I$ a direct summand.
After base change, proper underived exchange gives
$b^{-1}f_*J\cong f'_*a_X^{-1}J$. The spectral sequence

$$
R^ph'_*R^qf'_*a_Y^{-1}I\Longrightarrow R^{p+q}(h'f')_*a_X^{-1}I
$$

is computed using the injective $J$ and the assumed acyclicity of $hf$.
The $q>0$ terms vanish for $J$ by $\mathsf{IA}(f)$, and total-degree
vanishing for $hf$ forces $R^ph'_*a_Y^{-1}(f_*J)=0$ for $p>0$. Derived
direct image preserves finite direct sums and retracts, so the same vanishing
holds for the direct summand $a_Y^{-1}I$. This is Tag `0A4C`; the
stalk injectivity argument is written here because surjectivity is essential.
