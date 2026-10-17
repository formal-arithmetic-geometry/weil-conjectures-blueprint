+++
kind = "proof"
of = "sk-lem-failure-field"
uses = ["sk-prop-injectivity", "sk-lem-minimal"]
+++
Choose a failing square and a nonzero element of the cokernel of the
exchange map at a geometric point. For a qcqs scheme $Z'$ over the
source $Z$ of the direct-image morphism, let $P(Z')$ mean that this
fixed element stays outside the image after pullback to $Z'$. The
verification in [Stacks, Tag 0F07](https://stacks.math.columbia.edu/tag/0F07) gives three
properties:

1. **1.** thickenings preserve $P$, by topological invariance;
2. **2.** limits with affine transition maps preserve $P$, by continuity;
3. **3.** if $P(Z')$ holds and $V\subset Z'$ is a quasi-compact open with
   closed complement $W$, then $P(V)$ or $P(W)$ holds.

For the third property let $j\colon V\to Z'$ and $i\colon W\to Z'$ be
the inclusions, embed the coefficient sheaf $M$ into
$j_*J\oplus i_*i^{-1}M$, with $J$ injective on $V_{\mathrm{\acute et}}$, and apply
[sk-prop-injectivity]. Closed pushforward is exact. For the
open summand, with $j'$ and $g_V$ the base changes of $j$ and $g$,
$\mathrm{BC}(g,n,q-1)$ gives $R^aj'_*g_V^{-1}J=0$ for
$1\leq a<q$, so the Leray spectral sequence gives the required injection
into the degree-$q$ direct image from $V$.

By the second property and Zorn's lemma there is a minimal closed
subscheme with $P$; by the first it is reduced, and it is nonempty. Let
$\xi$ be the generic point of an irreducible component. Every affine
open neighbourhood of $\xi$ has $P$, since otherwise its closed
complement, a smaller closed subscheme, would have $P$. The limit of
these neighbourhoods is $\operatorname{Spec}\kappa(\xi)$, which has $P$
by the second property. This is the argument of
[Stacks, Tag 0F06](https://stacks.math.columbia.edu/tag/0F06).

*Complement.* In the notation of [sk-def-bc]:

Let $g:T\to S$, $\mathcal F$ be a failing datum: $g$ is a
quasi-compact quasi-separated *morphism* ([sk-def-bc]) but $T$
need not be a qcqs scheme, as [sk-lem-minimal] requires. Being an
isomorphism is local on $X$, and restriction to an affine open
$S'\subseteq S$ is pullback along an étale map, with which
$R^qg_*$, $R^qh_*$ and the base-change map commute; so the map already
fails over some affine open $S'$, and replacing $S$ by $S'$, $X$ by
$X\times_SS'$ and $T$ by $T\times_SS'$ we may assume $S$ affine (this
is the $S'$ of the statement; the hypothesis in degrees $\le q-1$ is
inherited, being universal). Now $T$, being qcqs over the affine
$S$, is a qcqs scheme. Since $\mathrm{BC}(f,\Lambda,q-1)$ holds, the
base-change map in degree $q$ is injective ([sk-prop-injectivity] (1)),
so it is not surjective: there is a geometric point $\bar x$ of $X$ and
an element $\xi$ of the stalk of $R^qh_*e^{-1}\mathcal F$ at $\bar x$
not in the image. Apply [sk-lem-minimal] to the property ``the chosen cokernel
element survives'' (for $T'\to T$ qcqs, the image of $\xi$ in the stalk
of the corresponding $R^qh'_*$ of the pulled-back sheaf is not in the image
of the base-change map): it fails for the empty scheme, over which the stalk of
$R^qh_*e^{-1}\mathcal F$ is $0$, so the image of $\xi$ is $0$ and
lies in the image; thickenings do not change the étale site; limits work by
the limit theorem for higher direct images. For the closed–open
split let $i:Z\to T'$ be closed with quasi-compact open complement
$j:V\to T'$, and let $\mathcal J$ be an injective sheaf of
$\Lambda$-modules on $V$ containing $j^{-1}\mathcal F'$; the injectivity of
[sk-prop-injectivity] (2) applied to the embedding
$\mathcal F'\to j_*\mathcal J\oplus i_*i^{-1}\mathcal F'$ puts the
surviving element into one of the two summands. The closed summand
is handled by the exactness of $i_*$. For the open summand one
cannot use exactness of $j_*$, which fails in general
($R^1j_*(\Z/\ell)\neq0$ for $j:\gm\hookrightarrow\Aaf^1$); instead
let $e':Y'=X\times_ST'\to T'$ be the base change of $f$ along
$T'\to S$ and $j':V\times_{T'}Y'\to Y'$. The hypothesis that
$\mathrm{BC}(f,\Lambda,r)$ holds universally for $r\le q-1$, applied to $e'$ and the qcqs morphism
$j$ — this is where the property after a *preliminary* base
change, $T'\to S$, and in *all* degrees $\le q-1$ is consumed
— gives $e'^{-1}j_*\mathcal J\cong j'_*e_V^{-1}\mathcal J$ (degree
$0$) and $R^aj'_*e_V^{-1}\mathcal J\cong e'^{-1}R^aj_*\mathcal J=0$
for $1\le a\le q-1$ ($\mathcal J$ is injective). The relative Leray
spectral sequence for $h'\circ j'$ then makes
$R^qh'_*e'^{-1}j_*\mathcal J\to R^q(h'\circ j')_*e_V^{-1}\mathcal J$
injective, and [sk-prop-injectivity] (3) for the square of $f$
along $g'\circ j:V\to S$ and $j^{-1}\mathcal F'\subseteq\mathcal J$
shows that the element survives on $V$. Hence [sk-lem-minimal] gives a
morphism $\Spec K\to T$ with $K$ a field over which the element survives;
taking $g$ to be the composite $\Spec K\to T\to S'$ and $\mathcal F$ the
pullback of the coefficient sheaf to $\Spec K$, the base-change map of the
square of $f'$ along $g$ is not surjective, hence not an isomorphism.
