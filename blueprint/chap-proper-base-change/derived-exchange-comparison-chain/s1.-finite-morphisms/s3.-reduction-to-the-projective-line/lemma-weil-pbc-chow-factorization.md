+++
id = "lemma-weil-pbc-chow-factorization"
kind = "lemma"
title = "Chow and projective factorization"
order = 1467
uses = ["cor-chow-lemma-proper", "lemma-nagata-projective-space-base-change-proper", "lemma-weil-pbc-cancellation", "lemma-weil-pbc-target-locality", "thm-chow-lemma"]
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
