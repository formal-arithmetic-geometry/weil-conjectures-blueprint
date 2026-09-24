+++
id = "lem-weil-pbc-chow-product-image-model"
kind = "lemma"
title = "The diagonal model and its projections"
order = 1688
uses = ["def-weil-pbc-chow-scheme-theoretic-closure", "def-weil-pbc-chow-segre-embedding", "def-weil-pbc-scheme-conventions", "lem-weil-pbc-chow-affine-immersion-projective", "lem-weil-pbc-chow-closed-model-proper", "lem-weil-pbc-chow-dense-closure-reduction", "lem-weil-pbc-chow-generic-cover", "lem-weil-pbc-chow-segre-closed-immersion", "lem-weil-pbc-closed-immersion-products"]
+++
Let $Y=\operatorname{Spec}A$ be affine, let $X\to Y$ be of finite type, and
let $X=U_1\cup\dots\cup U_m$ be the affine open cover of
[lem-weil-pbc-chow-generic-cover], with its dense open $U:=\bigcap_iU_i$.
Applying [lem-weil-pbc-chow-dense-closure-reduction] (which keeps $X$ proper
if it was, and keeps each $U_i$ affine and of finite type over $Y$), we assume
from now on that $U$ is scheme-theoretically dense in $X$. For each $i$, let
$U_i\hookrightarrow\mathbf P^{n_i}_Y$ be the immersion of
[lem-weil-pbc-chow-affine-immersion-projective], and let
$Z_i\subseteq\mathbf P^{n_i}_Y$ be the closed model of
[lem-weil-pbc-chow-closed-model-proper], so that $U_i\hookrightarrow Z_i$ is a
scheme-theoretically dense open immersion. Put

$$
 Z:=\prod_{i=1}^mZ_i,
$$

and let $\widetilde X\subseteq Z$ be the scheme-theoretic image
([def-weil-pbc-chow-scheme-theoretic-closure]) of the diagonal morphism

$$
 j=(j_1|_U,\dots,j_m|_U):U\longrightarrow Z.
$$

Then:

- (i) $U\hookrightarrow\widetilde X$ is a scheme-theoretically dense open
  immersion, and $\widetilde X\to Y$ is proper;
- (ii) the projections $\mathrm{pr}_i|_{\widetilde X}:\widetilde
  X\to\mathbf P^{n_i}_Y$ factor through $Z_i$, i.e. there are morphisms
  $p_i:\widetilde X\to Z_i$ with
  $p_i=(\mathrm{pr}_i|_{\widetilde X}\text{ co-restricted})$, and each $p_i$
  is proper;
- (iii) the composite

  $$
   \widetilde X\hookrightarrow Z\hookrightarrow\prod_{i=1}^m\mathbf P^{n_i}_Y
   \xrightarrow{\ s\ }\mathbf P^N_Y,\qquad N=\prod_{i=1}^m(n_i+1)-1,
  $$

  of the closed immersion $\widetilde X\hookrightarrow Z$, the product of the
  closed immersions $Z_i\hookrightarrow\mathbf P^{n_i}_Y$, and the Segre
  embedding ([def-weil-pbc-chow-segre-embedding],
  [lem-weil-pbc-chow-segre-closed-immersion]) is a closed immersion.

## Proof

*The reduction step is legitimate.* By
[lem-weil-pbc-chow-dense-closure-reduction], $X^{*}\to X$ is a surjective
closed immersion and $U\subseteq X^{*}$ is scheme-theoretically dense;
$\pi:X^{*}\to X$ is proper whenever $X\to Y$ is (a closed immersion followed
by a proper morphism is proper), so conclusions about properness pass from
$X^{*}$ to $X$, and the $U_i^{*}=X^{*}\cap U_i$ are affine, of finite type
over $Y$, with $U=\bigcap_iU_i^{*}$. Hence we may replace $X$ by $X^{*}$ and
$U_i$ by $U_i^{*}$.

*$j$ is an immersion.* By [lem-weil-pbc-chow-affine-immersion-projective] each
$j_i|_U$ factors as the closed immersion $U\hookrightarrow\mathbf A^{n_i}_Y$
followed by the open immersion $\mathbf A^{n_i}_Y\hookrightarrow\mathbf
P^{n_i}_Y$. The induced morphism $U\to\prod_i\mathbf A^{n_i}_Y$ is a closed
immersion: the target is affine with coordinate ring the tensor product over
$A$ of the coordinate rings of the $\mathbf A^{n_i}_Y$, and each of the
coordinate ring maps onto $B=\mathcal O_U(U)$ is surjective, hence so is the
tensor product map. Composing with the open immersion $\prod_i\mathbf
A^{n_i}_Y\hookrightarrow\prod_i\mathbf P^{n_i}_Y$ and using that
$\prod_iZ_i\subseteq\prod_i\mathbf P^{n_i}_Y$ is closed, we get that $j:U\to
Z$ is an immersion.

*Proof of (i).* Stacks Project, Morphisms, Lemma 29.7.7 (Tag
[01RG](https://stacks.math.columbia.edu/tag/01RG)) applied to the
quasi-compact immersion $j$ (its source $U$ is quasi-compact) shows that the
scheme-theoretic image $\widetilde X$ of $j$ contains $U$ as a
scheme-theoretically dense open subscheme. For properness: each $Z_i\to Y$ is
proper by [lem-weil-pbc-chow-closed-model-proper]; $Z=\prod_iZ_i$ is closed in
$\prod_i\mathbf P^{n_i}_Y$ (a product of closed immersions is a closed
immersion), and $\prod_i\mathbf P^{n_i}_Y$ is proper over $Y$ by
[lem-weil-pbc-chow-segre-closed-immersion] and
[def-weil-pbc-chow-segre-embedding] (its structure morphism is the composite
of the closed Segre immersion $\prod_i\mathbf P^{n_i}_Y\hookrightarrow\mathbf
P^N_Y$ with the proper $\mathbf P^N_Y\to Y$); hence $Z\to Y$ is proper, and
the closed subscheme $\widetilde X\subseteq Z$ is proper over $Y$ too
(`closed subscheme` means the composite of the closed immersion with the
proper morphism is proper).

*Proof of (ii).* The morphism $\mathrm{pr}_i\circ j$ equals $j_i|_U:\ U\to
Z_i\subseteq\mathbf P^{n_i}_Y$, i.e. it factors through the closed subscheme
$Z_i$; by the universal property of the scheme-theoretic image
([def-weil-pbc-chow-scheme-theoretic-closure]; equivalently Stacks Project,
Morphisms, Lemma 29.6.6, Tag
[01R9](https://stacks.math.columbia.edu/tag/01R9)), the induced morphism
$\mathrm{pr}_i|_{\widetilde X}:\widetilde X\to\mathbf P^{n_i}_Y$ thus factors
through $Z_i$, giving $p_i$. The morphism $p_i$ is proper by Stacks Project,
Morphisms, Lemma 29.42.7 (Tag
[01W6](https://stacks.math.columbia.edu/tag/01W6)): $\widetilde X\to Y$ is
proper by (i), the target $Z_i$ is separated over $Y$ (it is a closed
subscheme of the projective $Y$-scheme $\mathbf P^{n_i}_Y$, which is separated
over $Y$), and a morphism from a $Y$-proper scheme to a $Y$-separated scheme
is proper.

*Proof of (iii).* $\widetilde X\hookrightarrow Z$ is a closed immersion by the
definition of the scheme-theoretic image
([def-weil-pbc-chow-scheme-theoretic-closure]); the product of the closed
immersions $Z_i\hookrightarrow\mathbf P^{n_i}_Y$ is a closed immersion; and
$s$ is a closed immersion by [lem-weil-pbc-chow-segre-closed-immersion].
Compositions of closed immersions are closed immersions, which proves (iii).
