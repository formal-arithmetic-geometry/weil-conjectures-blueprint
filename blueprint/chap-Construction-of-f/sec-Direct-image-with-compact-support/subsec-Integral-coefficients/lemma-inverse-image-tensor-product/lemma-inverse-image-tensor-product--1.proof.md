+++
kind = "proof"
of = "lemma-inverse-image-tensor-product--1"
order = 494003
+++
The coefficient sheaves are pulled back from the point, and by
clause [corollary-finite-quotients-their-transition-maps--3] there is a canonical monoidal isomorphism
$f^{-1}\circ p_Y^*\simeq p_X^*$. Hence $f^{-1}\Lambda_Y\simeq\Lambda_X$ as
sheaves of rings, and the module inverse image
$f^*=\Lambda_X\otimes_{f^{-1}\Lambda_Y}f^{-1}(-)$ is $f^{-1}$, which is exact.
So $\mathbf Lf^*$ is computed termwise by $f^{-1}$, and
$H^q(\mathbf Lf^*K)=f^{-1}H^q(K)$. If $K$ is bounded, so is $\mathbf Lf^*K$,
and it remains to show that $f^{-1}N$ is constructible for every
constructible $\Lambda_Y$-module $N$.

First let $g:V\to W$ be a quasi-compact morphism of qcqs schemes, and let
$N$ be constructible on $W$ in the sense of Definition [definition-constructible-sheaves--2], with
stratification $W=\coprod_aW_a$. The inverse image of a quasi-compact open
under $g$ is quasi-compact, so the inverse images $V_a=g^{-1}(W_a)$ are
constructible. They are locally closed, and with the subscheme structures
$V\times_WW_a$ they form a finite stratification of $V$. Let
$\{U_{a,i}\to W_a\}$ be a pro-étale cover with
$N|_{U_{a,i}}\simeq\Lambda_{U_{a,i}}\otimes_{\Lambda(*)}P_{a,i}$ as in
condition (1) of Definition [definition-constructible-sheaves--1]. The base changes
$\{U_{a,i}\times_{W_a}V_a\to V_a\}$ form a pro-étale cover. Inverse image
commutes with restriction and with colimits, hence with
$-\otimes_{\Lambda(*)}P_{a,i}$ for the constant sheaf $P_{a,i}$, and it
carries $\Lambda_{U_{a,i}}$ to $\Lambda_{U_{a,i}\times_{W_a}V_a}$ by
clause [corollary-finite-quotients-their-transition-maps--3]. So $(g^{-1}N)|_{V_a}$ satisfies condition (1) with the
same finitely presented modules $P_{a,i}$, and $g^{-1}N$ is constructible on
$V$. Applied to a quasi-compact open immersion, this shows that
constructibility on a qcqs scheme passes to quasi-compact opens. Conversely,
if a qcqs scheme $V$ is covered by quasi-compact opens $V_1,\dots,V_m$ on each
of which a module is constructible, then it is constructible on $V$:
intersect the strata on $V_b$ with the constructible locally closed subset
$V_b\setminus(V_1\cup\dots\cup V_{b-1})$; condition (1) persists on the
smaller strata by restricting the covers.

Now let $f:X\to Y$ be arbitrary and $N$ constructible on $Y$. Then $Y$ is
covered by affine opens on which $N$ is constructible: by definition if $Y$
is arbitrary, and by the previous paragraph if $Y$ is qcqs, since an affine
open of $Y$ is then a quasi-compact open. By the previous paragraph, $N$ is
also constructible on every affine open contained in one of them. Let $V\subset X$
be an affine open. Its image is quasi-compact, so $V$ is covered by finitely
many affine opens $V_b$, each mapping into an affine open $W_b\subset Y$ on
which $N$ is constructible. The morphisms $V_b\to W_b$ are morphisms of affine
schemes, hence quasi-compact, so $(f^{-1}N)|_{V_b}$ is constructible, and by
the gluing remark $(f^{-1}N)|_V$ is constructible. Thus $f^{-1}N$ is
constructible on every affine open of $X$. If $X$ is qcqs, the gluing remark
applied to a finite covering of $X$ by affine opens shows that $f^{-1}N$ is
constructible on $X$ in the sense of Definition [definition-constructible-sheaves--2] for qcqs
schemes. Hence $\mathbf Lf^*K\in\Dbc(X,\Lambda)$.

*Source:* the proof of Lemma [lemma-inverse-image-tensor-product].
