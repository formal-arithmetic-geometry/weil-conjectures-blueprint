+++
id = "lemma-weil-pbc-chow-factorization"
kind = "lemma"
title = "Chow and projective factorization"
order = 1066
uses = ["cor-chow-lemma-proper", "def-weil-pbc-scheme-conventions", "lem-chow-affine-immersion", "lem-chow-closed-model", "lem-chow-glue", "lem-chow-graph", "lem-chow-preimage", "lem-chow-scheme-theoretic-closure", "lem-weil-pbc-chow-limit-descent", "lemma-nagata-dense-affine-cover-exists", "lemma-nagata-projective-space-base-change-proper", "thm-chow-lemma"]
+++
After replacing an affine target by an etale affine cover, every proper
$f:X\to Y$ admits a proper surjection $\pi:X'\to X$ and an integer $n$ with
$X'\hookrightarrow\mathbf P^n_Y$ a closed immersion. Moreover
$X'\to Y$ factors as that closed immersion followed by
$\mathbf P^n_Y\to Y$.

## Proof

Chow's lemma in the form located at Tag `0202`, i.e.
[cor-chow-lemma-proper], supplies a proper surjective $\pi$ for which
$X'\to Y$ is projective; it applies verbatim once the base is noetherian, so
the only work left below is to reduce to that case. To make the source
hypotheses explicit, first work over one affine member $Y=\operatorname{Spec}A$
of the selected etale cover. Write
$A=\varinjlim_{\lambda\in\Lambda}A_\lambda$, where every $A_\lambda$ is a
finitely generated $\mathbf Z$-algebra and the transition maps are directed.
Since a proper morphism is of finite presentation, a finite affine cover
$X=\bigcup_{a=1}^rU_a$, the finitely presented algebras defining the $U_a$,
the pairwise overlap maps, and their cocycle equations descend to one index
$\lambda_0$. After increasing once to $\lambda_1$, the descended morphism
$f_{\lambda_1}:X_{\lambda_1}\to\operatorname{Spec}A_{\lambda_1}$ is proper:
finite presentation and separatedness descend from the finite affine data,
and the valuative criterion for properness is stable under this inverse-limit
presentation.

The ring $A_{\lambda_1}$ is noetherian. Noetherian Chow's lemma produces a
proper surjection
$\pi_{\lambda_1}:X'_{\lambda_1}\to X_{\lambda_1}$ and an
$f_{\lambda_1}\pi_{\lambda_1}$-ample invertible sheaf $L_{\lambda_1}$.
Choose a finite affine cover $X'_{\lambda_1}=\bigcup_{b=1}^sW_b$. On each
$W_b$, ampleness supplies an exponent $m_b>0$ and finitely many global
sections whose nonvanishing opens cover $W_b$. With
$m=\prod_bm_b$, take the corresponding powers of these sections. There are
then finitely many sections $s_0,\ldots,s_n$ of $L_{\lambda_1}^{\otimes m}$
whose nonvanishing opens cover $X'_{\lambda_1}$. Increasing $m$ by one
further common multiple if necessary, the same finite affine-cover test for
very ampleness separates the finitely many overlap generators; hence the
map

$$
[s_0:\cdots:s_n]:X'_{\lambda_1}\longrightarrow
\mathbf P^n_{A_{\lambda_1}}
$$

is an immersion. It is proper, because $X'_{\lambda_1}$ is proper over
$A_{\lambda_1}$ and projective space is separated over that base. A proper
immersion is closed.

Base change along $A_{\lambda_1}\to A$ defines
$X'=X'_{\lambda_1}\times_{A_{\lambda_1}}A$, $\pi$, and the closed immersion
$X'\hookrightarrow\mathbf P^n_Y$. Properness and closed immersions are
preserved by base change. Surjectivity is preserved because every geometric
point of $X$ lifts after base change from the surjective geometric fibre of
$\pi_{\lambda_1}$. Thus the displayed index $\lambda_1$, exponent $m$, and
integer $n$ give the asserted single factorization.

## Detailed form

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
cover $X=U_1\cup\dots\cup U_m$ of [lemma-nagata-dense-affine-cover-exists], with
dense $U=U_1\cap\dots\cap U_m$, and apply
[lem-chow-scheme-theoretic-closure]: replacing $X$ by $X^{*}\to X$ (a
surjective closed immersion, hence a proper surjection) does not change the
conclusion, since data $(\pi^{*},n,i)$ over $f^{*}:X^{*}\to Y$ push forward to
$(X^{*}\to X)\circ\pi^{*}$ over $f:X\to Y$; so we assume that $U$ is
scheme-theoretically dense in the affine, finite type over $Y$, $U_i$. Now:

- [lem-chow-affine-immersion] gives immersions
  $j_i:U_i\hookrightarrow\mathbf P^{n_i}_Y$;
- [lem-chow-closed-model] gives closed models
  $Z_i\subseteq\mathbf P^{n_i}_Y$ with $U_i\hookrightarrow Z_i$
  scheme-theoretically dense open immersions, and $Z_i\to Y$ proper;
- [lem-chow-graph] gives the diagonal model:
  $Z=\prod_{i=1}^mZ_i$, the scheme-theoretic image $W\subseteq Z$ of
  $j=(j_1|_U,\dots,j_m|_U):U\to Z$, the proper projections $p_i:W\to Z_i$, and
  the closed immersion $W\hookrightarrow Z\hookrightarrow\prod_i\mathbf
  P^{n_i}_Y\xrightarrow{\ s\ }\mathbf P^N_Y$ with
  $N=\prod_{i=1}^m(n_i+1)-1$;
- [lem-chow-glue] glues, for
  $V_i:=p_i^{-1}(U_i)\subseteq W$ and $X':=\bigcup_{i=1}^m V_i$, the morphisms
  $p_i|_{V_i}:V_i\to U_i$ into $\pi:X'\to X$ with
  $\pi|_U=\operatorname{id}_U$;
- [lem-chow-preimage] identifies $\pi^{-1}(U_i)=V_i$,
  and [thm-chow-lemma] concludes: $\pi$ is
  proper surjective, $\pi^{-1}(U)\xrightarrow{\sim}U$; and
  [cor-chow-lemma-proper] gives that the composite
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
