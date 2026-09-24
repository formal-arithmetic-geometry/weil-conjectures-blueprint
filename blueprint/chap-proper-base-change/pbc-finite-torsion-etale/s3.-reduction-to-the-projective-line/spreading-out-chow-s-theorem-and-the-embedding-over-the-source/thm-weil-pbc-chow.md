+++
id = "thm-weil-pbc-chow"
kind = "theorem"
title = "Chow and projective factorization"
order = 1597
uses = ["def-weil-pbc-scheme-conventions"]
+++
Let $f:X\to Y$ be proper *and locally of finite presentation*, and let $Y$ be
affine. There exist a proper surjection $\pi:\widetilde X\to X$, an integer
$n\geq0$, and a closed immersion

$$
 i_Y:\widetilde X\hookrightarrow\mathbf P^n_Y
$$

such that $f\pi$ is the composite of $i_Y$ with $\mathbf P^n_Y\to Y$. The
assertion is stable under base change on $Y$.

**Status.** The theorem is stated for proper morphisms that are locally of
finite presentation, which is the hypothesis under which the descent lemma
[lem-weil-pbc-chow-limit-descent] holds; the noetherian case below and the
base-change stability are unchanged. What remains open is the general
finite-type case: for a proper morphism that is not finitely presented one
must not assert that $X$ itself descends. The prescribed route is the
approximation chain: $X$ is a closed subscheme of a finitely presented
$Y$-scheme (Stacks Project, Tag
[01ZJ](https://stacks.math.columbia.edu/tag/01ZJ)), Chow is applied to that
model, and the resulting $\pi$ and $i_Y$ are pulled back to $X$ along the
closed immersion. That chain is not yet written out, so the theorem is stated
in the form actually proved; every use of it in this chapter is for a morphism
of finite type over a field or over a finitely generated algebra, where local
finite presentation is automatic.

## Proof

*Reduction to the noetherian case.* By [lem-weil-pbc-chow-limit-descent] we
may write $X=X_0\times_{Y_0}Y$ with $Y_0=\operatorname{Spec}A_0$, $A_0$ a
finitely generated $\mathbf Z$-subalgebra of $A$, and $X_0\to Y_0$ proper. If
the assertion is known for $f_0:X_0\to Y_0$ with data $(\pi_0,n,i_0)$, then

$$
 \pi:=\pi_0\times_{Y_0}\operatorname{id}_Y:\
 \widetilde X:=\widetilde X_0\times_{Y_0}Y\longrightarrow X,
 \qquad
 i_Y:=i_0\times_{Y_0}\operatorname{id}_Y:\
 \widetilde X\hookrightarrow\mathbf P^n_{Y_0}\times_{Y_0}Y=\mathbf P^n_Y
$$

have the required properties: proper surjections and closed immersions are
stable under base change, and
$f\pi=(f_0\pi_0)\times\operatorname{id}=(p_0i_0)\times\operatorname{id}=p\circ
i_Y$, where $p:\mathbf P^n_Y\to Y$.

*The noetherian case.* Let $X$ be proper over the noetherian affine scheme
$Y=\operatorname{Spec}A$ (so $X$ is noetherian by Stacks Project, Morphisms,
Lemma 29.15.6, Tag [01T6](https://stacks.math.columbia.edu/tag/01T6), and
hence has only finitely many irreducible components, Stacks Project,
Properties, Lemma 28.5.7, Tag
[0BA8](https://stacks.math.columbia.edu/tag/0BA8)). Choose the finite affine
cover $X=U_1\cup\dots\cup U_m$ of [lem-weil-pbc-chow-generic-cover], with
dense $U=U_1\cap\dots\cap U_m$, and apply
[lem-weil-pbc-chow-dense-closure-reduction]: replacing $X$ by $X^{*}\to X$ (a
surjective closed immersion, hence a proper surjection) does not change the
conclusion, since data $(\pi^{*},n,i)$ over $f^{*}:X^{*}\to Y$ push forward to
$(X^{*}\to X)\circ\pi^{*}$ over $f:X\to Y$; so we assume that $U$ is
scheme-theoretically dense in the affine, finite type over $Y$, $U_i$. Now:

- [lem-weil-pbc-chow-affine-immersion-projective] gives immersions
  $j_i:U_i\hookrightarrow\mathbf P^{n_i}_Y$;
- [lem-weil-pbc-chow-closed-model-proper] gives closed models
  $Z_i\subseteq\mathbf P^{n_i}_Y$ with $U_i\hookrightarrow Z_i$
  scheme-theoretically dense open immersions, and $Z_i\to Y$ proper;
- [lem-weil-pbc-chow-product-image-model] gives the diagonal model:
  $Z=\prod_{i=1}^mZ_i$, the scheme-theoretic image $W\subseteq Z$ of
  $j=(j_1|_U,\dots,j_m|_U):U\to Z$, the proper projections $p_i:W\to Z_i$, and
  the closed immersion $W\hookrightarrow Z\hookrightarrow\prod_i\mathbf
  P^{n_i}_Y\xrightarrow{\ s\ }\mathbf P^N_Y$ with
  $N=\prod_{i=1}^m(n_i+1)-1$;
- [lem-weil-pbc-chow-projection-gluing] glues, for
  $V_i:=p_i^{-1}(U_i)\subseteq W$ and $X':=\bigcup_{i=1}^m V_i$, the morphisms
  $p_i|_{V_i}:V_i\to U_i$ into $\pi:X'\to X$ with
  $\pi|_U=\operatorname{id}_U$;
- [lem-weil-pbc-chow-fibres-proper-over-cover] identifies $\pi^{-1}(U_i)=V_i$,
  and [lem-weil-pbc-chow-proper-surjective-isomorphism] concludes: $\pi$ is
  proper surjective, $\pi^{-1}(U)\xrightarrow{\sim}U$; and
  [prop-weil-pbc-chow-closed-model-factorization] gives that the composite
  $i:X'\hookrightarrow W\hookrightarrow Z\hookrightarrow\prod_i\mathbf
  P^{n_i}_Y\to\mathbf P^N_Y$ is a closed immersion, and $f\circ\pi$ is the
  composite of $i$ with $\mathbf P^N_Y\to Y$.

Taking $\widetilde X:=X'$, $n:=N$, $i_Y:=i$ settles the noetherian case.

*Base-change stability.* Given data $(\pi,n,i_Y)$ for $f:X\to Y$ and any
morphism $Y'\to Y$, the pullbacks as above give a proper surjection
$X\times_YY'\to X'':=X\times_YY'$ and a closed immersion
$X\times_YY'\hookrightarrow\mathbf P^n_{Y'}$ satisfying the factorization,
because the properties used are stable under base change and the equality
$f\pi=p\circ i_Y$ is a morphism identity over $Y$ which base changes to the
corresponding identity over $Y'$.
